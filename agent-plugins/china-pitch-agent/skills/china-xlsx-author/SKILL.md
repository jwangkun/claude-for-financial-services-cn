---
name: china-xlsx-author
description: Create professional Excel workbooks for A-share financial analysis. Adapts the original xlsx-author skill for Chinese financial modeling standards, CAS conventions, and A-share formatting. Triggers on "A股Excel模型", "财务模型制作", "create model China", "build model xlsx", "制作模型", or "Excel model [company]".
---

# china-xlsx-author

## Purpose

Create professional **A股财务分析Excel模型** — structured workbooks for Chinese equity analysis.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "income")     → Income statement data
get_financials(ticker, "balance")    → Balance sheet data
get_financials(ticker, "cashflow")   → Cash flow data
get_quote(ticker)                    → Market data
```

### Secondary Sources
- 巨潮 — source filings
- 券商研报 — template references

## Workflow

### Step 1: Workbook Structure

**Standard A-share model structure:**

| Sheet | Content |
|-------|---------|
| 封面 (Cover) | Company, date, version, disclaimer |
| 假设 (Assumptions) | All model inputs, drivers |
| 利润表 (Income) | Historical + forecast P&L |
| 资产负债表 (Balance Sheet) | Historical + forecast BS |
| 现金流量表 (Cash Flow) | Historical + forecast CF |
| 营运资本 (Working Capital) | WC analysis, assumptions |
| 估值 (Valuation) | DCF, comps, sensitivity |
| 图表 (Charts) | Key visuals |
| 检查 (Checks) | Sum checks, balances |

### Step 2: Formatting Standards

**Chinese financial model formatting:**

| Element | Format |
|---------|--------|
| Headers | Bold, background color |
| Inputs | Blue font, light blue background |
| Calculations | Black font, no background |
| Hardcodes (to avoid) | Red font |
| Negative numbers | Red font or (XXX) |
| Percentage | % format, 1 decimal |
| Currency | ¥ or 万元 |
| Dates | YYYY-MM-DD or YYYY年MM月 |

**Color coding:**
```
蓝色 = 输入 (Inputs)
黑色 = 公式 (Calculations)
红色 = 警告 (Warnings / hardcodes)
绿色 = 链接 (Links)
灰色 = 标签 (Labels)
```

### Step 3: Income Statement Layout

**Standard P&L format (CAS):**

| Item | FY2021 | FY2022 | FY2023 | FY2024E | FY2025E |
|------|--------|--------|--------|---------|---------|
| **营业收入** | | | | | |
| 减: 营业成本 | | | | | |
| = 毛利 | | | | | |
| 毛利率 | | | | | |
| 减: 税金及附加 | | | | | |
| 减: 销售费用 | | | | | |
| 减: 管理费用 | | | | | |
| 减: 研发费用 | | | | | |
| 减: 财务费用 | | | | | |
| 加: 投资收益 | | | | | |
| 加: 公允价值变动 | | | | | |
| 减: 信用减值损失 | | | | | |
| 减: 资产减值损失 | | | | | |
| 加: 资产处置收益 | | | | | |
| = 营业利润 | | | | | |
| 加: 营业外收入 | | | | | |
| 减: 营业外支出 | | | | | |
| = 利润总额 | | | | | |
| 减: 所得税费用 | | | | | |
| = 净利润 | | | | | |
| 其中: 归母净利润 | | | | | |
| 其中: 扣非净利润 | | | | | |
| EPS (元/股) | | | | | |

### Step 4: Balance Sheet Layout

**Standard BS format (CAS):**

| Item | FY2021 | FY2022 | FY2023 | FY2024E | FY2025E |
|------|--------|--------|--------|---------|---------|
| **资产** | | | | | |
| 货币资金 | | | | | |
| 交易性金融资产 | | | | | |
| 应收票据 | | | | | |
| 应收账款 | | | | | |
| 预付款项 | | | | | |
| 存货 | | | | | |
| 其他流动资产 | | | | | |
| 流动资产合计 | | | | | |
| 长期股权投资 | | | | | |
| 固定资产 | | | | | |
| 在建工程 | | | | | |
| 无形资产 | | | | | |
| 商誉 | | | | | |
| 其他非流动资产 | | | | | |
| 非流动资产合计 | | | | | |
| **资产总计** | | | | | |
| | | | | | |
| **负债** | | | | | |
| 短期借款 | | | | | |
| 应付票据 | | | | | |
| 应付账款 | | | | | |
| 合同负债 | | | | | |
| 应付职工薪酬 | | | | | |
| 应交税费 | | | | | |
| 其他应付款 | | | | | |
| 流动负债合计 | | | | | |
| 长期借款 | | | | | |
| 应付债券 | | | | | |
| 预计负债 | | | | | |
| 非流动负债合计 | | | | | |
| **负债合计** | | | | | |
| | | | | | |
| **所有者权益** | | | | | |
| 股本 | | | | | |
| 资本公积 | | | | | |
| 盈余公积 | | | | | |
| 未分配利润 | | | | | |
| 归母股东权益 | | | | | |
| 少数股东权益 | | | | | |
| **所有者权益合计** | | | | | |
| **负债及权益总计** | | | | | |

### Step 5: Assumptions Sheet

**Key assumptions to centralize:**

| Category | Assumption | Value | Source |
|----------|-----------|-------|--------|
| Revenue growth | FY2024E | X% | |
| Revenue growth | FY2025E | X% | |
| Gross margin | FY2024E | X% | |
| SG&A % of revenue | FY2024E | X% | |
| Tax rate | Effective | X% | |
| D&A | % of PPE | X% | |
| CapEx | % of revenue | X% | |
| NWC | % of revenue | X% | |
| Terminal growth | | X% | |
| WACC | | X% | |

### Step 6: Valuation Sheet

**DCF layout:**

| Item | Value | Notes |
|------|-------|-------|
| Enterprise value | ¥XX亿 | |
| Less: Net debt | ¥XX亿 | |
| Equity value | ¥XX亿 | |
| Shares outstanding | XX亿股 | |
| Value per share | ¥XX | |
| Current price | ¥XX | |
| Upside/(Downside) | X% | |

**Football field:**

| Method | Low | Mid | High |
|--------|-----|-----|------|
| P/E | | | |
| P/B | | | |
| EV/EBITDA | | | |
| DCF | | | |
| **Range** | **¥XX** | **¥XX** | **¥XX** |

### Step 7: Checks Sheet

**Essential checks:**

| Check | Formula | Target | Result |
|-------|---------|--------|--------|
| BS balances | Assets - L - E | 0 | |
| CF ties | Ending cash - Beg cash - Net CF | 0 | |
| Revenue growth | (Rev - Rev_prev) / Rev_prev | Reasonable | |
| Margin check | GP / Revenue | Reasonable | |
| Debt schedule | ST + LT debt | = Total | |
| Retained earnings | RE beg + NI - Div | = RE end | |
| Depreciation | D&A / PPE | Reasonable | |

### Step 8: Charts & Presentation

**Key charts to include:**

| Chart | Purpose |
|-------|---------|
| Revenue & profit bridge | Historical + forecast |
| Margin trends | Gross, operating, net |
| Valuation multiples | Historical range |
| DCF sensitivity | Tornado chart |
| Peer comparison | Comps scatter plot |

## China-Specific Excel Conventions

### Unit Standards

| Unit | Usage |
|------|-------|
| 元 | Per-share items |
| 万元 | Most financial items |
| 亿元 | Large totals, market cap |

### Naming Conventions

| Item | Convention |
|------|-----------|
| Sheet names | Short, Chinese preferred |
| Cell references | Named ranges for key cells |
| File naming | [Ticker]_[Company]_[Date]_v[X] |

### Formula Conventions

| Convention | Example |
|------------|---------|
| Sheet references | '利润表'!B10 |
| Named ranges | Revenue, WACC, Shares |
| Chinese function names | SUM, IF, VLOOKUP |

## Quality Checks

Before finalizing:
- [ ] All sheets present and linked
- [ ] No hardcodes in calculation cells
- [ ] Historicals cross-checked
- [ ] CAS conventions applied
- [ ] BS balances and CF ties
- [ ] Valuation reasonable
- [ ] Charts update automatically
- [ ] All checks green
- [ ] Documentation complete
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
