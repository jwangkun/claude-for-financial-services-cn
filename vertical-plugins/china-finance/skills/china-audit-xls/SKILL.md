---
name: china-audit-xls
description: Audit financial models and Excel workbooks for A-share analysis. Adapts the original audit-xls skill for Chinese financial modeling standards, CAS conventions, and A-share-specific checks. Triggers on "A股模型审计", "财务模型核查", "audit model China", "audit xlsx", "模型QC", or "check model [company]".
---

# china-audit-xls

## Purpose

Audit **A股财务模型** — comprehensive quality checks for Chinese equity financial models.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_financials(ticker, "income")     → Actuals for cross-check
get_financials(ticker, "balance")    → BS for cross-check
get_financials(ticker, "cashflow")   → CF for cross-check
get_quote(ticker)                    → Market data
```

### Secondary Sources
- 巨潮 — source financials
- 审计报告 — reference data

## Workflow

### Step 1: Structural Audit

**Model structure checklist:**

| Area | Check | Pass Criteria |
|------|-------|--------------|
| Cover page | Company, date, version | Present and accurate |
| Assumptions | All key inputs centralized | No hardcoded values in calc |
| Historicals | All periods populated | 3-5 years |
| Forecast | Explicit forecast period | 3-5 years |
| Valuation | DCF, comps, football field | All methods present |
| Checks | Sum, balance, cross-ref | All checks green |
| Documentation | Methodology notes | Clear and complete |

### Step 2: Formula Audit

**Formula checks:**

| Check | Description | Pass Criteria |
|-------|-------------|--------------|
| No hardcodes | All inputs in assumptions | ✓ |
| Consistent formulas | Same formula across periods | ✓ |
| No circularity (unless intended) | Circular refs flagged | ✓ |
| Error handling | IFERROR used where needed | ✓ |
| Named ranges | Key cells named | ✓ |
| Sheet references | Cross-sheet refs work | ✓ |
| Broken links | No external links or all work | ✓ |

**Common hardcodes to find:**
- Growth rates embedded in formulas
- Multiples typed into cells
- Shares outstanding hardcoded
- Tax rates not in assumptions

### Step 3: Historicals Cross-Check

**Cross-check against source data:**

| Line Item | Model | iFind / AkShare / 巨潮 | Difference | Explanation |
|-----------|-------|----------------|------------|-------------|
| 营业收入 | | | | |
| 营业成本 | | | | |
| 归母净利润 | | | | |
| 总资产 | | | | |
| 净资产 | | | | |
| 经营现金流 | | | | |

**Cross-check tolerance:**
- Revenue, profit: ±2%
- Balance sheet: ±1%
- Cash flow: ±3% (timing differences)

### Step 4: CAS Compliance Check

**CAS-specific checks:**

| Check | Description |
|-------|-------------|
| Revenue net of VAT | 营业收入 not gross |
| R&D expensed | Not capitalized (unless criteria met) |
| Tax calculation | 25% / 15% rate applied correctly |
| Minority interest | Separated from parent equity |
| Government grants | Correct classification |
| 合同负债 | Recognized appropriately |
| 信用减值损失 | CAS 22 model applied |

### Step 5: Balance Sheet Integrity

**BS checks:**

| Check | Formula | Pass |
|-------|---------|------|
| BS balances | Assets = L + E | ✓ |
| Cash flow ties | Ending cash = Beginning + Net CF | ✓ |
| Debt schedule | Short + Long = Total debt | ✓ |
| Share count | Shares × Price = Market cap | ✓ |
| Minority interest | Correct % applied | ✓ |

### Step 6: Forecast Logic Check

**Forecast quality:**

| Check | Description | Pass |
|-------|-------------|------|
| Growth reasonable | Within industry range | ✓ |
| Margins stable | No unexplained jumps | ✓ |
| Working capital | Trends with revenue | ✓ |
| CapEx | Consistent with depreciation | ✓ |
| Debt service | Can be serviced from FCF | ✓ |
| Dividend | Consistent with policy | ✓ |

**Growth rate benchmarks:**

| Metric | Conservative | Base | Optimistic |
|--------|-------------|------|-----------|
| Revenue growth | 5-10% | 10-20% | 20-30% |
| Margin expansion | 0 ppts | 0-2 ppts | 2-5 ppts |
| Tax rate | 25% | 25% | 15% (if 高新) |

### Step 7: Valuation Check

**Valuation audit:**

| Method | Check | Pass |
|--------|-------|------|
| DCF | WACC reasonable (6-10%) | ✓ |
| DCF | Terminal growth < GDP growth | ✓ |
| DCF | FCF positive in base case | ✓ |
| Comps | Peer group appropriate | ✓ |
| Comps | Multiples reasonable | ✓ |
| Football field | Min/median/max consistent | ✓ |

**WACC components (China):**

| Component | Typical Range |
|-----------|--------------|
| Risk-free rate (CGB 10Y) | 2.0-3.0% |
| Equity risk premium | 6-8% |
| Cost of debt | 3-6% |
| Tax rate | 25% (15% for 高新) |

### Step 8: Sensitivity & Scenario Check

**Sensitivity audit:**

| Check | Description |
|-------|-------------|
| Sensitivity tables | Key variables tested |
| Scenarios | Base / Bull / Bear |
| Tornado chart | Key drivers identified |
| Monte Carlo (if used) | Assumptions reasonable |

### Step 9: Common A-share Model Errors

**Error checklist:**

| Error | Detection | Fix |
|-------|-----------|-----|
| 收入用含税 | VAT not removed | Divide by 1.13 |
| 税率错误 | Wrong rate applied | Verify 高新 status |
| 单位错误 | 千元 vs 万元 | Standardize |
| 季度加总错误 | Q+Q ≠ Annual | Check sum |
| 增长率计算 | Wrong base period | Verify formula |
| 少数股东损益 | Missing | Add if applicable |
| 折旧年限 | Wrong | Check FA notes |

### Step 10: Audit Report

**Standard audit output:**

```
【模型审计报告】[Company] [Date]

一、结构检查
   [Structure assessment]

二、公式检查
   [Formula audit results]

三、历史数据核对
   [Cross-check results]

四、CAS合规检查
   [CAS compliance]

五、预测逻辑检查
   [Forecast quality]

六、估值检查
   [Valuation audit]

七、发现的问题
   [List of issues with severity]

八、建议修复
   [Recommended fixes]

总体评价: [Pass / Pass with conditions / Fail]
```

## Quality Checks

Before completing:
- [ ] All structural checks passed
- [ ] No hardcodes found
- [ ] Historicals cross-checked
- [ ] CAS compliant
- [ ] BS/CF integrity verified
- [ ] Forecast logic sound
- [ ] Valuation reasonable
- [ ] All issues documented
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
