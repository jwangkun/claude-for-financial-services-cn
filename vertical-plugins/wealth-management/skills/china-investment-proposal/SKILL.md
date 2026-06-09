---
name: china-investment-proposal
description: Draft investment proposals for Chinese wealth management clients. Creates structured proposals with investment rationale, product recommendations, and risk disclosures. Adapted from the original investment-proposal skill for A-share products and Chinese regulatory requirements. Triggers on "A股投资建议书", "投资方案", "investment proposal China", "proposal for [client]", "investment recommendation A-share", or "build investment proposal".
---

# china-investment-proposal

## Purpose

Create professional **A股财富管理投资建议书** — structured proposals for Chinese wealth management clients.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_index_data("000001")              → Market context
get_index_data("399006")              → ChiNext context
get_quote(ticker)                     → Security analysis
get_fund_data(fund_code)              → Fund analysis
get_industry_stocks(industry="...")    → Sector analysis
```

### Secondary Sources
- Portfolio management system
- Research team — market outlook
- Product providers — fund/insurance data

## Workflow

### Step 1: Understand Client Needs

**Discovery questions:**

1. **Investment objective**: 保值增值 / 稳健增值 / 积极增值 / 收入型
2. **Time horizon**: 短期(<1年) / 中期(1-5年) / 长期(>5年)
3. **Risk tolerance**: 保守 / 稳健 / 积极 / 激进
4. **Liquidity needs**: 高 / 中 / 低
5. **Special considerations**: 税务, 遗产, 慈善, etc.

### Step 2: Market & Strategy Overview

**Current market assessment:**

```
市场展望 [Period]

一、宏观经济
   [GDP, policy, rates outlook]

二、权益市场
   - 估值水平: 沪深300 PE [Xx] (历史[X]%分位)
   - 资金面: 北向资金, 两融余额
   - 情绪指标: [Index]

三、行业配置观点
   超配 (Overweight): [Sectors] — [Rationale]
   标配 (Neutral): [Sectors]
   低配 (Underweight): [Sectors] — [Rationale]

四、风险提示
   [Key risks]
```

### Step 3: Investment Strategy

**Strategy design:**

| Component | Allocation | Rationale |
|-----------|-----------|-----------|
| A股权益 | XX% | Growth engine |
| 基金 (主动) | XX% | Professional management |
| 基金 (指数) | XX% | Low-cost beta |
| 债券/固收+ | XX% | Stability, income |
| 现金/货币基金 | XX% | Liquidity |
| 另类 (REITs, 黄金) | XX% | Diversification |

**A-share equity allocation:**

| Sector | Weight | Thesis |
|--------|--------|--------|
| 消费 | XX% | [Rationale] |
| 科技 | XX% | [Rationale] |
| 医药 | XX% | [Rationale] |
| 金融 | XX% | [Rationale] |
| 新能源 | XX% | [Rationale] |
| 其他 | XX% | [Rationale] |

### Step 4: Product Recommendations

**Recommended securities:**

| # | Type | Security | Ticker | Allocation | Rationale | Risk Level |
|---|------|----------|--------|-----------|-----------|------------|
| 1 | A股个股 | | | | | |
| 2 | 主动基金 | | | | | |
| 3 | 指数基金 | | | | | |
| 4 | 债券/理财 | | | | | |
| 5 | 现金管理 | | | | | |

**For each recommendation:**
- Investment thesis (3-5 bullet points)
- Expected return range
- Risk assessment
- Suitable for client profile
- Minimum investment
- Liquidity terms

### Step 5: Risk Assessment & Disclosure

**Risk factors (standard Chinese disclosures):**

```
风险揭示

一、市场风险
   投资有风险, 入市需谨慎。本投资方案涉及A股市场投资,
   股票价格可能因市场因素大幅波动。

二、流动性风险
   部分投资品可能存在流动性限制, 赎回/卖出可能受
   市场流动性影响。

三、政策风险
   国家政策、行业监管变化可能影响投资组合表现。

四、信用风险
   固定收益类产品存在发行人信用风险。

五、汇率风险
   [If applicable]

六、其他风险
   [Product-specific risks]
```

**Risk level match:**
- Conservative (保守型): 低风险产品为主, 权益<30%
- Balanced (稳健型): 中等风险, 权益30-60%
- Growth (积极型): 较高风险, 权益60-90%
- Aggressive (激进型): 高风险, 权益>90%

### Step 6: Expected Returns & Scenarios

**Return scenarios:**

| Scenario | Probability | Expected Return | Portfolio Value (3Y) |
|-----------|-------------|----------------|---------------------|
| 乐观 | 25% | +XX% | ¥XXX万 |
| 中性 | 50% | +X% | ¥XXX万 |
| 悲观 | 25% | -X% | ¥XXX万 |

### Step 7: Implementation Plan

**Implementation steps:**

| Step | Action | Timeline |
|------|--------|----------|
| 1 | 方案确认 | [Date] |
| 2 | 账户开立/激活 | [Date] |
| 3 | 建仓 (首批建仓) | [Date] |
| 4 | 分批建仓 (如需) | [Date range] |
| 5 | 首次复核 | [Date] |

**建仓策略:**
- 一次性建仓: 适合积极型, 市场低点
- 分批建仓: 适合稳健型, 降低择时风险
- 定投: 适合长期投资, 平滑成本

### Step 8: Monitoring & Review

**Review schedule:**

| Review Type | Frequency | Content |
|-------------|-----------|---------|
| 日常监控 | Daily | Market alerts, significant moves |
| 月度回顾 | Monthly | Performance, attribution |
| 季度复盘 | Quarterly | Full review, rebalancing |
| 年度规划 | Annual | Goal review, strategy update |

### Step 9: Proposal Document

**Standard proposal format:**

```
【投资建议书】
客户名称：[Name]
风险等级：[R1-R5]
投资期限：[X年]
建议日期：[Date]

一、客户需求分析
   [Goals, constraints, preferences]

二、市场展望
   [Current market assessment]

三、投资策略
   [Allocation strategy with rationale]

四、产品推荐
   [Detailed recommendations]

五、风险评估
   [Risk factors, suitability assessment]

六、预期表现
   [Return scenarios]

七、实施方案
   [Implementation plan]

八、后续服务
   [Review schedule, monitoring]

九、声明
   [Standard regulatory disclaimers]

客户签字：_________ 日期：_________
理财师签字：_________ 日期：_________
```

## China-Specific Considerations

### Suitability (适当性管理)

**China regulatory requirements:**
- 风险等级匹配: Product risk ≤ Client risk tolerance
- 投资者分类: 普通投资者 / 专业投资者
- 信息披露: Full and fair disclosure
- 冷静期: Cooling-off period for certain products
- 录音录像: Recording for in-person sales

### Common Investment Products (China)

| Product | Risk | Return | Liquidity |
|---------|------|--------|-----------|
| 银行理财 | Low | 2-4% | Medium |
| 货币基金 | Low | 1.5-2.5% | High |
| 国债 | Very low | 2-3% | Medium |
| 企业债 | Low-Medium | 3-5% | Medium |
| A股个股 | High | Variable | Medium |
| 主动基金 | Medium-High | Variable | Medium |
| 指数基金/ETF | Medium | Variable | High |
| 私募基金 | High | Variable | Low |
| 信托 | Medium-High | 5-8% | Low |
| 保险产品 | Low-Medium | Guaranteed + bonus | Low |

### Client Segmentation

| Type | Profile | Strategy |
|------|---------|----------|
| 保守型 | Risk-averse, capital preservation focus | Bonds, money market, blue chips |
| 稳健型 | Balanced, moderate growth | Balanced allocation, dividend stocks |
| 积极型 | Growth-oriented, can tolerate volatility | Growth stocks, sector funds |
| 激进型 | High risk tolerance, return-seeking | Small-caps, thematic, alternatives |

## Quality Checks

Before delivering:
- [ ] Client profile understood
- [ ] Allocation aligned with risk tolerance
- [ ] Products suitable and available
- [ ] Risk disclosures complete
- [ ] Expected returns realistic
- [ ] Implementation plan clear
- [ ] Regulatory disclosures included
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
