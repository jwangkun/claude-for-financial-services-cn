---
name: china-comps
description: Comparable company analysis for A-share stocks. Uses AkShare MCP to build peer groups, pull financial data, compute valuation multiples (PE, PB, PS), and assess relative value within a Chinese industry sector.
---

# china-comps

## Data Sources (Multi-Tier)

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）
Use ifind MCP when a valid `IFIND_AUTH_TOKEN` is configured.

```python
ifind_get_stock_info(ticker)             → Company profile, multiples
ifind_get_stock_financials(ticker, ...)  → Revenue, net income, margins
ifind_search_stocks(query)               → Industry-wide stock screening
```

### Tier 2 — AkShare（免费开源数据）
Fallback when iFind is unavailable.

```python
get_quote(ticker)              → Price, PE, PB, market cap
get_financials(ticker, "income", "annual")  → Revenue, net income
get_financials(ticker, "balance", "annual") → Book value
get_stock_info(ticker)         → Business description
```

> **数据源模式开关**: 当环境变量 `IFIND_DATA_SOURCE_MODE=ifind-only` 时，仅使用 iFind 数据源，禁用 AkShare 降级。

---
name: china-comps
description: Comparable company analysis for A-share stocks. Uses the AkShare MCP to build peer groups, pull financial data, compute valuation multiples (PE, PB, PS), and assess relative value within a Chinese industry sector. Use instead of the original comps-analysis skill when dealing with Chinese-listed equities.
---

# china-comps

## Workflow

### 1. Define the peer group

Start with the target stock, then use `get_industry_stocks(industry="<行业名称>")` to get the full peer set for that industry. Common industry names used in the 东方财富 classification:

| Industry | Example Leaders |
|----------|-----------------|
| 白酒 | {{SECTOR_LEADER}}, {{CHALLENGER_1}}, {{CHALLENGER_2}} |
| 半导体 | {{SECTOR_LEADER}}, {{CHALLENGER_1}}, {{CHALLENGER_2}} |
| 电池 | {{SECTOR_LEADER}}, {{CHALLENGER_1}}, {{CHALLENGER_2}} |
| 银行 | {{SECTOR_LEADER}}, {{CHALLENGER_1}}, {{CHALLENGER_2}} |
| 证券 | {{SECTOR_LEADER}}, {{CHALLENGER_1}}, {{CHALLENGER_2}} |
| 保险 | {{SECTOR_LEADER}}, {{CHALLENGER_1}}, {{CHALLENGER_2}} |
| 医疗器械 | {{SECTOR_LEADER}}, {{CHALLENGER_1}}, {{CHALLENGER_2}} |
| 光伏设备 | {{SECTOR_LEADER}}, {{CHALLENGER_1}}, {{CHALLENGER_2}} |
| 汽车整车 | {{SECTOR_LEADER}}, {{CHALLENGER_1}}, {{CHALLENGER_2}} |
| 软件开发 | {{SECTOR_LEADER}}, {{CHALLENGER_1}}, {{CHALLENGER_2}} |

### 2. Pull financial data for each peer

```
For each ticker in the peer set:
  get_quote(ticker)         → price, PE, PB, market cap
  get_financials(ticker, "income", "annual")     → revenue, net income
  get_financials(ticker, "balance", "annual")    → book value, debt
  get_stock_info(ticker)    → business description
```

### 3. Compute standard multiples

| Multiple | Formula | AkShare source field |
|----------|---------|---------------------|
| PE (TTM) | Price / EPS TTM | `get_quote` → 动态市盈率 |
| PB | Price / Book Value per share | `get_quote` → 市净率 |
| PS (TTM) | Market Cap / Revenue TTM | Compute from market cap + revenue |
| EV/EBITDA | Enterprise Value / EBITDA | Compute from market cap + debt - cash |
| Dividend Yield | DPS / Price | `get_quote` → 股息率 |

### 4. Present the comps table

Sort by market cap (largest first). Flag outliers (>2 standard deviations from mean). Include:
- Ticker, company name, price
- Market cap (亿 CNY)
- PE, PB, PS
- Revenue growth %, Net margin %
- 52-week high/low

### 5. Relative value assessment

- If target's PE is >1 std dev above peer mean → potentially overvalued
- If target's PE is >1 std dev below peer mean → potentially undervalued
- Flag companies with negative earnings separately
- Compare PEG ratios (PE / growth rate) when growth data is available

## Notes

- All financial data from AkShare is based on Chinese accounting standards (CAS), not IFRS/US GAAP
- Chinese market has 涨跌停 limits (±10% for main board, ±20% for ChiNext/STAR)
- A-share market cap includes both circulating (流通) and non-circulating shares — check if the user wants 流通市值 or 总市值
- For cross-market comps (A-share vs HK-listed), note that A-shares typically trade at a premium
