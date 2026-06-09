---
name: china-morning-note
description: Daily morning research note for A-share markets. Summarizes overnight developments, pre-market sentiment, trade ideas, and key events for the trading day. Adapted from the original morning-note skill for Chinese market conventions. Triggers on "早报", "晨会纪要", "今日策略", "morning note", "morning meeting", or "daily A-share preview".
---

# china-morning-note

## Purpose

Draft concise **A股晨会纪要/每日策略**, summarizing overnight developments and pre-market sentiment for the Chinese equity market. Designed for the typical Chinese sell-side 晨会 format (typically 7:00-8:30 AM before market open).

## Data Sources (Multi-Tier)

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 - Tonghuashun iFind (paid)
```python
ifind_search_news(query)       -> Real-time financial news
ifind_search_trending_news()   -> Trending events
ifind_index_data(query)        -> Index data
ifind_sector_data(query)       -> Sector data
```

### Tier 2 - AkShare / Other (free, fallback)

> Data source mode: `IFIND_DATA_SOURCE_MODE=ifind-only` for iFind-only mode.

## Data Sources (Legacy)

### Market Data

```python
get_market_overview()          → Top gainers, losers, most active
get_index_data("000001")       → 上证指数
get_index_data("399001")       → 深证成指
get_index_data("399006")       → 创业板指
get_index_data("000688")       → 科创50
get_stock_news(ticker="")      → Market headlines
```

### News & Sentiment

| Source | Coverage |
|--------|----------|
| china-news MCP | Stock-specific and market headlines from 东方财富 |
| 财联社 | Real-time financial news |
| 华尔街见闻 | Macro and market news |
| 证券时报 | Regulatory and market news |
| 中国新闻网 / 新华社 | Policy announcements |

### Macro Data (if relevant)

| Data | Source | Frequency |
|------|--------|-----------|
| PMI (制造业/非制造业) | 国家统计局 | Monthly |
| CPI / PPI | 国家统计局 | Monthly |
| Social financing / M2 | 央行 | Monthly |
| FX rate (USD/CNY) | 中国外汇交易中心 | Daily |
| Bond yields (10Y CGB) | 中国债券信息网 | Daily |
| 北向资金 | 沪深港通 | Daily |
| Southbound 南向资金 | 沪深港通 | Daily |

## Workflow

### Step 1: Overnight Developments

**Macro / Policy:**
- 央行 (PBoC) announcements — MLF/LPR rates, RRR cuts, open market operations
- 国务院 / 部委政策 — industry regulations, 产业政策
- 美联储 (Fed) developments — impact on A-share opening
- 外围市场 (overnight markets) — US equities, commodities, FX

**Company news:**
- Earnings releases from prior evening / overnight
- 业绩预告 (earnings preview notices)
- 增减持 (shareholder buy/sell announcements)
- 重大合同 (major contract wins)
- 回购 (share buybacks)

**Format:**
```
【宏观/政策】
- [News item with brief implication]
- [News item with brief implication]

【公司要闻】
- [Company]: [Event] — [Implication]
- [Company]: [Event] — [Implication]
```

### Step 2: Market Preview

**Previous session recap:**
- 上证指数: close, change, volume
- 深证成指: close, change
- 创业板指: close, change, 涨跌家数
- Sector performance: top 3 up/down sectors
- 北向资金: net buy/sell amount, direction

**Overnight markets:**
- 美股三大指数 (Dow, Nasdaq, 中证500) — impact on A-share opening
- Hang Seng Index (港股)
- Commodities: 原油, 铜, 黄金
- USD/CNY: exchange rate movement

### Step 3: Trade Ideas

**2-4 actionable ideas for the day:**

For each idea:
- **方向**: Long / Short / Watch
- **标的**: Company name + ticker
- **逻辑**: Brief thesis (1-2 sentences)
- **催化剂**: Key event to watch
- **风险**: Main risk factor

**Example format:**
```
【今日策略】
1. [方向] [标的]（[代码]）
   逻辑：[简要投资逻辑]
   催化剂：[近期催化剂]
   风险：[主要风险]

2. ...
```

### Step 4: Key Events Calendar

**Today's events:**
- Earnings releases (A-share companies reporting)
- Economic data releases (CPI, PMI, etc.)
- Policy events (PBoC MLF operations, 国新办发布会)
- Earnings calls (业绩说明会)
- Sector conferences / 策略会

### Step 5: Sector / Thematic Focus

**Sector of the day:**
- What's moving?
- Key drivers (policy, data, sentiment)
- Names to watch within sector

### Step 6: Draft the Note

**Standard A-share morning note format:**

```
【XX证券】A股晨会纪要 [YYYY-MM-DD]

一、市场回顾
   [Yesterday's close, sector performance, 北向资金]

二、隔夜外盘与大宗
   [Overnight US/Asia markets, commodities, FX]

三、重要资讯
   【宏观政策】...
   【公司要闻】...
   【行业动态】...

四、今日策略
   [Trade ideas with rationale]

五、重点事件日历
   [Today's scheduled events]

六、风险提示
   [Market-wide risks]
```

### Step 7: Delivery

**Tone guidelines:**
- Concise and actionable
- Opinionated but evidence-based
- Flag high-conviction ideas vs. lower-conviction
- Include risk management notes (止损位, 仓位建议)

**Typical length:**
- 300-600 words for daily note
- 800-1,500 words for weekly strategy piece

## China-Specific Morning Context

### Market Mechanics

| Item | A-share Convention |
|------|-------------------|
| Pre-market | No formal pre-market; some dark pools |
| Opening | 9:30 AM (集合竞价 9:15-9:25) |
| Closing | 3:00 PM (集合竞价 14:57-15:00) |
| Lunch break | 11:30 AM - 1:00 PM |
| Trading limits | ±10% (main), ±20% (创业板/科创板), ±30% (ST) |

### Common A-share Themes

- **政策市** (policy-driven market) — government announcements move markets
- **存量博弈** (capital rotation) — limited new money, sector rotation
- **北向资金** (Northbound flows) — tracked as sentiment indicator
- **两融余额** (margin balances) — leverage indicator
- **龙虎榜** (Dragon-Tiger list) — unusual activity names
- **涨跌停** — limit-up/limit-down stocks (market momentum)

### Common Catalysts in A-share

- 央行公开市场操作 (PBoC open market operations)
- LPR报价 (Loan Prime Rate announcements)
- PMI数据 (monthly PMI releases)
- 季报/年报窗口 (earnings season: Apr, Aug, Oct)
- 重要会议 (重要会议: 政治局会议, 中央经济工作会议)
- 行业监管政策 (sector regulation: 集采, 反垄断, etc.)
- 外资流入 (foreign inflow via 沪深港通)

## Quality Checks

Before delivering:
- [ ] Market data current and accurate
- [ ] Overnight developments captured
- [ ] Trade ideas actionable and time-relevant
- [ ] Event calendar complete
- [ ] Risk factors included
- [ ] Tone appropriate for morning meeting format
