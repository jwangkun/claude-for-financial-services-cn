"""AkShare MCP Server — Chinese financial data via MCP protocol.

Provides A-share market data, financial statements, industry classification,
and historical pricing. All data sourced from AkShare (open-source Chinese
financial data library, backed by East Money / 东方财富).

Usage:
    # Run as stdio server (for local Claude Desktop integration)
    python server.py

    # Run as HTTP/SSE server (for managed-agent deployment)
    python server.py --transport sse --port 8000
"""

import argparse
import json
import sys
from datetime import date, datetime
from typing import Any

import akshare as ak
import pandas as pd

import cn_sources as cn

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    from mcp import FastMCP

server = FastMCP("akshare-mcp", instructions="Chinese financial data via AkShare (A-share stocks, indices, fundamentals)")


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def _df_to_json(df: pd.DataFrame) -> str:
    """Convert a DataFrame to a JSON string (records format, dates serialized)."""
    if df is None or df.empty:
        return json.dumps([], ensure_ascii=False)
    df = df.where(pd.notna(df), None)
    return json.dumps(df.to_dict(orient="records"), ensure_ascii=False, default=str)


def _clean_code(code: str) -> str:
    """Normalize stock code (strip exchange prefix if present)."""
    return code.strip().upper().replace("SH", "").replace("SZ", "").replace("BJ", "").replace(".", "")


def _guess_code(ticker: str) -> str:
    """Try to infer the correct stock code format for AkShare.

    AkShare internally uses the a-shaare code without prefix, but different
    functions expect different formats — some need the market suffix (.SZ/.SH),
    some don't. We let AkShare handle this.
    """
    return ticker.strip().upper()


# ---------------------------------------------------------------------------
# MCP Tools
# ---------------------------------------------------------------------------

@server.tool()
def search_stock(keyword: str) -> str:
    """Search A-share stocks by keyword (code or name pinyin/Chinese).

    Returns matching stocks with code, name, and market.
    """
    try:
        if cn.em_available():
            try:
                df = ak.stock_info_a_code_name()
                mask = df["code"].astype(str).str.contains(keyword, case=False) | df["name"].str.contains(keyword, case=False)
                return _df_to_json(df[mask].head(20))
            except Exception:
                pass
        return json.dumps(cn.search_alt(keyword), ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": f"search_stock failed: {e}"}, ensure_ascii=False)


@server.tool()
def get_quote(ticker: str) -> str:
    """Get real-time A-share stock quote.

    Returns price, change %, volume, turnover, PE, PB, market cap, and more.
    """
    try:
        if cn.em_available():
            try:
                df = ak.stock_zh_a_spot_em()
                df = df[df["代码"] == ticker]
                if not df.empty:
                    return _df_to_json(df)
            except Exception:
                pass
        return json.dumps(cn.quote_alt(_clean_code(ticker)), ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": f"get_quote failed: {e}"}, ensure_ascii=False)


@server.tool()
def get_historical_data(ticker: str, start_date: str = "", end_date: str = "", frequency: str = "daily") -> str:
    """Get historical OHLCV price data for an A-share stock.

    Args:
        ticker: Stock code (e.g., "000001" for Ping An, "600519" for Maotai).
        start_date: Start date in YYYYMMDD format. Defaults to 1 year ago.
        end_date: End date in YYYYMMDD format. Defaults to today.
        frequency: "daily" (default), "weekly", "monthly".
    """
    try:
        if not end_date:
            end_date = date.today().strftime("%Y%m%d")
        if not start_date:
            start = date.today().replace(year=date.today().year - 1)
            start_date = start.strftime("%Y%m%d")
        if cn.em_available():
            try:
                df = ak.stock_zh_a_hist(symbol=ticker, period=frequency, start_date=start_date, end_date=end_date, adjust="qfq")
                return _df_to_json(df)
            except Exception:
                pass
        return _df_to_json(cn.hist_alt(_clean_code(ticker), start_date, end_date, frequency))
    except Exception as e:
        return json.dumps({"error": f"get_historical_data failed: {e}"}, ensure_ascii=False)


@server.tool()
def get_financials(ticker: str, statement_type: str = "income", period: str = "annual") -> str:
    """Get financial statement data for an A-share stock.

    Args:
        ticker: Stock code (e.g., "600519").
        statement_type: "income" (利润表), "balance" (资产负债表), "cashflow" (现金流量表).
        period: "annual" (年报), "quarterly" (季报).
    """
    try:
        # 新浪三大报表为主源（分表、字段全、海外网络可达）。
        # 同花顺摘要接口 indicator 仅支持 按报告期/按年度/按单季度，旧实现传表名会被忽略，
        # 且其"报告期"列为年份整数，按 "12-31" 过滤年报必为空，故仅以修正后的同花顺摘要兜底。
        try:
            df = cn.financials_sina(_clean_code(ticker), statement_type, period)
            if df is not None and not df.empty:
                return _df_to_json(df)
        except Exception:
            pass
        df = cn.financials_ths(_clean_code(ticker), period)
        if df is not None and not df.empty:
            return _df_to_json(df)
        return json.dumps({"error": "no financial data returned"}, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": f"get_financials failed: {e}"}, ensure_ascii=False)


@server.tool()
def get_industry_stocks(industry: str = "") -> str:
    """List all stocks in a given industry (东方财富行业分类).

    Args:
        industry: Industry name in Chinese (e.g., "半导体", "银行", "白酒").
                  If empty, returns all available industry names.
    """
    try:
        if cn.em_available():
            try:
                board_df = ak.stock_board_industry_name_em()
                if not industry:
                    return _df_to_json(board_df[["板块名称", "板块代码", "涨跌幅", "上涨家数", "下跌家数"]].head(50))
                return _df_to_json(ak.stock_board_industry_cons_em(symbol=industry))
            except Exception:
                pass
        return _df_to_json(cn.industry_alt(industry))
    except Exception as e:
        return json.dumps({"error": f"get_industry_stocks failed: {e}"}, ensure_ascii=False)


@server.tool()
def get_index_data(index_code: str = "000001") -> str:
    """Get A-share index historical data.

    Args:
        index_code: Index code (default "000001" for 上证指数).
                    Common: 000001(上证), 399001(深证), 399006(创业板), 000688(科创50).
    """
    try:
        mapping = {
            "000001": "sh000001",
            "399001": "sz399001",
            "399006": "sz399006",
            "000688": "sh000688",
            "000300": "sh000300",
            "000016": "sh000016",
        }
        symbol = mapping.get(index_code, f"sh{index_code}" if index_code.startswith("00") else index_code)
        df = ak.stock_zh_index_daily(symbol=symbol)
        return _df_to_json(df.tail(500))
    except Exception as e:
        return json.dumps({"error": f"get_index_data failed: {e}"}, ensure_ascii=False)


@server.tool()
def get_stock_info(ticker: str) -> str:
    """Get company profile and basic information for an A-share stock.

    Returns: industry, market cap, listing date, business scope, etc.
    """
    try:
        if cn.em_available():
            try:
                return _df_to_json(ak.stock_individual_info_em(symbol=ticker))
            except Exception:
                pass
        return _df_to_json(cn.stock_info_alt(_clean_code(ticker)))
    except Exception as e:
        return json.dumps({"error": f"get_stock_info failed: {e}"}, ensure_ascii=False)


@server.tool()
def get_market_overview() -> str:
    """Get A-share market overview — top gainers, top losers, most active by volume.

    Returns: ranked list of stocks with price, change %, volume, and turnover.
    """
    try:
        if cn.em_available():
            try:
                df = ak.stock_zh_a_spot_em()
                if not df.empty:
                    top_gainers = df.nlargest(10, "涨跌幅").to_dict(orient="records")
                    top_losers = df.nsmallest(10, "涨跌幅").to_dict(orient="records")
                    most_active = df.nlargest(10, "成交额").to_dict(orient="records")
                    return json.dumps({
                        "top_gainers": [{k: str(v) for k, v in r.items()} for r in top_gainers],
                        "top_losers": [{k: str(v) for k, v in r.items()} for r in top_losers],
                        "most_active": [{k: str(v) for k, v in r.items()} for r in most_active],
                    }, ensure_ascii=False)
            except Exception:
                pass
        return json.dumps(cn.market_overview_alt(), ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": f"get_market_overview failed: {e}"}, ensure_ascii=False)


@server.tool()
def get_fund_data(fund_code: str) -> str:
    """Get Chinese public fund (公募基金) basic data.

    Args:
        fund_code: Fund code (e.g., "000001" for Huitianfu).
    """
    try:
        if cn.em_available():
            try:
                df = ak.fund_etf_spot_em()
                result = df[df["代码"] == fund_code]
                if not result.empty:
                    return _df_to_json(result)
            except Exception:
                pass
        result = cn.fund_alt(fund_code)
        if result.empty:
            return json.dumps({"error": f"fund {fund_code} not found"}, ensure_ascii=False)
        return _df_to_json(result)
    except Exception as e:
        return json.dumps({"error": f"get_fund_data failed: {e}"}, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="AkShare MCP Server")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio", help="Transport protocol")
    parser.add_argument("--port", type=int, default=8000, help="Port for SSE transport")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host for SSE transport")
    args = parser.parse_args()

    if args.transport == "sse":
        print(f"Starting SSE server on http://{args.host}:{args.port}/mcp", file=sys.stderr)
        server.run(transport="sse", host=args.host, port=args.port)
    else:
        print("Starting stdio MCP server...", file=sys.stderr)
        server.run(transport="stdio")


if __name__ == "__main__":
    main()
