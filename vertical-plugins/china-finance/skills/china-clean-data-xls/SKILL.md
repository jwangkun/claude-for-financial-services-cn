---
name: china-clean-data-xls
description: Clean and normalize A-share financial data for modeling. Adapts the original clean-data-xls skill for Chinese financial statements, CAS conventions, and A-share data formats. Triggers on "A股数据清洗", "财务数据清洗", "clean financial data China", "数据清洗", or "normalize financial statements".
---

# china-clean-data-xls

## Purpose

Clean and normalize **A股财务数据** — prepare raw financial data from 巨潮 filings for modeling and analysis.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_financials(ticker, "income")     → Raw income statement
get_financials(ticker, "balance")    → Raw balance sheet
get_financials(ticker, "cashflow")   → Raw cash flow statement
```

### Secondary Sources
- 巨潮 — original filings (PDF/HTML)
- 审计报告 — audited figures

## Workflow

### Step 1: Data Extraction

**Extract from source documents:**

| Document | Key Data | Format |
|----------|----------|--------|
| 资产负债表 | Assets, liabilities, equity | 千元 |
| 利润表 | Revenue, expenses, profit | 千元 |
| 现金流量表 | Operating, investing, financing CF | 千元 |
| 报表附注 | Detail breakdowns | Text/number |
| 审计报告 | Audit opinion, adjustments | Text |

**Extraction checklist:**
- [ ] All periods extracted (typically 3-5 years)
- [ ] Quarterly data if needed
- [ ] Prior year comparatives
- [ ] Notes and footnotes captured

### Step 2: Normalize Units

**Unit standardization:**

| Issue | Solution |
|-------|----------|
| 千元 vs 万元 vs 元 | Standardize to 万元 |
| Different report dates | Align to same period-end |
| Segment data | Map to consistent segments |
| Currency | All CNY |

**Unit conversion:**
```
From 千元: divide by 10 → 万元
From 元: divide by 10,000 → 万元
From 亿元: multiply by 10,000 → 万元
```

### Step 3: Handle CAS-Specific Items

**CAS vs IFRS mapping:**

| CAS Line Item | Equivalent | Notes |
|---------------|-----------|-------|
| 营业收入 | Revenue | Net of VAT |
| 营业成本 | COGS | Includes VAT |
| 税金及附加 | Tax & surcharges | 城建税, 教育费附加 |
| 销售费用 | SG&A (selling) | |
| 管理费用 | G&A | |
| 研发费用 | R&D | Separated from G&A in new CAS |
| 财务费用 | Interest & finance costs | |
| 投资收益 | Investment income | Including 联营/合营 |
| 公允价值变动 | Fair value change | |
| 信用减值损失 | Credit impairment | New CAS 22 |
| 资产减值损失 | Asset impairment | |
| 资产处置收益 | Asset disposal | |
| 营业外收入 | Non-operating income | Including 政府补助 |
| 营业外支出 | Non-operating expense | |
| 所得税费用 | Income tax | |
| 净利润 | Net income | |
| 归母净利润 | Net income to parent | Key metric |
| 扣非净利润 | Non-GAAP net income | |

### Step 4: Fix Common Data Issues

**Common issues and fixes:**

| Issue | Detection | Fix |
|-------|-----------|-----|
| Missing periods | Gap in data | Flag for manual fill |
| Restated figures | Footnote "重述" | Use most recent restatement |
| Segment reclassification | Note disclosure | Map to new segments |
| One-time items | Large/unusual items | Flag for normalization |
| Related party | 关联交易标注 | Identify and quantify |
| Accounting change | Policy change note | Adjust comparables |
| Error | Doesn't sum | Investigate and correct |

### Step 5: Revenue Breakdown

**Revenue by type:**

| Type | CAS Line | Notes |
|------|----------|-------|
| 主营业务收入 | Core revenue | Main business |
| 其他业务收入 | Other revenue | Ancillary |
| 合计 | Total revenue | |

**Revenue by geography (if disclosed):**

| Region | Current Year | Prior Year | Growth |
|--------|-------------|------------|--------|
| 国内 | | | |
| 海外 | | | |
| 合计 | | | |

### Step 6: Expense Normalization

**Normalize non-recurring items:**

| Item | Treatment |
|------|-----------|
| 资产处置收益/损失 | Exclude from operations |
| 政府补助 (non-recurring) | Exclude or note separately |
| 诉讼/罚款 | Exclude |
| 减值 (one-time) | Exclude or normalize |
| 并购相关费用 | Exclude |

**Adjusted metrics:**
```
调整后营业收入 = 营业收入 - 其他业务收入
调整后营业成本 = 营业成本 (core only)
调整毛利率 = 调整后毛利 / 调整后收入
```

### Step 7: Balance Sheet Clean-up

**Balance sheet mapping:**

| CAS Item | Modeling Category |
|----------|------------------|
| 货币资金 | Cash & equivalents |
| 交易性金融资产 | Short-term investments |
| 应收票据 | Notes receivable |
| 应收账款 | Accounts receivable |
| 预付款项 | Prepayments |
| 其他应收款 | Other receivables |
| 存货 | Inventory |
| 其他流动资产 | Other current assets |
| 长期股权投资 | Long-term investments |
| 固定资产 | PPE |
| 在建工程 | Construction in progress |
| 无形资产 | Intangibles |
| 商誉 | Goodwill |
| 长期待摊费用 | Deferred charges |
| 其他非流动资产 | Other non-current |
| 短期借款 | Short-term debt |
| 应付票据 | Notes payable |
| 应付账款 | Accounts payable |
| 合同负债 | Contract liabilities |
| 应付职工薪酬 | Accrued compensation |
| 应交税费 | Taxes payable |
| 其他应付款 | Other payables |
| 一年内到期非流动负债 | Current portion LTD |
| 长期借款 | Long-term debt |
| 应付债券 | Bonds payable |
| 预计负债 | Provisions |
| 递延所得税负债 | DTL |
| 其他非流动负债 | Other non-current |
| 股本 | Share capital |
| 资本公积 | Capital reserve |
| 盈余公积 | Retained earnings (statutory) |
| 未分配利润 | Retained earnings |
| 归属于母公司股东权益 | Parent equity |
| 少数股东权益 | Minority interest |

### Step 8: Quality Checks

**Data quality checklist:**

| Check | Pass Criteria |
|-------|--------------|
| Balance sheet balances | Assets = Liabilities + Equity |
| Cash flow ties | CF = ending cash - beginning cash |
| Revenue matches | Cross-check with segment data |
| Tax reasonable | Tax / pre-tax income ~25% |
| Depreciation consistent | D&A / PPE stable |
| Interest matches | Interest / debt reasonable |

## China-Specific Data Issues

### Common Issues

| Issue | Example | Fix |
|-------|---------|-----|
| 单位不一致 | Some 千元, some 元 | Standardize |
| 会计政策变更 | Revenue recognition change | Adjust comparables |
| 报表格式变化 | New line items | Map to old format |
| 追溯调整 | Prior period restatement | Use restated figures |
| 外币报表 | Subsidiary in USD | Convert to CNY |

### CAS-Specific Treatments

| Item | CAS Treatment |
|------|--------------|
| 研发费用 | Must be expensed (not capitalized, generally) |
| 政府补助 | 总额法 vs 净额法 |
| 股份支付 | Expensed over vesting period |
| 保险合同 | CAS 25 (if applicable) |

## Quality Checks

Before passing data for modeling:
- [ ] All periods complete
- [ ] Units standardized
- [ ] Balance sheet balances
- [ ] Cash flow ties
- [ ] CAS items correctly mapped
- [ ] Non-recurring items flagged
- [ ] Restatements applied
- [ ] Quality issues documented
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
