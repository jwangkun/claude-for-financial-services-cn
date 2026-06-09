---
name: china-deal-sourcing
description: Discover and evaluate potential A-share investment opportunities for China-focused private equity and investment strategies. Adapted from the original deal-sourcing skill for Chinese market structure, data sources, and business practices. Triggers on "A股项目挖掘", "投资项目发现", "deal sourcing China", "find A-share deals", "sourcing opportunities China", or "discover investment targets".
---

# china-deal-sourcing

## Purpose

Identify and evaluate **A股及中国市场投资机会** — both listed and pre-IPO opportunities for China-focused investment strategies.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_market_overview()                     → Market movers
get_industry_stocks(industry="...")        → Industry peer lists
get_quote(ticker)                         → Valuation snapshot
get_financials(ticker, "income")          → Financial health check
```

### Secondary Sources

| Source | Use |
|--------|-----|
| 巨潮资讯 | Company filings, financials |
| 上交所/深交所 | Announcements, listing data |
| 企查查 / 天眼查 | Corporate structure, shareholders |
| 清科 / 投中数据 | Private equity deal flow |
| 券商直投 / 投行 | Deal pipeline |
| 行业展会/论坛 | Networking, deal sourcing |

## Workflow

### Step 1: Define Investment Criteria

**Strategy parameters:**

| Parameter | Options | Notes |
|-----------|---------|-------|
| Stage | Pre-IPO / Growth / Buyout / Distressed | 阶段 |
| Sector | 新能源, 半导体, 医药, 消费, etc. | 行业偏好 |
| Size | 市值区间 / 营收区间 | 投资规模 |
| Geography | 华东, 华南, 华北, etc. | 区域偏好 |
| Ownership | 国企 / 民企 / 混合 | 所有制偏好 |
| Growth | Revenue growth threshold | 成长性要求 |

### Step 2: Screen the Universe

**Screening approaches:**

**Approach 1: Market-based screen (A-share)**
```python
# Use AkShare to pull market data
get_market_overview()  # Top gainers/losers/volume
get_industry_stocks(industry="半导体")  # Sector peers
```

**Screen filters:**
- Market cap range
- Revenue growth threshold
- Margin profile
- Valuation multiples
- Trading liquidity
- Ownership structure

**Approach 2: Industry research**
- Identify growing sectors (行业景气度)
- Map value chain
- Find category leaders
- Identify consolidation opportunities

**Approach 3: Network sourcing**
- 产业资源 (Industry network)
- 券商/投行 deal flow
- 地方政府招商 (local government promotion)
- 行业协会 connections
- 创始人 network

### Step 3: Evaluate Targets

**Initial screening criteria:**

| Criterion | Threshold | Assessment |
|-----------|-----------|------------|
| Market size | >XX亿 TAM | Growing market |
| Company position | Top 5-10 in segment | Leadership potential |
| Revenue scale | >X亿 | Minimum viable |
| Growth rate | >XX% | Growth trajectory |
| Margin profile | Gross >XX%, Net >XX% | Profitability |
| Cash generation | Positive FCF | Sustainability |
| Management | Experienced, aligned | Execution capability |
| Competitive position | Moat / differentiation | Sustainability |

### Step 4: Assess Investment Thesis

**Thesis framework:**

1. **Why this company?**
   - Unique positioning
   - Competitive advantage
   - Growth runway

2. **Why now?**
   - Timing catalyst
   - Market inflection
   - Valuation entry point

3. **How to win?**
   - Value creation levers
   - Operational improvements
   - Financial engineering
   - Strategic additions

4. **What could go wrong?**
   - Key risks
   - Downside scenarios

### Step 5: Build Target Profile

**Profile template:**

```
【项目初筛】[Company]（[Ticker]）

一、基本信息
   行业：[Industry]
   板块：[Main / ChiNext / STAR / BJSE]
   市值：[XX亿]
   上市时间：[YYYY]

二、业务概览
   主营业务：[Description]
   收入结构：[Segments]
   核心客户：[Type / concentration]
   竞争优势：[Bullets]

三、财务快照
   Revenue: [X亿] (YoY: [X%])
   Gross Margin: [X%]
   Net Margin: [X%]
   ROE: [X%]
   Net Debt/EBITDA: [Xx]

四、估值快照
   Market Cap: [XX亿]
   PE (TTM): [Xx]
   PB: [Xx]
   vs Sector Median: [Premium/Discount X%]

五、投资逻辑
   [3-5 bullets]

六、初步风险
   [2-3 key risks]

七、下一步
   [Management meeting / DD / Pass]
```

### Step 6: Track & Nurture

**Deal tracking:**

| Target | Status | Owner | Next Action | Deadline |
|--------|--------|-------|-------------|----------|
| | Prospect → Intro → Active → DD → Closed | | | |

**Relationship management:**
- Founders / management contact cadence
- Industry event attendance
- 券商/FA relationship maintenance
- Local government / 招商关系

## China-Specific Sourcing Considerations

### Market Structure

| Segment | Description | Sourcing Approach |
|---------|-------------|-------------------|
| A股上市 | Already public | Secondary buyouts, 私有化 |
| Pre-IPO | Late-stage private | 券商直投, 产业基金 |
| 北交所 | SME innovation | Sector-specific funds |
| H股/A股 dual | HK + A-share | Premium capture |
| 并购退出 | M&A exit | Corporate buyers |

### Common Sourcing Channels

| Channel | Description | Quality |
|---------|-------------|---------|
| 券商投行部 | Investment banking deal flow | High quality, warm |
| FA (财务顾问) | Independent advisors | Medium-high quality |
| 产业网络 | Industry connections | High quality, relationship-based |
| 地方政府 | 招商引进 | Mixed quality, relationship-dependent |
| 展会/论坛 | Industry events | Medium quality, volume |
| 上市公司并购 | Public M&A | High quality, structured |

### Industry Hotspots (2024-2025)

| Sector | Dynamics | Sourcing Angle |
|--------|----------|----------------|
| 半导体 | 国产替代, 产能扩张 | Equipment, materials, design |
| 新能源 | 产能过剩, 出清 | distressed/bankruptcy opportunities |
| 医药 | 创新药, CXO | R&D-driven, global expansion |
| 高端制造 | 国产化, 出海 | Industrial automation, components |
| 消费 | 分化, 品牌化 | Premium brands, distribution |
| AI应用 | 落地加速 | Enterprise AI, industry solutions |

## Quality Checks

Before advancing target:
- [ ] Investment criteria alignment verified
- [ ] Market opportunity quantified
- [ ] Competitive position assessed
- [ ] Financial health checked
- [ ] Management quality evaluated
- [ ] Investment thesis articulated
- [ ] Risk factors identified
- [ ] Next steps defined
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
