"""Fallback data sources for networks where East Money push2 APIs are unreachable.

东财 push2 系接口在部分海外网络会被拒连/超时。本模块提供等价的真实数据替代源
（新浪 hq / 腾讯 qt / 同花顺板块 / 巨潮档案 / 新浪财报），server.py 在东财不可达
或调用失败时自动降级到这里。所有返回值均来自实时接口抓取，抓不到的字段直接
缺省，不做任何推算或填充。每条结果带 `_source` 标记数据来源。
"""

import json
import re
from datetime import date
from urllib.parse import quote

import akshare as ak
import pandas as pd
import requests

_UA = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
}

_EM_OK = None


def em_available(force: bool = False) -> bool:
    """Probe East Money push2 reachability once (3s timeout), cache the verdict."""
    global _EM_OK
    if _EM_OK is None or force:
        try:
            r = requests.get(
                "https://push2.eastmoney.com/api/qt/ulist.np/get",
                params={"secids": "1.000001", "fields": "f2"},
                headers=_UA,
                timeout=3,
            )
            _EM_OK = r.status_code == 200 and r.text.strip().startswith("{")
        except Exception:
            _EM_OK = False
    return _EM_OK


def code_prefix(code: str) -> str:
    code = code.strip()
    if code[:2] in ("60", "68", "90") or code[:3] in ("689",):
        return "sh"
    if code[:2] in ("00", "30", "20") or code[:3] in ("001", "002", "003", "301"):
        return "sz"
    if code[:2] in ("43", "83", "87", "92"):
        return "bj"
    return "sh" if code.startswith("6") else "sz"


# ---------------------------------------------------------------------------
# Real-time single-stock quote: Tencent qt (rich) -> Sina hq (basic)
# ---------------------------------------------------------------------------

def quote_alt(code: str) -> dict:
    sym = code_prefix(code) + code
    try:
        return _tencent_quote(sym)
    except Exception:
        return _sina_quote(sym)


def _tencent_quote(sym: str) -> dict:
    r = requests.get(f"https://qt.gtimg.cn/q={sym}", headers=_UA, timeout=10)
    r.encoding = "gbk"
    body = r.text.split('"')[1]
    f = body.split("~")
    if len(f) < 47:
        raise ValueError("tencent quote payload too short")
    out = {
        "代码": f[2],
        "名称": f[1],
        "最新价": f[3],
        "昨收": f[4],
        "今开": f[5],
        "成交量(手)": f[6],
        "涨跌额": f[31],
        "涨跌幅(%)": f[32],
        "最高": f[33],
        "最低": f[34],
        "成交额(万)": f[37],
        "换手率(%)": f[38],
        "市盈率TTM": f[39],
        "市净率": f[46],
        "总市值(亿)": f[45],
        "流通市值(亿)": f[44],
        "日期时间": f[30],
        "_source": "tencent-qt-realtime",
    }
    return {k: v for k, v in out.items() if v not in ("", None)}


def _sina_quote(sym: str) -> dict:
    r = requests.get(
        f"https://hq.sinajs.cn/list={sym}",
        headers={**_UA, "Referer": "https://finance.sina.com.cn"},
        timeout=10,
    )
    r.encoding = "gbk"
    f = r.text.split('"')[1].split(",")
    if len(f) < 32:
        raise ValueError("sina quote payload too short")
    price, prev = float(f[3]), float(f[2])
    return {
        "代码": sym[2:],
        "名称": f[0],
        "最新价": f[3],
        "昨收": f[2],
        "今开": f[1],
        "最高": f[4],
        "最低": f[5],
        "成交量(股)": f[8],
        "成交额(元)": f[9],
        "涨跌额": round(price - prev, 3),
        "涨跌幅(%)": round((price - prev) / prev * 100, 2) if prev else None,
        "日期": f[30],
        "时间": f[31],
        "_source": "sina-hq-realtime",
    }


# ---------------------------------------------------------------------------
# Historical OHLCV: Sina daily (qfq), resampled for weekly/monthly
# ---------------------------------------------------------------------------

def hist_alt(code: str, start_date: str, end_date: str, frequency: str = "daily") -> pd.DataFrame:
    sym = code_prefix(code) + code
    df = ak.stock_zh_a_daily(symbol=sym, start_date=start_date, end_date=end_date, adjust="qfq")
    df = df.rename(columns={
        "date": "日期", "open": "开盘", "high": "最高", "low": "最低",
        "close": "收盘", "volume": "成交量", "amount": "成交额",
    })
    keep = [c for c in ["日期", "开盘", "收盘", "最高", "最低", "成交量", "成交额"] if c in df.columns]
    df = df[keep]
    if frequency in ("weekly", "monthly") and not df.empty:
        rule = "W-FRI" if frequency == "weekly" else "ME"
        df = df.set_index(pd.to_datetime(df["日期"]))
        agg = {"开盘": "first", "收盘": "last", "最高": "max", "最低": "min"}
        if "成交量" in df.columns:
            agg["成交量"] = "sum"
        if "成交额" in df.columns:
            agg["成交额"] = "sum"
        df = df.resample(rule).agg(agg).dropna(how="all").reset_index()
        df["日期"] = df["日期"].dt.date
    df["_source"] = f"sina-daily-qfq-{frequency}"
    return df


# ---------------------------------------------------------------------------
# Financial statements: Sina three statements (primary), THS abstract (backup)
# ---------------------------------------------------------------------------

_STATEMENT_CN = {"income": "利润表", "balance": "资产负债表", "cashflow": "现金流量表"}


def financials_sina(code: str, statement_type: str = "income", period: str = "annual") -> pd.DataFrame:
    sym = code_prefix(code) + code
    df = ak.stock_financial_report_sina(stock=sym, symbol=_STATEMENT_CN.get(statement_type, "利润表"))
    df["报告日"] = df["报告日"].astype(str)
    df = df.sort_values("报告日", ascending=False)
    if period == "annual":
        df = df[df["报告日"].str.endswith("1231")].head(5)
    else:
        df = df.head(8)
    df = df.copy()
    df["_source"] = "sina-financial-report"
    return df


def financials_ths(code: str, period: str = "annual") -> pd.DataFrame:
    indicator = "按年度" if period == "annual" else "按报告期"
    df = ak.stock_financial_abstract_ths(symbol=code, indicator=indicator)
    df = df.sort_values(df.columns[0], ascending=False).head(5 if period == "annual" else 8)
    df = df.copy()
    df["_source"] = f"ths-abstract-{indicator}"
    return df


# ---------------------------------------------------------------------------
# Industry boards: THS
# ---------------------------------------------------------------------------

def industry_alt(industry: str = "") -> pd.DataFrame:
    boards = ak.stock_sector_spot(indicator="新浪行业")
    boards = boards.rename(columns={"板块": "板块名称", "label": "板块代码"})
    if not industry:
        out = boards.copy()
        out["_source"] = "sina-sector-spot"
        return out
    hit = boards[boards["板块名称"].astype(str).str.contains(industry, na=False)]
    if hit.empty:
        # 新浪行业分类粒度较粗，匹配不到时退回同花顺板块名录供改写查询
        names = ak.stock_board_industry_name_ths().rename(columns={"name": "板块名称", "code": "板块代码"})
        names = names[names["板块名称"].astype(str).str.contains(industry, na=False)].copy()
        names["_source"] = "ths-industry-boards(名录，无成分接口，请改用相近新浪行业名)"
        return names
    cons = ak.stock_sector_detail(sector=hit.iloc[0]["板块代码"])
    cons = cons.copy()
    cons["_source"] = f"sina-sector-detail({hit.iloc[0]['板块名称']})"
    return cons


# ---------------------------------------------------------------------------
# Company profile: cninfo (巨潮资讯)
# ---------------------------------------------------------------------------

def stock_info_alt(code: str) -> pd.DataFrame:
    df = ak.stock_profile_cninfo(symbol=code)
    df = df.copy()
    df["_source"] = "cninfo-profile"
    return df


# ---------------------------------------------------------------------------
# Market overview: Sina index spot (major indices snapshot)
# ---------------------------------------------------------------------------

_MAJOR_INDICES = ["sh000001", "sz399001", "sz399006", "sh000300", "sh000688", "sh000016"]


def market_overview_alt() -> dict:
    df = ak.stock_zh_index_spot_sina()
    major = df[df["代码"].isin(_MAJOR_INDICES)]
    return {
        "major_indices": json.loads(major.to_json(orient="records", force_ascii=False)),
        "note": "东财全市场行情接口在当前网络不可达，提供新浪主要指数实时快照替代；个股请用 get_quote。",
        "_source": "sina-index-spot-realtime",
    }


# ---------------------------------------------------------------------------
# ETF/fund data: Sina ETF category
# ---------------------------------------------------------------------------

def fund_alt(fund_code: str) -> pd.DataFrame:
    df = ak.fund_etf_category_sina(symbol="ETF基金")
    hit = df[df["代码"].astype(str).str.contains(fund_code, na=False)]
    hit = hit.copy()
    hit["_source"] = "sina-etf-spot"
    return hit


# ---------------------------------------------------------------------------
# Stock search: Tencent smartbox suggest
# ---------------------------------------------------------------------------

def search_alt(keyword: str) -> list:
    q = quote(keyword.encode("utf-8"))
    r = requests.get(f"https://smartbox.gtimg.cn/s3/?v=2&q={q}&t=all", headers=_UA, timeout=10)
    m = re.search(r'"(.*)"', r.text)
    results = []
    if m and m.group(1) != "N":
        for entry in m.group(1).split("^"):
            parts = entry.split("~")
            if len(parts) >= 3 and parts[0] in ("sh", "sz", "bj", "hk", "us"):
                name = parts[2]
                if "\\u" in name:
                    try:
                        name = name.encode("ascii", errors="ignore").decode("unicode_escape")
                    except Exception:
                        pass
                results.append({
                    "code": parts[1],
                    "name": name,
                    "market": parts[0],
                    "_source": "tencent-smartbox",
                })
    return results
