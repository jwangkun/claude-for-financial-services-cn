---
name: china-variance-commentary
description: Write variance commentary for A-share financial results. Adapts the original variance-commentary skill for Chinese financial statements, CAS conventions, and Chinese business terminology. Triggers on "A股业绩点评", "财报点评", "variance commentary China", "业绩分析", "variances [company]", or "commentary on [company] results".
---

# china-variance-commentary

## Purpose

Write professional **A股业绩点评** — structured variance commentary on Chinese company financial results.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "income")     → Revenue, profit data
get_financials(ticker, "balance")    → Balance sheet data
get_quote(ticker)                    → Market context
```

### Secondary Sources
- 巨潮 — earnings releases
- 券商研报 — consensus estimates
- 慧博 / 同花顺 — 一致预期

## Workflow

### Step 1: Gather Actuals and Estimates

**Data collection:**

| Metric | Actual (Actuals) | Consensus (一致预期) | Prior | YoY | QoQ |
|--------|-----------------|---------------------|-------|-----|-----|
| 营业收入 | | | | | |
| 毛利率 | | | | | |
| 归母净利润 | | | | | |
| 扣非净利润 | | | | | |
| EPS | | | | | |
| 经营现金流 | | | | | |

### Step 2: Variance Analysis

**Variance table:**

| Metric | Actual | Consensus | Variance | % vs Cons | % vs Prior | Impact |
|--------|--------|-----------|----------|-----------|------------|--------|
| 营业收入 | | | | | | |
| 毛利率 | | | | | | |
| 归母净利润 | | | | | | |
| 扣非净利润 | | | | | | |
| EPS | | | | | | |
| ROE | | | | | | |

**Variance classification:**

| Variance | Classification | Commentary |
|----------|---------------|------------|
| Revenue +5% vs cons | Slight beat | |
| Revenue +15% vs cons | Strong beat | |
| Revenue -5% vs cons | Slight miss | |
| Revenue -15% vs cons | Significant miss | |

### Step 3: Driver Analysis

**Key drivers decomposition:**

**Revenue drivers:**
```
收入变动 = 量增 + 价增 + 产品结构 + 收购/处置

分解:
1. 销量变化: +X% (驱动因素)
2. 价格变化: +X% (提价/促销)
3. 产品组合: +X% (高毛利产品占比提升)
4. 其他: +X% (并表/汇率)
```

**Margin drivers:**
```
毛利率变动 = 原材料成本 + 人工成本 + 制造费用 + 产品结构

分解:
1. 原材料: -X ppts (价格上涨/下降)
2. 人工: +X ppts (效率提升/人工成本上涨)
3. 制造费用: +X ppts (产能利用率)
4. 产品结构: +X ppts (高毛利产品占比)
5. 其他: X ppts
```

**Net profit bridge:**

```
归母净利润变动
├── 营业收入影响: +¥XX万
├── 毛利率影响: +¥XX万
├── 费用率影响: +¥XX万
│   ├── 销售费用: -¥XX万
│   ├── 管理费用: +¥XX万
│   └── 研发费用: +¥XX万
├── 其他收益影响: +¥XX万
├── 投资收益影响: +¥XX万
├── 减值损失影响: -¥XX万
├── 营业外收支影响: +¥XX万
├── 所得税影响: -¥XX万
└── 归母净利润变动: +¥XX万
```

### Step 4: Segment Commentary

**By segment:**

| Segment | Revenue | Growth | Margin | Comment |
|---------|---------|--------|--------|---------|
| | | | | |

**By geography:**

| Region | Revenue | Growth | Comment |
|--------|---------|--------|---------|
| 国内 | | | |
| 海外 | | | |

### Step 5: Balance Sheet Commentary

**Key BS changes:**

| Item | Change | Driver | Impact |
|------|--------|--------|--------|
| 货币资金 | | | |
| 应收账款 | | | |
| 存货 | | | |
| 商誉 | | | |
| 有息负债 | | | |

### Step 6: Cash Flow Commentary

**Cash flow analysis:**

| Item | Amount | Change | Comment |
|------|--------|--------|---------|
| 经营活动现金流 | | | |
| 投资活动现金流 | | | |
| 筹资活动现金流 | | | |
| 现金净增加额 | | | |

**Key observations:**
- OCF vs Net income comparison
- CapEx intensity
- Dividend payment
- Debt activity

### Step 7: Forward-Looking Commentary

**Guidance and outlook:**

| Area | Commentary |
|------|-----------|
| 收入指引 | Management guidance |
| 利润指引 | Earnings outlook |
| 投资计划 | CapEx plans |
| 战略方向 | Strategic initiatives |

### Step 8: Write the Commentary

**Standard format (业绩点评):**

```
【业绩点评】[Company] [Period] [Beat/Miss/In-line]

核心结论:
- 营收XX亿, 同比+/-X%, 超/低于预期X%
- 归母净利润XX亿, 同比+/-X%, 超/低于预期X%
- 扣非净利润XX亿, 同比+/-X%

要点:
1. [Key driver 1]
2. [Key driver 2]
3. [Key driver 3]

详细分析:

一、营业收入
   [Revenue commentary with drivers]

二、盈利能力
   [Margin analysis]

三、费用分析
   [Expense commentary]

四、资产负债表
   [Key BS changes]

五、现金流量
   [CF commentary]

六、展望
   [Forward-looking]

风险提示:
- [Key risks]

风险提示: 本内容仅供研究参考, 不构成投资建议。
```

## China-Specific Commentary Considerations

### Key Metrics to Highlight

| Metric | Why Important |
|--------|---------------|
| 归母净利润 | Standard metric for A-share investors |
| 扣非净利润 | Shows core business quality |
| 经营现金流 | Cash generation quality |
| 毛利率/净利率 | Profitability trends |
| ROE | Return on equity benchmark |
| 资产负债率 | Leverage concern |

### Common Earnings Themes

| Pattern | Typical Commentary |
|---------|-------------------|
| 收入增, 利润降 | Margin compression |
| 利润增, 现金流降 | Earnings quality concern |
| 高政府补助 | Sustainability question |
| 大额减值 | Asset quality |
| 关联交易高 | Revenue quality |
| 合同负债大增 | Future revenue visibility |

### Language Conventions

| English | Chinese |
|---------|---------|
| Beat estimates | 超预期 |
| Miss estimates | 低于预期 |
| In-line | 符合预期 |
| Year-over-year | 同比 |
| Quarter-over-quarter | 环比 |
| Adjusted | 调整后 |
| Recurring | 经常性 |
| One-time | 一次性 |
| Core | 核心 / 扣非 |

## Quality Checks

Before delivering:
- [ ] All actuals verified from source
- [ ] Consensus figures cited
- [ ] Variances calculated correctly
- [ ] Drivers identified and explained
- [ ] Balance sheet / CF covered
- [ ] Forward outlook included
- [ ] Risks highlighted
- [ ] Chinese terminology correct
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
