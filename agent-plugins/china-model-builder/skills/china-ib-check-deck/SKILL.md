---
name: china-ib-check-deck
description: Quality check investment banking pitch decks for A-share M&A and capital raising transactions. Adapts the original ib-check-deck skill for Chinese market standards, CAS financials, and domestic IB conventions. Triggers on "投行deck检查", "IB deck QC", "check pitch deck China", "deck quality check", "材料质量检查", or "review deck [company/transaction]".
---

# china-ib-check-deck

## Purpose

Quality-check **A股投行材料** — comprehensive quality assurance for Chinese investment banking pitch decks and transaction materials.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "income")     → Financial data verification
get_financials(ticker, "balance")    → Balance sheet verification
get_quote(ticker)                    → Market data verification
```

### Secondary Sources
- 巨潮 — source documents
- 审计报告 — reference financials
- 行业报告 — market data

## Workflow

### Step 1: Deck Structure Review

**Structure checklist:**

| Section | Required | Present | Quality |
|---------|----------|---------|---------|
| 封面 (Cover) | ✓ | | |
| 目录 (TOC) | ✓ | | |
| 交易概述 (Transaction Overview) | ✓ | | |
| 公司概览 (Company Overview) | ✓ | | |
| 行业分析 (Industry Analysis) | ✓ | | |
| 财务表现 (Financial Performance) | ✓ | | |
| 交易逻辑 (Investment Rationale) | ✓ | | |
| 估值 (Valuation) | ✓ | | |
| 风险提示 (Risk Factors) | ✓ | | |
| 附录 (Appendix) | ✓ | | |

### Step 2: Data Accuracy Check

**Data verification:**

| Data Point | Source | Model/File | Match? | Notes |
|------------|--------|-----------|--------|-------|
| Revenue (latest) | 巨潮 | | | |
| Net income (latest) | 巨潮 | | | |
| EBITDA | Calculated | | | |
| Market cap | iFind / AkShare | | | |
| P/E | Calculated | | | |
| P/B | Calculated | | | |
| EV | Calculated | | | |
| Net debt | Balance sheet | | | |
| Share count | Annual report | | | |

**Tolerance levels:**
- Revenue, profit: ±2%
- Balance sheet: ±1%
- Multiples: ±5%
- Market data: ±1%

### Step 3: Financial Statement Review

**Financial consistency checks:**

| Check | Description | Pass |
|-------|-------------|------|
| Revenue growth | Consistent across slides | ✓ |
| Margin trends | Consistent across slides | ✓ |
| Balance sheet totals | Assets = L + E | ✓ |
| Cash flow ties | Beginning + CF = Ending | ✓ |
| Debt schedule | Short + Long = Total | ✓ |
| Share count | Consistent throughout | ✓ |

### Step 4: CAS Compliance

**CAS-specific checks:**

| Check | Description |
|-------|-------------|
| Revenue | Net of VAT (不含税) |
| R&D | Expensed (unless capitalized per criteria) |
| Tax | 25% rate applied correctly |
| Minority interest | Separated from parent |
| 合同负债 | Recognized per CAS 14 |
| 信用减值损失 | CAS 22 model |

### Step 5: Valuation Review

**Valuation checks:**

| Method | Check | Pass |
|--------|-------|------|
| DCF | WACC components reasonable | ✓ |
| DCF | Terminal growth < GDP | ✓ |
| DCF | FCF positive in base case | ✓ |
| Comps | Peer group appropriate | ✓ |
| Comps | Multiples reasonable range | ✓ |
| Football field | Consistent range | ✓ |
| Target price | Matches valuation | ✓ |

### Step 6: Visual Quality

**Design QA:**

| Element | Check |
|---------|-------|
| 模板一致性 | All slides use same template |
| 字体 | Chinese fonts render correctly |
| 颜色 | Consistent color scheme |
| 图表 | All charts labeled, sourced |
| 表格 | Clean, readable format |
| 对齐 | Proper alignment throughout |
| 图片 | High resolution, appropriate |
| 页码 | Present and correct |

### Step 7: Regulatory Compliance

**Required elements:**

| Element | Required | Present |
|---------|----------|---------|
| 风险提示 | ✓ | |
| 免责声明 | ✓ | |
| 数据来源 | ✓ | |
| 评级说明 | ✓ | |
| 适当性提示 | ✓ | |

**Risk factors checklist:**
- [ ] Market risk (市场风险)
- [ ] Industry risk (行业风险)
- [ ] Company-specific risk (公司风险)
- [ ] Policy risk (政策风险)
- [ ] Liquidity risk (流动性风险)

### Step 8: Transaction-Specific Checks

**M&A specific:**

| Check | Description |
|-------|-------------|
| Transaction rationale | Clear and compelling |
| Synergies | Quantified and realistic |
| Accretion/dilution | Calculated and shown |
| Integration plan | Mentioned |
| Regulatory approval | Identified |

**Capital raising specific:**

| Check | Description |
|-------|-------------|
| Use of proceeds | Detailed and specific |
| Investor return | IRR / cash-on-cash |
| Market comparables | Similar transactions |
| Timing | Market window assessment |

### Step 9: Cross-Reference Check

**Cross-reference audit:**

| Reference | Location | Correct? |
|-----------|----------|----------|
| Revenue figure | [Slide X] | |
| Net income | [Slide Y] | |
| Target price | [Slide Z] | |
| P/E multiple | [Slide W] | |
| Market cap | [Slide V] | |

### Step 10: QC Report

**Standard QC output:**

```
【Deck QC 报告】[Company/Transaction] [Date]

一、结构检查
   完整性: [Pass/Fail]
   逻辑性: [Pass/Fail]
   
二、数据准确性
   财务数据: [Pass/Fail with notes]
   市场数据: [Pass/Fail with notes]
   估值数据: [Pass/Fail with notes]
   
三、CAS合规性
   [Pass/Fail with notes]
   
四、设计质量
   [Pass/Fail with notes]
   
五、监管合规
   风险提示: [Pass/Fail]
   免责声明: [Pass/Fail]
   
六、发现的问题
   严重 (Critical):
   [List]
   
   中等 (Major):
   [List]
   
   轻微 (Minor):
   [List]
   
七、建议修复
   [Prioritized list]
   
总体评价: [Approve / Revise / Reject]
```

## China-Specific QC Considerations

### Common Issues in A-share Decks

| Issue | Detection | Fix |
|-------|-----------|-----|
| 收入含税 | VAT not removed | Divide by 1.13 |
| 税率错误 | Wrong rate | Verify 高新 status |
| 单位不一致 | Mixed 千元/万元 | Standardize |
| 会计政策 | Wrong treatment | Check CAS |
| 数据来源 | Missing citations | Add source |
| 风险提示 | Missing/incomplete | Add required risks |

### Regulatory Requirements

| Requirement | Content |
|-------------|---------|
| 风险揭示 | Standard risk factors |
| 免责声明 | Standard disclaimer |
| 适当性 | Suitability statement |
| 历史业绩 | Past performance disclaimer |

## Quality Checks

Before approving:
- [ ] Structure complete
- [ ] Data verified
- [ ] CAS compliant
- [ ] Valuation sound
- [ ] Design quality
- [ ] Regulatory compliant
- [ ] All issues addressed
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
