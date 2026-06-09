---
name: china-tax-loss-harvesting
description: Tax-loss harvesting strategies for A-share portfolios. Adapts the original tax-loss-harvesting skill for Chinese tax rules, A-share market conventions, and domestic tax treatment. Triggers on "A股税务亏损抵扣", "亏损抵扣", "tax loss harvesting China", "税务优化", "亏损抵扣策略", or "harvest tax losses [portfolio]".
---

# china-tax-loss-harvesting

## Purpose

Implement **A股税务亏损抵扣** — systematic tax-loss harvesting for Chinese investment portfolios.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_quote(ticker)                     → Current prices for holdings
get_historical_data(ticker)           → Cost basis / purchase history
```

### Secondary Sources
- Broker records — cost basis, trade history
- Tax filings — prior year losses
- 交易所 — tax treatment rules

## Workflow

### Step 1: Identify Tax-Loss Positions

**Loss identification:**

| Position | Ticker | Cost Basis | Current Value | Unrealized Loss | Loss % |
|----------|--------|-----------|--------------|-----------------|--------|
| | | ¥XX | ¥XX | ¥XX | X% |

**Loss screening criteria:**
- Unrealized loss > 10% of cost basis
- Loss amount significant relative to portfolio
- Holding period appropriate for tax treatment

### Step 2: Understand A-share Tax Rules

**China tax treatment for securities:**

| Item | Tax Rate | Notes |
|------|----------|-------|
| 证券买卖价差 | **暂免** (temporarily exempt) | Capital gains on stocks |
| 股息红利 | 20% (持股>1年减半至10%, >1年免征) | Dividend tax |
| 基金分红 | 暂免 (some funds) | Fund distributions |
| 买卖印花税 | 0.05% (seller only) | Stamp duty |
| 证券交易佣金 | 0.02-0.03% | Commission |

**Current status of capital gains tax:**
- Individuals: Capital gains on stocks are currently **temporarily exempt** (暂免征收)
- However, losses can be used to offset gains within the same year
- Loss carryforward rules may apply

### Step 3: Calculate Tax Benefit

**Tax benefit calculation:**

| Scenario | Gain | Loss | Taxable Gain | Tax Saved |
|----------|------|------|--------------|-----------|
| Without TLH | ¥XX | — | ¥XX | — |
| With TLH | ¥XX | ¥XX | ¥XX | ¥XX |
| **Benefit** | | | | **¥XX** |

**Note:** In the current A-share environment where capital gains are largely exempt, tax-loss harvesting benefits may be limited. However:
- Harvesting losses can be valuable if tax rules change
- Offsetting gains within the same year
- Potential future tax benefit if capital gains tax is introduced

### Step 4: Identify Replacement Securities

**Replacement criteria:**

| Criterion | Requirement |
|-----------|-------------|
| Same sector | Similar industry exposure |
| Similar characteristics | Market cap, growth, quality |
| Not substantially identical | Avoid wash sale rules |
| Tax-efficient | Consider dividend treatment |

**Wash sale considerations (China):**
- No explicit wash sale rule currently
- However, substantially identical securities may be disallowed
- Best practice: 30-day waiting period

### Step 5: Execution Strategy

**Execution options:**

| Strategy | Description | Pros | Cons |
|----------|-------------|------|------|
| Full exit | Sell and replace | Clean loss realization | Market risk |
| Partial exit | Reduce position | Partial benefit | Partial benefit only |
| Swap | Sell loss, buy similar | Maintain exposure | Timing risk |
| Delay | Wait for recovery | No transaction costs | Missed opportunity |

### Step 6: Implementation Plan

**Step-by-step plan:**

| Step | Action | Timing |
|------|--------|--------|
| 1 | Identify loss positions | Pre-year-end |
| 2 | Evaluate replacement options | Pre-year-end |
| 3 | Check wash sale rules | Pre-year-end |
| 4 | Execute sales | Before year-end |
| 5 | Execute purchases | After sale (or simultaneously) |
| 6 | Document transactions | Immediately |
| 7 | File tax forms | Tax filing deadline |

### Step 7: Document for Tax Filing

**Required documentation:**

| Document | Content |
|----------|---------|
| Trade confirmations | Sale and purchase tickets |
| Cost basis records | Purchase prices, dates |
| Loss calculations | Realized loss amounts |
| Replacement securities | Identified alternatives |
| Market rationale | Investment thesis |

### Step 8: Year-End Checklist

**Year-end TLH checklist:**

| Date | Action |
|------|--------|
| Nov | Review portfolio for loss positions |
| Dec 1-15 | Identify replacement securities |
| Dec 15-20 | Execute loss sales |
| Dec 20-31 | Execute replacements |
| Dec 31 | Final portfolio review |
| Jan | File tax documentation |

## China-Specific TLH Considerations

### Current Tax Environment

| Factor | Status | Implication |
|--------|--------|-------------|
| 资本利得税 | 暂免 (temporarily exempt) | Limited current benefit |
| 印花税 | 0.05% | Cost on sale |
| 股息红利税 | 20% (10% for >1yr) | Consider in replacement |
| 交易佣金 | 0.02-0.03% | Trading cost |

### When TLH Makes Sense in China

| Scenario | Benefit |
|----------|---------|
| Offset short-term gains | Use losses against gains |
| Reset cost basis | Lower future gains if taxed |
| Prepare for tax changes | If capital gains taxed in future |
| Portfolio rebalancing | Combine with rebalancing |

### A-share Market Timing

| Consideration | Guidance |
|--------------|----------|
| 年末效应 | Year-end selling pressure |
| 涨跌停限制 | May prevent execution |
| 流动性 | Ensure liquidity for exit |
| 政策窗口 | Tax policy change risk |

## TLH for Different Client Types

### Individual Investors

| Consideration | Guidance |
|---------------|----------|
| 持股期限 | >1 year for dividend tax benefit |
| 高频交易 | May trigger scrutiny |
| 金额门槛 | Focus on significant positions |

### Institutional Investors

| Consideration | Guidance |
|---------------|----------|
| 交易成本 | Factor in commission impact |
| 市场冲击 | Large position impact |
| 会计处理 | NAV impact timing |
| 合规审查 | Documentation requirements |

## Quality Checks

Before executing:
- [ ] Loss positions identified
- [ ] Tax benefit calculated
- [ ] Replacement securities identified
- [ ] Wash sale rules considered
- [ ] Execution plan clear
- [ ] Documentation prepared
- [ ] Timing appropriate
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
