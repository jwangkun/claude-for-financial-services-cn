---
name: china-portfolio-rebalance
description: Portfolio rebalancing analysis for A-share wealth management portfolios. Analyzes allocation drift, generates rebalancing trades, and optimizes for tax efficiency. Adapted from the original portfolio-rebalance skill for Chinese portfolios. Triggers on "A股组合再平衡", "调仓", "rebalance China", "portfolio rebalance A-share", "rebalance portfolio", or "adjust allocation [client]".
---

# china-portfolio-rebalance

## Purpose

Perform **A股投资组合再平衡** — analyze allocation drift, generate rebalancing recommendations, and optimize trade execution.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_quote(ticker)                     → Current prices for holdings
get_historical_data(ticker)           → Tax lot / cost basis context
```

### Secondary Sources
- Portfolio management system
- Wind / Choice — market data
- Tax rules — A-share tax treatment

## Workflow

### Step 1: Current Allocation

**Portfolio snapshot:**

| Asset Class | Target % | Current % | Drift | Market Value | Action |
|-------------|----------|-----------|-------|--------------|--------|
| | | | | | |

**Within A-share equity:**

| Sector | Target | Current | Drift | Action |
|--------|--------|---------|-------|--------|
| 消费 | XX% | XX% | ±X% | Buy/Sell/Hold |
| 科技 | XX% | XX% | ±X% | Buy/Sell/Hold |
| 医药 | XX% | XX% | ±X% | Buy/Sell/Hold |
| 金融 | XX% | XX% | ±X% | Buy/Sell/Hold |
| 新能源 | XX% | XX% | ±X% | Buy/Sell/Hold |
| 其他 | XX% | XX% | ±X% | Buy/Sell/Hold |

### Step 2: Identify Drift

**Drift thresholds:**

| Drift Level | Action |
|-------------|--------|
| ±2% | Monitor, no action |
| ±3-5% | Consider rebalancing |
| ±5%+ | Rebalance recommended |

**Drift causes:**
- Market price movements
- Dividend reinvestment
- Previous trades
- Cash flows (contributions/withdrawals)

### Step 3: Generate Rebalancing Trades

**Rebalancing logic:**

| Situation | Action |
|-----------|--------|
| Sector overweight + price up | Trim position |
| Sector underweight + price down | Add to position |
| Overweight + price down | Monitor (may converge) |
| Underweight + price up | Monitor (may converge) |

**Trade list:**

| Action | Ticker | Security | Current % | Target % | Trade Amount | Est. Shares |
|--------|--------|----------|-----------|----------|-------------|------------|
| Buy | | | | | | |
| Sell | | | | | | |
| Hold | | | | | | |

### Step 4: Tax Considerations

**A-share tax treatment:**

| Item | Tax Rate | Notes |
|------|----------|-------|
| 股票买卖价差 | 暂免 (temporarily exempt) | Capital gains on stocks |
| 股息红利 | 20% (持股>1年减半/免征) | Dividend tax |
| 基金分红 | 暂免 (some funds) | Fund distributions |
| 买卖印花税 | 0.05% (seller only) | Stamp duty |

**Tax-loss harvesting opportunities:**

| Position | Cost Basis | Current Value | Unrealized Loss | Tax Benefit |
|----------|-----------|--------------|-----------------|-------------|
| | | | | |

**Tax-efficient selling:**
- Prioritize selling positions with losses
- Consider holding period for dividend tax
- Batch sales to minimize stamp duty impact

### Step 5: Execution Plan

**Trade sequencing:**

| Priority | Trade | Rationale |
|----------|-------|-----------|
| 1 | | Tax loss harvesting |
| 2 | | Largest drift correction |
| 3 | | Smaller adjustments |

**Execution considerations:**
- Market impact (liquidity)
- Trading costs (commissions, stamp duty)
- Market timing (volatility)
- Block trading for large positions

### Step 6: Rebalancing Report

**Standard rebalancing report:**

```
【组合再平衡报告】[Client] [Date]

一、当前配置 vs 目标配置
   [Allocation table with drift]

二、再平衡建议
   [Trade list]

三、税务影响
   [Tax implications]

四、执行计划
   [Sequencing and timing]

五、预期效果
   [Projected post-rebalance allocation]
```

## China-Specific Rebalancing Considerations

### A-share Market Characteristics

| Factor | Rebalancing Implication |
|--------|------------------------|
| 涨跌停限制 | May prevent immediate rebalancing |
| T+1 settlement | Trade settlement timeline |
| 印花税 | 0.05% on sell side |
| 佣金 | Varies by broker (typically 0.02-0.03%) |
| 最低手续费 | Minimum commission threshold |

### Tax-Loss Harvesting (A-share)

**China-specific TLH:**
- Capital gains on stocks: currently tax-exempt (暂免)
- Losses: can offset gains within the same asset class
- 股息红利 tax: 20%, reduced to 10% for >1 year holding, 0% for >1 year (recent changes)
- Fund distributions: tax treatment varies by fund type

### Common Rebalancing Triggers

| Trigger | Frequency | Action |
|---------|-----------|--------|
| Calendar rebalancing | Quarterly/Semi-annual | Systematic rebalance |
| Drift threshold | When ±5% | Opportunistic rebalance |
| Cash inflow | As received | Deploy to underweights |
| Client request | Ad-hoc | Targeted rebalance |
| Tax planning | Year-end | Harvest losses, reset cost basis |

## Quality Checks

Before executing:
- [ ] Allocations calculated correctly
- [ ] Trades aligned with policy
- [ ] Tax implications assessed
- [ ] Trading costs estimated
- [ ] Client approval obtained
- [ ] Execution plan sequenced

After rebalancing:
- [ ] Trades confirmed
- [ ] Allocation updated
- [ ] Tax lots recorded
- [ ] Client notified
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
