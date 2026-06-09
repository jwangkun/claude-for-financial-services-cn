---
name: china-competitive-analysis
description: Competitive landscape analysis for A-share companies and Chinese industries. Maps competitors, compares positioning, and assesses relative strengths. Adapted from the original competitive-analysis skill for Chinese market context. Triggers on "A股竞争格局", "行业竞争分析", "competitive landscape China", "competitive analysis A-share", or "[company] competitors China".
---

# china-competitive-analysis

## Purpose

Analyze **A股行业竞争格局**, mapping competitive dynamics for Chinese companies and industries.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_industry_stocks(industry="...")    → Full peer list
get_quote(ticker)                     → Valuation, market cap
get_financials(ticker, "income")      → Revenue, margins
get_financials(ticker, "balance")     → Assets, debt
get_stock_info(ticker)                → Business description
```

### Secondary Sources
- 巨潮年报 — detailed segment data
- 券商行业报告 — analyst competitive analysis
- Wind / Choice — market share data
- 行业协会 — industry statistics

## Workflow

### Step 1: Map the Competitive Set

**Industry definition:**
```python
# Get full industry composition
get_industry_stocks(industry="白酒")
```

**Tier the competitors:**

| Tier | Description | Examples |
|------|-------------|---------|
| Tier 1 (龙头) | Market leaders, >10% share | {{SECTOR_LEADER}} ({{EXAMPLE_SECTOR}}) |
| Tier 2 (挑战者) | Strong #2-5, growing share | {{CHALLENGER_1}}, {{CHALLENGER_2}} |
| Tier 3 (跟随者) | Niche players, regional | {{NICH_PLAYER}} |
| Tier 4 (边缘) | Declining or niche | {{LOW_END_PLAYER}} |

### Step 2: Competitive Comparison Matrix

**Core comparison table:**

| Company | Revenue (亿) | YoY | Gross Margin | Net Margin | ROE | Market Cap (亿) | PE (TTM) | Market Share |
|---------|-------------|-----|-------------|------------|-----|----------------|----------|-------------|
| | | | | | | | | |

**Expand with competitive dimensions:**

| Dimension | Leader | Challenger 1 | Challenger 2 | Follower |
|-----------|--------|-------------|-------------|---------|
| 品牌力 (Brand) | | | | |
| 渠道能力 (Distribution) | | | | |
| 产品力 (Product quality) | | | | |
| 成本优势 (Cost advantage) | | | | |
| 研发投入 (R&D) | | | | |
| 国际化 (International) | | | | |

### Step 3: Market Share Analysis

**Share trends:**

| Company | 2020 | 2021 | 2022 | 2023 | 2024E | Trend |
|---------|------|------|------|------|-------|-------|
| | | | | | | ↑ / → / ↓ |

**Concentration metrics:**
- CR3, CR5, CR10 (top 3/5/10 concentration)
- HHI (Herfindahl-Hirschman Index)
- Market share distribution

### Step 4: Competitive Positioning

**Positioning map:**

For 2x2 matrices, use:
- X-axis: Price (价格) or Scale (规模)
- Y-axis: Quality (品质) or Growth (增速)

Example for {{EXAMPLE_SECTOR}}:
```
         高端/品质
           |
   {{SECTOR_LEADER}}    |   {{CHALLENGER_1}}/{{CHALLENGER_2}}
           |
   {{NICH_PLAYER}} |   {{NATIONAL_BRAND}}
           |
           |________________
              低端/性价比    高端/溢价
```

### Step 5: Barriers to Entry

**China-specific barriers:**

| Barrier Type | Examples |
|-------------|---------|
| 品牌护城河 | Consumer brand loyalty, 品牌认知 |
| 渠道壁垒 | Distribution network, 经销商体系 |
| 规模效应 | Cost advantages from scale |
| 技术壁垒 | Patents, know-how, 技术积累 |
| 牌照/资质 | Regulatory licenses, 牌照 |
| 资金壁垒 | Capital requirements |
| 政策壁垒 | Industry access restrictions |
| 数据壁垒 | Data network effects |

### Step 6: Threat Assessment

**New entrants:**
- Likely sources (related industries, overseas)
- Barriers effectiveness

**Substitutes:**
- Alternative products/services
- Switching costs

**Supplier power:**
- Input concentration
- Price volatility (e.g., 原材料)

**Buyer power:**
- Customer concentration
- Switching costs

**Rivalry intensity:**
- Number and size of competitors
- Industry growth rate
- Differentiation level
- Exit barriers

### Step 7: Competitive Dynamics

**Historical evolution:**
- How has competitive landscape changed?
- What drove shifts (policy, technology, demand)?

**Current dynamics:**
- Price competition (价格战)
- Capacity expansion
- M&A activity
- New product launches

**Future outlook:**
- Likely consolidation?
- New entrants?
- Technology disruption?

## China-Specific Considerations

### Industry Structure

| Pattern | Description | Example Industries |
|---------|-------------|-------------------|
| 寡头垄断 | Few large players | 白酒 (top 5 >80%) |
| 分散竞争 | Fragmented, many players | 餐饮, 零售 |
| 区域割据 | Regional champions | 啤酒, 食品加工 |
| 龙头集中 | Consolidating toward leaders | 家电, 医药流通 |

### Competitive Behavior

- **价格战** (price wars) — common in commoditized sectors
- **渠道争夺** (channel competition) — 经销商, 线上平台
- **产能扩张** (capacity race) — leads to overcapacity
- **并购整合** (consolidation M&A) — industry rationalization
- **国际化** (going global) — emerging competitive frontier

### Government Role

- 产业政策 shapes competitive dynamics
- 国企 vs 民企 competitive dynamics
- 地方保护 (local protectionism) in some industries
- 反垄断 enforcement affects market structure

## Output Format

**Standard competitive analysis deliverable:**

```
【行业】竞争格局分析

一、行业概述
   市场规模, 增速, 发展阶段

二、竞争地图
   Tier划分, 市场份额

三、核心竞争要素
   各玩家优势对比

四、竞争动态
   价格, 渠道, 产能, 并购

五、壁垒分析
   进入壁垒, 现有壁垒有效性

六、趋势展望
   行业整合, 新进入者, 技术变革

七、结论与启示
   投资/战略含义
```

## Quality Checks

Before delivering:
- [ ] Competitive set complete and relevant
- [ ] Market share data sourced
- [ ] Comparison matrix comprehensive
- [ ] Barriers analyzed
- [ ] Competitive dynamics explained
- [ ] Forward outlook included
- [ ] Strategic implications drawn
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
