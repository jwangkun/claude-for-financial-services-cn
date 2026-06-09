---
name: china-unit-economics
description: Unit economics analysis for China-focused portfolio companies. Adapted from the original unit-economics skill for Chinese business models, pricing, and market dynamics. Triggers on "A股单位经济模型", "单元经济模型", "unit economics China", "unit economics [company]", "LTV/CAC China", or "Cohort analysis [company]".
---

# china-unit-economics

## Purpose

Analyze **A股及中国市场单元经济模型** — per-unit economics, customer economics, and cohort analysis for portfolio companies.

## Key Metrics

### Core Framework (Same as Global)

| Metric | Formula | Target |
|--------|---------|--------|
| LTV (Customer Lifetime Value) | ARPU × Lifetime × Gross Margin | >3x CAC |
| CAC (Customer Acquisition Cost) | Sales & Marketing / New Customers | <12-month payback |
| LTV/CAC | LTV / CAC | >3.0x |
| CAC Payback (months) | CAC / (ARPU × Gross Margin %) | <12 months |
| NRR (Net Revenue Retention) | (Start + Expansion - Churn) / Start | >100% |
| GRR (Gross Revenue Retention) | (Start - Churn) / Start | >85% |
| ARR | Annual Recurring Revenue | Growing |
| Churn Rate | Lost customers / Total | <5% monthly |

### China-Specific Metrics

| Metric | Description | China Context |
|--------|-------------|---------------|
| 获客成本 | CAC in Chinese context | 线上投放 + 线下渠道 |
| 用户生命周期价值 | LTV for Chinese consumers | Higher for tier-1 |
| 复购率 | Repeat purchase rate | Critical for DTC brands |
| 客单价 | Average order value | 价格敏感 market |
| 渠道成本 | Channel economics | 经销商 vs DTC |
| 补贴依赖 | Subsidy / discount dependence | Common in China |

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
# For public companies, extract proxies
get_financials(ticker, "income")    → Revenue, opex
get_financials(ticker, "balance")   → Customer-related assets
get_financials(ticker, "cashflow")  → Cash flow
```

### Secondary Sources
- 巨潮 — company filings with segment data
- 管理层指引 — management guidance
- 券商研报 — unit economics estimates
- 行业数据 — industry benchmarks

## Workflow

### Step 1: Define Unit Economics Model

**Business model identification:**

| Business Model | Unit Definition | Revenue Model |
|----------------|-----------------|---------------|
| 消费品 | 每单 / 每用户 | Transaction |
| SaaS | 每客户 (年) | Subscription |
| 电商 | 每订单 / 每用户 | Transaction |
| 制造业 | 每件 / 每吨 | Unit sales |
| 平台 | 每GMV / 每交易 | Take rate |
| 广告 | 每曝光 / 每点击 | CPM / CPC |

### Step 2: Build Unit Economics Model

**Standard model:**

```python
# Unit economics calculation
Unit_Price = XX元
Unit_Cost = XX元 (COGS)
Unit_Contribution = Unit_Price - Unit_Cost

# Customer economics (for subscription/DTC)
CAC = XX元 (acquisition cost per customer)
ARPU = XX元/年 (average revenue per user)
Gross_Margin = XX%
Customer_Lifetime = X年 (or 1/churn rate)
LTV = ARPU × Lifetime × Gross_Margin
LTV_CAC = LTV / CAC
Payback_Months = CAC / (ARPU × Gross_Margin / 12)
```

### Step 3: Cohort Analysis

**Cohort table (retention):**

| Cohort | Month 0 | Month 1 | Month 2 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|---------|---------|----------|
| Jan | 100% | XX% | XX% | XX% | XX% | XX% |
| Feb | 100% | XX% | XX% | XX% | XX% | XX% |
| Mar | 100% | XX% | XX% | XX% | XX% | XX% |

**Cohort revenue:**

| Cohort | Month 0 | Month 1 | Month 2 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|---------|---------|----------|
| Jan | ¥X | ¥X | ¥X | ¥X | ¥X | ¥X |
| Feb | ¥X | ¥X | ¥X | ¥X | ¥X | ¥X |

### Step 4: Benchmarking

**China-specific benchmarks by industry:**

| Industry | CAC Payback | LTV/CAC | Typical ARPU |
|----------|-------------|---------|--------------|
| 消费品牌 | 6-12 months | 3-5x | ¥200-500 |
| SaaS (ToB) | 12-18 months | 3-5x | ¥5,000-50,000 |
| 电商 | 1-3 months | 2-4x | ¥100-300 |
| 游戏 | 1-2 months | 4-10x | ¥50-200 |
| 在线教育 | 3-6 months | 2-4x | ¥1,000-5,000 |
| 金融科技 | 6-12 months | 3-5x | ¥500-2,000 |

### Step 5: Sensitivity Analysis

**Key sensitivities:**

| Variable | -20% | -10% | Base | +10% | +20% |
|----------|------|------|------|------|------|
| ARPU | | | | | |
| Gross margin | | | | | |
| Customer lifetime | | | | | |
| CAC | | | | | |

### Step 6: Recommendations

**Based on unit economics:**

| LTV/CAC | Assessment | Recommendation |
|---------|------------|---------------|
| >5x | Excellent | Scale aggressively |
| 3-5x | Good | Scale with monitoring |
| 2-3x | Acceptable | Optimize CAC/margin |
| 1-2x | Poor | Fix model before scaling |
| <1x | Broken | Fundamental rethink |

## China-Specific Considerations

### Customer Acquisition in China

| Channel | CAC | Quality | Notes |
|---------|-----|---------|-------|
| 线上投放 (Online ads) | Medium | Variable | 抖音, 小红书, 百度 |
| 社交裂变 (Social referral) | Low | Medium | 拼多多 model |
| 经销商 (Distribution) | Low | Depends | 渠道下沉 |
| 线下门店 (Offline stores) | High | High | Premium experience |
| 直播带货 (Livestream) | Medium | Variable | 抖音, 淘宝直播 |
| 私域运营 (Private traffic) | Low | High | WeChat ecosystem |

### China Consumer Behavior

| Behavior | Impact on Unit Economics |
|----------|-------------------------|
| 价格敏感 | Lower ARPU, higher churn on price increases |
| 社交驱动 | Viral referral reduces CAC |
| 品牌忠诚度 | Higher LTV for established brands |
| 渠道偏好 | Multi-channel complexity |
| 促销依赖 | Revenue quality concerns |

### E-commerce Unit Economics

**Key metrics for China e-commerce:**

| Metric | Formula | Benchmark |
|--------|---------|-----------|
| GMV | Gross merchandise value | Top-line |
| Take rate | Revenue / GMV | 3-10% |
| Customer acquisition | CAC / order | ¥20-200 |
| Return rate | Returns / orders | 5-20% (sector varies) |
| AOV | Revenue / orders | ¥50-500 |
| Fulfillment cost | Logistics / order | ¥5-30 |

## Quality Checks

Before delivering:
- [ ] Unit defined clearly
- [ ] Revenue model correct
- [ ] CAC/LTV calculated correctly
- [ ] Cohort data (if available) incorporated
- [ ] Benchmarking relevant
- [ ] Sensitivities run
- [ ] Recommendations actionable
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
