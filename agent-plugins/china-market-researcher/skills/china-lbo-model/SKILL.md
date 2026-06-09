---
name: china-lbo-model
description: Leveraged buyout model for A-share and China-market LBO scenarios. Adapts the standard LBO-model methodology for Chinese debt markets, CAS accounting, and AkShare data. Use instead of the original lbo-model skill when analyzing leveraged buyouts involving Chinese targets or China-based sponsors.
---

# china-lbo-model

## Purpose

Build institutional-quality LBO models for transactions in the China market, accounting for:
- Chinese debt market structures (bank loans, 公司债, 中期票据)
- CAS accounting standards
- A-share trading restrictions and considerations
- China-specific tax treatment

## Key Differences from US LBO Models

| Parameter | US LBO | China LBO |
|-----------|--------|-----------|
| Debt market | Public bonds, institutional loans | Bank syndicated loans, 公司债, ABS |
| Typical leverage | 5-7x EBITDA | 3-5x EBITDA (bank-driven) |
| High-yield market | Developed | Limited (mostly onshore/offshore 高收益债) |
| Covenant package | Bond covenants, bank covenants | Primarily bank-led covenants |
| Management roll | Standard | Often 管理层持股 + earn-out |
| Tax rate | 21% federal | 25% standard (高新技术企业 15%) |
| Currency | USD | CNY (人民币) |
| Accounting | US GAAP / IFRS | CAS (企业会计准则) |

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "income", "annual")   → 利润表 (EBIT, Net Income)
get_financials(ticker, "balance", "annual")  → 资产负债表 (Debt, Cash)
get_financials(ticker, "cashflow", "annual") → 现金流量表 (FCF, CapEx)
get_quote(ticker)                            → Current valuation
get_historical_data(ticker)                  → Trading history
get_stock_info(ticker)                       → Company profile
```

### Secondary Sources
- 巨潮资讯 — public filings for historicals
- 公司公告 — debt agreements, covenant packages
- 银行间市场交易商协会 — bond issuance data
- Wind / 同花顺 — comparable transaction multiples

## Workflow

### Step 1: Company & Transaction Setup

**Transaction Structure (China-specific):**

- **Buyer type**: 战略投资者 (strategic) vs 财务投资者 (financial sponsor)
- ** Listed status**: A-share delisting process vs 借壳上市 (reverse merger)
- **Deal structure**: 股权收购 vs 资产收购 vs 吸收合并
- **Lock-up**: 限售期 considerations (typically 12-36 months)

**Entry Valuation:**
- Current market cap (流通市值 or 总市值)
- Control premium benchmark: 20-40% typical for China M&A (vs 20-30% US)
- Take-private premium for A-share delistings: 30-50%

### Step 2: Sources & Uses

**Sources:**
- Senior debt (银行借款): 40-60% of total consideration
- Subordinated debt / 夹层融资: 5-15%
- Equity ( sponsor equity ): 30-50%
- Revolver (循环额度): 10-20% of EBITDA
- Seller note / 卖方分期付款: common in China

**Uses:**
- Purchase equity
- Refinance existing debt
- Transaction fees (typically higher in China: 2-4%)
- 印花税 (stamp tax): 0.05% on equity transfer
- 增值税 on asset deals: 6% (一般纳税人) or 3% (小规模纳税人)

**China-specific cost items:**
- 印花税 (Stamp tax): 0.05% of deal value for equity transfers
- 契税 (Deed tax): 3-5% for asset acquisitions
- 土地增值税 (Land appreciation tax): for real estate assets
- 中介费用 (Advisory fees): typically 1.5-3% for IB, legal, accounting

### Step 3: Operating Model

Build 5-year projections following standard LBO methodology:

**Revenue assumptions:**
- Historical growth rate baseline
- Synergy adjustments (cost savings, revenue uplift)
- China-specific factors:
  - 产能利用率 (capacity utilization) trends
  - 新产能投放 (new capacity ramp)
  - 市场份额变化 (market share dynamics)

**Margin assumptions:**
- Gross margin: track 毛利率
- Operating margin: 营业利润率
- Note: Chinese industrial companies often have thinner margins than Western peers

**Working capital:**
- 应收账款 (AR) days — often elevated in China
- 存货 (Inventory) days — FIFO only (no LIFO under CAS)
- 应付账款 (AP) days
- Net working capital as % of revenue change

**CapEx:**
- 资本支出 intensity (Chinese industrials often capex-heavy)
- Maintenance vs growth CapEx split

### Step 4: Debt Schedule

**China-specific debt structures:**

1. **Senior secured bank loan (银行借款)**
   - Typically 3-5 year tenor
   - SOFR/LPR + spread (1-3%)
   - Covenants: 资产负债率, 利息覆盖倍数, 流动比率
   - Amortization: typically 1-3% per year (bullet maturity)

2. **Subordinated debt / 夹层融资**
   - Mezzanine structures gaining market share
   - 10-15% coupon typical
   - Often includes equity kicker (认股权证)

3. **High-yield bonds / 高收益债**
   - Limited market, mostly offshore
   - 7-12% coupon range
   - 3-5 year maturity

4. **Revolver (循环贷款)**
   - Based on 应收账款 or 存货 collateral
   - LTV: 50-70% of eligible collateral

**Interest calculation:**
- Average debt balance method or daily balance
- LIBOR/SOFR replaced with LPR for onshore RMB loans
- Add credit spread based on company rating

### Step 5: Returns Analysis

**IRR calculation** (same methodology as US LBO):
- Sponsor equity contributions
- Dividend recapitalizations
- Exit proceeds

**MOIC calculation**:
- Total cash returned / Total cash invested

**Exit multiples:**
- Comparable to china-comps analysis
- Typical EV/EBITDA exit: 6-12x for China industrials
- IPO exit: increasingly common (A-share IPO for delisted targets)

**Sensitivity tables:**
- Entry multiple vs exit multiple
- EBITDA growth vs leverage level
- IRR vs MOIC matrix

### Step 6: Scenario Analysis

**Bear case:**
- Revenue growth below plan
- Margin compression
- Higher borrowing costs
- Covenant tightness

**Base case:**
- Plan assumptions achieved
- Standard amortization schedule
- Target exit in year 4-5

**Bull case:**
- Revenue synergies materialize
- Margin expansion through 规模效应
- Lower financing costs
- IPO exit at premium

## China-Specific Considerations

### A-Share Delisting / 私有化
- 全面要约收购 (General offer) required for >30% stake
- Minimum offer price: typically 6 months highest trading price
- Post-delisting: 3 years before re-listing (创业板/科创板: 2 years)
- 回购价格 must meet regulatory minimums

### Regulatory Approvals
- 反垄断审查 (SAMR merger control)
- 经营者集中申报 for deals above thresholds
- 外资安全审查 (foreign investment review)
- 行业准入 (sector-specific approvals)

### Tax Considerations
- 资本利得税: not separately levied on individuals
- Corporate: 25% (or 15% for 高新技术企业)
- Withholding tax on dividends to foreign investors: 10% ( treaty relief possible)
- 转让所得税 on asset transfers: 25% corporate or 20% individual

### Working Capital Norms
- Chinese companies often have:
  - Higher AR days (less efficient collections)
  - Higher inventory days (especially manufacturing)
  - Higher AP days (supplier financing)
- Net WC often runs 5-15% of revenue for industrials

### Debt Market Access
- Investment-grade: 3-5% borrowing cost
- High-yield: 8-15% (offshore bonds)
- Bank loans: LPR + 100-300 bps
- Shadow banking restrictions affect 信托融资 availability

## Excel Model Structure

### Sheet Architecture

1. **Sources & Uses** — deal structure
2. **Operating Model** — 5-year projections
3. **Debt Schedule** — all tranches with amortization
4. **Returns Summary** — IRR, MOIC, equity bridge
5. **Sensitivity** — entry/exit multiple sensitivity

### Key Formulas

```excel
// EBITDA
=Gross Profit + D&A - S&M - G&A

// Unlevered FCF
=NOPAT + D&A - CapEx - ΔNWC

// Levered FCF
=Unlevered FCF - Interest - Mandatory Amortization - Dividends

// Debt at end of year
=Beginning Debt + New Draws - Mandatory Amort - Optional Prepayment

// Interest expense
=Average Debt × Interest Rate

// IRR
=IRR(Equity contributions, dividends, exit proceeds)

// MOIC
=Exit Equity Value / Total Equity Invested
```

## Output Checklist

Before delivering:

- [ ] Sources & Uses balance (Total Sources = Total Uses)
- [ ] Debt schedule amortizes correctly
- [ ] Interest calculated on average or period-end debt (consistent)
- [ ] All hardcoded inputs sourced and commented
- [ ] IRR and MOIC calculations verified
- [ ] Sensitivity tables fully populated
- [ ] Scenario analysis included (Bear/Base/Bull)
- [ ] China-specific taxes/fees included in Uses
- [ ] CAS conventions documented
- [ ] File named: `[Ticker]_LBO_Model_[Date].xlsx`

## Reference

This skill extends the base `lbo-model` skill. For Excel formatting standards, formula conventions, and section checkpoint methodology, refer to:
- `lbo-model/SKILL.md` — base LBO methodology
- `xlsx-author/SKILL.md` — Excel file creation standards
- `audit-xls/SKILL.md` — model validation and audit procedures
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
