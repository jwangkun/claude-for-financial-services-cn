---
name: china-accrual-schedule
description: Build accrual schedules for A-share fund administration. Tracks revenue recognition, expense accruals, and working capital timing for fund accounting. Adapted from the original accrual-schedule skill for fund accounting standards. Triggers on "基金应计项目", "应计计提基金", "accrual schedule fund", "NAV accruals", or "accruals [fund]".
---

# china-accrual-schedule

## Purpose

Build **基金应计项目时间表** — comprehensive accrual tracking for fund accounting and NAV calculation.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "income")     → Revenue, expenses
get_fund_data(fund_code)             → Fund NAV data
get_quote(ticker)                    → Security prices
```

### Secondary Sources
- 基金公司 — fund accounting records
- 托管行 — custody data
- Wind / Choice — market data

## Workflow

### Step 1: Identify Accrual Items

**Fund-specific accruals:**

| Category | Items | Frequency |
|----------|-------|-----------|
| 收入应计 (Income accruals) | Dividends, interest | Daily |
| 费用应计 (Expense accruals) | Management fee, custodian fee | Daily/Monthly |
| 交易应计 (Trade accruals) | Purchases, sales | T+1 |
| 税费应计 (Tax accruals) | Withholding tax | As incurred |
| 其他应计 (Other accruals) | Miscellaneous | As needed |

### Step 2: Income Accruals

**Dividend accruals:**

| Security | Ex-date | Pay-date | Shares | Rate | Accrued Amount |
|----------|---------|----------|--------|------|----------------|
| | | | | ¥/股 | |
| **Total dividends** | | | | | **¥XX** |

**Bond interest accruals:**

| Bond | Coupon | Pay-date | Face Value | Accrued Interest |
|------|--------|----------|-----------|-----------------|
| | X% | | ¥XX | ¥XX |
| **Total bond interest** | | | | **¥XX** |

**Other income accruals:**
- 逆回购利息 (Reverse repo interest)
- 存款利息 (Bank deposit interest)
- 基金分红 (Fund distributions)

### Step 3: Expense Accruals

**Management fee:**

| Parameter | Value |
|-----------|-------|
| Annual rate | X.XX% |
| Daily rate | X.XXXX% (annual / 365) |
| Calculation | AUM × daily rate × days |
| Accrued MTD | ¥XX |
| Accrued YTD | ¥XX |

**Custodian fee:**

| Parameter | Value |
|-----------|-------|
| Annual rate | X.XX% |
| Calculation | AUM × rate × days/365 |
| Accrued | ¥XX |

**Other expenses:**
- 交易佣金 (Trading commissions)
- 审计费 (Audit fees)
- 信息披露费 (Disclosure fees)
- 律师费 (Legal fees)
- 银行费用 (Bank charges)

### Step 4: Trade Accruals

**T+1 trade settlement:**

| Trade Date | Settlement | Security | Type | Quantity | Price | Amount | Status |
|-----------|-----------|----------|------|----------|-------|--------|--------|
| | | | Buy/Sell | | ¥X.XX | ¥XX | T / T+1 / Settled |

**Trades in transit:**
- Purchases not yet settled
- Sales not yet settled
- Corporate actions pending

### Step 5: Tax Accruals

**Withholding tax:**

| Type | Rate | Applies To | Accrued |
|------|------|-----------|---------|
| 股息红利税 | 20% (10% for >1yr) | A-share dividends | ¥XX |
| 债券利息税 | 20% | Corporate bond interest | ¥XX |
| 增值税 | 6% | Management fee (if applicable) | ¥XX |

### Step 6: Accrual Schedule

**Daily/Monthly accrual tracking:**

| Date | Dividend | Interest | Mgmt Fee | Custodian | Other | Net Accrual |
|------|----------|----------|----------|-----------|-------|-------------|
| | | | | | | |
| MTD | | | | | | |
| YTD | | | | | | |

### Step 7: NAV Impact

**Accruals impact on NAV:**

| Accrual Type | Impact | Amount |
|-------------|--------|--------|
| Accrued income | +NAV | ¥XX |
| Accrued expenses | -NAV | ¥XX |
| Net accrual impact | +NAV | ¥XX |

### Step 8: Reconciliation

**Accrual reconciliation:**

| Item | Fund Books | Custodian | Difference | Notes |
|------|-----------|-----------|------------|-------|
| Dividends | | | | |
| Management fee | | | | |
| Custodian fee | | | | |
| Other accruals | | | | |

## China-Specific Considerations

### Fund Accounting Standards

| Standard | Applies |
|----------|---------|
| 基金会计核算 | All public funds |
| 企业会计准则 | Private funds |
| 证券投资基金 | Mutual funds |

### Common Accrual Patterns

| Fund Type | Key Accruals |
|-----------|-------------|
| 股票型基金 | Dividend accruals |
| 债券型基金 | Interest accruals (daily) |
| 货币基金 | Interest accruals (daily) |
| 混合型基金 | Both dividends and interest |

### Tax Considerations

| Tax | Rate | Treatment |
|-----|------|-----------|
| 股息红利 | 20% (10% for >1yr) | Withholding |
| 利息收入 | 20% | Withholding |
| 价差收益 | 暂免 | No tax on capital gains |

## Quality Checks

Before finalizing:
- [ ] All income items accrued
- [ ] All expenses accrued
- [ ] Calculations verified
- [ ] Reconciliation complete
- [ ] NAV impact quantified
- [ ] Documentation complete
