---
name: china-initiating-coverage
description: Institutional-quality equity research initiation reports for A-share companies. Covers company analysis, financial modeling, valuation, chart preparation, and final report assembly. Adapted from the original initiating-coverage skill for Chinese market conventions, CAS accounting, and AkShare data sources. Triggers on "A股首次覆盖", "首次评级", "initiate coverage China", "initiate on [company]", "A股研究报告", or "start research on [company]".
---

# china-initiating-coverage

## Purpose

Create institutional-quality **A股首次覆盖研究报告**, following Chinese sell-side research standards.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_stock_info(ticker)                    → Company profile
get_quote(ticker)                        → Current valuation
get_historical_data(ticker)              → Trading history
get_financials(ticker, "income")         → Historical P&L
get_financials(ticker, "balance")        → Historical BS
get_financials(ticker, "cashflow")        → Historical CF
get_industry_stocks(industry="...")       → Peer companies
```

### Secondary Sources

- **巨潮资讯** — official filings (annual reports, prospectus)
- **上交所 / 深交所** — listing documents, announcements
- **公司官网** — investor relations, presentations
- **慧博 / Wind / Choice** — consensus estimates
- **券商研报** — existing analyst coverage (if any)
- **行业协会** — industry data

## Workflow

### Task 1: Company Research

**Company overview:**
- Business description (主营业务)
- History and development (发展历程)
- Ownership structure (股权结构)
- Management team (管理层)
- Shareholder composition (股东构成)

**Business segments:**

| Segment | Revenue % | Margin | Growth Driver |
|---------|-----------|--------|---------------|
| | | | |

**Key questions to answer:**
1. What does the company do? How does it make money?
2. What is its competitive advantage? (护城河)
3. What are the key growth drivers?
4. What are the main risks?
5. Who are the comparable companies?

### Task 2: Financial Modeling

Build a financial model (refer to `china-3-statement-model` skill):

**Historical analysis (3-5 years):**

| Metric | 2020 | 2021 | 2022 | 2023 | 2024E | 2025E | 2026E |
|--------|------|------|------|------|-------|-------|-------|
| Revenue (亿) | | | | | | | |
| YoY Growth | | | | | | | |
| Gross Margin | | | | | | | |
| Operating Margin | | | | | | | |
| Net Margin | | | | | | | |
| ROE | | | | | | | |
| Net Debt/EBITDA | | | | | | | |

**Key modeling considerations (see china-3-statement-model):**
- CAS accounting standards
- 25% tax rate (or 15% for 高新技术企业)
- 千元 vs 元 unit normalization
- 增值税 treatment
- 商誉 flagging
- R&D expense treatment

### Task 3: Valuation Analysis

**Build comprehensive valuation:**

1. **DCF** (refer to `china-dcf` skill)
   - WACC with CGB risk-free rate
   - 6-8% China ERP
   - 25% tax rate
   - CNY denominated

2. **Comparable companies** (refer to `china-comps` skill)
   - Peer set from same 东方财富 industry
   - PE, PB, PS, EV/EBITDA multiples
   - Regression analysis if >5 peers

3. **Precedent transactions** (if available)
   - China M&A comparable multiples
   - Control premium analysis

4. **Sum-of-the-parts** (if multi-segment)
   - Segment-level DCF or multiples
   - Conglomerate discount assessment

**Valuation summary:**

| Method | Value (元/股) | Weight | Rationale |
|--------|--------------|--------|-----------|
| DCF | | | |
| PE comps | | | |
| PB comps | | | |
| EV/EBITDA comps | | | |
| SOTP | | | |
| **Implied target** | | | |

### Task 4: Chart Preparation

**Required charts:**

1. **Revenue & earnings history**
   - 5-year historical + 3-year projected
   - Bar chart: Revenue
   - Overlay: Net income, margins

2. **Valuation multiple history**
   - PE band (5-year)
   - PB band (5-year)
   - Current vs historical average

3. **Peer comparison**
   - Scatter: Growth vs Multiple
   - Bar: Key metrics vs peers

4. **Share price chart**
   - 2-year price history
   - Key events annotated

**Chart standards:**
- Dark theme or light theme (consistent with firm template)
- Chinese labels where appropriate
- Source: AkShare historical data
- Include A-share specific markers (涨跌停, 财报日期)

### Task 5: Report Assembly

**Standard A-share initiation report format:**

```
【XX证券】[公司名称]（[代码]）首次覆盖报告：[评级]

投资要点：
  - [3-5 bullet investment highlights]
  - 目标价：¥XX.XX (X% upside/downside)
  - 评级：买入/增持/中性/减持/卖出

一、投资逻辑
   [Core thesis, 2-3 paragraphs]

二、公司分析
   - 业务概述
   - 竞争优势
   - 管理团队
   - 股权结构

三、行业分析
   - 市场规模与增速
   - 竞争格局
   - 政策环境
   - 发展趋势

四、财务分析
   - 历史财务表现
   - 盈利驱动因素
   - 财务健康度
   - 关键假设

五、估值分析
   - 估值方法概述
   - DCF analysis
   - Comparable companies
   - Valuation summary
   - Target price derivation

六、风险提示
   - [Company-specific risks]
   - [Industry risks]
   - [Market risks]
   - [Policy risks]

附录：
   - 财务报表预测
   - 详细估值模型
   - 公司资料
```

**Report length:**
- Summary: 1 page
- Full report: 15-30 pages
- Financial model appendix: 10-15 pages

## China-Specific Considerations

### Rating Conventions (A-share)

| Rating | Chinese Equivalent | Implied Return |
|--------|-------------------|----------------|
| Buy | 买入 | >15% upside |
| Overweight / Accumulate | 增持 | 5-15% upside |
| Neutral / Hold | 中性 | -5% to +5% |
| Underweight / Reduce | 减持 | -5% to -15% |
| Sell | 卖出 | <-15% downside |

**Note:** Some firms use 5-point scale (买入/增持/中性/减持/卖出), others use 3-point (买入/增持/减持).

### Coverage Initiation Practices

**Pre-initiation checklist:**
- [ ] Company filings reviewed (年报, 招股说明书)
- [ ] Management meeting completed (if possible)
- [ ] Industry research thorough
- [ ] Peer comparison complete
- [ ] Financial model built and validated
- [ ] Valuation analysis complete
- [ ] Conflicts of interest disclosed

**Common initation triggers:**
- New IPO (新股)
- IPO quiet period expiry (typically 30-180 days)
- Market cap reaches coverage threshold
- New sector coverage mandate
- Material corporate action (M&A, restructuring)

### China-Specific Risks to Highlight

| Risk Category | Examples |
|--------------|---------|
| 政策风险 | Regulatory changes, industry policy shifts |
| 市场风险 | A-share volatility, retail sentiment |
| 流动性风险 | Low float, low turnover |
| 公司治理 | Related party transactions, pledge risk |
| 行业风险 | Overcapacity, demand cyclicality |
| 汇率风险 | For exporters/importers |
| 商誉减值 | Goodwill impairment risk |
| 质押风险 | Share pledge unwinding |

### Regulatory Compliance

**Chinese regulatory requirements for research:**
- 投资者适当性管理 (suitability)
- 利益冲突披露 (conflict of interest)
- 研究报告留痕 (research record retention)
- 静默期规定 (quiet period before IPOs)
- 预测免责声明 (disclaimer on estimates)

## Quality Checks

Before delivering:
- [ ] All financial data sourced from AkShare / 巨潮
- [ ] Financial model balanced and validated
- [ ] Valuation analysis comprehensive
- [ ] Peer comparison adequate (>3 peers)
- [ ] Rating and target price justified
- [ ] Risk factors comprehensive
- [ ] Report follows standard format
- [ ] All citations complete
- [ ] Compliance disclosures included
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
