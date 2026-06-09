---
name: china-earnings-preview
description: Pre-earnings analysis for A-share stocks. Builds scenario frameworks (actual vs consensus, beat/miss cases), identifies key metrics to watch, and prepares positioning notes before Chinese companies report quarterly results. Use instead of the original earnings-preview skill for A-share coverage. Triggers on "A股财报前瞻", "季报前瞻", "业绩前瞻", "earnings preview", "what to watch for [company] earnings", or "pre-earnings setup".
---

# china-earnings-preview

## Purpose

Build **A股季报/年报前瞻分析**, preparing for company earnings releases with scenario frameworks and key metrics to watch.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_quote(ticker)                        → Current valuation, PE/PB
get_historical_data(ticker)              → Trading context, 52-wk range
get_financials(ticker, "income", "annual")  → Historical revenue/EPS trends
# News (china-news MCP — separate server)
get_stock_news(ticker="{{TICKER}}")          → Pre-earnings context
get_industry_stocks(industry="...")      → Peer trading multiples
```

### Consensus Estimates Sources

| Source | Access | Notes |
|--------|--------|-------|
| Wind 一致预期 | Institutional | Most comprehensive |
| Choice 一致预期 | Institutional | Alternative |
| 慧博投研 | Web / API | Good coverage |
| 同花顺 iFinD | Web / API | Retail-friendly UI |
| 东方财富 | Web | Free, some coverage |
| 巨潮 业绩预告 | Regulatory | Mandatory disclosures |

**If consensus unavailable**, derive from:
- Historical growth rates
- Management guidance from prior calls
- Industry benchmarks

### Secondary Sources
- 公司公告 (earnings preview notices 业绩预告)
- 行业研究报告 (sector reports)
- 卖方研报 (broker research summaries)

## Workflow

### Step 1: Establish Baseline

**Historical performance (last 4-8 quarters):**

| Quarter | Revenue (亿) | YoY | Net Income (亿) | YoY | EPS (元) | Net Margin |
|---------|-------------|-----|----------------|-----|----------|------------|
| Q1 2024 | | | | | | |
| Q2 2024 | | | | | | |
| Q3 2024 | | | | | | |
| Q4 2023 | | | | | | |

**Identify trends:**
- Accelerating or decelerating growth?
- Margin expansion or compression?
- Seasonal patterns?
- One-time items to normalize?

### Step 2: Gather Consensus Estimates

**Consensus table:**

| Metric | Q1 2024 Estimate | Range (Low-High) | # Analysts |
|--------|-----------------|-------------------|------------|
| Revenue (亿) | | | |
| YoY Growth | | | |
| Net Income (亿) | | | |
| EPS (元) | | | |
| Gross Margin | | | |
| Net Margin | | | |

**Beat probability assessment:**
- Strong beat (>+10%): Company has history of under-promising
- Moderate beat (+5% to +10%): Consensus well-established
- In-line (-5% to +5%): Typical range
- Miss risk (<-5%): Macro headwinds, order delays

### Step 3: Identify Key Metrics to Watch

**Company-specific KPIs:**

For each company, identify 3-5 metrics that will drive the report:

| Metric | Why It Matters | Watch Threshold | Risk if Missed |
|--------|---------------|-----------------|----------------|
| e.g., 白酒批价 | Price indicator for channel health | >950元/瓶 | Demand softness |
| e.g., 动力电池装机量 | Volume indicator | >XX GWh | Market share loss |
| e.g., 云业务收入增速 | Growth engine health | >30% | Cloud slowdown |

**Sector-wide KPIs (for sector previews):**

| Sector | Key Metrics |
|--------|-------------|
| 白酒 | 批价、库存、回款、动销 |
| 半导体 | 产能利用率、出货量、ASP、库存天数 |
| 新能源汽车 | 交付量、单车收入、毛利率、电池成本 |
| 医药 | 创新药收入、研发费用、集采影响 |
| 银行 | NIM、不良率、拨备覆盖率 |
| 券商 | 经纪/投行/资管收入、股基交易量 |
| 光伏 | 硅料/组件价格、排产、海外出货 |
| 房地产 | 销售额、拿地、融资成本 |

### Step 4: Build Scenario Framework

**Three-scenario model:**

```
BEAR CASE (超预期悲观)
  Revenue: -X% vs consensus
  Net Income: -Y% vs consensus
  Key factor: [specific risk]
  Likely catalysts: 业绩预告大幅下调, 行业负面政策

BASE CASE (符合预期)
  Revenue: ±Z% vs consensus
  Net Income: ±W% vs consensus
  Key factor: [steady state]
  Likely outcome: 符合预期, 股价波动±5%

BULL CASE (超预期乐观)
  Revenue: +A% vs consensus
  Net Income: +B% vs consensus
  Key factor: [positive surprise driver]
  Likely catalysts: 新品放量, 成本下降超预期
```

### Step 5: Position Analysis

**What does the market expect?**

- Recent stock price performance into earnings
- Implied move from options (if A-share options available)
- Sentiment from 北向资金 trends
- Broker recommendations distribution

**Position sizing considerations:**
- High expectations (high PE) → asymmetric risk to downside
- Low expectations (depressed stock) → upside potential on beat
- Earnings as catalyst: upcoming product launch, policy change

### Step 6: Pre-Earnings Positioning Note

**Standard structure:**

```
[公司名称]（[代码]）[季/年报] 前瞻：[主题/焦点]

一、业绩预期
  - 关键指标一致预期一览
  - 预测区间

二、情景分析
  - 乐观/基准/悲观情景

三、关注要点
  - 最重要的 3-5 个指标
  - 预期 vs 实际的关键差异点

四、估值与预期
  - 当前估值水平
  - 市场情绪指标
  - 北向资金动向

五、情景判断与策略
  - 不同情景下的股价反应
  - 可能的交易策略

六、风险提示
  - 关键下行风险
```

### Step 7: Post-Earnings Follow-up

After actual results are released:
- Compare actual vs preview scenarios
- Update the earnings-analysis model
- Revise forward estimates
- Note any material guidance changes

## China-Specific Pre-Earnings Considerations

### Earnings Calendar (A-share)

| Report Type | Deadline | Typical Release Time |
|-------------|----------|----------------------|
| Q1 / Q3季报 | 1 month after quarter-end | Before market open or after close |
| Semi-annual report (中报) | 2 months after H1 | Before market open |
| Annual report (年报) | 4 months after year-end | Typically Jan-Apr |

**Release pattern:**
- Most companies release before market open (8:00-9:00 AM)
- Some release after market close (after 15:00)
- 创业板/科创板 may have more flexible schedules

### 业绩预告 (Earnings Preview Notice)

- Mandatory if actual vs prior period variance >50%
- Published typically 2-4 weeks before formal report
- Format: 预增 (increase), 预减 (decrease), 扭亏 (turn to profit), 首亏 (first loss), 续亏 (continued loss)
- Provides directional guidance before formal report

### Consensus Reliability

**Caveats for Chinese consensus:**
- Fewer analysts covering A-shares vs US large caps
- Estimates may be stale (update frequency lower)
- Institutional vs retail analyst coverage varies significantly
- Broker research sometimes biased ( conflicted interests )
- Cross-reference multiple sources when possible

### Policy Risk

- Regulatory changes can materially impact earnings overnight
- 行业政策 (industry policy) shifts common in:
  - 医药 (pharmaceuticals — 集采)
  - 教育 (education — 双减)
  - 互联网 (internet — antitrust)
  - 新能源 (renewables — subsidy changes)
- Factor policy risk into scenario analysis

## Quality Checks

Before delivering preview:

- [ ] Historical data complete and accurate (AkSource verified)
- [ ] Consensus estimates sourced (or clearly noted as unavailable)
- [ ] Scenario framework covers bull/base/bear
- [ ] Key watch items identified with rationale
- [ ] China-specific risks flagged (政策, 集采, etc.)
- [ ] Valuation context included
- [ ] Pre-earnings positioning actionable
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
