---
name: china-buyer-list
description: Build a list of potential strategic and financial acquirers for A-share sell-side M&A mandates. Adapted from the original buyer-list skill for Chinese market acquirer universe. Triggers on "A股买方名单", "潜在收购方", "buyer list China", "strategic buyers China", "who would buy this A-share company", or "build buyer universe".
---

# china-buyer-list

## Purpose

Build **A股潜在收购方名单**, identifying both strategic and financial buyers for a sell-side M&A mandate.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_industry_stocks(industry="...")   → Industry peer list
get_quote(ticker)                    → Valuation for comparable analysis
get_financials(ticker, "income")     → Revenue for size comparison
```

### Secondary Sources
- 巨潮公告 — M&A history
- Wind / Choice — transaction database
- 券商研报 — sector M&A analysis
- 企查查 / 天眼查 — corporate structure, related entities

## Workflow

### Step 1: Define Target Profile

**Target characteristics:**
- Industry / sector
- Revenue size
- Geography
- Growth profile
- Ownership structure (listed / unlisted, controlling shareholder)

### Step 2: Build Strategic Buyer Universe

**Strategic buyer categories:**

| Category | Rationale | Examples |
|----------|-----------|---------|
| 同业龙头 (Industry peers) | Horizontal integration, market share | 白酒: 头部酒企 |
| 上下游整合 (Vertical integration) | Supply chain control | 车企 → 电池厂 |
| 多元化集团 (Conglomerates) | Diversification | 华润, 招商局 |
| 国企整合 (SOE consolidation) | Policy-driven consolidation | 央企/国企 |
| 民企扩张 (Private expansion) | Growth through M&A | 美的, 海尔 |

**For each potential strategic buyer:**
- Strategic rationale (why would they buy?)
- Fit assessment (complementarity, synergies)
- Financial capacity (cash, debt capacity)
- Historical M&A activity
- Regulatory approval likelihood

### Step 3: Build Financial Sponsor Universe

**Financial buyer categories:**

| Category | Description | Typical China Players |
|----------|-------------|----------------------|
| 私募股权 (PE) | Traditional buyout funds | 高瓴, 红杉, 鼎晖, 中信产业基金 |
| 产业基金 (Industry funds) | Sector-specific | 国家集成电路产业投资基金 |
| 并购基金 (Buyout funds) | A-share focused | 中金, 中信, 华泰联合 |
| 国资平台 (SOE investment arms) | Policy-driven | 地方国资, 国投 |

**Screening criteria:**
- Fund size vs deal size
- Sector focus alignment
- Track record in China
- Currency availability (RMB vs USD)
- Hold period preference
- Regulatory approval track record

### Step 4: Assess Buyer Fit

**Fit scoring matrix:**

| Buyer | Strategic Fit | Financial Capacity | Reg. Risk | Historical Activity | Overall Score |
|-------|---------------|-------------------|-----------|---------------------|---------------|
| | 1-5 | 1-5 | 1-5 | 1-5 | |

**Scoring criteria:**
- Strategic fit: How natural is the combination?
- Financial capacity: Can they afford it?
- Regulatory risk: Likelihood of approval?
- Historical activity: Do they acquire actively?

### Step 5: Prioritize Outreach

**Priority tiers:**

| Tier | Criteria | Approach |
|------|----------|----------|
| Tier 1 | High strategic fit, strong capacity, low reg risk | Direct outreach first |
| Tier 2 | Good fit, some hurdles | Secondary outreach |
| Tier 3 | Possible fit, significant challenges | Contingency / backup |

**Outreach considerations:**
- Relationship warmth (existing connections)
- Cultural/language compatibility
- Deal team familiarity with buyer
- Expected timeline

### Step 6: Document the List

**Standard buyer list format:**

```
【目标公司】潜在收购方名单

一、战略买方

1. [Buyer Name]
   属性：[国企/民企/外企]
   逻辑：[Why they would buy]
   历史并购：[Relevant deals]
   风险：[Regulatory / Integration risks]
   优先级：[Tier 1/2/3]

2. ...

二、财务买方

1. [Fund Name]
   类型：[PE/产业基金/并购基金]
   规模：[AUM]
   重点行业：[Sector focus]
   投资偏好：[Deet size, hold period]
   优先级：[Tier 1/2/3]

2. ...
```

## China-Specific Considerations

### Strategic Buyer Landscape

**Key strategic buyer types in China:**

| Type | Description | Typical Targets |
|------|-------------|-----------------|
| 央企集团 | Central SOE conglomerates | Large industrials, resources |
| 地方国企 | Provincial/municipal SOEs | Regional champions |
| 头部民企 | Leading private companies | Adjacent businesses |
| 互联网巨头 | Alibaba, Tencent, ByteDance | Tech, media, consumer |
| 金融机构 | Banks, insurers | Financial services |
| 地产集团 | Real estate developers | Diversification targets |

### Financial Sponsor Landscape

| Fund Type | Typical Size | Focus | Example Funds |
|-----------|-------------|-------|---------------|
| 美元基金 (USD funds) | Large | Growth, buyout | 高瓴, 红杉, Hillhouse |
| 人民币基金 (RMB funds) | Medium | Domestic focus | 中信产业基金, 鼎晖 |
| 产业基金 (Industry funds) | Large | National strategic | 大基金 (半导体) |
| 并购基金 (Buyout funds) | Medium | A-share M&A | 中金资本 |

### Regulatory Considerations

- **经营者集中申报**: SAMR review for deals above thresholds
- **外资安全审查**: Foreign investment review (if applicable)
- **国有股权转让**: 国有资产评估, 产权交易所挂牌
- **反垄断**: Market share thresholds
- **行业准入**: Sector-specific approvals

### Common Transaction Patterns

| Pattern | Description | Frequency |
|---------|-------------|-----------|
| 借壳上市 | Backdoor listing | Moderate |
| 吸并 | Merger of equals or absorption | Moderate |
| 协议转让 | Block trade / agreement transfer | Common for control |
| 要约收购 | General offer for remaining shares | Required for >30% |
| 定增 | Private placement | Common for acquisitions |

## Quality Checks

Before delivering:
- [ ] Buyer universe comprehensive (both strategic and financial)
- [ ] Each buyer assessed for fit
- [ ] Regulatory risks considered
- [ ] Prioritization logical
- [ ] Contact approach appropriate
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
