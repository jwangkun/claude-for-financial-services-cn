---
name: china-pptx-author
description: >
  Generic PowerPoint authoring skill for A-share investment analysis and pitch decks.
  Creates professional 路演PPT / 投资分析PPT for any A-share company using live data
  from iFind MCP (Tier-1) and AkShare MCP (Tier-2 fallback) tools. All company-specific values are parameterized — never hardcoded.
  Triggers on "A股PPT制作", "投资PPT", "制作PPT", "路演PPT", "pitch deck",
  "PowerPoint [company/ticker]", or any request to create slides for a Chinese stock.
  When invoked, use the `generate_a_share_ppt` script with --company and --ticker args.
---

# china-pptx-author

## Purpose

Generate professional **A股投资分析PPT** for any listed company.
This skill is a generic engine — every output is driven by two parameters:

| Parameter | Example | Description |
|-----------|---------|-------------|
| `{{COMPANY_NAME}}` | {{COMPANY_NAME}} | Full Chinese company name (e.g., 贵州茅台) |
| `{{TICKER}}` | {{TICKER}} | 6-digit A-share code (e.g., 600519) |
| `{{OUTPUT_PATH}}` | ./output.pptx | Where to save the PPTX file |

All financial figures, price data, peer valuations, and company descriptions are
fetched live from iFind / AkShare / public APIs. **Nothing is hardcoded.**

---

## Data Pipeline

### Step 1: Resolve Company Info

```python
# MCP tool: search_stock
search_stock(keyword="{{COMPANY_NAME}}")
# → confirms ticker, exchange (SH/SZ), full legal name
```

```python
# MCP tool: get_quote
get_quote(ticker="{{TICKER}}")
# → live price, PE, PB, market cap, turnover, 52-week range
```

```python
# MCP tool: get_financials
get_financials(ticker="{{TICKER}}", statement_type="income", period="annual")
# → annual income statement: revenue, net profit, margins, EPS, etc.
get_financials(ticker="{{TICKER}}", statement_type="balance", period="annual")
# → balance sheet: assets, liabilities, equity
get_financials(ticker="{{TICKER}}", statement_type="cashflow", period="annual")
# → cash flow statement
```

```python
# MCP tool: get_historical_data
get_historical_data(ticker="{{TICKER}}", frequency="weekly", start_date="{{START_DATE}}", end_date="{{END_DATE}}")
# → OHLCV price history for trend charts
```

```python
# MCP tool: get_industry_stocks
get_industry_stocks(industry="{{INDUSTRY_NAME}}")
# → peer companies in the same sector for comps analysis
```

### Step 2: Fetch Peer Data

```python
# For each peer returned by get_industry_stocks, call get_quote to get PE/PB
# Focus on top 5-8 comparable companies by revenue/market cap
```

### Step 3: Generate Charts

Use matplotlib to create:
1. **Revenue & Profit trend** — from `get_financials(income)`
2. **Margin trends** — gross margin, net margin, ROE over time
3. **Growth rates** — YoY revenue and profit growth
4. **Peer comparison** — horizontal bar chart of PE and PB vs peers
5. **Price trend** — from `get_historical_data`
6. **Valuation range** — football field based on peer PE distribution

All chart titles and labels must include `{{COMPANY_NAME}}` dynamically.

---

## Presentation Structure

The default deck is **12 slides**. Adjust sections based on `deck_type` parameter.

### Template (parameterized)

```
Slide 1:  Cover
    {{COMPANY_NAME}} ({{TICKER}}.{{EXCHANGE}})
    {{REPORT_TITLE}}  |  {{DATE}}
    机密文件 | 仅供内部参考

Slide 2:  投资摘要 (Investment Highlights)
    • {{HIGHLIGHT_1}}
    • {{HIGHLIGHT_2}}
    • {{HIGHLIGHT_3}}
    目标价: ¥{{TARGET_PRICE_LOW}} - ¥{{TARGET_PRICE_HIGH}}
    评级: {{RATING}}

Slide 3:  公司概览 (Company Overview)
    {{COMPANY_DESCRIPTION}}
    主营业务: {{MAIN_BUSINESS}}
    成立时间 | 上市板块 | 控股股东 (all from search_stock / get_quote)

Slide 4:  行业分析 (Industry Overview)
    {{INDUSTRY_NAME}} — market size, trends, policy
    Data from: get_industry_stocks result analysis

Slide 5:  财务分析 (Financial Summary)
    [Chart: Revenue & Profit]  [Chart: Margin Trends]
    [Chart: Growth Rates]
    All data from get_financials(income, annual)

Slide 6:  运营指标 (Operating Metrics)
    Segment breakdown, KPIs (if available from financials)

Slide 7:  可比公司估值 (Trading Comparables)
    [Chart: Peer PE/PB comparison]
    Table: Peer | Market Cap | P/E | P/B | EV/EBITDA

Slide 8:  估值分析 (Valuation)
    [Chart: Football field]
    DCF / PE / PB ranges derived from peer analysis

Slide 9:  投资逻辑 (Investment Thesis)
    3-5 key investment bullets derived from data analysis

Slide 10: 风险提示 (Risk Factors)
    Generic risk categories, customized from industry context

Slide 11: 投资建议 (Recommendation)
    评级 + 目标价 range + upside calculation

Slide 12: 免责声明 (Disclaimer)
    Standard A-share research disclaimer
```

### Deck Type Variants

| deck_type | Slides | Audience | Key sections |
|-----------|--------|----------|--------------|
| `pitch` | 12 | Clients/Investors | Full deck above |
| `deep_dive` | 20-30 | Internal IC | Add: detailed financial model, sensitivity, scenario analysis |
| `initiation` | 15-20 | Internal | Emphasize: company overview, industry, thesis |
| `sector` | 10-15 | Internal | Emphasize: industry analysis, peer comparison |
| `morning_note` | 5-8 | Internal | Condensed: key data, thesis, recommendation |

---

## Design Standards

| Element | Standard |
|---------|----------|
| 模板 | Corporate blue/gold theme (configurable) |
| 字体 | 微软雅黑 / system default sans-serif |
| 字号 | Title 24-32pt, Body 12-16pt |
| 配色 | Primary: #1A3C6E (deep blue), Accent: #C8A032 (gold) |
| 每页标题 | Chinese + English bilingual |
| 数据来源 | Cite at bottom of each data slide |
| 页码 | Bottom center |
| 免责声明 | Last slide, mandatory |

---

## Content Rules

| Rule | Guideline |
|------|-----------|
| 每页一个主题 | One idea per slide |
| 标题先行 | Clear headline at top of every slide |
| 数据可视化 | Charts > tables > text |
| 中文为主 | Primary language Chinese, with English subtitles |
| 术语统一 | Use standard A-share terminology (see below) |
| 不编造数据 | If data unavailable from API, show "N/A" or omit |

### A-Share Terminology

| English | Chinese |
|---------|---------|
| Revenue | 营业收入 |
| Net income (attributable) | 归母净利润 |
| Gross margin | 毛利率 |
| Net margin | 净利率 |
| ROE | ROE (净资产收益率) |
| EPS | 每股收益 |
| P/E | 市盈率 |
| P/B | 市净率 |
| Target price | 目标价 |
| Rating | 评级 |
| Upside | 上行空间 |
| YoY | 同比 |
| QoQ | 环比 |
| Market cap | 总市值 |
| Turnover | 换手率 |

---

## Quality Checklist

Before delivering the PPT:
- [ ] All `{{PLACEHOLDER}}` replaced with live data
- [ ] Charts readable, labeled, sourced
- [ ] Numbers consistent across slides (revenue matches across chart/table/text)
- [ ] Company name and ticker correct throughout
- [ ] Peer data reflects actual industry comparables
- [ ] Disclaimer slide included
- [ ] File named: `{{COMPANY_NAME}}_{{TICKER}}_{{REPORT_TITLE}}.pptx`

---

## Usage

Invoke the generation script (from project root):

```bash
cd {{PROJECT_ROOT}} && python3 scripts/generate_a_share_ppt.py \
  --company "{{COMPANY_NAME}}" \
  --ticker "{{TICKER}}" \
  --industry "{{INDUSTRY_NAME}}" \
  --output "{{OUTPUT_PATH}}" \
  --type {{DECK_TYPE}} \
  --title "{{REPORT_TITLE}}"
```

Required args: `--company`, `--ticker`
Optional: `--industry` (for peer lookup), `--output`, `--type` (pitch/deep_dive/initiation), `--title`

If `--industry` is omitted, the script attempts to infer it from the company's sector classification.
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
