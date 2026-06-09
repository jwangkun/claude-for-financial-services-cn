---
name: china-financial-plan
description: Create financial plans for Chinese wealth management clients covering retirement, education, estate, and cash-flow planning. Adapted from the original financial-plan skill for Chinese tax rules, social security, and local financial products. Triggers on "A股财务规划", "理财规划", "financial plan China", "retirement plan China", "财务规划客户", "退休规划", "教育金规划", or "comprehensive financial plan".
---

# china-financial-plan

## Purpose

Create comprehensive **中国家庭/个人财务规划** — retirement, education, estate, and cash-flow planning adapted for Chinese context.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_index_data("000001")              → A股 historical returns
get_fund_data(fund_code)              → Fund performance data
```

### Secondary Sources
- 社保 — social security data
- 公积金 — housing fund data
- Wind / Choice — investment product data
- Insurance companies — insurance product info

## Workflow

### Step 1: Client Profile & Goals

**Client demographics:**

| Attribute | Detail |
|-----------|--------|
| 年龄 | |
| 职业 | |
| 家庭结构 | Single / Married / Children |
| 收入 | Annual income (税前) |
| 支出 | Monthly/annual expenses |
| 资产 | Current net worth |
| 负债 | Mortgage, other debt |

**Financial goals:**

| Goal | Timeline | Target Amount | Priority |
|------|----------|---------------|----------|
| 退休金 | XX years | ¥XXX万 | High/Med/Low |
| 子女教育 | XX years | ¥XXX万 | High/Med/Low |
| 购房 | X years | ¥XXX万 | High/Med/Low |
| 旅游/生活方式 | Ongoing | ¥XX万/年 | |
| 遗产规划 | Long-term | | |

### Step 2: Cash Flow Analysis

**Income sources:**

| Source | Monthly | Annual | Stability |
|--------|---------|--------|-----------|
| 工资收入 | ¥X | ¥XX | Stable/Variable |
| 经营收入 | ¥X | ¥XX | Variable |
| 投资收入 | ¥X | ¥XX | Variable |
| 租金收入 | ¥X | ¥XX | Semi-stable |
| 其他 | ¥X | ¥XX | |

**Expense breakdown:**

| Category | Monthly | Annual | Notes |
|----------|---------|--------|-------|
| 住房 (房贷/房租) | ¥X | ¥XX | |
| 食品 | ¥X | ¥XX | |
| 交通 | ¥X | ¥XX | |
| 子女教育 | ¥X | ¥XX | |
| 医疗 | ¥X | ¥XX | |
| 娱乐/旅游 | ¥X | ¥XX | |
| 保险 | ¥X | ¥XX | |
| 赡养老人 | ¥X | ¥XX | |
| 其他 | ¥X | ¥XX | |
| **Total** | **¥X** | **¥XX** | |

**Savings rate:** Savings / Income = X%

### Step 3: Net Worth Statement

**Assets:**

| Asset Category | Current Value | Expected Growth |
|---------------|--------------|-----------------|
| 现金及活期 | ¥XX | |
| 存款 (定期/大额) | ¥XX | |
| A股投资 | ¥XX | |
| 基金 | ¥XX | |
| 债券 | ¥XX | |
| 房产 | ¥XX | |
| 保险现金价值 | ¥XX | |
| 其他 | ¥XX | |
| **Total Assets** | **¥XX** | |

**Liabilities:**

| Liability | Amount | Interest Rate | Remaining Term |
|-----------|--------|--------------|----------------|
| 房贷 | ¥XX | X.X% | X years |
| 车贷 | ¥XX | X.X% | X years |
| 其他贷款 | ¥XX | X.X% | X years |
| **Total Liabilities** | **¥XX** | | |

**Net worth:** ¥XX万

### Step 4: Retirement Planning

**Retirement projection:**

| Parameter | Value |
|-----------|-------|
| Current age | XX |
| Retirement age | XX |
| Years to retirement | XX |
| Desired retirement income | ¥XX万/年 |
| Expected retirement duration | XX years |
| Current retirement savings | ¥XX万 |

**Projection:**

| Year | Age | Projected Savings | Required |
|------|-----|-------------------|----------|
| Now | XX | ¥XX万 | — |
| +5y | XX | ¥XX万 | ¥XX万 |
| +10y | XX | ¥XX万 | ¥XX万 |
| +15y | XX | ¥XX万 | ¥XX万 |
| Retirement | XX | ¥XX万 | ¥XX万 |

**Gap analysis:** Shortfall / Surplus of ¥XX万

**Solution options:**
- Increase savings rate
- Adjust investment returns assumption
- Delay retirement
- Part-time work in retirement

### Step 5: Education Planning

**Education cost estimate (China):**

| Stage | Duration | Annual Cost | Total Cost |
|-------|----------|-------------|------------|
| 幼儿园 | 3 years | ¥X-X万 | ¥X-X万 |
| 小学/初中 | 9 years | ¥X-X万 | ¥X-X万 |
| 高中 | 3 years | ¥X-X万 | ¥X-X万 |
| 国内大学 | 4 years | ¥X-X万 | ¥X-X万 |
| 海外本科 | 4 years | ¥XX-XXX万 | ¥XX-XXX万 |
| 海外硕士 | 1-2 years | ¥XX-XXX万 | ¥XX-XXX万 |

**Education fund projection:**

| Child Age | Years to College | Target Amount | Current Savings | Monthly Savings Needed |
|-----------|-----------------|---------------|----------------|----------------------|
| | | | | |

### Step 6: Investment Allocation

**Recommended allocation (A-share focus):**

| Asset Class | Conservative | Balanced | Growth |
|-------------|-------------|----------|--------|
| A股权益 | 20% | 40% | 60% |
| 基金 (主动/被动) | 20% | 25% | 20% |
| 债券 | 40% | 25% | 10% |
| 现金/理财 | 15% | 7% | 5% |
| 其他 (REITs, 黄金) | 5% | 3% | 5% |

**Within A-share equity:**

| Sector | Allocation | Rationale |
|--------|-----------|-----------|
| 消费 | XX% | Defensive, long-term growth |
| 科技 | XX% | Growth, innovation |
| 医药 | XX% | Demographics, defensive |
| 金融 | XX% | Value, dividends |
| 新能源 | XX% | Policy support |
| 其他 | XX% | Diversification |

### Step 7: Risk Management

**Insurance needs:**

| Type | Coverage | Annual Premium |
|------|----------|---------------|
| 医疗险 | ¥XX万 | ¥X,XXX |
| 重疾险 | ¥XX万 | ¥X,XXX |
| 意外险 | ¥XX万 | ¥X,XXX |
| 寿险 | ¥XX万 | ¥X,XXX |
| 养老险 | ¥XX万/年 | ¥X,XXX |

**Emergency fund:** 3-6 months expenses = ¥XX万

### Step 8: Tax Optimization

**China-specific tax planning:**

| Area | Strategy |
|------|----------|
| 个税 | 专项附加扣除 (education, mortgage, elderly) |
| 社保 | Optimal contribution levels |
| 公积金 | Maximize employer match |
| 投资 | 股息红利税收优化 |
| 房产 | 房产税 planning (if applicable) |

## China-Specific Considerations

### Social Security (社保)

| Type | Contribution | Benefits |
|------|-------------|----------|
| 养老保险 | ~28% of salary | Retirement pension |
| 医疗保险 | ~10% of salary | Medical coverage |
| 失业保险 | ~1% | Unemployment benefit |
| 工伤保险 | Employer | Work injury |
| 生育保险 | Employer | Maternity |
| 住房公积金 | 5-12% each side | Housing fund |

### Common Financial Products (China)

| Product | Return | Risk | Liquidity |
|---------|--------|------|-----------|
| 银行活期 | ~0.3% | Very low | High |
| 银行理财 | 2-4% | Low | Medium |
| 国债 | 2-3% | Very low | Medium |
| 货币基金 (余额宝等) | 1.5-2.5% | Low | High |
| A股 | -30% to +50%+ | High | Medium |
| 基金 (主动) | -20% to +40% | Medium-High | Medium |
| 基金 (指数) | -25% to +35% | Medium | Medium |
| 信托 | 5-8% | Medium-High | Low |
| 私募 | Variable | High | Low |

### Common Client Types

| Type | Characteristics | Planning Focus |
|------|----------------|---------------|
| 工薪阶层 | Stable income, limited savings | Systematic investing, tax optimization |
| 中小企业主 | Variable income, business exposure | Diversification, succession planning |
| 高净值 | Significant assets, complex needs | Tax optimization, estate planning |
| 退休人员 | Fixed income, preservation | Income generation, capital preservation |
| 年轻家庭 | Early career, children | Accumulation, education funding |

## Quality Checks

Before delivering:
- [ ] Client goals clearly defined
- [ ] Cash flow analysis complete
- [ ] Net worth accurate
- [ ] Projections realistic
- [ ] Allocation appropriate for risk profile
- [ ] Tax optimization considered
- [ ] Insurance needs assessed
- [ ] Recommendations actionable
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
