---
name: china-ai-readiness
description: Assess an A-share portfolio company's AI readiness for China-focused private equity investments. Evaluates data infrastructure, technology stack, talent, and AI adoption opportunities in the Chinese market context. Triggers on "A股公司AI评估", "AI readiness China", "AI assessment portfolio company", "AI转型评估", or "artificial intelligence readiness [company]".
---

# china-ai-readiness

## Purpose

Evaluate **A股被投企业AI就绪度** — assessing portfolio companies' preparedness for AI adoption and transformation in the Chinese market context.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_quote(ticker)                        → Company valuation context
get_financials(ticker, "income")         → Revenue scale, R&D spend
get_stock_info(ticker)                   → Business description
```

### Secondary Sources
- 巨潮 — company filings, R&D disclosure
- 券商研报 — technology assessments
- 行业报告 — AI adoption benchmarks

## Workflow

### Step 1: Assess Data Infrastructure

**Data readiness dimensions:**

| Dimension | Assessment | China Context |
|-----------|-----------|---------------|
| 数据积累 (Data accumulation) | Years of data, volume | Chinese companies often have rich transaction data |
| 数据质量 (Data quality) | Completeness, accuracy | Legacy systems may have gaps |
| 数据打通 (Data integration) | Siloed vs unified | Common challenge: ERP/WMS/CRM not integrated |
| 数据治理 (Data governance) | Policies, standards | Often underdeveloped |
| 数字化基础 (Digital foundation) | ERP, cloud adoption | Varies widely by industry/company age |

### Step 2: Evaluate Technology Stack

**Technology assessment:**

| Layer | Questions | Typical China Status |
|-------|-----------|---------------------|
| 基础设施 | Cloud? On-premise? | Mix of on-premise and hybrid |
| 数据平台 | Data warehouse? BI tools? | Often Excel-heavy |
| 应用系统 | ERP, CRM, WMS, MES? | ERP common (用友, 金蝶, SAP) |
| 开发能力 | Internal IT team? | Varies; often outsourced |
| 技术投入 | IT spend as % revenue? | Typically 1-3% |

### Step 3: Talent Assessment

**AI/tech talent:**

| Role | Availability in China | Typical Company Status |
|------|----------------------|----------------------|
| 数据科学家 | Scarce, expensive | Usually not in-house |
| 算法工程师 | Scarce | Outsourced or absent |
| 数据工程师 | Available | Often basic level |
| 业务分析师 | Available | Excel-based mostly |
| 数字化领导 | Rare | Gap at leadership level |

### Step 4: Business Process Readiness

**Process digitization level:**

| Process | Assessment | AI Potential |
|---------|-----------|-------------|
| 客户管理 | CRM adoption | Customer analytics, personalization |
| 供应链 | ERP, WMS | Demand forecasting, optimization |
| 生产制造 | MES, IoT | Predictive maintenance, quality |
| 财务管理 | ERP, Excel | Automated reporting, anomaly detection |
| 营销销售 | WeChat, 抖音 | Targeted marketing, conversion |
| 人力资源 | Basic HR system | Workforce analytics |

### Step 5: Identify AI Opportunities

**Opportunity mapping:**

| Business Function | AI Application | Expected Impact | Effort |
|------------------|---------------|-----------------|--------|
| 销售预测 | Demand forecasting | 10-20% accuracy improvement | Medium |
| 客户洞察 | Customer segmentation | 15-25% marketing ROI | Medium |
| 供应链优化 | Inventory optimization | 10-30% inventory reduction | High |
| 质量控制 | Defect detection | 30-50% defect reduction | High |
| 财务自动化 | Invoice processing | 50-80% time savings | Low |
| 客服 | Chatbot | 30-50% cost reduction | Medium |

### Step 6: Competitive Benchmarking

**Peer comparison:**

| Company | Digital Investment (% rev) | Key AI Initiatives | Maturity |
|---------|---------------------------|-------------------|----------|
| Target | [X%] | [Description] | Level 1-5 |
| Peer 1 | [X%] | [Description] | Level |
| Peer 2 | [X%] | [Description] | Level |
| Industry avg | [X%] | | Level |

### Step 7: Develop AI Roadmap

**Phased approach:**

**Phase 1: Foundation (0-6 months)**
- Data audit and cleanup
- Identify quick-win AI applications
- Hire/develop data team
- Cloud migration planning

**Phase 2: Pilot (6-18 months)**
- 1-2 AI pilots
- Data platform build-out
- Training and change management
- Measure and iterate

**Phase 3: Scale (18-36 months)**
- Expand AI across functions
- Advanced analytics capabilities
- AI-driven decision making
- Competitive advantage establishment

### Step 8: Investment Implications

**For PE investors:**

| Scenario | Implication |
|----------|-------------|
| High readiness | Accelerate with AI investment; value creation potential |
| Medium readiness | 1-2 year improvement path; build data foundation |
| Low readiness | Significant gap; may limit exit multiple expansion |
| No readiness | Strategic question: can this company compete long-term? |

**Value creation through AI:**
- Margin expansion (automation)
- Revenue growth (better targeting, personalization)
- Valuation multiple expansion (tech premium)
- Competitive positioning

## China-Specific AI Context

### China AI Landscape

| Layer | Key Players / Technologies |
|-------|---------------------------|
| Foundation models | 百度文心, 阿里通义, 讯飞星火, 智谱 |
| Computer vision | 商汤, 旷视, 依图 |
| NLP | 百度, 科大讯飞 |
| Industry AI | 海康, 大华 (vision), 格灵深瞳 |
| Cloud AI | 阿里云, 腾讯云, 华为云, 百度智能云 |

### China AI Adoption Patterns

| Industry | AI Readiness | Key Applications |
|----------|-------------|-------------------|
| 制造业 | Medium-High | Quality control, predictive maintenance |
| 零售 | Medium | Customer analytics, recommendation |
| 金融 | High | Risk scoring, fraud detection |
| 医疗 | Medium | Imaging, drug discovery |
| 物流 | Medium-High | Route optimization, warehouse |
| 农业 | Low-Medium | Precision agriculture |

### Data Considerations (China)

- **数据安全法** (Data Security Law) — data localization requirements
- **个人信息保护法** (PIPL) — personal data restrictions
- **数据跨境** — cross-border data transfer restrictions
- **政府数据** — access to government data sources

## Quality Checks

Before delivering:
- [ ] Data infrastructure assessed
- [ ] Technology stack documented
- [ ] Talent gap identified
- [ ] AI opportunities mapped
- [ ] Roadmap realistic and phased
- [ ] Investment implications clear
- [ ] China regulatory context included
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
