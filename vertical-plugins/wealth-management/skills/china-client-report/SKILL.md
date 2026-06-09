---
name: china-client-report
description: Generate client-facing performance reports for Chinese wealth management clients. Adapted from the original client-report skill for A-share portfolios, Chinese regulatory requirements, and local reporting conventions. Triggers on "A股客户报告", "客户持仓报告", "client report China", "wealth report A-share", "客户业绩报告", or "portfolio report for [client]".
---

# china-client-report

## Purpose

Create professional **A股财富管理客户报告** — performance reports for Chinese wealth management clients.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_index_data("000001")              → 上证指数 benchmark
get_index_data("399006")              → 创业板指 benchmark
get_index_data("000300")              → 沪深300 benchmark
get_quote(ticker)                     → Individual security performance
get_fund_data(fund_code)              → Fund performance
```

### Secondary Sources
- 基金公司 — fund data
- Wind / Choice — comprehensive market data
- 晨星中国 — fund ratings

## Workflow

### Step 1: Portfolio Snapshot

**Client portfolio summary:**

| Metric | Value | Change |
|--------|-------|--------|
| Total AUM (总资产) | ¥XX.X万 | ±X% |
| Market value | ¥XX.X万 | ±X% |
| Cash position | ¥XX.X万 | |
| YTD return | X.XX% | |
| Since inception | X.XX% (annualized) | |
| Benchmark (沪深300) | X.XX% | |

### Step 2: Performance Attribution

**Performance by asset class:**

| Asset Class | Allocation | Market Value | Period Return | Contribution |
|-------------|-----------|--------------|---------------|-------------|
| A股股票 | XX% | ¥XX | X.XX% | X.XX% |
| 基金 | XX% | ¥XX | X.XX% | X.XX% |
| 债券 | XX% | ¥XX | X.XX% | X.XX% |
| 现金/理财 | XX% | ¥XX | X.XX% | X.XX% |
| **Total** | **100%** | | **X.XX%** | |

**Performance by sector:**

| Sector | Allocation | Return | Contribution |
|--------|-----------|--------|-------------|
| 消费 | XX% | X.XX% | X.XX% |
| 科技 | XX% | X.XX% | X.XX% |
| 医药 | XX% | X.XX% | X.XX% |
| 金融 | XX% | X.XX% | X.XX% |
| 新能源 | XX% | X.XX% | X.XX% |
| 其他 | XX% | X.XX% | X.XX% |

### Step 3: Holdings Review

**Top positions:**

| Security | Ticker | Allocation | Market Value | Period Return | vs Benchmark |
|----------|--------|-----------|--------------|---------------|-------------|
| | | | | | |

**Positions with significant changes:**
- New positions added
- Positions sold
- Significant gainers (>20%)
- Significant losers (>15%)

### Step 4: Market Context

**Market environment:**

```
一、市场回顾
   上证指数: [Close] ([Change]%)
   深证成指: [Close] ([Change]%)
   创业板指: [Close] ([Change]%)
   
   市场特征:
   - 成交量: [XX亿]
   - 北向资金: [净买入/净卖出 XX亿]
   - 领涨板块: [List]
   - 领跌板块: [List]

二、宏观要闻
   - [Key macro developments]
   - [Policy changes]
   - [Market-moving events]
```

### Step 5: Commentary

**Performance commentary:**

```
一、整体表现
   [Period return, benchmark comparison, attribution summary]

二、主要贡献
   [Top contributors to performance]

三、主要拖累
   [Biggest detractors from performance]

四、操作回顾
   [Trading activity summary]

五、市场展望
   [Brief market outlook]
```

### Step 6: Recommendations

**Forward-looking recommendations:**

| Action | Rationale | Priority |
|--------|-----------|----------|
| | | High / Medium / Low |

### Step 7: Format & Delivery

**Standard Chinese client report format:**

```
【XX财富】客户投资报告 [Period]
客户名称：[Client Name]
报告期：[Period]

一、账户概览
   [Portfolio snapshot table]

二、业绩表现
   [Performance attribution]

三、持仓分析
   [Holdings review]

四、市场回顾
   [Market context]

五、投研观点
   [Commentary]

六、展望与建议
   [Outlook and recommendations]
```

## China-Specific Considerations

### Benchmark Selection

| Client Profile | Appropriate Benchmark |
|---------------|----------------------|
| A股均衡 | 沪深300 |
| A股成长 | 创业板指 |
| A股价值 | 中证红利 |
| 偏债混合 | 沪深300 × 60% + 中债 × 40% |
| 基金组合 | 基金业绩基准加权 |

### Regulatory Disclosures

**Required disclosures (China):**
- 过往业绩不预示未来表现
- 投资有风险, 入市需谨慎
- 管理人责任声明
- 风险等级匹配 (适当性)
- 费率披露

### Common A-share Client Concerns

| Concern | Typical Response |
|---------|-----------------|
| 账户亏损 | Explain market cycle, quality of holdings |
| 净值波动 | Normal for equity investing |
| 为什么买/卖 | Investment rationale |
| 市场方向 | Tactical positioning |
| 个股风险 | Risk management process |
| 赎回 | Liquidity, timing considerations |

## Quality Checks

Before delivering:
- [ ] All holdings accurately reflected
- [ ] Performance calculations correct
- [ ] Attribution complete
- [ ] Market context accurate
- [ ] Commentary balanced
- [ ] Recommendations appropriate
- [ ] Regulatory disclosures included
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
