---
name: china-market-data
description: Query A-share and Chinese financial market data via multiple data sources. Tier-1 paid source is iFind (同花顺, covers stocks/funds/macro/bonds/HK-US/ESG/index-sectors). Tier-2 free source is AkShare (行情/财报/行业/指数). Use whenever the agent needs Chinese financial data — compatible with 沪深 A 股, 科创板, 创业板, 北交所, and 港股通 stocks.
---

# china-market-data

## Data sources (multi-tier)

### Tier 1 — 同花顺 iFind（付费精确数据）
- 覆盖：股票、基金、宏观经济、新闻公告、债券、港美股、指数板块
- MCP 服务：`ifind-mcp`（需 `IFIND_AUTH_TOKEN` 密钥）
- 优势：精确财务数据、一致预期、ESG评级、债券详情、港美股、宏观行业指标
- 并发限制：免费版 2/s，个人版 5/s，企业版 10/s

### Tier 2 — AkShare（免费开源数据）
- 覆盖：A 股行情、财报、行业分类、指数
- MCP 服务：`akshare-mcp`（无需密钥，直接启动）
- 优势：无并发限制，适合高频批量查询

### Tier 3 — 新闻公告（免费）
- MCP 服务：`china-news-mcp`
- 覆盖：个股新闻、市场头条

### 数据源优先级策略

| 场景 | 首选 | 备选 |
|------|------|------|
| 股票财务报表（利润表/资产负债表） | `ifind_get_stock_financials` | `get_financials` |
| 股票基本面/行情 | `ifind_get_stock_info` | `get_stock_info` / `get_quote` |
| 智能选股 | `ifind_search_stocks` | `search_stock`（仅关键词） |
| 股东/股本结构 | `ifind_get_stock_shareholders` | — |
| 风险指标（夏普/Beta/波动率） | `ifind_get_risk_indicators` | — |
| ESG 评级 | `ifind_get_esg_data` | — |
| 基金资料/行情/持仓 | `ifind_search_funds` / `ifind_get_fund_*` | `get_fund_data` |
| 宏观经济指标 | `ifind_search_edb` → `ifind_get_edb_data` | — |
| 债券数据 | `ifind_bond_*` | — |
| 港美股 | `ifind_*_global_stock*` | — |
| 指数/板块 | `ifind_index_data` / `ifind_sector_data` | `get_index_data` |
| 新闻/公告 | `ifind_search_news` / `ifind_search_notice` | `get_stock_news` |
| 行业分类/成分股 | `ifind_sector_data` | `get_industry_stocks` |
| 市场概览（涨跌幅榜） | — | `get_market_overview` |

> 规则：iFind 工具查询失败或超并发时，自动降级到 AkShare。

---

## iFind MCP tools（`mcp__ifind__*`）

### 股票服务

| Tool | Purpose |
|------|---------|
| `ifind_search_stocks` | 自然语言智能选股 |
| `ifind_get_stock_summary` | 股票信息摘要 |
| `ifind_get_stock_info` | 基本资料 / 日频行情 / 技术指标 |
| `ifind_get_stock_shareholders` | 股本结构与股东 |
| `ifind_get_stock_financials` | 财务数据与指标 |
| `ifind_get_risk_indicators` | 风险定量指标 |
| `ifind_get_stock_events` | 上市公司重大事件 |
| `ifind_get_esg_data` | ESG 评级数据 |

### 基金服务

| Tool | Purpose |
|------|---------|
| `ifind_search_funds` | 基金搜索 |
| `ifind_get_fund_profile` | 基金基本资料 |
| `ifind_get_fund_market_performance` | 基金行情与业绩 |
| `ifind_get_fund_ownership` | 基金份额与持有人 |
| `ifind_get_fund_portfolio` | 基金持仓明细 |
| `ifind_get_fund_financials` | 基金财务指标 |
| `ifind_get_fund_company_info` | 基金公司信息 |

### 宏观经济 / 行业经济指标

| Tool | Purpose |
|------|---------|
| `ifind_search_edb` | 指标模糊搜索（先搜再查） |
| `ifind_get_edb_data` | 指标数据查询 |

### 新闻公告

| Tool | Purpose |
|------|---------|
| `ifind_search_news` | 新闻资讯语义检索 |
| `ifind_search_notice` | 上市公司公告语义检索 |
| `ifind_search_trending_news` | 热点事件资讯 |

### 债券

| Tool | Purpose |
|------|---------|
| `ifind_bond_basic_info` | 债券基本信息 |
| `ifind_bond_market_data` | 债券行情与估值 |
| `ifind_bond_financial_data` | 发债主体财务 |
| `ifind_bond_special_data` | 可转债/信用债特殊条款 |

### 港美股

| Tool | Purpose |
|------|---------|
| `ifind_search_global_stocks` | 港美股智能选股 |
| `ifind_global_stock_profile` | 港美股基本资料 |
| `ifind_global_stock_quotes` | 港美股行情 |
| `ifind_global_stock_financial` | 港美股财务 |
| `ifind_global_stock_events` | 港美股公告事件 |

### 指数板块

| Tool | Purpose |
|------|---------|
| `ifind_index_data` | 指数行情 / 技术指标 / 估值 |
| `ifind_sector_data` | 板块行情 / 成分股分析 |

---

## AkShare MCP tools（`mcp__akshare__*`）

| Tool | Purpose |
|------|---------|
| `search_stock` | Search A-share stocks by code or name |
| `get_quote` | Real-time quote (price, PE, PB, market cap) |
| `get_historical_data` | OHLCV history (daily/weekly/monthly), forward-adjusted |
| `get_financials` | 利润表/资产负债表/现金流量表 |
| `get_industry_stocks` | 行业分类 & 成分股 (东方财富行业) |
| `get_index_data` | 指数行情 (上证/深证/创业板/科创50) |
| `get_stock_info` | 公司基本信息 & 业务范围 |
| `get_market_overview` | 涨幅榜/跌幅榜/成交额榜 |
| `get_fund_data` | 公募基金/ETF 行情 |

The **china-news** MCP server provides:

| Tool | Purpose |
|------|---------|
| `get_stock_news` | 个股新闻 |
| `get_market_headlines` | 市场头条 |

---

## Workflow

### 1. Identify the stock/security

```python
# iFind — 自然语言选股
ifind_search_stocks(query="电子行业市值大于100亿")

# AkShare — 关键词搜索
search_stock(keyword="茅台")
```

### 2. Pull market data

```python
# iFind — 精确财务
ifind_get_stock_financials(query="贵州茅台2024年年报的ROE、ROA、净利润增速")

# AkShare — 历史行情
get_historical_data(ticker="600519", start_date="20240101", end_date="20241231", frequency="daily")

# AkShare — 财务报表
get_financials(ticker="600519", statement_type="income", period="annual")
```

### 3. Industry / peer context

```python
# iFind — 板块分析
ifind_sector_data(query="白酒板块的成分股个数及过去5日平均涨跌幅")

# AkShare — 行业成分
get_industry_stocks(industry="白酒")

# iFind — 指数
ifind_index_data(query="沪深300过去10个交易日的涨跌幅和收盘点数")
```

### 4. Macro / EDB indicators

```python
# 先搜索再取数
ifind_search_edb(query="新能源汽车产量相关指标")
ifind_get_edb_data(query="新能源汽车产量当月值（202301-202506）")
```

### 5. News and sentiment

```python
# iFind — 公告语义检索
ifind_search_notice(query="贵州茅台2024年年度报告 分红", time_start="2025-01-01", time_end="2025-12-31", size=5)

# AkShare — 个股新闻
get_stock_news(ticker="600519")
```

## Note on data coverage

- **A-shares**: Full coverage via both iFind and AkShare (SH, SZ, BJ, STAR, ChiNext)
- **Hong Kong stocks (港股通)**: iFind 完整覆盖；AkShare 部分覆盖
- **US-listed Chinese ADRs**: iFind 通过 `ifind_global_stock_*` 覆盖
- **Funds**: iFind 完整覆盖（资料/行情/持仓/持有人）；AkShare 仅 ETF 行情
- **Bonds**: iFind 覆盖信用债/可转债/回购；AkShare 需扩展
- **ESG**: 仅 iFind 提供
- **宏观经济**: iFind EDB 覆盖最广；AkShare 有基础宏观数据
