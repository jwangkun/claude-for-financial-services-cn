"""Wind MCP Server — 万得 Wind 金融数据 MCP 代理。

将万得 Wind 远程 MCP 服务封装为本地 FastMCP 服务器，提供 A 股、港美股、基金、
指数、债券、宏观、研报和分析数据。

Usage:
    python server.py                              # stdio (本地)
    python server.py --transport sse --port 8003  # SSE (部署)

Env:
    WIND_API_KEY  — Wind API 密钥（优先于 mcp_config.json）
"""

import argparse
import json
import os
import sys
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
    "wind-mcp",
    instructions="万得 Wind 金融数据 — A股/港美股/基金/指数/债券/宏观/研报/分析",
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_CONFIG_PATH = Path(__file__).parent / "mcp_config.json"


def _load_api_key() -> str:
    key = os.environ.get("WIND_API_KEY", "").strip()
    if key:
        return key
    if _CONFIG_PATH.exists():
        cfg = json.loads(_CONFIG_PATH.read_text(encoding="utf-8"))
        key = cfg.get("api_key", "").strip()
        if key and key != "your-wind-api-key-here":
            return key
    home_cfg = Path.home() / ".wind-aifinmarket" / "config"
    if home_cfg.exists():
        cfg = json.loads(home_cfg.read_text(encoding="utf-8"))
        key = cfg.get("api_key", "").strip()
        if key:
            return key
    return ""


API_KEY = _load_api_key()
BASE_URL = "https://mcp.wind.com.cn"

# SSL verification — enabled by default. Set WIND_SSL_NO_VERIFY=1 to disable
# (INSECURE — only for development environments with self-signed certs).
_SSL_NO_VERIFY = os.environ.get("WIND_SSL_NO_VERIFY", "").strip() in ("1", "true", "yes")
if _SSL_NO_VERIFY:
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    print("WARNING: SSL certificate verification DISABLED (WIND_SSL_NO_VERIFY=1). "
          "This is INSECURE — only use in development.", file=sys.stderr)


class CompatibleSSLAdapter(HTTPAdapter):
    """SSL adapter that enforces TLS 1.2+ while keeping hostname verification enabled.

    Set WIND_SSL_NO_VERIFY=1 to disable certificate verification (INSECURE — dev only).
    """

    def init_poolmanager(self, *args, **kwargs):
        ctx = create_urllib3_context()
        ctx.minimum_version = ssl.TLSVersion.TLSv1_2
        kwargs["ssl_context"] = ctx
        return super().init_poolmanager(*args, **kwargs)


_session = requests.Session()
_session.mount("https://", CompatibleSSLAdapter())

SERVER_URLS = {
    "stock_data":        f"{BASE_URL}/mcp-server/stock_data",
    "global_stock_data": f"{BASE_URL}/mcp-server/global_stock_data",
    "fund_data":         f"{BASE_URL}/mcp-server/fund_data",
    "index_data":        f"{BASE_URL}/mcp-server/index_data",
    "bond_data":         f"{BASE_URL}/mcp-server/bond_data",
    "financial_docs":    f"{BASE_URL}/mcp-server/financial_docs",
    "economic_data":     f"{BASE_URL}/mcp-server/economic_data",
    "analytics_data":    f"{BASE_URL}/mcp-server/analytics_data",
}

# ---------------------------------------------------------------------------
# Session & rate-limit management
# ---------------------------------------------------------------------------

_sessions: dict[str, str] = {}
_req_ids: dict[str, int] = {}
_lock = threading.Lock()

CONCURRENCY_LIMIT = int(os.environ.get("WIND_CONCURRENCY", "5"))
_semaphore = threading.Semaphore(CONCURRENCY_LIMIT)


def _next_id(server_type: str) -> int:
    with _lock:
        _req_ids[server_type] = _req_ids.get(server_type, 0) + 1
        return _req_ids[server_type]


def _headers(server_type: Optional[str] = None) -> dict:
    h = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "Authorization": f"Bearer {API_KEY}",
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
            verify=not _SSL_NO_VERIFY,
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
    with _lock:
        if server_type in _sessions:
            return
    payload = {
        "jsonrpc": "2.0",
        "id": _next_id(server_type),
        "method": "initialize",
        "params": {
            "protocolVersion": "2025-03-26",
            "capabilities": {},
            "clientInfo": {"name": "wind-mcp-proxy", "version": "1.0.0"},
        },
    }
    resp, data = _post(server_type, payload, timeout=30)
    resp.raise_for_status()
    session_id = resp.headers.get("Mcp-Session-Id")
    if not session_id:
        print(f"[WARN] Wind {server_type} initialize 未返回 Mcp-Session-Id", file=sys.stderr)
        raise RuntimeError(f"Wind {server_type} 初始化失败：未获取到会话 ID")
    with _lock:
        _sessions[server_type] = session_id
    notify = {"jsonrpc": "2.0", "method": "notifications/initialized"}
    _session.post(
        SERVER_URLS[server_type],
        json=notify,
        headers=_headers(server_type),
        verify=not _SSL_NO_VERIFY,
        timeout=10,
    )


def _call_wind(server_type: str, tool_name: str, arguments: dict) -> str:
    """Proxy a tool call to the Wind remote MCP and return JSON string."""
    if not API_KEY:
        return json.dumps(
            {"error": "Wind API Key 未配置。请设置 WIND_API_KEY 环境变量或在 mcp_config.json 中配置密钥。申请地址：https://aifinmarket.wind.com.cn/#/home"},
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
    except requests.exceptions.Timeout:
        return json.dumps({"error": f"Wind {server_type} 请求超时"}, ensure_ascii=False)
    except requests.exceptions.ConnectionError:
        return json.dumps({"error": f"无法连接 Wind {server_type} 服务，请检查网络"}, ensure_ascii=False)
    except Exception as e:
        print(f"[ERROR] wind-mcp {server_type}/{tool_name}: {e}", file=sys.stderr)
        return json.dumps({"error": f"Wind 请求失败，请检查日志"}, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Stock data tools (8)
# ---------------------------------------------------------------------------

@server.tool()
def wind_search_stocks(query: str) -> str:
    """万得智能选股。支持自然语言条件筛选 A 股股票。

    Args:
        query: 自然语言选股条件，如 "电子行业市值大于100亿"
    """
    return _call_wind("stock_data", "search_stocks", {"query": query})


@server.tool()
def wind_get_stock_info(query: str) -> str:
    """查询股票基本资料、日频行情与技术指标。

    Args:
        query: 股票简称 + 指标 + 时间，如 "格力电器上市时间" 或 "三花智控近5日涨跌幅"
    """
    return _call_wind("stock_data", "get_stock_info", {"query": query})


@server.tool()
def wind_get_stock_financials(query: str) -> str:
    """查询股票财务数据与指标，支持多主体多指标。

    Args:
        query: 股票简称 + 财务指标 + 财报日期，如 "科大讯飞2025年三季度的ROE"
    """
    return _call_wind("stock_data", "get_stock_financials", {"query": query})


@server.tool()
def wind_get_stock_shareholders(query: str) -> str:
    """查询股本结构与股东数据。

    Args:
        query: 股票简称 + 指标，如 "光明乳业流通股占比"
    """
    return _call_wind("stock_data", "get_stock_shareholders", {"query": query})


@server.tool()
def wind_get_stock_events(query: str) -> str:
    """查询上市公司重大事件（IPO、增发、重组等）。

    Args:
        query: 股票 + 事件相关指标，如 "摩尔线程IPO首发股本数量"
    """
    return _call_wind("stock_data", "get_stock_events", {"query": query})


@server.tool()
def wind_get_stock_consensus(query: str) -> str:
    """查询一致预期数据（营收/利润/EPS 预测）。

    Args:
        query: 股票简称 + 预期指标，如 "贵州茅台2025年一致预期净利润"
    """
    return _call_wind("stock_data", "get_stock_consensus", {"query": query})


@server.tool()
def wind_get_stock_technical(query: str) -> str:
    """查询技术指标（MACD/KDJ/RSI/布林带等）。

    Args:
        query: 股票简称 + 技术指标，如 "比亚迪近20日MACD"
    """
    return _call_wind("stock_data", "get_stock_technical", {"query": query})


@server.tool()
def wind_get_stock_summary(query: str) -> str:
    """获取股票信息摘要，包括基本面、财务状况等概览。

    Args:
        query: 股票简称 + 查询内容，如 "茅台财务状况"
    """
    return _call_wind("stock_data", "get_stock_summary", {"query": query})


# ---------------------------------------------------------------------------
# Global stock data tools (5)
# ---------------------------------------------------------------------------

@server.tool()
def wind_search_global_stocks(query: str, market: str = "港股") -> str:
    """港美股智能选股。

    Args:
        query: 选股条件，如 "汽车行业且市盈率低于50"
        market: "港股" 或 "美股"
    """
    return _call_wind("global_stock_data", "search_global_stocks", {"query": query, "market": market})


@server.tool()
def wind_get_global_stock_info(query: str) -> str:
    """查询港美股行情数据与技术指标。

    Args:
        query: 股票名称/代码 + 时间 + 指标，如 "苹果和特斯拉近10个交易日的涨跌幅"
    """
    return _call_wind("global_stock_data", "get_global_stock_info", {"query": query})


@server.tool()
def wind_get_global_stock_financials(query: str) -> str:
    """查询港美股财务数据与估值指标。

    Args:
        query: 股票名称/代码 + 指标，如 "Google和Meta最新报告期的ROE、ROA"
    """
    return _call_wind("global_stock_data", "get_global_stock_financials", {"query": query})


@server.tool()
def wind_get_global_stock_events(query: str) -> str:
    """查询港美股公告事件（IPO、回购、分红等）。

    Args:
        query: 股票名称/代码 + 事件指标，如 "特斯拉IPO日期及价格"
    """
    return _call_wind("global_stock_data", "get_global_stock_events", {"query": query})


@server.tool()
def wind_compare_global_stocks(query: str) -> str:
    """跨市场对比（A 股 vs 港股 vs 美股同行业）。

    Args:
        query: 对比条件，如 "中美新能源车企估值对比"
    """
    return _call_wind("global_stock_data", "compare_global_stocks", {"query": query})


# ---------------------------------------------------------------------------
# Fund data tools (6)
# ---------------------------------------------------------------------------

@server.tool()
def wind_search_funds(query: str) -> str:
    """搜索基金（模糊名称或选基需求）。

    Args:
        query: 基金名称或选基条件，如 "南方基金新能源ETF"
    """
    return _call_wind("fund_data", "search_funds", {"query": query})


@server.tool()
def wind_get_fund_info(query: str) -> str:
    """查询基金基本资料（发行日期、费率等）。

    Args:
        query: 基金名称 + 指标，如 "工银双盈债券A的发行日期与费率"
    """
    return _call_wind("fund_data", "get_fund_info", {"query": query})


@server.tool()
def wind_get_fund_nav(query: str) -> str:
    """查询基金净值数据。

    Args:
        query: 基金名称 + 时间范围，如 "华夏沪深300ETF近一年净值走势"
    """
    return _call_wind("fund_data", "get_fund_nav", {"query": query})


@server.tool()
def wind_get_fund_portfolio(query: str) -> str:
    """查询基金持仓明细。

    Args:
        query: 基金名称 + 日期，如 "工银优质成长混合A在2025-06-30的股票投资占比"
    """
    return _call_wind("fund_data", "get_fund_portfolio", {"query": query})


@server.tool()
def wind_compare_funds(query: str) -> str:
    """基金对比分析。

    Args:
        query: 基金名称列表 + 对比维度，如 "对比易方达蓝筹和景顺长城新兴成长近3年收益率"
    """
    return _call_wind("fund_data", "compare_funds", {"query": query})


@server.tool()
def wind_get_fund_performance_attribution(query: str) -> str:
    """查询基金业绩归因分析。

    Args:
        query: 基金名称 + 时间，如 "张坤管理的易方达蓝筹精选2024年业绩归因"
    """
    return _call_wind("fund_data", "get_fund_performance_attribution", {"query": query})


# ---------------------------------------------------------------------------
# Index data tools (5)
# ---------------------------------------------------------------------------

@server.tool()
def wind_search_indices(query: str) -> str:
    """搜索指数。

    Args:
        query: 指数关键词，如 "半导体指数"
    """
    return _call_wind("index_data", "search_indices", {"query": query})


@server.tool()
def wind_get_index_info(query: str) -> str:
    """查询指数行情与技术指标。

    Args:
        query: 指数名称 + 时间 + 指标，如 "沪深300过去10个交易日涨跌幅"
    """
    return _call_wind("index_data", "get_index_info", {"query": query})


@server.tool()
def wind_get_index_constituents(query: str) -> str:
    """查询指数成分股。

    Args:
        query: 指数名称 + 条件，如 "中证500成分股市值前10"
    """
    return _call_wind("index_data", "get_index_constituents", {"query": query})


@server.tool()
def wind_get_index_weights(query: str) -> str:
    """查询指数权重分布。

    Args:
        query: 指数名称 + 维度，如 "沪深300行业权重分布"
    """
    return _call_wind("index_data", "get_index_weights", {"query": query})


@server.tool()
def wind_compare_indices(query: str) -> str:
    """指数对比分析。

    Args:
        query: 指数名称 + 对比维度，如 "沪深300 vs 中证500近5年走势对比"
    """
    return _call_wind("index_data", "compare_indices", {"query": query})


# ---------------------------------------------------------------------------
# Bond data tools (5)
# ---------------------------------------------------------------------------

@server.tool()
def wind_search_bonds(query: str) -> str:
    """搜索债券。

    Args:
        query: 债券关键词，如 "广东地方债"
    """
    return _call_wind("bond_data", "search_bonds", {"query": query})


@server.tool()
def wind_get_bond_info(query: str) -> str:
    """查询债券行情数据。

    Args:
        query: 债券简称/代码 + 指标，如 "23广东11近五日收盘价"
    """
    return _call_wind("bond_data", "get_bond_info", {"query": query})


@server.tool()
def wind_get_bond_rating(query: str) -> str:
    """查询信用评级数据。

    Args:
        query: 债券简称/代码 + 评级指标，如 "华海转债最新信用评级"
    """
    return _call_wind("bond_data", "get_bond_rating", {"query": query})


@server.tool()
def wind_get_bond_yield(query: str) -> str:
    """查询到期收益率。

    Args:
        query: 债券简称/代码 + 时间，如 "26国债01最新到期收益率"
    """
    return _call_wind("bond_data", "get_bond_yield", {"query": query})


@server.tool()
def wind_get_bond_spread(query: str) -> str:
    """查询利差分析。

    Args:
        query: 债券类型 + 对比条件，如 "AA+城投债与国债利差近一年走势"
    """
    return _call_wind("bond_data", "get_bond_spread", {"query": query})


# ---------------------------------------------------------------------------
# Financial docs tools (5)
# ---------------------------------------------------------------------------

@server.tool()
def wind_search_research(query: str) -> str:
    """搜索研究报告。

    Args:
        query: 研报关键词，如 "新能源行业深度研究"
    """
    return _call_wind("financial_docs", "search_research", {"query": query})


@server.tool()
def wind_get_announcements(query: str) -> str:
    """查询上市公司公告。

    Args:
        query: 公告关键词 + 股票，如 "贵州茅台2024年度报告"
    """
    return _call_wind("financial_docs", "get_announcements", {"query": query})


@server.tool()
def wind_get_financial_report(query: str) -> str:
    """获取财报原文。

    Args:
        query: 股票 + 报告期，如 "宁德时代2025年三季报原文"
    """
    return _call_wind("financial_docs", "get_financial_report", {"query": query})


@server.tool()
def wind_get_prospectus(query: str) -> str:
    """获取招股说明书。

    Args:
        query: 公司名 + 招股书类型，如 "中芯国际科创板招股说明书"
    """
    return _call_wind("financial_docs", "get_prospectus", {"query": query})


@server.tool()
def wind_get_credit_report(query: str) -> str:
    """获取信用评级报告。

    Args:
        query: 债券/主体 + 评级机构，如 "中诚信对贵州茅台主体信用评级报告"
    """
    return _call_wind("financial_docs", "get_credit_report", {"query": query})


# ---------------------------------------------------------------------------
# Economic data tools (5)
# ---------------------------------------------------------------------------

@server.tool()
def wind_search_economic_indicators(query: str) -> str:
    """搜索宏观经济指标。

    Args:
        query: 指标关键词，如 "PMI相关指标"
    """
    return _call_wind("economic_data", "search_economic_indicators", {"query": query})


@server.tool()
def wind_get_economic_data(query: str) -> str:
    """下载宏观经济数据。

    Args:
        query: 指标名称 + 时间范围，如 "CPI当月同比202301-202506"
    """
    return _call_wind("economic_data", "get_economic_data", {"query": query})


@server.tool()
def wind_compare_economic_data(query: str) -> str:
    """国别经济数据对比。

    Args:
        query: 对比条件，如 "中美日GDP增速对比"
    """
    return _call_wind("economic_data", "compare_economic_data", {"query": query})


@server.tool()
def wind_get_economic_forecast(query: str) -> str:
    """查询经济预测数据。

    Args:
        query: 预测指标，如 "2025年中国GDP增速预测"
    """
    return _call_wind("economic_data", "get_economic_forecast", {"query": query})


@server.tool()
def wind_get_leading_indicators(query: str) -> str:
    """查询领先指标。

    Args:
        query: 领先指标名称，如 "中国制造业PMI领先指标"
    """
    return _call_wind("economic_data", "get_leading_indicators", {"query": query})


# ---------------------------------------------------------------------------
# Analytics data tools (5)
# ---------------------------------------------------------------------------

@server.tool()
def wind_factor_analysis(query: str) -> str:
    """因子分析。

    Args:
        query: 因子分析条件，如 "沪深300动量因子近一年表现"
    """
    return _call_wind("analytics_data", "factor_analysis", {"query": query})


@server.tool()
def wind_backtest(query: str) -> str:
    """策略回测。

    Args:
        query: 回测条件，如 "双均线策略在沪深300上近5年回测"
    """
    return _call_wind("analytics_data", "backtest", {"query": query})


@server.tool()
def wind_risk_model(query: str) -> str:
    """风险模型。

    Args:
        query: 风险模型条件，如 "沪深300成分股Barra风险因子暴露"
    """
    return _call_wind("analytics_data", "risk_model", {"query": query})


@server.tool()
def wind_portfolio_optimization(query: str) -> str:
    """组合优化。

    Args:
        query: 优化条件，如 "沪深300成分股最小方差组合"
    """
    return _call_wind("analytics_data", "portfolio_optimization", {"query": query})


@server.tool()
def wind_scenario_analysis(query: str) -> str:
    """情景分析。

    Args:
        query: 情景条件，如 "利率上升50bp对银行股影响"
    """
    return _call_wind("analytics_data", "scenario_analysis", {"query": query})


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Wind MCP Server")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    parser.add_argument("--port", type=int, default=8003)
    parser.add_argument("--host", type=str, default="127.0.0.1")
    args = parser.parse_args()

    if not API_KEY:
        print(
            "WARNING: Wind API Key 未配置。"
            "请设置 WIND_API_KEY 环境变量或在 mcp_config.json 中配置密钥。"
            "申请地址：https://aifinmarket.wind.com.cn/#/home",
            file=sys.stderr,
        )

    if args.transport == "sse":
        if args.host in ("0.0.0.0", "::"):
            print(
                f"WARNING: SSE server binding to {args.host} — accessible from ANY network. "
                "Use --host 127.0.0.1 for local-only access or put a reverse proxy in front.",
                file=sys.stderr,
            )
        print(f"Starting Wind SSE server on http://{args.host}:{args.port}/mcp", file=sys.stderr)
        server.run(transport="sse", host=args.host, port=args.port)
    else:
        print("Starting Wind stdio MCP server...", file=sys.stderr)
        server.run(transport="stdio")


if __name__ == "__main__":
    main()
