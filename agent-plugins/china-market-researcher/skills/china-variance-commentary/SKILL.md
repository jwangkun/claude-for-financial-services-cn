---
name: china-variance-commentary
description: Write variance commentary for A-share fund performance and portfolio changes. Adapts the original variance-commentary skill for fund accounting and Chinese fund reporting conventions. Triggers on "基金业绩点评", "组合表现分析", "variance commentary fund", "基金表现分析", "业绩归因", or "commentary on [fund] performance".
---

# china-variance-commentary

## Purpose

Write professional **基金业绩点评** — structured variance commentary on fund performance and portfolio changes.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_fund_data(fund_code)              → Fund NAV, performance
get_quote(ticker)                     → Individual security performance
get_index_data("000001")              → Benchmark data
```

### Secondary Sources
- 基金公司 — fund performance data
- 托管行 — custody data
- Wind / Choice — performance analytics

## Workflow

### Step 1: Gather Performance Data

**Performance snapshot:**

| Metric | Period | Benchmark | Active Return |
|--------|--------|-----------|--------------|
| 净值增长率 | X.XX% | X.XX% | X.XX% |
| 年化收益率 | X.XX% | X.XX% | X.XX% |
| 波动率 | X.XX% | X.XX% | |
| 夏普比率 | X.XX | | |
| 最大回撤 | X.XX% | | |
| 卡尔马比率 | X.XX | | |

### Step 2: Attribution Analysis

**Performance attribution:**

| Factor | Contribution | Description |
|--------|-------------|-------------|
| 资产配置 (Allocation) | X.XX% | Sector/security weight decisions |
| 个股选择 (Selection) | X.XX% | Security picking within sectors |
| 交互效应 (Interaction) | X.XX% | Combined effect |

### Step 3: Sector Attribution

**Sector performance:**

| Sector | Weight | Return | Contribution | Benchmark Weight | Benchmark Return | Allocation Effect | Selection Effect |
|--------|--------|--------|-------------|-----------------|-----------------|-----------------|-----------------|
| | | | | | | | |
| **Total** | **100%** | | | | | | |

### Step 4: Top/Bottom Contributors

**Best/worst performers:**

| # | Security | Ticker | Weight | Period Return | Contribution |
|---|----------|--------|--------|--------------|-------------|
| 1 (Best) | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| ... | | | | | |
| (Worst) | | | | | |
| (2nd Worst) | | | | | |
| (3rd Worst) | | | | | |

### Step 5: Risk Analysis

**Risk metrics:**

| Metric | Value | Benchmark | Assessment |
|--------|-------|-----------|-----------|
| 波动率 | X.XX% | X.XX% | Higher/Lower |
| 最大回撤 | X.XX% | X.XX% | |
| 下行偏差 | X.XX% | X.XX% | |
| VaR (95%) | X.XX% | | |
| Beta | X.XX | | |
| Alpha | X.XX% | | |

### Step 6: Holdings Changes

**Changes since last period:**

| Action | Security | Ticker | Reason | Impact |
|--------|----------|--------|--------|--------|
| New buy | | | | |
| Add to | | | | |
| Reduce | | | | |
| Sold | | | | |

### Step 7: Market Context

**Market environment:**

| Factor | Current | Prior Period | Change |
|--------|---------|-------------|--------|
| 上证指数 | | | |
| 沪深300 | | | |
| 创业板指 | | | |
| 北向资金 | | | |
| 成交量 | | | |

### Step 8: Commentary

**Standard format:**

```
【业绩点评】[Fund Name] [Period]
报告期：[Date]
单位净值：¥X.XXXX
净值增长率：+/-X.XX%
基准收益率：+/-X.XX%
超额收益：+/-X.XX%

一、业绩概览
   [Overall performance summary]

二、归因分析
   [Attribution breakdown]

三、行业分析
   [Sector attribution]

四、重仓股表现
   [Top/bottom contributors]

五、风险指标
   [Risk metrics]

六、持仓变动
   [Changes in portfolio]

七、市场回顾
   [Market context]

八、展望
   [Forward outlook]
```

## China-Specific Considerations

### Fund Benchmarks

| Fund Type | Typical Benchmark |
|-----------|------------------|
| 股票型基金 | 沪深300 / 创业板指 |
| 债券型基金 | 中债综合指数 |
| 混合型基金 | 沪深300 × 50% + 中债 × 50% |
| 指数基金 | Tracking index |
| QDII | Relevant foreign index |

### Performance Presentation

| Convention | China Practice |
|-----------|----------------|
| Return calculation | Geometric |
| Benchmark | Contractual |
| Reporting frequency | Daily for public funds |
| Risk metrics | Standard set |

## Quality Checks

Before delivering:
- [ ] Performance data accurate
- [ ] Attribution complete
- [ ] Top/bottom contributors identified
- [ ] Risk metrics calculated
- [ ] Holdings changes documented
- [ ] Market context current
- [ ] Commentary balanced
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
