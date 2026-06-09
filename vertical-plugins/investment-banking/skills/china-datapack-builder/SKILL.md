---
name: china-datapack-builder
description: Build professional data packs for A-share investment banking deals — M&A due diligence, IC materials, company profiles. Adapted from the original datapack-builder skill for Chinese data sources (AkShare, 巨潮, exchange filings) and CAS accounting. Triggers on "A股数据包", "投行数据包", "datapack China", "due diligence pack A-share", or "IC data pack [company]".
---

# china-datapack-builder

## Purpose

Build professional **A股投行数据包 (Data Pack)** for investment banking workflows — M&A due diligence, IC review, deal execution.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_financials(ticker, "income", "annual")   → P&L history
get_financials(ticker, "balance", "annual")  → Balance sheet
get_financials(ticker, "cashflow", "annual") → Cash flow
get_quote(ticker)                            → Current valuation
get_historical_data(ticker)                  → Trading history
get_industry_stocks(industry="...")           → Peer comparison
get_stock_info(ticker)                       → Company profile
```

### Secondary Sources

- **巨潮资讯** — mandatory filings (年报, 中报, 季报)
- **上交所 / 深交所** — announcements, filings
- **公司官网** — investor materials
- **企查查 / 天眼查** — corporate structure
- **Wind / Choice** — comprehensive data

## Workflow

### Step 1: Define Pack Scope

**Data pack types:**

| Pack Type | Purpose | Typical Content |
|-----------|---------|-----------------|
| Company overview | Initial target screening | Financials, profile, peers |
| Due diligence | Pre-deal deep dive | 3-statement, quality of earnings, debt |
| IC preparation | Investment committee | Executive summary, model, risks |
| M&A comps | Comparable transactions | Precedent deals, trading comps |
| Sector deep dive | Market context | Industry overview, competitive map |

### Step 2: Gather Source Materials

**Financial data collection:**

```python
# 3-5 years historicals
for year in range(2020, 2025):
    get_financials(ticker, "income", "annual")
    get_financials(ticker, "balance", "annual")
    get_financials(ticker, "cashflow", "annual")
```

**Corporate information:**
- 公司股权结构 (ownership structure)
- 子公司/参股公司 (subsidiaries / associates)
- 关联交易 (related party transactions)
- 对外担保 (guarantees)
- 诉讼仲裁 (litigation / arbitration)

**Market data:**
- Current and historical share price
- Trading volumes and liquidity
- Ownership breakdown (institutional, retail, 北向)
- Shareholder changes over time

### Step 3: Normalize & Structure

**Data normalization standards:**

1. **Currency**: All figures in CNY (人民币)
2. **Units**: Consistent (亿元 preferred for large companies)
3. **Periods**: Align fiscal years (typically Dec 31)
4. **Adjustments**: Normalize for one-time items

**Standard data pack sections:**

#### Section 1: Executive Summary
- 1-page overview
- Key investment highlights
- Valuation summary
- Critical risks

#### Section 2: Company Overview
- Business description
- History and milestones
- Organizational structure
- Management team
- Shareholder structure

#### Section 3: Financial Summary
- Income statement (3-5 years)
- Balance sheet (3-5 years)
- Cash flow statement (3-5 years)
- Key ratios and metrics
- Revenue bridge

#### Section 4: Operating Metrics
- Revenue by segment
- Volume / unit data (if relevant)
- Capacity / utilization
- Geographic breakdown

#### Section 5: Quality of Earnings
- Revenue quality (cash conversion)
- Margin analysis
- One-time items identification
- Earnings sustainability

#### Section 6: Balance Sheet Analysis
- Asset quality
- Working capital efficiency
- Debt structure
- Off-balance sheet items

#### Section 7: Peer Comparison
- Trading multiples
- Financial metrics
- Operating metrics
- Valuation dispersion

#### Section 8: Transaction History
- Historical M&A
- Capital raising history
- Major corporate actions

#### Section 9: Risk Factors
- Company-specific risks
- Industry risks
- Regulatory risks
- Market risks

### Step 4: Excel Workbook Structure

**Recommended tabs:**

| Tab | Content |
|-----|---------|
| 封面 (Cover) | Pack title, date, confidentiality |
| 摘要 (Summary) | Key data points, valuation |
| 利润表 (Income Statement) | Historical + projected |
| 资产负债表 (Balance Sheet) | Historical + projected |
| 现金流量表 (Cash Flow) | Historical + projected |
| 财务指标 (Key Metrics) | Ratios, growth rates |
| 可比公司 (Comparable Cos) | Peer analysis |
| 估值 (Valuation) | DCF, multiples, football field |
| 运营数据 (Operating Data) | Volume, capacity, etc. |
| 公司治理 (Governance) | Ownership, management, related party |
| 风险 (Risks) | Risk factor analysis |

### Step 5: Quality Standards

**Data integrity:**
- [ ] All figures sourced from 巨潮 PDF or AkShare
- [ ] Cross-referenced against multiple sources where possible
- [ ] Adjustments documented
- [ ] No transcription errors

**Formatting:**
- [ ] Consistent formatting throughout
- [ ] Clear section headers
- [ ] Source citations in cell comments
- [ ] Professional appearance

**Completeness:**
- [ ] All sections relevant to deal type included
- [ ] Key risks identified and documented
- [ ] Valuation analysis complete
- [ ] Peer comparison adequate

## China-Specific Considerations

### Regulatory Filings

| Filing | Frequency | Source | Key Data |
|--------|-----------|--------|----------|
| 年报 (Annual report) | Annual | 巨潮 | Full financials, MD&A, risks |
| 中报 (Semi-annual) | Semi-annual | 巨潮 | Condensed financials |
| 季报 (Quarterly) | Quarterly | 巨潮 | Condensed financials |
| 业绩预告 | As required | 巨潮 | Directional guidance |
| 重大事项公告 | Ad-hoc | 巨潮 | M&A, contracts, etc. |

### Common Data Issues

| Issue | Solution |
|-------|----------|
| 千元 vs 元 units | Check 财务报表附注 for units |
| 合并 vs 母公司报表 | Use 合并报表 for group analysis |
| 非经常性损益 | Flag and normalize |
| 政府补助 | Identify and separate |
| 关联交易占比高 | Flag for due diligence |

### Industry-Specific Data

| Industry | Special Data Needs |
|----------|-------------------|
| 白酒 | 批价数据, 渠道库存, 经销商数量 |
| 半导体 | 产能数据, 晶圆出货, 客户结构 |
| 新能源 | 装机量, 产能, 技术参数 |
| 医药 | 管线数据, 临床进展, 集采中标 |
| 房地产 | 可售资源, 去化率, 土储 |

## Quality Checks

Before delivering:
- [ ] Data pack scope clearly defined
- [ ] All financials complete and accurate
- [ ] Source materials documented
- [ ] Adjustments transparent
- [ ] Peer comparison relevant
- [ ] Valuation analysis included
- [ ] Risk factors comprehensive
- [ ] Excel workbook well-structured
- [ ] Confidentiality notices included
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
