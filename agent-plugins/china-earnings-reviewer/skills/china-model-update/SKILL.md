---
name: china-model-update
description: Update A-share financial models with new quarterly data, management guidance, or macro changes. Reflects actuals, rolls estimates forward, flags material changes, and updates valuation. Adapted from the original model-update skill for Chinese market conventions and AkShare data. Triggers on "A股模型更新", "模型更新", "plug earnings into model", "update model for [company]", "刷新预测", or "更新财务模型".
---

# china-model-update

## Purpose

Update existing **A股财务模型** with new data, ensuring all cells are traceable to sources and all changes are documented.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "income", "quarterly")   → Q[X] actual results
get_financials(ticker, "balance", "quarterly")  → BS update
get_financials(ticker, "cashflow", "quarterly") → CF update
get_financials(ticker, "income", "annual")      → Full year update
get_quote(ticker)                               → Current market data
get_stock_info(ticker)                          → Any company changes
```

### Secondary Sources

- **巨潮资讯** — official filings for exact figures
- **业绩说明会 transcript** — management commentary
- **管理层指引** — guidance from earnings calls
- **Wind / Choice / 同花顺** — consensus updates

## Workflow

### Step 1: Identify What Changed

**Change triggers:**
- Quarterly earnings release (季报/年报)
- Management guidance update (管理层指引调整)
- Macro assumption change (rate, tax, policy)
- Model error or refinement
- M&A or restructuring event

**Change log template:**

| Date | Change Type | Item | Old Value | New Value | Reason |
|------|-------------|------|-----------|-----------|--------|
| | Earnings update | Revenue FY25E | XX亿 | XX亿 | Q1 actuals beat |
| | Guidance | Tax rate | 25% | 25% | No change |
| | Macro | CapEx % | 5% | 6% | New plant announced |

### Step 2: Update Historical Actuals

**Quarterly actuals:**

```
[Company] Q[X] 20XX Actuals (from AkShare / 巨潮):
- 营业收入: XXX亿 (YoY: +XX%)
- 毛利率: XX% (vs prior: XX%)
- 归母净利润: XXX亿 (YoY: +XX%)
- EPS: X.XX元
- 经营现金流: XXX亿
```

**Update sequence:**
1. Drop Q[X] actuals into historical columns
2. Verify sum checks (quarterly sum = annual)
3. Update LTM (Last Twelve Months) calculations
4. Check annual-to-quarter relationships

### Step 3: Roll Forward Estimates

**Revenue projections:**
- Update growth rates based on Q[X] performance
- Consider:
  - Order backlog changes
  - New product ramp
  - Market share gains/losses
  - Capacity expansion

**Margin projections:**
- Update gross margin based on actual trend
- Update opex ratios based on actual leverage
- Flag structural changes (input costs, pricing power)

**Balance sheet projections:**
- Update working capital assumptions
- Update debt schedule if refinancing occurred
- Update CapEx plans

### Step 4: Update Valuation

**Market data refresh:**

```python
get_quote(ticker)  # Current price, PE, PB
```

**Valuation metrics to update:**
- Current stock price and change
- Trading multiple (PE, PB, EV/Sales, EV/EBITDA)
- 52-week range position
- Relative to sector median
- Implied growth vs historical

**DCF updates (if applicable):**
- Roll forward projections by one year
- Update market data inputs (beta, risk-free rate, shares)
- Update terminal growth if outlook changed

### Step 5: Flag Material Changes

**Change significance assessment:**

| Change | Threshold | Action |
|--------|-----------|--------|
| Revenue estimate | ±5% | Update model, note driver |
| Net income estimate | ±10% | Update model, revise target price |
| Margin estimate | ±100 bps | Update model, assess sustainability |
| CapEx estimate | ±20% | Update model, check FCF impact |
| Multiple assumption | ±1x | Sensitivity check, document rationale |

**Red flags to highlight:**
- Revenue growth deceleration >500 bps
- Margin compression >300 bps
- Working capital deterioration
- Debt increase >20% vs prior forecast
- Management guidance lower than consensus

### Step 6: Document Changes

**Model update memo:**

```
[公司名称]（[代码]）模型更新 [Date]

一、更新内容
   [Bullet list of changes made]

二、关键变动
   Revenue FY25E: [Old] → [New] ([Change]%)
   Net Income FY25E: [Old] → [New] ([Change]%)
   Driver: [Explanation]

三、估值影响
   新目标价: ¥XX.XX (之前 ¥XX.XX)
   调整幅度: +X% / -X%
   调整逻辑: [Brief rationale]

四、后续关注
   - [Next catalyst]
   - [Key metric to monitor]
   - [Risk factor]
```

### Step 7: QC Checklist

**Before finalizing:**

- [ ] All Q[X] actuals sourced from 巨潮 PDF or AkShare
- [ ] Historical data matches reported figures exactly
- [ ] All formulas intact (no broken references)
- [ ] LTM calculations updated
- [ ] Forward estimates reflect new information
- [ ] Valuation inputs refreshed (price, shares, multiples)
- [ ] Target price recalculated
- [ ] Change log complete
- [ ] Cell comments added for new inputs
- [ ] Model balances correctly

## China-Specific Update Considerations

### Earnings Season Timing

| Report | Deadline | Typical Release Window |
|--------|----------|------------------------|
| Q1季报 | Apr 30 | Apr 1-30 |
| 中报 | Aug 31 | Aug 1-31 |
| Q3季报 | Oct 31 | Oct 1-31 |
| 年报 | Apr 30 | Jan-Apr |

**Model update priority:**
- Annual report: Complete overhaul of historicals
- Semi-annual: Major update, adjust full-year estimates
- Quarterly: Incremental update, verify full-year trajectory

### 业绩预告 Integration

If company issued 业绩预告:
- Use as directional signal before formal report
- Adjust estimates if variance >20% from prior
- Flag for detailed update when formal report arrives

### Consensus Management

- Update consensus assumptions based on new information
- If company guidance differs from consensus, flag divergence
- Note if management commentary suggests estimate revision

### Regulatory Changes

Monitor for:
- Tax rate changes (高新技术企业 reclassification)
- Accounting standard updates
- Industry-specific regulation impacts on assumptions
- Dividend policy changes (影响 DCF terminal value)

## Quality Checks

Before delivering:
- [ ] All new actuals traceable to source
- [ ] Formulas verified (no hardcodes in calculations)
- [ ] Estimates logically consistent with new data
- [ ] Valuation update reflects current market conditions
- [ ] Changes documented in update memo
- [ ] Model passes basic QC (balance checks, sum checks)
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
