---
name: china-cim-builder
description: Structure and draft Confidential Information Memorandums (CIMs) for A-share sell-side M&A processes. Organizes company information into professional, investor-ready documents with Chinese market context. Triggers on "A股CIM", "保密信息备忘录", "CIM China", "confidential memorandum A-share", or "offering memorandum [company]".
---

# china-cim-builder

## Purpose

Draft **A股并购CIM (Confidential Information Memorandum)** for sell-side M&A processes — comprehensive, confidential company overviews for potential buyers.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_stock_info(ticker)                        → Company profile
get_quote(ticker)                            → Valuation snapshot
get_historical_data(ticker)                  → Trading history
get_financials(ticker, "income", "annual")    → Historical P&L
get_financials(ticker, "balance", "annual")   → Historical BS
get_financials(ticker, "cashflow", "annual")  → Historical CF
get_industry_stocks(industry="...")            → Industry peers
```

### Secondary Sources
- **巨潮** — full annual reports, announcements
- **公司官网** — IR materials, presentations
- **券商研报** — existing research
- **企查查 / 天眼查** — corporate structure, subsidiaries

## Workflow

### Step 1: Define CIM Scope

**CIM types:**

| Type | Use | Typical Length |
|------|-----|---------------|
| Full CIM | Comprehensive sell-side | 50-100 pages |
| Summary CIM | Initial teaser + overview | 15-25 pages |
| Teaser | Anonymous preview | 1-2 pages |
| Management presentation | Buyer meeting | 20-40 slides |

### Step 2: Standard CIM Structure

**A-share CIM sections:**

```
一、交易概述 (Transaction Overview)
   - 交易背景
   - 交易结构
   - 时间表

二、公司概览 (Company Overview)
   - 公司简介
   - 发展历程
   - 业务模式
   - 组织结构
   - 管理层介绍

三、行业分析 (Industry Analysis)
   - 市场规模
   - 发展趋势
   - 竞争格局
   - 政策环境

四、经营分析 (Operating Analysis)
   - 业务拆分
   - 核心竞争优势
   - 客户结构
   - 渠道网络
   - 供应链

五、财务分析 (Financial Analysis)
   - 历史财务表现
   - 财务比率分析
   - 盈利质量
   - 现金流分析

六、估值分析 (Valuation Analysis)
   - 交易比较 (可比交易)
   - 交易倍数 (Trading comps)
   - DCF估值
   - 估值区间

七、风险因素 (Risk Factors)
   - 行业风险
   - 公司风险
   - 市场风险
   - 政策风险

八、附录 (Appendices)
   - 详细财务报表
   - 管理层简历
   - 术语表
```

### Step 3: Gather Content

**For each section:**

1. **Company overview**: From 巨潮 annual report + AkShare
2. **Financials**: From AkShare / 巨潮 (3-5 years)
3. **Industry**: From research reports, industry data
4. **Competitive position**: Peer comparison via AkShare
5. **Management**: From 年报 / 公司官网
6. **Valuation**: Built from comps + DCF

### Step 4: Write the CIM

**Writing guidelines:**
- Professional, neutral tone
- Factual, avoid superlatives
- Balanced presentation (include risks)
- Chinese business English appropriate for cross-border
- Chinese terminology where buyers expect it

**Key sections detail:**

#### Company Overview
- History and evolution
- Current structure (corporate org chart)
- Core business lines with revenue contribution
- Geographic footprint
- Key milestones

#### Industry Analysis
- Market size and growth trajectory
- Supply/demand dynamics
- Regulatory framework
- Technology trends
- Entry barriers

#### Financial Analysis
- 5-year historical summary
- Key ratio trends
- Revenue bridge (growth decomposition)
- Margin analysis
- Balance sheet quality
- Cash flow profile

#### Valuation
- Comparable transactions (precedent deals)
- Trading comparables
- DCF summary
- Valuation range and rationale

### Step 5: Quality Standards

**CIM quality checklist:**

| Section | Requirement |
|---------|-------------|
| Confidentiality | Prominent watermark and notice |
| Executive summary | Compelling, concise (1-2 pages) |
| Financials | Complete, consistent, sourced |
| Industry | Contextual, data-backed |
| Risks | Comprehensive, not minimized |
| Formatting | Professional, consistent |
| Graphics | Charts, tables, org charts |

## China-Specific Considerations

### Regulatory Disclosures

**Mandatory disclosure content:**
- 关联交易 (related party transactions) — flag prominently
- 对外担保 (guarantees to third parties)
- 重大诉讼仲裁 (material litigation)
- 股权质押 (share pledges)
- 同业竞争 (competitive businesses of related parties)

### Ownership Structure

**Common in China CIMs:**
- 股权结构图 (ownership structure diagram)
- 实际控制人 (actual controller identification)
- 一致行动人 (concert party arrangements)
- 股权激励 (ESOP/scheme details)
- 限售股 (restricted shares, lock-up schedule)

### Industry-Specific Content

| Industry | Special CIM Sections |
|----------|---------------------|
| 白酒 | 批价历史, 渠道库存, 品牌矩阵 |
| 半导体 | 产能规划, 技术路线, 客户认证 |
| 新能源 | 技术迭代, 产能规划, 补贴依赖 |
| 医药 | 管线组合, 临床数据, 集采风险 |
| 房地产 | 土储质量, 去化率, 融资结构 |

### Valuation Context

**A-share premium context:**
- A-share companies often trade at premium to H-shares
- Liquidity premium for listed targets
- Control premium expectations (20-40%)
- 私有化 premium requirements (30-50%)

## Quality Checks

Before finalizing:
- [ ] Confidentiality notices prominent
- [ ] All financial data sourced
- [ ] Industry context complete
- [ ] Risk factors comprehensive
- [ ] Valuation analysis sound
- [ ] Regulatory items flagged
- [ ] Formatting professional
- [ ] No identifying information leaked (if teaser phase)
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
