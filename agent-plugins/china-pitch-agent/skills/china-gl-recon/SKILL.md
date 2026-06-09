---
name: china-gl-recon
description: General ledger reconciliation for A-share fund administration. Tracks fund accounting reconciliations including securities, cash, income, and expense accruals. Adapted from the original gl-recon skill for fund accounting standards. Triggers on "基金总账核对", "基金科目核对", "GL reconciliation fund", "fund accounting recon", or "reconcile [fund] books".
---

# china-gl-recon

## Purpose

Perform **基金总账核对** — comprehensive general ledger reconciliation for fund accounting.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "balance")    → Portfolio company BS
get_fund_data(fund_code)              → Fund holdings and NAV
get_quote(ticker)                     → Security prices
```

### Secondary Sources
- 基金公司 — fund accounting system
- 托管行 — custody records
- Wind / Choice — market data

## Workflow

### Step 1: Identify GL Accounts

**Fund accounting COA:**

| Category | Accounts | Purpose |
|----------|----------|---------|
| 资产 (Assets) | Securities, cash, receivables | Investments |
| 负债 (Liabilities) | Payables, accruals | Amounts owed |
| 所有者权益 | NAV | Fund value |
| 收入 (Revenue) | Dividends, interest, gains | Investment income |
| 费用 (Expenses) | Management fee, custodian fee | Fund costs |
| 已实现损益 | Realized gains/losses | Trading P&L |
| 未实现损益 | Unrealized appreciation | Mark-to-market |

### Step 2: Securities Reconciliation

**Securities holdings recon:**

| Security | Ticker | Fund Records | Custodian | Difference | Status |
|----------|--------|-------------|-----------|------------|--------|
| | | | | | |
| | | | | | |
| **Total** | | | | | |

**Reconciliation items:**
- 在途交易 (Trades in transit)
- 配股/增发 (Rights issues)
- 分红到账 (Dividend settlements)
- 利息到账 (Interest settlements)

### Step 3: Cash Reconciliation

**Cash recon:**

| Account | GL Balance | Bank Statement | Custodian | Difference |
|---------|-----------|----------------|-----------|------------|
| 清算备付金 | | | | |
| 结算备付金 | | | | |
| 银行存款 | | | | |
| **Total** | | | | |

### Step 4: Income Reconciliation

**Income reconciliation:**

| Type | Fund Records | Custodian | Source Docs | Difference |
|------|-------------|-----------|-------------|------------|
| 现金股息 | | | | |
| 股票股息 | | | | |
| 债券利息 | | | | |
| 回购利息 | | | | |
| 基金分红 | | | | |
| 已实现利得 | | | | |
| **Total** | | | | |

### Step 5: Expense Reconciliation

**Expense reconciliation:**

| Expense | Fund Records | Custodian | Invoice/Contract | Difference |
|---------|-------------|-----------|-----------------|------------|
| 管理费 | | | | |
| 托管费 | | | | |
| 交易佣金 | | | | |
| 审计费 | | | | |
| 信息披露费 | | | | |
| 律师费 | | | | |
| **Total** | | | | |

### Step 6: Accrual Reconciliation

**Accrual reconciliation:**

| Accrual Type | Calculation | Custodian | Difference |
|-------------|-------------|-----------|------------|
| 应收股息 | | | |
| 应收利息 | | | |
| 应付管理费 | | | |
| 应付托管费 | | | |
| 应付交易费用 | | | |

### Step 7: NAV Reconciliation

**NAV reconciliation:**

| Component | Fund Books | Custodian | Difference |
|-----------|-----------|-----------|------------|
| Securities | | | |
| Cash | | | |
| Receivables | | | |
| Payables | | | |
| Accruals | | | |
| **NAV** | | | |

**NAV per unit check:**

| | Fund | Custodian | Difference |
|--|------|-----------|------------|
| NAV (¥) | | | |
| Shares outstanding | | | |

### Step 8: P&L Reconciliation

**P&L reconciliation:**

| P&L Item | Fund Books | Verified | Notes |
|----------|-----------|----------|-------|
| 收入合计 | | | |
| 费用合计 | | | |
| 已实现损益 | | | |
| 未实现损益 | | | |
| 利润合计 | | | |

### Step 9: Trade Reconciliation

**Trade recon:**

| Trade Date | Security | Type | Quantity | Price | Fund | Custodian | Match? |
|-----------|----------|------|----------|-------|------|-----------|--------|
| | | | | | | | |

### Step 10: Exception Report

**Exception log:**

| # | Exception | Type | Amount | Resolution | Status |
|---|-----------|------|--------|-------------|--------|
| | | | | | |

## China-Specific Considerations

### Fund Accounting Standards

| Standard | Applies |
|----------|---------|
| 基金会计核算 | All funds |
| 企业会计准则 | Private funds |
| 证券投资基金信息披露 | Disclosure requirements |

### Common Issues

| Issue | Cause | Resolution |
|-------|-------|-----------|
| 交易时滞 | T+1 settlement | Track trades in transit |
| 分红时滞 | Ex-date vs pay-date | Accrue correctly |
| 费用计提 | Timing differences | Standardize cut-off |
| 估值差异 | Different pricing sources | Agree on source |

## Quality Checks

Before completing:
- [ ] Securities reconciled
- [ ] Cash reconciled
- [ ] Income reconciled
- [ ] Expenses reconciled
- [ ] Accruals reconciled
- [ ] NAV tied out
- [ ] P&L reconciled
- [ ] Exceptions resolved
- [ ] Sign-offs obtained
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
