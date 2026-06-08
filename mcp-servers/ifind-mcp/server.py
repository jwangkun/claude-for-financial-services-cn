"""iFind MCP Server — 同花顺 iFind 金融数据 MCP 代理。

将同花顺 iFind 远程 MCP 服务封装为本地 FastMCP 服务器，提供股票、基金、
宏观经济、新闻公告、债券、港美股和指数板块数据。

Usage:
    python server.py                              # stdio (本地)
    python server.py --transport sse --port 8002  # SSE (部署)

Env:
    IFIND_AUTH_TOKEN  — iFind MCP 密钥（优先于 mcp_config.json）
"""

import argparse
import json
import os
import sys
import time
import ssl
import threading
from pathlib import Path
from typing import Any, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    from mcp import FastMCP

server = FastMCP(
    "ifind-mcp",
    instructions="同花顺 iFind 金融数据 — 股票/基金/宏观/新闻/债券/港美股/指数板块",
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_CONFIG_PATH = Path(__file__).parent / "mcp_config.json"

def _load_auth_token() -> str:
    token = os.environ.get("IFIND_AUTH_TOKEN", "").strip()
    if token:
        return token
    if _CONFIG_PATH.exists():
        cfg = json.loads(_CONFIG_PATH.read_text(encoding="utf-8"))
        token = cfg.get("auth_token", "").strip()
        if token and token != "您的 iFinD-MCP 密钥":
            return token
    return ""

AUTH_TOKEN = _load_auth_token()
BASE_URL = "https://api-mcp.51ifind.com:8643/ds-mcp-servers"

# Custom SSL adapter for compatibility with iFind API (Python 3.12+ SSL fix)
class CompatibleSSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = create_urllib3_context()
        ctx.check_hostname = False
        # Allow older TLS versions for compatibility
        ctx.minimum_version = ssl.TLSVersion.TLSv1_2
        kwargs["ssl_context"] = ctx
        return super().init_poolmanager(*args, **kwargs)

_session = requests.Session()
_session.mount("https://", CompatibleSSLAdapter())

SERVER_URLS = {
    "stock":        f"{BASE_URL}/hexin-ifind-ds-stock-mcp",
    "fund":         f"{BASE_URL}/hexin-ifind-ds-fund-mcp",
    "edb":          f"{BASE_URL}/hexin-ifind-ds-edb-mcp",
    "news":         f"{BASE_URL}/hexin-ifind-ds-news-mcp",
    "bond":         f"{BASE_URL}/hexin-ifind-ds-bond-mcp",
    "global_stock": f"{BASE_URL}/hexin-ifind-ds-global-stock-mcp",
    "index":        f"{BASE_URL}/hexin-ifind-ds-index-mcp",
}

# ---------------------------------------------------------------------------
# Session & rate-limit management
# ---------------------------------------------------------------------------

_sessions: dict[str, str] = {}
_req_ids: dict[str, int] = {}
_lock = threading.Lock()

# 并发控制：免费版 2，个人版 5，企业版 10
CONCURRENCY_LIMIT = int(os.environ.get("IFIND_CONCURRENCY", "2"))
_semaphore = threading.Semaphore(CONCURRENCY_LIMIT)


def _next_id(server_type: str) -> int:
    _req_ids[server_type] = _req_ids.get(server_type, 0) + 1
    return _req_ids[server_type]


def _headers(server_type: Optional[str] = None) -> dict:
    h = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "Authorization": AUTH_TOKEN,
    }
    if server_type and server_type in _sessions:
        h["Mcp-Session-Id"] = _sessions[server_type]
    return h


def _post(server_type: str, payload: dict, timeout: int = 60) -> tuple:
    _semaphore.acquire()
    try:
        resp = _session.post(
            SERVER_URLS[server_type],
            json=payload,
            headers=_headers(server_type),
            verify=False,
            timeout=timeout,
        )
        data = None
        if resp.text.strip():
            try:
                data = resp.json()
            except Exception:
                data = resp.text
        return resp, data
    finally:
        _semaphore.release()


def _init_session(server_type: str) -> None:
    if server_type in _sessions:
        return
    payload = {
        "jsonrpc": "2.0",
        "id": _next_id(server_type),
        "method": "initialize",
        "params": {
            "protocolVersion": "2025-03-26",
            "capabilities": {},
            "clientInfo": {"name": "ifind-mcp-proxy", "version": "1.1.0"},
        },
    }
    resp, data = _post(server_type, payload, timeout=30)
    resp.raise_for_status()
    session_id = resp.headers.get("Mcp-Session-Id")
    if not session_id:
        raise RuntimeError(f"iFind initialize 未返回 Mcp-Session-Id: {data}")
    _sessions[server_type] = session_id
    notify = {"jsonrpc": "2.0", "method": "notifications/initialized"}
    _session.post(
        SERVER_URLS[server_type],
        json=notify,
        headers=_headers(server_type),
        verify=False,
        timeout=10,
    )


def _call_ifind(server_type: str, tool_name: str, arguments: dict) -> str:
    """Proxy a tool call to the iFind remote MCP and return JSON string."""
    if not AUTH_TOKEN:
        return json.dumps(
            {"error": "iFind auth_token 未配置。请设置 IFIND_AUTH_TOKEN 环境变量或在 mcp_config.json 中配置密钥。"},
            ensure_ascii=False,
        )
    if server_type not in SERVER_URLS:
        return json.dumps({"error": f"未知服务类型: {server_type}"}, ensure_ascii=False)

    _init_session(server_type)
    payload = {
        "jsonrpc": "2.0",
        "id": _next_id(server_type),
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": arguments},
    }
    try:
        resp, data = _post(server_type, payload)
        if isinstance(data, dict) and "error" in data:
            return json.dumps({"error": data["error"]}, ensure_ascii=False)
        resp.raise_for_status()
        return json.dumps(data, ensure_ascii=False, default=str)
    except Exception as e:
        return json.dumps({"error": f"iFind 请求失败: {e}"}, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Stock tools
# ---------------------------------------------------------------------------

@server.tool()
def ifind_search_stocks(query: str) -> str:
    """同花顺智能选股。支持自然语言条件筛选 A 股股票。

    Args:
        query: 自然语言选股条件，如 "电子行业市值大于100亿"
    """
    return _call_ifind("stock", "search_stocks", {"query": query})


@server.tool()
def ifind_get_stock_summary(query: str) -> str:
    """获取股票信息摘要，包括基本面、财务状况等概览。

    Args:
        query: 股票简称 + 查询内容，如 "茅台财务状况"
    """
    return _call_ifind("stock", "get_stock_summary", {"query": query})


@server.tool()
def ifind_get_stock_info(query: str) -> str:
    """查询股票基本资料、日频行情与技术指标。

    Args:
        query: 股票简称 + 指标 + 时间，如 "格力电器上市时间" 或 "三花智控近5日涨跌幅"
    """
    return _call_ifind("stock", "get_stock_info", {"query": query})


@server.tool()
def ifind_get_stock_shareholders(query: str) -> str:
    """查询股本结构与股东数据。

    Args:
        query: 股票简称 + 指标，如 "光明乳业流通股占比"
    """
    return _call_ifind("stock", "get_stock_shareholders", {"query": query})


@server.tool()
def ifind_get_stock_financials(query: str) -> str:
    """查询股票财务数据与指标，支持多主体多指标（不超过5个）。

    Args:
        query: 股票简称 + 财务指标 + 财报日期，如 "科大讯飞2025年三季度的ROE"
    """
    return _call_ifind("stock", "get_stock_financials", {"query": query})


@server.tool()
def ifind_get_risk_indicators(query: str) -> str:
    """查询风险定量指标（夏普比率、波动率、Beta等）。

    Args:
        query: 股票 + 时间 + 指标，如 "航天电子在2026-03-19的夏普比率"
    """
    return _call_ifind("stock", "get_risk_indicators", {"query": query})


@server.tool()
def ifind_get_stock_events(query: str) -> str:
    """查询上市公司重大事件（IPO、增发、重组等）。

    Args:
        query: 股票 + 事件相关指标，如 "摩尔线程IPO首发股本数量"
    """
    return _call_ifind("stock", "get_stock_events", {"query": query})


@server.tool()
def ifind_get_esg_data(query: str) -> str:
    """查询 ESG 评级数据。

    Args:
        query: 股票 + ESG评级指标，如 "诚意药业中诚信ESG评级"
    """
    return _call_ifind("stock", "get_esg_data", {"query": query})


# ---------------------------------------------------------------------------
# Fund tools
# ---------------------------------------------------------------------------

@server.tool()
def ifind_search_funds(query: str) -> str:
    """搜索基金（模糊名称或选基需求）。

    Args:
        query: 基金名称或选基条件，如 "南方基金新能源ETF"
    """
    return _call_ifind("fund", "search_funds", {"query": query})


@server.tool()
def ifind_get_fund_profile(query: str) -> str:
    """查询基金基本资料（发行日期、费率等）。

    Args:
        query: 基金名称 + 指标，如 "工银双盈债券A(010068)的发行日期与发行费率"
    """
    return _call_ifind("fund", "get_fund_profile", {"query": query})


@server.tool()
def ifind_get_fund_market_performance(query: str) -> str:
    """查询基金行情与业绩数据。

    Args:
        query: 基金名称 + 时间范围 + 指标，如 "方正富邦策略精选A(010072)在近一月收益率"
    """
    return _call_ifind("fund", "get_fund_market_performance", {"query": query})


@server.tool()
def ifind_get_fund_ownership(query: str) -> str:
    """查询基金份额与持有人数据。

    Args:
        query: 基金名称 + 日期 + 指标，如 "湘财长弘灵活配置混合A(010076)在2025-06-30的申购总份额"
    """
    return _call_ifind("fund", "get_fund_ownership", {"query": query})


@server.tool()
def ifind_get_fund_portfolio(query: str) -> str:
    """查询基金持仓明细。

    Args:
        query: 基金名称 + 日期 + 指标，如 "工银优质成长混合A(010088)在2025-06-30的股票投资占比"
    """
    return _call_ifind("fund", "get_fund_portfolio", {"query": query})


@server.tool()
def ifind_get_fund_financials(query: str) -> str:
    """查询基金财务指标。

    Args:
        query: 基金名称 + 日期 + 指标，如 "泰康浩泽混合A(010081)在2025-06-30的利润"
    """
    return _call_ifind("fund", "get_fund_financials", {"query": query})


@server.tool()
def ifind_get_fund_company_info(query: str) -> str:
    """查询基金公司信息。

    Args:
        query: 基金名称 + 基金公司维度指标，如 "蜂巢丰瑞的所属基金公司基金经理数量"
    """
    return _call_ifind("fund", "get_fund_company_info", {"query": query})


# ---------------------------------------------------------------------------
# EDB (macro / industry) tools
# ---------------------------------------------------------------------------

@server.tool()
def ifind_search_edb(query: str) -> str:
    """搜索宏观经济/行业经济指标（模糊搜索）。

    Args:
        query: 行业/产品/指标描述，如 "光模块产业链相关指标"
    """
    return _call_ifind("edb", "search_edb", {"query": query})


@server.tool()
def ifind_get_edb_data(query: str) -> str:
    """查询宏观经济/行业经济指标数据。建议先用 ifind_search_edb 确认指标名称。

    Args:
        query: 指标名称 + 时间范围，如 "光伏电池产量202301-202506"
    """
    return _call_ifind("edb", "get_edb_data", {"query": query})


# ---------------------------------------------------------------------------
# News tools
# ---------------------------------------------------------------------------

@server.tool()
def ifind_search_news(query: str, time_start: str = "", time_end: str = "", size: int = 5) -> str:
    """新闻资讯语义检索，返回相关段落而非全文。

    Args:
        query: 搜索内容
        time_start: 开始日期 (YYYY-MM-DD)
        time_end: 结束日期 (YYYY-MM-DD)
        size: 返回条数
    """
    params = {"query": query, "size": size}
    if time_start:
        params["time_start"] = time_start
    if time_end:
        params["time_end"] = time_end
    return _call_ifind("news", "search_news", params)


@server.tool()
def ifind_search_notice(query: str, time_start: str = "", time_end: str = "", size: int = 5) -> str:
    """上市公司公告语义检索。

    Args:
        query: 搜索内容，如 "光迅科技2024年度报告 光模块技术"
        time_start: 开始日期 (YYYY-MM-DD)
        time_end: 结束日期 (YYYY-MM-DD)
        size: 返回条数
    """
    params = {"query": query, "size": size}
    if time_start:
        params["time_start"] = time_start
    if time_end:
        params["time_end"] = time_end
    return _call_ifind("news", "search_notice", params)


@server.tool()
def ifind_search_trending_news(keyword: str, industry_name: str = "", time_scope: str = "24小时", size: int = 5) -> str:
    """热点事件资讯查询，注重时效性。

    Args:
        keyword: 关键词
        industry_name: 行业名称（可选）
        time_scope: 时效范围，如 "24小时"、"一周"
        size: 返回条数
    """
    params = {"keyword": keyword, "time_scope": time_scope, "size": size}
    if industry_name:
        params["industry_name"] = industry_name
    return _call_ifind("news", "search_trending_news", params)


# ---------------------------------------------------------------------------
# Bond tools
# ---------------------------------------------------------------------------

@server.tool()
def ifind_bond_basic_info(query: str) -> str:
    """查询债券基本信息与发债主体资料。

    Args:
        query: 债券简称/代码 + 查询内容，如 "23广东11的发行期限与发行总额"
    """
    return _call_ifind("bond", "bond_basic_info", {"query": query})


@server.tool()
def ifind_bond_market_data(query: str) -> str:
    """查询债券行情数据与估值分析（久期、凸性等）。

    Args:
        query: 债券简称/代码 + 指标 + 时间，如 "26国债01近五日收盘价、涨跌幅与最新久期、凸性"
    """
    return _call_ifind("bond", "bond_market_data", {"query": query})


@server.tool()
def ifind_bond_financial_data(query: str) -> str:
    """查询债券发债主体财务数据与指标。

    Args:
        query: 债券简称/代码 + 时间 + 指标，如 "24辽港01在20251231的资产负债率"
    """
    return _call_ifind("bond", "bond_financial_data", {"query": query})


@server.tool()
def ifind_bond_special_data(query: str) -> str:
    """查询债券特殊指标（信用债评级、回购、可转债条款等）。

    Args:
        query: 债券简称/代码 + 指标，如 "华海转债的最新转股价格及转换比例"
    """
    return _call_ifind("bond", "bond_special_data", {"query": query})


# ---------------------------------------------------------------------------
# Global stock (HK/US) tools
# ---------------------------------------------------------------------------

@server.tool()
def ifind_search_global_stocks(query: str, market: str = "港股") -> str:
    """港美股智能选股。

    Args:
        query: 选股条件，如 "汽车行业且市盈率低于50"
        market: "港股" 或 "美股"
    """
    return _call_ifind("global_stock", "search_global_stocks", {"query": query, "market": market})


@server.tool()
def ifind_global_stock_profile(query: str) -> str:
    """查询港美股基本资料与股本结构。

    Args:
        query: 股票名称/代码 + 指标，如 "智谱、minimax的所属行业、上市日期与发行价"
    """
    return _call_ifind("global_stock", "global_stock_profile", {"query": query})


@server.tool()
def ifind_global_stock_quotes(query: str) -> str:
    """查询港美股行情数据与技术指标。

    Args:
        query: 股票名称/代码 + 时间 + 指标，如 "苹果和特斯拉近10个交易日的涨跌幅、换手率"
    """
    return _call_ifind("global_stock", "global_stock_quotes", {"query": query})


@server.tool()
def ifind_global_stock_financial(query: str) -> str:
    """查询港美股财务数据与估值指标。

    Args:
        query: 股票名称/代码 + 指标，如 "Google和Meta在最新报告期的ROE、ROA、利润增速"
    """
    return _call_ifind("global_stock", "global_stock_financial", {"query": query})


@server.tool()
def ifind_global_stock_events(query: str) -> str:
    """查询港美股公告事件（IPO、回购、分红、ESG等）。

    Args:
        query: 股票名称/代码 + 事件指标，如 "minimax的IPO日期、数量、价格及保荐人"
    """
    return _call_ifind("global_stock", "global_stock_events", {"query": query})


# ---------------------------------------------------------------------------
# Index / sector tools
# ---------------------------------------------------------------------------

@server.tool()
def ifind_index_data(query: str) -> str:
    """查询指数行情、技术指标与估值指标。

    Args:
        query: 指数名称 + 时间 + 指标，如 "沪深300过去10个交易日的涨跌幅和收盘点数"
    """
    return _call_ifind("index", "index_data", {"query": query})


@server.tool()
def ifind_sector_data(query: str) -> str:
    """查询板块行情、财务分析与成分股指标。

    Args:
        query: 板块名称 + 时间 + 指标，如 "医疗设备板块的成分股个数及过去5日平均涨跌幅"
    """
    return _call_ifind("index", "sector_data", {"query": query})


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="iFind MCP Server")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    parser.add_argument("--port", type=int, default=8002)
    parser.add_argument("--host", type=str, default="0.0.0.0")
    args = parser.parse_args()

    if not AUTH_TOKEN:
        print(
            "WARNING: iFind auth_token 未配置。"
            "请设置 IFIND_AUTH_TOKEN 环境变量或在 mcp_config.json 中配置密钥。",
            file=sys.stderr,
        )

    if args.transport == "sse":
        print(f"Starting iFind SSE server on http://{args.host}:{args.port}/mcp", file=sys.stderr)
        server.run(transport="sse", host=args.host, port=args.port)
    else:
        print("Starting iFind stdio MCP server...", file=sys.stderr)
        server.run(transport="stdio")


if __name__ == "__main__":
    main()
