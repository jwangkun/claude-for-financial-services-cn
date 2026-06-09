---
name: china-merger-model
description: Accretion/dilution and merger consequences analysis for A-share M&A transactions. Adapted from the original merger-model skill for Chinese GAAP, CAS accounting, and China market transaction structures. Triggers on "A股并购分析", "并购模型", "accretion dilution China", "merger model A-share", or "M&A consequences [company]".
---

# china-merger-model

## Purpose

Build **A股并购分析模型**, analyzing accretion/dilution, synergy capture, and purchase price allocation for M&A transactions involving Chinese companies.

## Key Differences from US Merger Models

| Parameter | US M&A Model | China M&A Model |
|-----------|-------------|-----------------|
| Accounting | US GAAP / IFRS | CAS (企业会计准则) |
| Tax rate | 21% | 25% (or 15% for 高新技术企业) |
| Currency | USD | CNY |
| Goodwill | Indefinite life | Amortized or tested under CAS |
| Stamp duty | Negligible | 0.05% on equity transfer |
| VAT on asset deals | Varies | 6% or 3% depending on 纳税人类型 |
| Deal structure | Stock/cash common | 股权/资产/吸收合并 |
| Premium | 20-30% typical | 20-40% typical for China |

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_financials(ticker_acquirer, "income")   → Acquirer P&L
get_financials(ticker_target, "income")     → Target P&L
get_quote(ticker_acquirer)                  → Acquirer valuation
get_quote(ticker_target)                    → Target valuation
get_industry_stocks(industry="...")          → Peer comparables
```

### Secondary Sources
- 巨潮公告 — transaction announcements (收购公告)
- 交易所 — deal-related filings
- 评估报告 — target valuation reports
- Wind / Choice — comparable transaction multiples

## Workflow

### Step 1: Transaction Setup

**Transaction structure (China-specific):**

| Structure | Description | Tax Impact |
|-----------|-------------|------------|
| 股权收购 | Acquirer buys target equity | 印花税 0.05% |
| 资产收购 | Acquirer buys target assets | 增值税 + 契税 |
| 吸收合并 | Target merged into acquirer | 印花税 on asset transfer |
| 借壳上市 | Reverse merger / backdoor listing | Complex, case-specific |

**Key terms:**

| Term | Chinese | Notes |
|------|---------|-------|
| Purchase price | 交易对价 | Typically includes earnout |
| Control premium | 控股权溢价 | 20-40% typical in China |
| Earnout | 业绩承诺/对赌 | Common in China M&A |
| Lock-up | 锁定期 | 12-36 months for sellers |
| Stamp tax | 印花税 | 0.05% of deal value |
| VAT | 增值税 | 6% on asset deals |
| Deed tax | 契税 | 3-5% on real estate/assets |

### Step 2: Sources & Uses

**Sources:**

| Source | Typical % | Notes |
|--------|-----------|-------|
| Cash on hand | 30-50% | Acquirer's existing cash |
| Debt financing | 40-60% | Bank loans, bonds |
| Equity issuance | 0-30% | 增发 / 定增 |
| Seller financing | Variable | 卖方分期付款 common |

**Uses:**

| Use | Typical % | Notes |
|-----|-----------|-------|
| Equity purchase | 85-95% | 股权转让对价 |
| Transaction fees | 2-4% | IB, legal, accounting |
| 印花税 | 0.05% | Stamp tax |
| 增值税 | 0-6% | On asset deals only |
| Refinancing | Variable | Target debt repayment |

### Step 3: Pro Forma Financials

**Pro forma balance sheet:**
- Acquirer BS + Target BS ± purchase accounting adjustments
- Goodwill calculation
- Debt assumption / payoff
- Cash funding

**Pro forma income statement:**

| Line Item | Acquirer | Target | Pro Forma | Synergies | Adjusted |
|-----------|----------|--------|-----------|-----------|----------|
| Revenue | | | A+B | | |
| COGS | | | | | |
| Gross Profit | | | | | |
| OpEx | | | | | |
| EBIT | | | | | |
| Interest | | | | | |
| Taxes | | | | | |
| Net Income | | | | | |

**Synergy assumptions:**
- Revenue synergies: cross-selling, pricing power (typically modest)
- Cost synergies: headcount reduction, procurement savings, facility consolidation
- Implementation costs: integration costs in first 1-2 years

### Step 4: Accretion/Dilution Analysis

**Per-share analysis:**

```python
Pro forma EPS = (Acquirer NI + Target NI + Synergies - Incremental Interest) / Pro forma Shares

Accretion/(Dilution) = (Pro forma EPS / Acquirer Standalone EPS) - 1
```

**Typical thresholds:**
- Accretive: >+2%
- Neutral: -2% to +2%
- Dilutive: <-2%

**EPS accretion alone is insufficient** — also analyze:
- Cash EPS impact
- FCF per share impact
- ROIC accretion
- Strategic rationale

### Step 5: Valuation Analysis

**Football field:**

| Method | Acquirer Standalone | Pro Forma | Premium Paid |
|--------|--------------------:|----------:|-------------:|
| Last price | | | |
| 30-day VWAP | | | |
| 90-day VWAP | | | |
| Premium to peer median | | | |

**Transaction multiples:**

| Multiple | Acquirer | Target | Premium |
|----------|----------|--------|---------|
| EV/Revenue | | | |
| EV/EBITDA | | | |
| P/E | | | |

### Step 6: China-Specific Considerations

**Earnout / 业绩承诺:**
- Very common in China M&A
- Typically 3-year profit commitment
- Compensation mechanism for shortfall
- Impacts deal accounting and future earnings

**Regulatory approval:**
- 经营者集中申报 (SAMR merger control)
- 外资安全审查 (if foreign buyer)
- 行业主管部门批准 (sector-specific)
- 反垄断审查 timeline: 180 days standard

**Tax optimization:**
- Step acquisition vs direct acquisition
- Asset deal vs equity deal trade-offs
- 特殊性税务处理 (special tax treatment) for restructuring

**Share issuance:**
- 定增 (private placement) approval process
- Lock-up periods for new shares
- Dilution impact calculation

### Step 7: Scenario Analysis

**Bear/Base/Bull scenarios:**

- Revenue assumptions
- Synergy realization
- Integration costs
- Financing costs

### Step 8: Output

**Standard merger model output:**

| Scenario | Standalone EPS | Pro Forma EPS | Accretion | Pro Forma P/E | P/E Multiple Change |
|----------|---------------|---------------|-----------|---------------|--------------------|
| Bear | | | | | |
| Base | | | | | |
| Bull | | | | | |

**Key outputs:**
1. Accretion/dilution by scenario
2. Pro forma financials
3. Transaction multiples
4. Synergy value estimate
5. Strategic rationale summary

## Quality Checks

Before delivering:
- [ ] Sources & Uses balance
- [ ] Pro forma shares calculated correctly
- [ ] Synergy assumptions documented
- [ ] Accretion/dilution formula verified
- [ ] Tax and fee assumptions appropriate for China
- [ ] Regulatory considerations noted
- [ ] Scenario analysis complete
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
