---
name: china-client-review
description: Prepare for Chinese wealth management client meetings with performance summaries, talking points, and relationship context. Adapted from the original client-review skill for A-share portfolios and Chinese client conventions. Triggers on "A股客户回顾", "客户会议准备", "client review China", "wealth client review", "客户回访准备", or "prepare for client meeting [client]".
---

# china-client-review

## Purpose

Prepare comprehensive **A股财富管理客户会议材料** — performance summaries, talking points, and relationship context for client meetings.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_index_data("000001")              → 上证 benchmark
get_index_data("399006")              → 创业板 benchmark
get_index_data("000300")              → 沪深300 benchmark
```

### Secondary Sources
- Portfolio management system (client holdings)
- Wind / Choice — market data
- Research team — market outlook

## Workflow

### Step 1: Client Profile Review

**Client context:**

| Attribute | Detail |
|-----------|--------|
| 客户名称 | |
| 风险等级 | C1-C5 (conservative to aggressive) |
| 投资目标 | 保值 / 增值 / 养老 / 教育 / 传承 |
| 投资期限 | Short / Medium / Long term |
| 流动性需求 | High / Medium / Low |
| 特殊需求 | 税务优化, 慈善, 家族信托 |

### Step 2: Portfolio Performance Summary

**Performance dashboard:**

| Metric | YTD | 1Y | 3Y | Since Inception |
|--------|-----|----|----|-----------------|
| Portfolio return | X.XX% | X.XX% | X.XX% | X.XX% |
| Benchmark (沪深300) | X.XX% | X.XX% | X.XX% | X.XX% |
| Active return | X.XX% | X.XX% | X.XX% | X.XX% |
| Best period | | | | |
| Worst period | | | | |

**Performance attribution:**

| Driver | Contribution |
|--------|-------------|
| Security selection | X.XX% |
| Sector allocation | X.XX% |
| Cash/bond yield | X.XX% |
| Fees | X.XX% |
| **Total** | **X.XX%** |

### Step 3: Holdings Review

**Portfolio composition:**

| Asset Class | Allocation | Benchmark | Active |
|-------------|-----------|-----------|--------|
| A股权益 | XX% | XX% | ±X% |
| 基金 | XX% | XX% | ±X% |
| 债券/理财 | XX% | XX% | ±X% |
| 现金 | XX% | XX% | ±X% |

**Top positions:**

| Security | Ticker | Allocation | Period Return | Comment |
|----------|--------|-----------|---------------|---------|
| | | | | |

**Changes since last meeting:**

| Action | Security | Reason | Date |
|--------|----------|---------|------|
| Buy | | | |
| Sell | | | |
| Rebalance | | | |

### Step 4: Talking Points

**Meeting agenda:**

```
一、业绩回顾
   - 整体表现 vs 基准
   - 主要贡献/拖累
   - 操作回顾

二、市场展望
   - 当前市场环境
   - 行业配置观点
   - 风险提示

三、组合分析
   - 配置合理性评估
   - 是否需要调整
   - 新机会/风险提示

四、客户需求
   - 听取客户反馈
   - 调整投资目标
   - 流动性需求变化

五、下一步计划
   - 具体操作建议
   - 下次会议时间
```

### Step 5: Personalized Insights

**Client-specific topics:**

| Topic | Details |
|-------|---------|
| 近期大额交易 | Explain rationale |
| 重大盈亏 | Contextualize, don't overemphasize |
| 分红/利息收入 | Highlight cash generation |
| 税务考虑 | Tax-loss harvesting opportunities |
| 目标进度 | Progress toward goals |

### Step 6: Market Outlook Brief

**Brief market context:**

```
市场展望 [Period]

一、宏观经济
   - GDP预期
   - 货币政策 (央行取向)
   - 财政政策

二、权益市场
   - A股估值水平 (PE/PB历史分位)
   - 资金面 (北向/南向, 两融)
   - 情绪指标

三、行业观点
   - 看多: [Sectors]
   - 看空: [Sectors]
   - 中性: [Sectors]

四、风险因素
   - [Key risks]
```

### Step 7: Action Items & Follow-up

**Meeting outcomes:**

| Action | Owner | Deadline |
|--------|-------|----------|
| | | |

**Next meeting:**
- Scheduled date
- Preliminary agenda
- Pre-work items

## China-Specific Considerations

### Client Communication Style

| Preference | Approach |
|------------|----------|
| 保守型 | Emphasize capital preservation, downside protection |
| 稳健型 | Balanced risk-return, steady growth |
| 进取型 | Growth opportunities, upside potential |
| 专业型 | Detailed analysis, data-driven |

### Common Client Concerns (A-share)

| Concern | Response Strategy |
|---------|------------------|
| 账户亏损 | Explain cycle, quality of holdings, recovery path |
| 为什么亏钱 | Attribute clearly, don't blame market |
| 能不能赚钱 | Realistic return expectations |
| 什么时候涨 | Market timing acknowledgment + process focus |
| 个股为什么跌/涨 | Fundamental explanation |
| 要不要赎回 | Assess goals, time horizon, alternatives |

### Regulatory Considerations

- 适当性管理 (suitability assessment)
- 风险揭示 (risk disclosure)
- 业绩比较基准 (benchmark disclosure)
- 费用披露 (fee transparency)
- 冷静期规定 (cooling-off period for new investments)

## Quality Checks

Before meeting:
- [ ] Portfolio data current
- [ ] Performance calculations accurate
- [ ] Talking points prepared
- [ ] Market outlook current
- [ ] Meeting materials organized
- [ ] Regulatory disclosures included

After meeting:
- [ ] Meeting minutes documented
- [ ] Action items assigned
- [ ] Portfolio adjustments executed
- [ ] Next meeting scheduled
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
