---
name: china-value-creation-plan
description: Post-close value creation plans for China-focused portfolio companies. Adapted from the original value-creation-plan skill for Chinese business context, management practices, and market dynamics. Triggers on "A股投后增值", "价值提升计划", "value creation plan China", "100-day plan China", "portfolio value creation", or "value creation [company]".
---

# china-value-creation-plan

## Purpose

Develop **A股投后价值提升计划** — structured value creation roadmaps for China-focused portfolio companies.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_quote(ticker)                        → Current valuation
get_financials(ticker, "income")         → Financial baseline
get_industry_stocks(industry="...")       → Peer benchmarks
```

### Secondary Sources
- 巨潮 — company filings
- 券商研报 — sector analysis
- Wind / Choice — operational data

## Workflow

### Step 1: Baseline Assessment

**Current state analysis:**

| Dimension | Current State | Gap to Best-in-Class |
|-----------|--------------|---------------------|
| Revenue growth | [X%] | [X%] |
| Gross margin | [X%] | [X%] |
| EBITDA margin | [X%] | [X%] |
| ROE | [X%] | [X%] |
| Working capital | [X days] | [X days] |
| Capex efficiency | [X% of rev] | [X% of rev] |

### Step 2: Identify Value Creation Levers

**Standard levers (adapted for China):**

| Lever | Description | Typical Impact | Timeline |
|-------|-------------|---------------|----------|
| 营收增长 | Organic growth acceleration | 20-50% revenue uplift | 12-36 months |
| 毛利率优化 | Pricing, mix, cost reduction | 300-800 bps | 6-18 months |
| 运营效率 | Working capital, OpEx | 100-300 bps margin | 6-18 months |
| 渠道拓展 | New channels, geographies | 15-30% revenue | 12-24 months |
| 并购整合 | Add-on acquisitions | 20-50% value | 12-36 months |
| 成本优化 | Headcount, procurement | 10-20% OpEx | 6-12 months |
| 数字化 | Digital transformation | 20-40% efficiency | 12-36 months |
| 品牌升级 | Premium positioning | 10-20% pricing | 12-24 months |
| 国际化 | Overseas expansion | New growth vector | 24-48 months |
| 资本运作 | Refinancing, restructuring | Cost savings | 6-12 months |

### Step 3: 100-Day Plan

**First 100 days post-close:**

| Week | Priority | Action | Expected Outcome |
|------|----------|--------|-----------------|
| 1-2 | Management alignment | Management calls, strategy session | Aligned priorities |
| 3-4 | Financial deep dive | Detailed financial analysis | Identified quick wins |
| 5-8 | Operational assessment | Site visits, process review | Improvement roadmap |
| 9-12 | Quick wins execution | Low-hanging fruit | Early wins, momentum |

**Quick wins (high impact, low effort):**
- Working capital optimization
- Non-core asset disposal
- Supplier renegotiation
- Pricing optimization
- Headcount rationalization

### Step 4: 3-Year Value Creation Roadmap

**Year 1: Foundation**

| Quarter | Focus | Key Initiatives |
|---------|-------|-----------------|
| Q1 | Stabilize | Management retention, quick wins |
| Q2 | Optimize | Cost reduction, working capital |
| Q3 | Grow | Revenue acceleration, new products |
| Q4 | Review | Progress check, plan adjustment |

**Year 2: Acceleration**

| Quarter | Focus | Key Initiatives |
|---------|-------|-----------------|
| Q1 | Scale | Channel expansion, capacity |
| Q2 | Innovate | R&D investment, new products |
| Q3 | Expand | Geographic / segment expansion |
| Q4 | Consolidate | M&A, integration |

**Year 3: Exit Preparation**

| Quarter | Focus | Key Initiatives |
|---------|-------|-----------------|
| Q1 | Optimize | Final push on margins |
| Q2 | Clean up | Balance sheet optimization |
| Q3 | Prepare | IPO / sale readiness |
| Q4 | Execute | Exit execution |

### Step 5: Financial Impact Model

**Value creation waterfall:**

| Value Driver | Impact (亿) | Probability |
|-------------|-------------|-------------|
| Revenue growth | +X | High/Med/Low |
| Margin expansion | +X | High/Med/Low |
| Multiple expansion | +X | High/Med/Low |
| De-leveraging | +X | High/Med/Low |
| **Total Value Creation** | **+X** | |

**EBITDA bridge:**

| Item | Year 0 | Year 1 | Year 2 | Year 3 |
|------|--------|--------|--------|--------|
| Baseline EBITDA | | | | |
| Revenue growth | | +X | +X | +X |
| Margin improvement | | +X | +X | +X |
| Cost savings | | +X | +X | +X |
| M&A | | +X | | |
| **Target EBITDA** | | | | |

### Step 6: Monitoring & Governance

**KPIs to track:**

| KPI | Frequency | Target |
|-----|-----------|--------|
| Revenue growth | Monthly | >XX% |
| EBITDA margin | Quarterly | >XX% |
| Customer acquisition | Monthly | <¥XX |
| Cash conversion | Quarterly | >XX% |
| Market share | Semi-annual | Top X |

**Governance structure:**
- Board seats (董事会席位)
- Monthly/quarterly reporting
- Management incentive alignment (管理层激励)
- Annual strategy review

## China-Specific Value Creation

### Management Alignment

| Tool | Application in China |
|------|---------------------|
| 管理层股权激励 (ESOP) | 期权, 限制性股票, 虚拟股 |
| 跟投机制 | Management co-investment |
| 对赌协议 (VAM) | Performance-based earnout |
| 董事会席位 | Board representation |
| 重大事项一票否决 | Veto rights on key decisions |

### Common Improvement Areas

| Area | Typical Challenge | Solution |
|------|------------------|----------|
| 财务管理 | Weak FP&A, cash management | Implement financial controls |
| 销售体系 | Chaotic channel management | Systematic channel strategy |
| 生产管理 | Low efficiency, high waste | Lean manufacturing |
| 数字化 | Legacy IT systems | ERP, CRM implementation |
| 人才管理 | Limited management depth | External hires, training |
| 公司治理 | Related party issues | Governance overhaul |

### China Market Considerations

| Factor | Value Creation Impact |
|--------|----------------------|
| 政策周期 | Align value creation with policy cycles |
| 市场规模 | TAM still large in many sectors |
| 竞争格局 | Consolidation opportunities |
| 数字化 | Leapfrog opportunities |
| 国际化 | Export potential for many sectors |

## Quality Checks

Before delivering:
- [ ] Baseline data current and accurate
- [ ] Value creation levers realistic
- [ ] Financial impact quantified
- [ ] Timeline achievable
- [ ] KPIs measurable
- [ ] Governance structure defined
- [ ] Risk factors addressed
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
