---
name: china-roll-forward
description: Roll forward A-share financial models for new periods. Adapts the original roll-forward skill for Chinese financial statements, CAS conventions, and A-share reporting calendars. Triggers on "A股模型滚动", "模型更新", "roll forward model China", "roll forward", "更新财务模型", or "project [company] [period]".
---

# china-roll-forward

## Purpose

Roll forward **A股财务模型** — update financial models for new reporting periods.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "income")     → Latest actuals
get_financials(ticker, "balance")    → Latest BS
get_financials(ticker, "cashflow")   → Latest CF
```

### Secondary Sources
- 巨潮 — latest filings
- 业绩预告 — early guidance
- 券商研报 — updated estimates

## Workflow

### Step 1: Identify New Period

**Period identification:**

| Period Type | Frequency | Typical Timing |
|-------------|-----------|----------------|
| 一季报 (Q1) | Quarterly | April 30 deadline |
| 中报 (H1) | Semi-annual | August 31 deadline |
| 三季报 (Q3) | Quarterly | October 31 deadline |
| 年报 (Annual) | Annual | April 30 deadline |

**Calendar:**
```
Q1: 1月1日 - 3月31日 → 披露截止 4月30日
H1: 1月1日 - 6月30日 → 披露截止 8月31日
Q3: 1月1日 - 9月30日 → 披露截止 10月31日
FY: 1月1日 - 12月31日 → 披露截止 次年4月30日
```

### Step 2: Pull Latest Actuals

**Data to pull:**

| Statement | Key Line Items |
|-----------|---------------|
| 利润表 | Revenue, gross profit, operating profit, net income |
| 资产负债表 | Cash, AR, inventory, PPE, debt, equity |
| 现金流量表 | OCF, investing CF, financing CF |
| 附注 | Segment data, related party, provisions |

### Step 3: Update Model Structure

**Model update checklist:**

| Section | Action |
|---------|--------|
| Historicals | Replace with latest actuals |
| QTD data | Add new period actuals |
| YTD data | Update year-to-date |
| LTM data | Recalculate LTM |
| Growth rates | Recalculate YoY/QoQ |
| Ratios | Recalculate all ratios |
| Graphs | Update charts |

### Step 4: Validate Actuals

**Actuals validation:**

| Check | Method |
|-------|--------|
| 报表平衡 | Assets = Liabilities + Equity |
| 勾稽关系 | CF = ΔCash |
| 季度加总 | Q1+Q2+Q3+Q4 = Annual |
| 同比计算 | (Current - Prior) / Prior |
| 环比率 | (Current - Qprior) / Qprior |

**Common CAS adjustments:**
- 增值税处理 (Revenue net of VAT)
- 政府补助分类 (Operating vs non-operating)
- 研发费用 (Separate from G&A)
- 信用减值损失 (CAS 22 expected credit loss)

### Step 5: Update Forecasts

**Forecast update logic:**

| Scenario | Action |
|----------|--------|
| In-line | No change to full-year forecast |
| Beat | Assess if full-year guidance should be raised |
| Miss | Assess if full-year guidance should be lowered |
| Guidance change | Update model for management guidance |

**Forecast roll-forward:**

| Period | Prior | Actual | New Forecast | Change |
|--------|-------|--------|--------------|--------|
| Q1 | | | | |
| Q2 | | | | |
| Q3 | | | | |
| Q4 | | | | |
| Full year | | | | |

### Step 6: Update Valuation

**Valuation update:**

| Input | Prior | Current | Change |
|-------|-------|---------|--------|
| Current price | | | |
| Shares outstanding | | | |
| Market cap | | | |
| P/E (NTM) | | | |
| P/B | | | |
| EV/EBITDA | | | |
| Target price | | | |
| Upside/downside | | | |

### Step 7: Update Narrative

**Narrative updates:**

| Section | Update |
|---------|--------|
| Investment thesis | Review and update |
| Key drivers | Reflect latest results |
| Catalysts | Update timeline |
| Risks | Review and update |
| Target price | Update with new base |

### Step 8: Quality Checks

**Roll-forward QC:**

| Check | Pass Criteria |
|-------|--------------|
| All actuals pulled | All periods updated |
| Sum checks pass | Quarterly = Annual |
| Ratios recalculated | All formulas updated |
| Graphs updated | All charts reflect new data |
| Valuation current | Target price updated |
| No hardcodes | All cells formula-driven |
| CAS compliant | Chinese conventions applied |

## China-Specific Roll-Forward Considerations

### Reporting Calendar

| Filing | Deadline | Typical Release |
|--------|----------|-----------------|
| 业绩预告 (optional) | Before filing | 10-15 days before |
| 一季报 | April 30 | April |
| 中报 | August 31 | August |
| 三季报 | October 31 | October |
| 年报 | April 30 | Late March-April |

### Common Update Triggers

| Trigger | Action |
|---------|--------|
| Scheduled earnings | Full model update |
| 业绩预告 | Preliminary forecast update |
| Guidance change | Update full-year forecast |
| M&A announcement | Model for transaction impact |
| Policy change | Sector/company impact |
| Analyst day | Update long-term assumptions |

## Quality Checks

Before completing:
- [ ] Latest actuals pulled and entered
- [ ] All historical periods updated
- [ ] Forecasts rolled forward
- [ ] Valuation updated
- [ ] Sum checks pass
- [ ] No hardcodes introduced
- [ ] Documentation updated
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
