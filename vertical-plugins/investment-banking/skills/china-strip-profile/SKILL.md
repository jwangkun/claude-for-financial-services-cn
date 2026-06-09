---
name: china-strip-profile
description: Create one-page company profile slides (strip profiles) for A-share targets in pitch books and deal materials. Adapted from the original strip-profile skill for Chinese companies, A-share market data, and Chinese business terminology. Triggers on "A股公司简介", "公司概况", "strip profile China", "one-pager A-share", or "target profile for [company]".
---

# china-strip-profile

## Purpose

Create professional **A股目标公司简介/Strip Profile** slides for pitch books and deal materials.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_stock_info(ticker)                     → Company profile
get_quote(ticker)                         → Current valuation
get_historical_data(ticker)               → Stock performance
get_financials(ticker, "income", "annual")  → Revenue, profit
get_financials(ticker, "balance", "annual") → Assets, debt
get_industry_stocks(industry="...")        → Peer context
get_stock_news(ticker)                    → Recent news
```

### Secondary Sources

- **巨潮资讯** — annual reports, prospectus (招股说明书)
- **企查查 / 天眼查** — corporate structure, subsidiaries
- **公司官网** — investor relations materials
- **券商研报** — existing research (if covered)

## Workflow

### Step 1: Gather Target Information

**Company basics:**
- 公司全称 (Full name)
- 股票代码 (Ticker)
- 上市板块 (Listing board: 主板/创业板/科创板/北交所)
- 上市日期 (Listing date)
- 行业分类 (Industry classification)
- 总部地址 (Headquarters)
- 员工人数 (Employee count)

**Business description:**
- 主营业务 (Core business)
- 产品/服务 (Products/services)
- 商业模式 (Business model)
- 客户结构 (Customer base)
- 地域分布 (Geographic footprint)

**Financial snapshot (most recent):**

| Metric | FY2023 | FY2022 | YoY |
|--------|--------|--------|-----|
| Revenue (亿) | | | |
| Net Income (亿) | | | |
| Gross Margin | | | |
| Net Margin | | | |
| ROE | | | |
| Net Debt/EBITDA | | | |

**Market data:**
- Current price (latest close)
- Market cap (总市值 / 流通市值)
- 52-week high/low
- YTD performance
- Average daily turnover

### Step 2: Identify Key Investment Highlights

**Highlight categories:**

1. **Market leadership** (市场地位)
   - Market share rank
   - Competitive advantages
   - Barriers to entry

2. **Financial profile** (财务特征)
   - Revenue scale and growth
   - Margin profile
   - Cash generation
   - Balance sheet strength

3. **Growth drivers** (成长动力)
   - New products / expansion
   - Market opportunities
   - Capacity additions

4. **Valuation context** (估值位置)
   - Current multiples vs history
   - vs peers
   - Upside/downside

### Step 3: Build Slide Content

**Standard strip profile layout (1 slide, typically):**

**Left panel — Company snapshot:**
```
[公司LOGO/名称] [股票代码]
[行业] | [上市板块] | [上市日期]

公司简介：
[2-3 sentences on business model]

核心财务 (最近财年):
  营业收入: XX亿 (YoY: +XX%)
  净利润: XX亿 (YoY: +XX%)
  毛利率: XX%
  净利率: XX%
  ROE: XX%
  有息负债: XX亿
```

**Right panel — Key metrics / highlights:**
```
[3-5 bullet investment highlights]
- 市场地位: ...
- 成长动力: ...
- 竞争优势: ...
- 估值水平: ...
```

**Bottom — Charts:**
- Revenue / profit history (3-5 years)
- PE band or comparable multiples
- Share price performance

### Step 4: Visual Design

**Design guidelines:**
- Clean, professional layout
- Consistent with firm's pitch deck template
- Key numbers prominently displayed
- Charts simple and readable
- Chinese labels appropriate for audience

**Color scheme (default if no template):**
- Section headers: Dark blue `#1F4E79` with white text
- Data cells: Light grey `#F2F2F2` or white
- Accent: Company brand colors (research via web search)
- Text: Black / dark grey

### Step 5: Quality Check

**Before finalizing:**
- [ ] All financials sourced from 巨潮 or AkShare
- [ ] Market data current
- [ ] Key highlights compelling and factual
- [ ] Charts readable and properly labeled
- [ ] Brand colors correct (researched, not assumed)
- [ ] Formatting consistent with deck template

## China-Specific Considerations

### Listing Boards

| Board | Requirements | Characteristics |
|-------|-------------|-----------------|
| 主板 (Main Board) | Profitable, established | Large-caps, mature companies |
| 创业板 (ChiNext) | Growth, innovation | Tech, healthcare, growth |
| 科创板 (STAR Market) | Hard tech, R&D | Semiconductors, biotech, advanced mfg |
| 北交所 (BJSE) | SMEs, innovative | Smaller, earlier-stage companies |

### A-share Specifics

- 涨跌停 limits affect trading profile
- 北向资金 ownership tracked for large-caps
- 股东户数 changes (from quarterly reports)
- 限售股比例 (restricted shares) affects float
- 质押比例 (share pledge ratio) — flag if >30%

### Industry-Specific Metrics

| Industry | Key Metrics to Highlight |
|----------|-------------------------|
| 白酒 | 批价, 渠道库存, 动销增速 |
| 半导体 | 产能利用率, 技术节点, 客户认证 |
| 新能源 | 产能, 出货量, 技术路线 |
| 医药 | 管线, 研发投入, 集采中标 |
| 银行 | NIM, 不良率, 拨备覆盖率 |
| 互联网 | DAU/MAU, ARPU, 变现效率 |
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
