---
name: china-gl-recon
description: General ledger reconciliation for A-share companies. Adapts the original gl-recon skill for Chinese accounting standards, chart of accounts, and common reconciliation items. Triggers on "A股总账核对", "总账调节", "GL reconciliation China", "科目余额表", or "reconcile [company] accounts".
---

# china-gl-recon

## Purpose

Perform **A股总账核对** — comprehensive general ledger reconciliation for Chinese companies.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "balance")    → Balance sheet accounts
get_financials(ticker, "income")     → P&L accounts
```

### Secondary Sources
- 巨潮 — financial statements
- 审计报告 — reconciliation notes
- 科目余额表 — trial balance

## Workflow

### Step 1: Understand the Chart of Accounts

**Common Chinese COA structure:**

| Category | Account Code Range | Key Accounts |
|----------|-------------------|--------------|
| 资产 (Assets) | 1001-1999 | Cash, AR, inventory, PPE |
| 负债 (Liabilities) | 2001-2999 | AP, debt, provisions |
| 所有者权益 (Equity) | 3001-3999 | Capital, reserves, retained earnings |
| 成本 (Cost) | 4001-4999 | COGS, production costs |
| 损益 (P&L) | 5001-5999 | Revenue, expenses, gains/losses |

**Key accounts to reconcile:**

| Account | CAS Code | Reconciliation Item |
|---------|----------|-------------------|
| 银行存款 | 1002 | Bank statement |
| 应收账款 | 1122 | AR aging |
| 其他应收款 | 1187 | Related party, advances |
| 存货 | 1403 | Inventory count |
| 固定资产 | 1601 | Fixed asset register |
| 应付账款 | 2202 | Supplier statements |
| 应付职工薪酬 | 2211 | Payroll records |
| 应交税费 | 2221 | Tax returns |
| 未分配利润 | 3405 | P&L close check |

### Step 2: Balance Sheet Reconciliation

**BS recon checklist:**

| Account | GL Balance | Supporting Docs | Reconciled Amount | Difference |
|---------|-----------|-----------------|-------------------|------------|
| 货币资金 | | Bank statements | | |
| 应收账款 | | Aging report | | |
| 预付款项 | | Supplier statements | | |
| 存货 | | Count sheets | | |
| 其他应收款 | | Detail listing | | |
| 长期股权投资 | | Investment records | | |
| 固定资产 | | Asset register | | |
| 应付账款 | | Supplier confirmations | | |
| 应付职工薪酬 | | Payroll records | | |
| 应交税费 | | Tax returns | | |
| 短期借款 | | Loan agreements | | |
| 长期借款 | | Loan agreements | | |

### Step 3: Bank Reconciliation

**Bank recon:**

| Item | GL | Bank Stmt | Difference |
|------|-----|-----------|------------|
| Balance per GL | ¥XX | | |
| Add: Deposits in transit | | ¥XX | |
| Less: Outstanding checks | | ¥XX | |
| Add/Less: Errors | | ¥XX | |
| Adjusted GL balance | | | ¥XX |
| Balance per bank | | ¥XX | |
| Reconciled | ✓ / ✗ | | |

**Common reconciling items (China):**
- 在途存款 (Deposits in transit)
- 未兑现支票 (Outstanding checks)
- 银行手续费 (Bank charges)
- 利息收入 (Interest income)
- 未达账项 (Unrecorded items)

### Step 4: AR Reconciliation

**AR aging recon:**

| Aging | GL Balance | Aging Report | Confirmed | Difference |
|-------|-----------|--------------|-----------|------------|
| 0-30 days | | | | |
| 31-60 days | | | | |
| 61-90 days | | | | |
| 91-180 days | | | | |
| >180 days | | | | |
| Total | | | | |

**AR recon items:**
- 账龄分析 (Aging analysis)
- 坏账准备 (Allowance for doubtful accounts)
- 关联方应收 (Related party AR)
- 票据应收 (Notes receivable)
- 预收账款冲减 (Advances from customers)

### Step 5: AP Reconciliation

**AP recon:**

| Vendor | GL Balance | Vendor Statement | Confirmed | Difference |
|--------|-----------|-----------------|-----------|------------|
| | | | | |
| | | | | |
| Total | | | | |

### Step 6: Inventory Reconciliation

**Inventory recon:**

| Item | GL | Count | Difference | Reason |
|------|-----|-------|------------|--------|
| 原材料 | | | | |
| 在产品 | | | | |
| 产成品 | | | | |
| Total | | | | |

**Inventory recon items:**
- 实物盘点 (Physical count)
- 在途存货 (Goods in transit)
- 已发出商品 (Consignment goods)
- 存货跌价准备 (Obsolescence reserve)

### Step 7: Fixed Asset Reconciliation

**FA recon:**

| Asset | GL | Register | Tag Count | Difference |
|-------|-----|----------|-----------|------------|
| | | | | |
| Total | | | | |

**FA recon items:**
- 资产标签 (Asset tagging)
- 折旧计算 (Depreciation calculation)
- 减值测试 (Impairment testing)
- 处置记录 (Disposal records)
- 资本化 vs 费用化 (Capitalization policy)

### Step 8: Payroll Reconciliation

**Payroll recon:**

| Item | GL | Payroll Records | Tax Filing | Difference |
|------|-----|----------------|------------|------------|
| 工资 | | | | |
| 社保 | | | | |
| 公积金 | | | | |
| 个税 | | | | |
| Total | | | | |

### Step 9: Tax Reconciliation

**Tax recon:**

| Tax Type | GL | Tax Return | Difference |
|-----------|-----|------------|------------|
| 增值税 | | | |
| 企业所得税 | | | |
| 附加税 | | | |
| 个税 | | | |
| 社保/公积金 | | | |

### Step 10: P&L Close Check

**P&L to retained earnings:**

```
期初未分配利润
+ 本年净利润 (from P&L close)
- 提取盈余公积
- 提取任意公积
- 应付股利
= 期末未分配利润
```

**Verify:**
- P&L close → retained earnings
- 利润分配 entries
- Tax entries
- Dividend entries

## China-Specific Recon Considerations

### Common Issues

| Issue | Detection | Resolution |
|-------|-----------|------------|
| 在途资金 | Bank recon | Timing difference |
| 未达账项 | Bank recon | Follow up |
| 关联方挂账 | AR/AP aging | Related party recon |
| 发票差异 | Tax recon | Timing/cut-off |
| 折旧差异 | FA recon | Policy check |

### CAS-Specific Items

| Item | Treatment |
|------|-----------|
| 增值税 | Pass-through, check VAT output/input |
| 政府补助 | Verify classification |
| 股份支付 | Expense recognition check |
| 汇兑损益 | FX difference verification |

## Quality Checks

Before completing:
- [ ] All significant accounts reconciled
- [ ] Differences investigated and resolved
- [ ] Documentation complete
- [ ] Sign-offs obtained
- [ ] Adjustments proposed (if any)
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
