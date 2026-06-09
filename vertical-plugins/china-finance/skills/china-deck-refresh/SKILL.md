---
name: china-deck-refresh
description: Refresh and update existing A-share investment presentation decks with latest data. Adapts the original deck-refresh skill for Chinese presentations, A-share data updates, and domestic market conventions. Triggers on "更新PPT", "刷新演示", "refresh deck China", "update presentation", "更新演示文稿", or "refresh slides [company]".
---

# china-deck-refresh

## Purpose

Refresh **A股投资分析PPT** — update existing presentation decks with latest financial data and market information.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_quote(ticker)                     → Latest stock price
get_financials(ticker, "income")      → Latest financials
get_index_data("000001")              → Market context
get_industry_stocks(industry="...")    → Updated peer data
```

### Secondary Sources
- 巨潮 — latest filings
- Wind / Choice — market data

## Workflow

### Step 1: Inventory Existing Deck

**Deck audit:**

| Slide | Title | Data to Update | Status |
|-------|-------|---------------|--------|
| 1 | Cover | Date, version | |
| 2 | Investment Summary | Target price, rating | |
| 3 | Company Overview | Market cap, shares | |
| 4 | Financial Highlights | Latest results | |
| 5 | Revenue Bridge | Latest actuals | |
| 6 | Margin Analysis | Latest margins | |
| 7 | Peer Comparison | Updated multiples | |
| 8 | Valuation | Price, multiples | |
| 9 | Risk Factors | Current risks | |
| 10 | Recommendation | Target price | |

### Step 2: Update Financial Data

**Data update checklist:**

| Data Item | Source | Update Frequency |
|-----------|--------|-----------------|
| Stock price | iFind / AkShare | Daily |
| Market cap | Calculated | Daily |
| P/E, P/B | Calculated | Daily |
| Revenue (LTM) | iFind / AkShare / 巨潮 | Quarterly |
| Net income (LTM) | iFind / AkShare / 巨潮 | Quarterly |
| Margins | Calculated | Quarterly |
| Peer multiples | iFind / AkShare | Quarterly |
| Forecast estimates | 券商研报 | Quarterly |

### Step 3: Update Charts

**Chart update priorities:**

| Priority | Chart | Update Trigger |
|----------|-------|----------------|
| 1 | Stock price chart | Always |
| 2 | Revenue/profit | New quarterly results |
| 3 | Margin trends | New quarterly results |
| 4 | Peer comparison | New quarterly results |
| 5 | Valuation | Daily / new results |
| 6 | Financial trends | New annual results |

**Chart update steps:**
1. Identify linked Excel data sources
2. Update source data
3. Refresh chart (right-click → refresh)
4. Verify chart accuracy
5. Update chart date if needed

### Step 4: Update Text Content

**Text update checklist:**

| Element | Update |
|---------|--------|
| 日期 | Current date |
| 版本号 | Increment version |
| 股价 | Latest closing price |
| 市值 | Latest market cap |
| 目标价 | If changed |
| 评级 | If changed |
| 财务数据 | Latest actuals |
| 一致预期 | Updated consensus |
| 行业数据 | Latest industry reports |
| 新闻/事件 | Recent developments |

### Step 5: Maintain Consistency

**Consistency checks:**

| Check | Description |
|-------|-------------|
| 数据一致性 | Same numbers across all slides |
| 日期一致性 | All dates current |
| 评级一致性 | Rating consistent throughout |
| 目标价一致性 | Target price matches valuation slide |
| 图表一致性 | Same color scheme, labeling |

### Step 6: Version Control

**Version tracking:**

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| v1.0 | | Initial | |
| v1.1 | | Updated financials | |
| v1.2 | | New earnings | |
| v2.0 | | Major refresh | |

**File naming:**
```
[Ticker]_[Company]_[ReportType]_v[X.X]_[YYYYMMDD].pptx
Example: {{TICKER}}_{{COMPANY_NAME}}_{{REPORT_TITLE}}_v2.1_20240605.pptx
```

### Step 7: Quality Assurance

**QA checklist:**

| Check | Pass Criteria |
|-------|--------------|
| All data current | Latest available |
| No broken charts | All charts display |
| Consistent numbers | Cross-slide verification |
| No typos | Spell check |
| Formatting intact | Design unchanged |
| Links working | All links functional |
| File size reasonable | Not bloated |

### Step 8: Distribution

**Distribution preparation:**

| Item | Action |
|------|--------|
| File format | Save as .pptx (editable) + .pdf (distribution) |
| File size | Compress if >50MB |
| Naming | Follow convention |
| Version note | Brief change summary |
| Distribution list | Email / shared drive |

## Common Update Scenarios

### Scenario 1: Quarterly Earnings Update

| Action | Detail |
|--------|--------|
| Update P&L | Add latest quarter actuals |
| Update BS | Add latest quarter BS |
| Update CF | Add latest quarter CF |
| Update charts | Refresh financial charts |
| Update commentary | Reflect latest results |
| Update target price | If changed |
| Version bump | vX.X → vX.X+1 |

### Scenario 2: Daily/Weekly Market Update

| Action | Detail |
|--------|--------|
| Update price | Latest closing price |
| Update market cap | Recalculate |
| Update multiples | Recalculate P/E, P/B |
| Update price chart | Add recent data |
| Version bump | Minor version |

### Scenario 3: Full Refresh (Semi-annual)

| Action | Detail |
|--------|--------|
| All financials | Full year actuals + new forecasts |
| All charts | Complete refresh |
| Peer set | Update peer group |
| Valuation | Full revaluation |
| All commentary | Comprehensive update |
| Version bump | Major version |

## China-Specific Considerations

### A-share Update Frequency

| Update Type | Frequency | Trigger |
|-------------|-----------|---------|
| 盘中更新 | Daily | Market movement |
| 盘后更新 | Daily | Close of trading |
| 业绩更新 | Quarterly | Earnings release |
| 深度更新 | Semi-annual | Full refresh |

### Common Issues

| Issue | Solution |
|-------|----------|
| 图表链接断开 | Re-link data source |
| 字体缺失 | Embed fonts or use standard fonts |
| 版本混乱 | Clear version control |
| 数据不一致 | Cross-slide verification |

## Quality Checks

Before distributing:
- [ ] All data updated
- [ ] All charts refreshed
- [ ] Consistency verified
- [ ] No broken links
- [ ] QA complete
- [ ] Version noted
- [ ] File formats correct
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
