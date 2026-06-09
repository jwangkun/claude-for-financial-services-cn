---
name: china-roll-forward
description: Roll forward fund accounting records for new reporting periods. Adapts the original roll-forward skill for Chinese fund administration and reporting requirements. Triggers on "基金账务滚动", "账务更新", "roll forward fund", "update fund books", "基金新期间", or "roll forward [fund] [period]".
---

# china-roll-forward

## Purpose

Roll forward **基金账务** — update fund accounting records for new periods.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "income")     → Holdings financials
get_fund_data(fund_code)              → Fund NAV data
get_quote(ticker)                     → Latest prices
```

### Secondary Sources
- 基金公司 — fund accounting system
- 托管行 — custody records
- 巨潮 — portfolio company filings

## Workflow

### Step 1: Identify New Period

**Fund reporting periods:**

| Period | Type | Frequency | Deadline |
|--------|------|-----------|----------|
| 日 | Daily | Daily | T+1 |
| 周 | Weekly | Weekly | |
| 月 | Monthly | Monthly | |
| 季 | Quarterly | Quarterly |季报后 |
| 半年 | Semi-annual | Semi-annual |中报后 |
| 年 | Annual | Annual |年报后 |

### Step 2: Close Prior Period

**Period-end closing checklist:**

| Item | Action |
|------|--------|
| 收入确认 | Close all income accruals |
| 费用计提 | Close all expense accruals |
| 已实现损益 | Calculate realized P&L |
| 未实现损益 | Mark-to-market |
| 分红处理 | Process distributions |
| 费用分配 | Allocate to NAV |

### Step 3: Carry Forward Balances

**Balance carry-forward:**

| Account | Ending Balance | Carried Forward | Notes |
|---------|---------------|----------------|-------|
| 银行存款 | | | |
| 证券投资 | | | |
| 应收利息 | | | |
| 应收股利 | | | |
| 应付费用 | | | |
| 实收基金 | | | |
| 未分配利润 | | | |

### Step 4: Update Holdings

**Holdings update:**

| Security | Ticker | Prior Qty | Trades | New Qty | Price | Market Value |
|----------|--------|-----------|--------|---------|-------|--------------|
| | | | | | | |

### Step 5: Update Accruals

**Accrual roll-forward:**

| Accrual Type | Prior | Additions | Usage | Reversal | New |
|-------------|-------|-----------|-------|----------|-----|
| 应收股息 | | | | | |
| 应收利息 | | | | | |
| 应付管理费 | | | | | |
| 应付托管费 | | | | | |

### Step 6: Calculate New NAV

**NAV calculation:**

| Item | Amount |
|-------|--------|
| Beginning NAV | ¥XX |
| + Income earned | ¥XX |
| + Realized gains | ¥XX |
| + Unrealized gains | ¥XX |
| - Expenses | ¥XX |
| - Distributions | ¥XX |
| **Ending NAV** | **¥XX** |
| Shares outstanding | XX |
| **NAV per share** | **¥XX** |

### Step 7: Update Financial Statements

**Fund financial statements:**

| Statement | Update |
|-----------|--------|
| 资产负债表 | New balances |
| 利润表 | New period activity |
| 净值变动表 | NAV changes |
| 会计报表附注 | Disclosures |

### Step 8: Performance Calculation

**Performance update:**

| Metric | MTD | QTD | YTD | Since Inception |
|--------|-----|-----|-----|-----------------|
| Return | X.XX% | X.XX% | X.XX% | X.XX% |
| Benchmark | X.XX% | X.XX% | X.XX% | X.XX% |
| Active return | X.XX% | X.XX% | X.XX% | X.XX% |

### Step 9: Reconciliation

**New period reconciliation:**

| Item | Fund Books | Custodian | Match? |
|-------|-----------|-----------|--------|
| Securities | | | |
| Cash | | | |
| NAV | | | |
| P&L | | | |

## China-Specific Considerations

### Fund Accounting Calendar

| Event | Timing |
|-------|--------|
| 估值日 | Daily / T+1 |
| 净值公告 | T+2 for daily NAV |
| 季报披露 | Within 15 days of quarter-end |
| 半年报 | Within 60 days of H1 end |
| 年报 | Within 90 days of year-end |

### Cut-off Rules

| Item | Cut-off Rule |
|------|-------------|
| 交易 | Trade date basis |
| 收入 | Ex-dividend date |
| 费用 | Incurrence basis |
| 税费 | Withholding date |

## Quality Checks

Before completing:
- [ ] Prior period closed properly
- [ ] Balances carried forward
- [ ] New period activity recorded
- [ ] NAV calculated correctly
- [ ] Reconciliation complete
- [ ] Performance calculated
- [ ] Reports generated
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
