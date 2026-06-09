---
name: china-accrual-schedule
description: Build accrual schedules for A-share companies tracking revenue recognition, expense accruals, and working capital timing. Adapted from the original accrual-schedule skill for CAS accounting and Chinese business practices. Triggers on "A股应计项目", "应计计提", "accrual schedule China", "应计账款分析", or "working capital accruals [company]".
---

# china-accrual-schedule

## Purpose

Build **A股应计项目时间表** — comprehensive accrual schedules for financial analysis and audit preparation.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "income")     → Revenue, expenses
get_financials(ticker, "balance")    → Working capital accounts
```

### Secondary Sources
- 巨潮 — annual/quarterly reports
- 审计报告 — accrual methodology

## Workflow

### Step 1: Identify Accrual Items

**Revenue accruals:**

| Item | Description | Typical Items |
|------|-------------|---------------|
| 预收账款 (Deferred revenue) | Advance from customers | Prepayments, deposits |
| 应收账款 (Accounts receivable) | Revenue recognized, not yet collected | Trade receivables |
| 合同负债 (Contract liabilities) | New CAS term for prepayments | Contract-based |
| 应收票据 (Notes receivable) | Commercial acceptance/bank bills | Bills from customers |

**Expense accruals:**

| Item | Description | Typical Items |
|------|-------------|---------------|
| 应付账款 (Accounts payable) | Expenses incurred, not yet paid | Trade payables |
| 应付职工薪酬 (Accrued salaries) | Year-end bonus, unpaid wages | Bonus accruals |
| 应付利息 (Accrued interest) | Interest on loans, bonds | Interest payable |
| 预计负债 (Provisions) | Estimated obligations | Warranty, litigation |
| 递延收益 (Deferred income) | Government grants | Subsidy income |
| 预提费用 (Accrued expenses) | General accruals | Utilities, rent |

**Other accruals:**

| Item | Description |
|------|-------------|
| 应交税费 (Taxes payable) | Income tax, VAT, surcharges |
| 应付股利 (Dividends payable) | Declared but unpaid |
| 其他应付款 (Other payables) | Miscellaneous |

### Step 2: Build Accrual Schedule

**Monthly/quarterly accrual tracking:**

| Accrual Item | Jan | Feb | ... | Q1 | Q2 | Q3 | Q4 | Full Year |
|--------------|-----|-----|-----|----|----|----|----|-----------|
| 应收账款增加 | | | | | | | | |
| 预收账款增加 | | | | | | | | |
| 应付账款增加 | | | | | | | | |
| 应付职工薪酬 | | | | | | | | |
| ... | | | | | | | | |
| **Net accruals** | | | | | | | | |

### Step 3: Analyze Accrual Quality

**Accrual ratios:**

| Ratio | Formula | Interpretation |
|-------|---------|---------------|
| 总应计率 | (ΔCA - ΔCash - ΔCL) / Average Assets | >0 = accrual-based earnings |
| 应收账款/收入 | AR / Revenue | Rising = potential issues |
| 应付账款/成本 | AP / COGS | Trend analysis |
| 预收账款/收入 | Deferred rev / Revenue | Customer prepayments |
| 经营现金流/净利润 | OCF / Net Income | <1 = accrual concern |

**Accrual quality flags:**

| Flag | Warning |
|------|---------|
| 应收账款增速 >> 收入增速 | Potential revenue inflation |
| 应付账款突然减少 | Potential window dressing |
| 预收账款大幅波动 | Revenue recognition timing |
| 其他应付款异常 | Related party tunneling |

### Step 4: CAS-Specific Accrual Items

**China-specific accruals:**

| Item | CAS Treatment | Notes |
|------|--------------|-------|
| 增值税 | Pass-through, not revenue | 不含税收入 |
| 政府补助 | 递延收益 or 其他收益 | Timing impact |
| 坏账准备 | 预期信用损失模型 | CAS 22 |
| 存货跌价准备 | Lower of cost or NRV | CAS 1 |
| 固定资产减值 | When indicators exist | CAS 8 |
| 商誉减值 | Annual test (no reversal) | CAS 8 |
| 辞退福利 | Employee termination | CAS 9 |

### Step 5: Working Capital Accruals

**Working capital accrual schedule:**

| Item | Beginning | Additions | Usage | Reversal | Ending |
|------|-----------|-----------|-------|----------|--------|
| 坏账准备 | | | | | |
| 存货跌价准备 | | | | | |
| 固定资产减值 | | | | | |
| 预计负债 (产品质量) | | | | | |

### Step 6: Revenue Recognition Accruals

**CAS 14 revenue recognition:**

| Scenario | Recognition | Accrual Impact |
|-----------|-------------|----------------|
| 商品销售 (Goods) | 控制权转移时 | 通常为交付时 |
| 提供服务 (Services) | 期间内逐步 | 劳务成本匹配 |
| 建造合同 (Construction) | 产出法/投入法 | 长期合同 |
| 特许经营 (Franchise) | 持续期间 | 品牌使用费 |

**Revenue accrual items:**
- 发出商品 (Goods in transit)
- 委托代销 (Consignment)
- 工程结算 (Construction settlement)
- 会员费/预付费 (Membership / prepaid)

### Step 7: Period-End Accrual Review

**Month-end / year-end accrual checklist:**

| Area | Items to Review |
|------|----------------|
| Revenue | Unbilled revenue, returns, allowances |
| Purchases | Uninvoiced goods/services |
| Payroll | Bonus, overtime, social insurance |
| Interest | Accrued but unpaid |
| Taxes | Tax provisions |
| Depreciation | Monthly depreciation |
| Provisions | Legal, warranty, restructuring |

## China-Specific Considerations

### Common Accrual Patterns

| Industry | Typical Accruals |
|----------|-----------------|
| 制造业 | Raw material AP, bonus accruals |
| 零售 | Lease accruals, loyalty programs |
| 房地产 | 预收账款 (presale), construction accruals |
| 建筑 | 工程结算 (progress billing) |
| 软件 | Deferred revenue, support accruals |
| 医药 | Rebates, returns provisions |

### Audit Considerations (China)

| Area | Focus |
|------|-------|
| 大额应计 | Materiality threshold |
| 关联方 | Related party payables |
| 期限 | Aging of receivables |
| 坏账 | Adequacy of allowance |
| 政府补助 | Compliance with grant conditions |

## Quality Checks

Before delivering:
- [ ] All significant accruals identified
- [ ] Schedule ties to financial statements
- [ ] Trends analyzed
- [ ] Quality flags addressed
- [ ] CAS compliance verified
- [ ] Audit implications noted
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
