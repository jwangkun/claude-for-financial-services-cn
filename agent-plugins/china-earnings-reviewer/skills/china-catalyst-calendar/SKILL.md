---
name: china-catalyst-calendar
description: Track upcoming catalysts for A-share coverage universe — earnings dates, regulatory announcements, sector conferences, product launches, and policy events relevant to Chinese equities. Adapted from the original catalyst-calendar skill for A-share market conventions. Triggers on "A股催化剂日历", "事件日历", "财报日历", "earnings calendar A-share", "upcoming catalysts China", or "what's coming up for [company]".
---

# china-catalyst-calendar

## Purpose

Build and maintain a **A股催化剂日历** tracking upcoming events that could materially impact stock prices within a coverage universe.

## Catalyst Types (A-share Specific)

### 1. Earnings & Financial Reports

| Event | Typical Timing | Notes |
|-------|---------------|-------|
| 业绩预告 (earnings preview) | 1-4 weeks before | Mandatory if variance >50% from prior |
| 季报 (quarterly report) | 1 month after quarter-end | 10-day grace period possible |
| 中报 (semi-annual report) | 2 months after H1 | 15-day grace period |
| 年报 (annual report) | 4 months after year-end | Most important event of the year |
| 业绩说明会 (earnings call) | Same day or next trading day | 上证e互动 / 深交所互动易 |

### 2. Regulatory & Policy Events

| Event | Impact | Typical Timing |
|-------|--------|---------------|
| 央行MLF/LPR操作 | High (liquidity, rates) | 15th of each month (MLF) |
| 央行降准/降息 | Very high | Ad-hoc, 国新办发布会 |
| 国务院政策发布 | Sector-specific | Ad-hoc |
| 部委监管政策 (NMPA, MIIT, etc.) | Industry-specific | Ad-hoc |
| 集采结果 (volume-based procurement) | Pharma/medtech | Quarterly cycles |
| 行业准入政策变化 | Sector-specific | Ad-hoc |
| 反垄断调查 | Specific companies | Ad-hoc |

### 3. Corporate Events

| Event | Impact | Notes |
|-------|--------|-------|
| 股东大会 (AGM) | Low-medium | Voting on key items |
| 分红/送股/转增 (dividend/rights) | Medium | Ex-dividend date matters |
| 限售股解禁 (lock-up expiry) | Medium-high | Watch large blocks |
| 增减持公告 (shareholder transactions) | Low-medium | 5% threshold triggers disclosure |
| 回购 (share buyback) | Low-medium | Implementation tracking |
| 并购重组 (M&A announcements) | High | 停牌 until announcement |
| 增发/配股 (seasoned equity) | High | Dilution impact |
| 可转债发行/转股 | Medium | Conversion tracking |

### 4. Sector / Industry Events

| Event | Example Sectors | Notes |
|-------|----------------|-------|
| 行业展会/论坛 | 新能源, 半导体, 医药 | Networking, product announcements |
| 政策研讨会 | 环保, 教育, 互联网 | Policy direction signals |
| 行业协会数据发布 | 汽车, 光伏, 风电 | Monthly/quarterly stats |
| 国际展会 (CES, IFA, etc.) | 消费电子 | New product launches |

### 5. Macro Data Releases

| Indicator | Frequency | Impact |
|-----------|-----------|--------|
| PMI (制造业/非制造业) | Monthly (1st) | Market-wide |
| CPI / PPI | Monthly (9-10th) | Rates, commodities |
| 社会融资规模 / M2 | Monthly (10-15th) | Liquidity |
| 外汇储备 | Monthly | FX sentiment |
| 工业增加值 | Monthly | Growth indicator |
| 零售数据 | Monthly | Consumption |
| 就业数据 | Quarterly | Labor market |

## Data Sources (Multi-Tier)

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 - Tonghuashun iFind (paid)
```python
ifind_get_stock_events(query)  -> Key corporate events, dividends, buybacks
ifind_search_notice(query)     -> Announcement search
ifind_search_news(query)       -> Related news
ifind_get_stock_info(ticker)   -> Company profile, share structure
```
### Tier 2 - AkShare (free, fallback)

### Company-Specific

```python
# AkShare MCP
get_financials(ticker, "income", "annual")   → Historical earnings pattern
get_quote(ticker)                            → Current trading status
get_stock_info(ticker)                       → Company basic info

# Web sources for calendar data
# - 巨潮公告搜索: cninfo.com.cn
# - 上交所公告: sse.com.cn
# - 深交所公告: szse.cn
```

### Market-Wide

```python
get_index_data("000001")  # 上证指数 context
get_stock_news(ticker="") # General market news
```

> Data source mode: `IFIND_DATA_SOURCE_MODE=ifind-only` for iFind-only mode.

## Workflow

### Step 1: Define Coverage Universe

Identify the stocks and sectors to track. Typical A-share coverage universe:
- 50-200 names
- Organized by sector/industry
- Priority tiers (P1 = must-track, P2 = watchlist)

### Step 2: Build Calendar Entries

**For each catalyst, record:**

```json
{
  "date": "2024-04-25",
  "type": "earnings",
  "subtype": "季报",
  "ticker": "{{TICKER}}",
  "company": "{{COMPANY_NAME}}",
  "importance": "high",
  "notes": "Q1 2024 results; watch 批价 and inventory",
  "status": "confirmed"
}
```

**Catalyst types in JSON:**
- `earnings` — quarterly/semi/annual reports
- `earnings_call` — 业绩说明会
- `regulatory` — 监管政策发布
- `policy` — 宏观政策 (央行, 国务院)
- `corporate` — 公司事件 (分红, 解禁, M&A)
- `macro_data` — 经济数据发布
- `sector_event` — 行业展会/论坛
- `lockup_expiry` — 限售股解禁

### Step 3: Prioritize Catalysts

**Importance levels:**
- **Critical**: Likely to move stock >10% (earnings, M&A, major policy)
- **High**: Likely to move stock 5-10% (regulatory decisions, industry data)
- **Medium**: Watch item, context-setting (dividend, conference participation)
- **Low**: Background noise (routine filings, minor announcements)

### Step 4: Pre-Catalyst Preparation

**1 week before critical catalysts:**
- Pull latest data and consensus
- Prepare scenario analysis
- Draft preliminary positioning note
- Alert stakeholders if high-impact

**1 day before critical catalysts:**
- Final data check
- Confirm release timing (morning vs afternoon)
- Prepare pre-market positioning note
- Set monitoring alerts

### Step 5: Post-Catalyst Update

After catalyst passes:
- Record actual outcome
- Compare vs scenario framework
- Update price target / thesis if material
- Move to "completed" section
- Flag next catalyst in queue

## Calendar Format

### Weekly View

```
【本周催化剂日历】[YYYY-MM-DD 至 YYYY-MM-DD]

周一 [Date]
  - [Time] [Ticker] [Company] — [Event type] — [Importance]
  - [Time] [Macro event] — [Impact assessment]

周二 [Date]
  ...

本周重点：
- [Top 2-3 catalysts to watch]
- [Market-wide risk events]
```

### Monthly View

```
【X月重要事件日历】

财报窗口:
- [Week 1]: [Sector] Q[X] results: [List of companies]
- [Week 2]: [Sector] Q[X] results: [List of companies]

政策窗口:
- [Date]: [Policy event] — [Expected impact]

解禁窗口:
- [Date]: [Ticker] — [Amount] shares unlocking — [Risk assessment]

宏观数据:
- [Date]: [Indicator] — [Consensus] — [Previous]
```

### Upcoming Catalysts Table

| Date | Company | Event | Importance | Watch Item |
|------|---------|-------|------------|------------|
| {{DATE}} | {{COMPANY_NAME}} ({{TICKER}}) | {{EVENT_TYPE}} | {{IMPORTANCE}} | {{WATCH_ITEMS}} |
| Example | 贵州茅台 (600519) | Q1 年报 | Critical | 批价, 动销 |
| 04-30 | 工信部 | 新能源车月度数据 | Medium | 销量, 渗透率 |

## China-Specific Considerations

### Earnings Calendar Patterns

| Season | Months | Key Notes |
|--------|--------|-----------|
| Q1 earnings | Late April | 年报 + Q1季报 叠加, 信息密集 |
| H1 earnings | Late August | 中报窗口, 分红预案公布 |
| Q3 earnings | Late October | 三季报, 全年预测调整 |
| Annual earnings | Jan-April | 年报密集发布, 分红方案 |

### Lock-up Expiry (限售股解禁)

- 首发限售股 (IPO lock-up): typically 12 months
- 定增限售股 (private placement): typically 6-18 months
- 股权激励限售股: varies by plan
- High lock-up expiry → potential selling pressure

**Risk assessment:**
- Large percentage of float unlocking (>5%) → high risk
- Concentrated holders (single entity) → higher impact
- Company in downtrend → higher probability of sale

### Regulatory Calendar

**Recurring policy events:**
- 中央经济工作会议 (Central Economic Work Conference): Dec
- 两会 (Two Sessions / NPC & CPPCC): Mar
- 政治局会议 (Politburo meeting): Monthly (economics discussed ~quarterly)
- 国新办发布会 (State Council Info Office presser): Ad-hoc
- 央行货币政策执行报告: Quarterly

### Dividend Calendar

- 股权登记日 (record date): critical for dividend capture
- 除权除息日 (ex-dividend date): price adjusts
- 分红实施公告: typically 2-4 weeks after AGM approval
- 高送转 (high bonus issue): historically market-positive event

## Integration with Other Skills

| Related Skill | Integration Point |
|---------------|-------------------|
| china-earnings-analysis | Post-earnings catalyst review |
| china-earnings-preview | Pre-earnings scenario setup |
| china-thesis-tracker | Catalyst milestone tracking |
| china-morning-note | Daily catalyst briefing |
| china-market-researcher | Sector catalyst themes |

## Quality Checks

Before delivering:
- [ ] Calendar covers 4-12 weeks ahead
- [ ] All critical catalysts flagged
- [ ] Dates verified against official sources
- [ ] Importance levels assigned consistently
- [ ] Watch items specific and actionable
- [ ] Pre-catalyst preparation tasks defined
