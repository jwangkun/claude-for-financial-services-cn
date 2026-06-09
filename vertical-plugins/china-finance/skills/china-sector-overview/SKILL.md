---
name: china-sector-overview
description: Comprehensive A-share sector and industry landscape reports — market size, competitive positioning, policy environment, key A-share players, trading multiples, and thematic trends. Adapted from the original sector-overview skill for Chinese market structure and terminology. Triggers on "A股行业分析", "行业研究", "板块分析", "sector overview China", "A-share sector deep dive", "白酒/半导体/新能源 行业分析", or "[industry] landscape China".
---

# china-sector-overview

## Purpose

Create comprehensive **A股行业/板块深度报告** covering market dynamics, competitive positioning, regulatory environment, key players, trading multiples, and thematic trends.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_industry_stocks(industry="白酒")     → 板块成分股
get_quote(ticker)                        → 个股行情、估值
get_financials(ticker, "income")         → 财务数据对比
get_index_data("000001")                 → 大盘基准
# News (china-news MCP — separate server)
get_stock_news(ticker="{{TICKER}}")          → 行业新闻
get_market_overview()                    → 涨幅榜/成交额榜
```

### Secondary Sources

| Source | Use |
|--------|-----|
| 东方财富行业板块 | Industry classification, sector indices |
| 巨潮资讯 | Company filings for competitive analysis |
| 国家统计局 / 海关总署 | Macro data (industry output, trade) |
| 行业协会 (中汽协, 硅业分会, etc.) | Sector-specific statistics |
| Wind / Choice / 同花顺 | Comprehensive sector data |
| 券商研报 | Analyst consensus and frameworks |

## Workflow

### Step 1: Define Scope & Angle

**Clarify:**
- Sector / industry focus (e.g., 白酒, 半导体, 新能源汽车)
- Angle (e.g., investment theme, competitive analysis, turnaround story)
- Geographic scope (A-share only, or include HK-listed / US-listed Chinese)
- Time horizon (cyclical analysis, secular trends, near-term trade)

### Step 2: Market Size & Structure

**Industry overview:**

| Metric | Data | Source |
|--------|------|--------|
| Total market size | 市场规模 (亿元/亿元) | 国家统计局, 行业协会 |
| Growth rate | 同比增速 / CAGR | Historical data |
| Market share | CR5, CR10 concentration | Company filings |
| Penetration rate | For new industries | Industry reports |
| Export/import | 进出口数据 | 海关总署 |

**A-share representation:**
- Number of listed companies in sector
- Total market cap (总市值 / 流通市值)
- Average PE / PB multiples
- Liquidity (average daily turnover)

### Step 3: Competitive Landscape

**Peer mapping:**

```python
# Get all stocks in an industry
get_industry_stocks(industry="白酒")
```

**For each major player, pull:**
```python
get_quote(ticker)           → Price, market cap, multiples
get_financials(ticker)      → Revenue, margins, growth
get_stock_info(ticker)      → Business description
```

**Competitive analysis table:**

| Company | Ticker | Market Cap (亿) | Revenue (亿) | YoY Growth | Gross Margin | Net Margin | PE (TTM) | Market Share |
|---------|--------|----------------|-------------|------------|-------------|------------|----------|-------------|
| | | | | | | | | |

**Competitive positioning:**
- Market share trends (gaining or losing)
- Product positioning (premium, mid-tier, mass market)
- Geographic footprint (national vs regional)
- Distribution strength (渠道能力)
- Brand equity (品牌力)

### Step 4: Trading Multiples & Valuation

**Sector multiples:**

| Metric | Current | 1Y High | 1Y Low | 5Y Average | Historical High | Historical Low |
|--------|---------|---------|--------|------------|----------------|----------------|
| Average PE | | | | | | |
| Average PB | | | | | | |
| Average PS | | | | | | |
| EV/EBITDA | | | | | | |

**Multiple dispersion:**
- Premium names (high multiple vs sector)
- Value names (low multiple vs sector)
- Historical range and where we are in cycle

### Step 5: Policy Environment

**China-specific policy analysis:**

| Policy Area | Current Status | Impact |
|-------------|---------------|--------|
| 产业政策 | 支持/限制/中性 | Direct sector impact |
| 环保政策 | 双碳目标 | Cost structure impact |
| 监管政策 | 集采/反垄断 | Margin / market share impact |
| 补贴政策 | 新能源/半导体补贴 | Competitiveness impact |
| 货币政策 | 宽松/中性/紧缩 | Financing cost impact |

**Key regulatory bodies:**
- 发改委 (NDRC) — industrial policy, pricing
- 工信部 (MIIT) — manufacturing, tech, telecom
- 生态环境部 (MEE) — environmental compliance
- 卫健委 (NHC) — healthcare, pharmaceuticals
- 证监会 (CSRC) — capital markets
- 央行 (PBoC) — monetary policy

### Step 6: Key Drivers & Trends

**Secular trends (3-5 year):**
- Technology adoption (技术替代)
- Consumption upgrade/downgrade (消费升级/降级)
- Demographic shifts (人口结构)
- Supply chain localization (供应链国产化)
- Environmental transition (双碳/ESG)

**Cyclical factors:**
- Inventory cycles (库存周期)
- Capacity utilization (产能利用率)
- Pricing trends (价格趋势)
- Demand momentum (需求 momentum)

### Step 7: Investment Themes

**Thematic angles:**

1. **Policy-driven**: 国产替代, 新基建, 乡村振兴
2. **Demand-driven**: 消费升级, 老龄化, 出海
3. **Supply-driven**: 产能出清, 行业整合, 龙头集中
4. **Technology-driven**: AI应用, 新能源, 生物医药创新

**For each theme:**
- Investment thesis
- Key names to express the theme
- Timeline and catalysts
- Risks and headwinds

### Step 8: Trading Ideas

**Ideas shortlist (from sector overview):**

| Idea | Ticker | Direction | Thesis | Catalyst | Risk |
|------|--------|-----------|--------|----------|------|
| | | Long / Short | | | |

### Step 9: Report Structure

**Standard A-share sector overview format:**

```
【XX证券】[行业] 深度报告：[标题]

一、行业概述
   市场规模、增速、发展阶段

二、竞争格局
   主要玩家、市场份额、竞争要素

三、政策环境
   监管框架、产业政策、影响分析

四、财务分析
   行业盈利能力、ROE、杠杆水平

五、估值分析
   当前 multiples vs 历史 vs 国际对标

六、核心驱动因素
   长期趋势、短期催化、周期位置

七、投资建议
   重点标的、目标价、评级

八、风险提示
   政策风险、需求风险、竞争风险
```

## China-Specific Considerations

### A-share Market Structure

| Feature | Description | Implication |
|---------|-------------|-------------|
| 涨跌停限制 | ±10% (main), ±20% (创业板/科创板) | Price discovery slower |
| 散户占比高 | Retail ~60-80% of turnover | More sentiment-driven |
| 政策驱动 | Government announcements move markets | Monitor policy closely |
| 板块轮动 | Sector rotation common | Timing important |
| 北向资金 | Foreign inflows tracked daily | Sentiment indicator |

### Industry Classification

**Common sector classifications:**
- 申万行业分类 (SW Industry) — most widely used
- 中信行业分类 (CITIC) — alternative
- 证监会行业分类 — regulatory standard
- 东方财富行业 — data vendor specific

**Use `get_industry_stocks(industry="...")` with Chinese industry names.**

### Sector-Specific Metrics

| Sector | Key Metrics |
|--------|-------------|
| 白酒 | 批价, 库存, 回款, 动销, 渠道库存 |
| 半导体 | 产能利用率, 出货量, ASP, 库存天数 |
| 新能源汽车 | 交付量, 单车收入, 电池成本, 渗透率 |
| 医药 | 创新药收入, 研发费用率, 集采中标 |
| 银行 | NIM, 不良率, 拨备覆盖率, ROE |
| 券商 | 经纪/投行/资管收入, 股基交易量, 两融余额 |
| 光伏 | 硅料/组件价格, 排产, 海外出货 |
| 房地产 | 销售额, 拿地, 融资成本, 去化周期 |
| 食品饮料 | 动销, 库存, 提价能力 |
| 互联网 | DAU/MAU, ARPU, 收入增速, 利润率 |

### Policy Risk Framework

**High policy-sensitivity sectors:**
1. 医药 — 集采 (volume-based procurement)
2. 互联网 — 反垄断, 数据安全
3. 教育 — 双减 (reduced private tutoring)
4. 金融 — 监管周期, 利率政策
5. 房地产 — 三道红线, 限购限贷
6. 新能源 — 补贴退坡, 产能过剩

**Policy risk assessment:**
- Current policy stance (支持/中性/限制)
- Upcoming regulatory events
- Historical policy impact patterns
- Best/worst case scenarios

## Quality Checks

Before delivering:
- [ ] Industry definition clear and consistent
- [ ] Market size data sourced (统计局 or industry association)
- [ ] Competitive landscape covers top 5-10 players
- [ ] Financials sourced from iFind / AkShare / 巨潮
- [ ] Valuation multiples calculated consistently
- [ ] Policy environment analyzed
- [ ] Investment themes articulated
- [ ] Ideas shortlist included (3-5 names)
- [ ] Risk factors specific to China market included
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
