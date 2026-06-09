---
name: china-dcf
description: DCF valuation model for A-share stocks using Chinese financial data. Uses AkShare MCP for financial statements, WACC inputs (risk-free rate from China government bond yields), and growth projections. Use instead of the original dcf-model skill for Chinese equities.
---

# china-dcf

## Data Sources (Multi-Tier)

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）
```python
ifind_get_stock_financials(ticker, ...)  -> Historical financials
ifind_get_stock_info(ticker)             -> Market data, shares outstanding
ifind_get_risk_indicators(ticker)        -> Beta, volatility for WACC
```

### Tier 2 - AkShare (free, open-source, fallback)
```python
get_financials(ticker, "income", "annual")     -> Historical P and L
get_financials(ticker, "balance", "annual")    -> Historical BS
get_quote(ticker)                              -> Market cap, price
```

> Data source mode switch: When env var `IFIND_DATA_SOURCE_MODE=ifind-only`, use iFind exclusively.
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare




## Key differences from US-market DCF

| Parameter | US DCF Convention | China DCF Convention |
|-----------|-------------------|---------------------|
| Risk-free rate | US 10Y Treasury | China 10Y CGB (国债收益率, ~2.5-3.5%) |
| Equity risk premium | ~5-6% (historical US) | ~6-8% (China A-share ERP) |
| Tax rate | US corporate 21% | China corporate 25% (高新技术企业 15%) |
| Terminal growth | US GDP growth (~2%) | China GDP growth (~4-5%) |
| Currency | USD | CNY |
| Reporting standard | US GAAP / IFRS | CAS (中国会计准则) |

## Workflow

### Step 1: Pull financials

```
get_financials(ticker, "income", "annual")   → last 5 years
get_financials(ticker, "balance", "annual")
get_financials(ticker, "cashflow", "annual")
```

### Step 2: Get market data

```
get_quote(ticker)  → price, market cap, PE, PB
get_index_data("000001") → benchmark return for beta estimation
```

### Step 3: Build projections

- Project revenue using historical growth rates adjusted for China macro outlook
- Assume 65-75% operating margin for 白酒 / high-margin sectors
- Assume 15-25% operating margin for manufacturing
- CapEx as % of revenue: check historical from cashflow statement

### Step 4: Compute WACC

```
WACC = E/(D+E) * Ke + D/(D+E) * Kd * (1 - tax_rate)

Ke = Rf + β * ERP
  Rf   = China 10Y CGB yield (use ak.bond_zh_us_rate() or web search for latest)
  β    = regression on 上证指数 returns (or use comparable firm beta)
  ERP  = 6-8% (China-specific equity risk premium)

Kd   = China 5Y corporate bond yield + credit spread
```

### Step 5: Terminal value

```
Terminal Value = FCF_(n+1) / (WACC - g)
g = 3-4% for mature Chinese companies (China nominal GDP growth)
```

## Notes

- Chinese fiscal year ends December 31 for most companies
- 北向资金 (Northbound flow) data can be used as sentiment indicator
- 商誉 (goodwill) impairments are common in China M&A — flag if goodwill > 30% of equity
- Some Chinese financial statements are reported in 千元 (thousands of CNY) vs 元 — check the unit
