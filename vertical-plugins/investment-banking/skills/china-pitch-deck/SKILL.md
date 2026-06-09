---
name: china-pitch-deck
description: Populate A-share investment banking pitch deck templates with data from source files. Adapted from the original pitch-deck skill for Chinese companies, A-share market data, and Chinese business context. Triggers on "A股Pitch Deck", "路演PPT", "pitch deck China", "pitch deck A-share", or "fill pitch template for [company]".
---

# china-pitch-deck

## Purpose

Populate **A股投行 Pitch Deck / 路演材料** templates with financial data, charts, and narrative for Chinese target companies.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_stock_info(ticker)                        → Company overview
get_quote(ticker)                            → Current valuation, multiples
get_historical_data(ticker)                  → Stock performance chart data
get_financials(ticker, "income", "annual")    → Revenue, profit trends
get_financials(ticker, "balance", "annual")   → Balance sheet
get_financials(ticker, "cashflow", "annual")  → Cash flow
get_industry_stocks(industry="...")            → Peer companies
```

### Secondary Sources

- **巨潮资讯** — annual reports, IR presentations
- **公司官网** — investor relations materials
- **券商研报** — existing research for reference
- **Wind / Choice** — comprehensive data

## Workflow

### Step 1: Understand the Template

**Typical A-share pitch deck sections:**

| Slide # | Section | Content |
|---------|---------|---------|
| 1 | Cover | Company name, ticker, transaction overview |
| 2 | Executive Summary | Investment highlights, valuation summary |
| 3 | Company Overview | Business model, history, structure |
| 4 | Industry Overview | Market size, trends, policy |
| 5 | Competitive Landscape | Market share, positioning |
| 6 | Financial Summary | Revenue, profit, margins (historical) |
| 7 | Operating Metrics | Key KPIs by segment |
| 8 | Trading Comparables | Peer multiples, dispersion |
| 9 | Precedent Transactions | Comparable M&A |
| 10 | DCF Valuation | Football field, sensitivity |
| 11 | Transaction Rationale | Why now, why this buyer |
| 12 | Risks & Mitigations | Key risks and how to address |

### Step 2: Gather Data

**For each section, pull required data:**

```python
# Company data
get_stock_info(ticker)
get_quote(ticker)

# Financial history
get_financials(ticker, "income", "annual")
get_financials(ticker, "balance", "annual")
get_financials(ticker, "cashflow", "annual")

# Peer data
peers = get_industry_stocks(industry="...")
for peer in peers:
    get_quote(peer["代码"])
    get_financials(peer["代码"], "income", "annual")
```

### Step 3: Populate Each Slide

**Slide-by-slide guidelines:**

#### Slide 1: Cover
- Company name and logo
- Stock code and listing board
- Transaction description
- Date and confidentiality

#### Slide 2: Executive Summary
- 3-5 investment highlights
- Key financial metrics (revenue, profit, growth)
- Valuation summary (range, midpoint)
- Recommendation

#### Slide 3: Company Overview
- Business description (主营业务)
- History and milestones
- Organizational structure
- Management team
- Geographic footprint

#### Slide 4: Industry Overview
- Market size and growth (市场规模, 增速)
- Key trends (发展趋势)
- Policy environment (政策环境)
- A-share sector context

#### Slide 5: Competitive Landscape
- Market share map
- Competitive positioning
- Key competitors with comparison table
- Competitive advantages (竞争优势)

#### Slide 6: Financial Summary
- Revenue and profit history (3-5 years)
- Margin trends
- Growth rates
- Key ratio trends

#### Slide 7: Operating Metrics
- Segment revenue breakdown
- Volume/unit metrics
- Capacity/utilization
- Quality metrics (ROE, FCF)

#### Slide 8: Trading Comparables
- Peer comparison table
- Scatter plot (Growth vs Multiple)
- Multiple dispersion analysis
- Where target trades vs peers

#### Slide 9: Precedent Transactions
- Comparable China M&A deals
- Transaction multiples
- Premiums paid
- Strategic rationale

#### Slide 10: DCF & Football Field
- DCF valuation summary
- Football field chart
- Sensitivity tables
- Target price range

#### Slide 11: Transaction Rationale
- Strategic fit
- Synergy potential
- Why now
- Value creation plan

#### Slide 12: Risks
- Key risk factors
- Mitigation strategies
- Probability and impact assessment

### Step 4: Design & Formatting

**Design principles:**
- Consistent with firm's pitch deck template
- Clean, professional appearance
- Data-driven, not text-heavy
- Key numbers prominent
- Charts simple and readable

**China-specific formatting:**
- 人民币 (CNY) as currency
- A-share terminology (主板/创业板/科创板)
- Chinese company names with tickers
- Policy context where relevant

### Step 5: Quality Check

**Before finalizing:**
- [ ] All data sourced from 巨潮 / AkShare
- [ ] Charts readable and properly labeled
- [ ] Numbers consistent across slides
- [ ] Valuation analysis sound
- [ ] Design consistent with template
- [ ] Confidentiality marked
- [ ] All citations included

## China-Specific Pitch Considerations

### Transaction Context

| Transaction Type | A-share Considerations |
|-----------------|------------------------|
| 借壳上市 (Backdoor listing) | Shell company analysis, regulatory timeline |
| 吸收合并 (Merger) | Exchange ratio, shareholder approval |
| 重大资产重组 (Major asset restructuring) | CSRC review, disclosure requirements |
| 私有化 (Take-private) | Premium required, relisting timeline |
| 产业并购 (Strategic M&A) | Synergy focus, anti-monopoly review |

### Valuation Benchmarks

**A-share M&A premiums:**
- Control premium: 20-40% typical
- Strategic premium: 30-50%
- Take-private: 30-50% minimum
- Distressed: varies widely

**Comparable multiples (China):**
- EV/Revenue: 2-10x (varies by sector)
- EV/EBITDA: 6-15x (typical for industrials)
- P/E: 10-40x (sector dependent)

### Regulatory Context

**Key regulations to reference:**
- 《上市公司重大资产重组管理办法》
- 《上市公司收购管理办法》
- 反垄断审查 (SAMR)
- 经营者集中申报 thresholds

## Quality Checks

Before delivering:
- [ ] All financial data sourced and accurate
- [ ] Valuation analysis complete
- [ ] Charts and tables populated correctly
- [ ] Design consistent with template
- [ ] China-specific context included
- [ ] Risk factors appropriate
- [ ] Confidentiality marked
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
