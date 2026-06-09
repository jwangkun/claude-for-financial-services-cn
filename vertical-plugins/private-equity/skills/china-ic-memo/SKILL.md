---
name: china-ic-memo
description: Investment Committee memo drafting for China-focused PE/IB deals. Adapted from the original ic-memo skill for Chinese market context, terminology, and decision frameworks. Triggers on "A股投委会", "IC Memo", "investment memo China", "投委会材料", "IC memo A-share", or "committee memo [company]".
---

# china-ic-memo

## Purpose

Draft **A股投资委员会备忘录 (IC Memo)** — structured decision documents for investment committee reviews.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_quote(ticker)                        → Valuation context
get_financials(ticker, "income")         → Financials
get_industry_stocks(industry="...")       → Peer comparables
```

### Secondary Sources
- 巨潮 — company filings
- Wind / Choice — comprehensive data
- 券商研报 — existing research
- 尽调报告 — DD findings

## Workflow

### Step 1: Structure the Memo

**Standard A-share IC memo format:**

```
【机密】投资委员会备忘录

项目名称：[Target Company]
交易类型：[Investment type: 股权投资 / 并购 / 老股转让]
推荐团队：[Team name]
日期：[Date]

═══════════════════════════════════════════

一、投资建议 (Recommendation)
   [One-paragraph summary]
   建议：[批准 / 有条件批准 / 否决]
   投资金额：[XX亿]
   目标股权：[XX%]
   目标价格：[¥XX / EV XX亿]

二、交易概述 (Transaction Overview)
   - 标的公司：[Name], [Industry], [Listing status]
   - 交易结构：[Structure description]
   - 预计交割：[Date]
   - 投资回报预期：[Xx% IRR, Xx MOIC]

三、投资逻辑 (Investment Thesis)
   [3-5 bullet points]
   1. [Key driver 1]
   2. [Key driver 2]
   3. [Key driver 3]

四、市场与行业分析 (Market & Industry)
   - 市场规模：[XX亿], 增速 [X%]
   - 竞争格局：[Description]
   - 政策环境：[Policy context]
   - 趋势判断：[Secular trends]

五、目标公司分析 (Target Analysis)
   - 商业模式：[Description]
   - 竞争优势：[Bullets]
   - 管理团队：[Assessment]
   - 财务表现：[Summary]

六、估值分析 (Valuation)
   - 交易估值：[XX亿 / Xx PE]
   - 可比交易：[Comparable M&A]
   - DCF估值：[XX亿]
   - 估值区间：[XX-XX亿]
   - Upside/Downside：[X% / X%]

七、风险因素 (Risk Factors)
   - [Risk 1]: [Mitigation]
   - [Risk 2]: [Mitigation]
   - [Risk 3]: [Mitigation]

八、交易结构 (Transaction Structure)
   - 投资金额：[XX亿]
   - 股权比例：[XX%]
   - 董事会席位：[X席]
   - 业绩承诺：[如有]
   - 反稀释条款：[Description]
   - 退出安排：[IPO / 并购 / 回购]

九、退出策略 (Exit Strategy)
   - 主要路径：[A股IPO / 并购 / 老股转让]
   - 预计时间：[3-5年]
   - 目标回报：[Xx IRR]
   - 备选方案：[Alternative exits]

十、结论与建议 (Conclusion)
   [Summary and committee ask]
   需要委员会决策的事项：
   1. [Decision item 1]
   2. [Decision item 2]
```

### Step 2: Key Sections Detail

#### Investment Thesis

**Thesis quality check:**
- Is it specific (not generic)?
- Are the 2-3 key drivers clear?
- Is there a clear "why now"?
- Is the return potential quantified?

#### Valuation

**China-specific valuation considerations:**
- A-share premium context
- Comparable transactions (precedent deals)
- Control premium (20-40% typical)
- Liquidity discount for restricted shares
- DCF with China-specific assumptions

#### Risk Factors

**Standard A-share IC risk framework:**

| Risk Category | Specific Risks |
|--------------|---------------|
| 市场风险 | A-share volatility, 涨跌停, retail sentiment |
| 政策风险 | Regulatory changes, 行业政策 |
| 公司治理 | 关联交易, 股东质押, 同业竞争 |
| 行业风险 | 产能过剩, 技术迭代, 竞争恶化 |
| 流动性风险 | 解禁压力, 交易量不足 |
| 退出风险 | IPO窗口, 并购买家兴趣 |
| 汇率风险 | For USD-denominated funds |

#### Exit Strategy

**A-share exit analysis:**

| Route | Timeline | Probability | Expected Multiple |
|-------|----------|-------------|-------------------|
| A股IPO | 3-5 years | Medium | 3-8x |
| 并购退出 | 2-4 years | High | 2-4x |
| 老股转让 | 2-4 years | Medium | 1.5-3x |
| S基金 | 1-3 years | Low-Medium | 0.8-1.5x NAV |

### Step 3: Decision Framework

**Investment committee decision criteria:**

| Criterion | Weight | Assessment |
|-----------|--------|------------|
| 投资逻辑清晰度 | 20% | Strong / Adequate / Weak |
| 团队质量 | 20% | Strong / Adequate / Weak |
| 市场吸引力 | 15% | Large / Medium / Small |
| 竞争壁垒 | 15% | High / Medium / Low |
| 财务表现 | 15% | Strong / Adequate / Weak |
| 估值合理性 | 10% | Cheap / Fair / Expensive |
| 风险可控性 | 5% | Low / Medium / High |

**Overall recommendation:**
- 强烈推荐 (Strong recommend): >80% criteria met
- 推荐 (Recommend): 60-80% met
- 有条件推荐 (Conditional): 40-60% met, conditions clear
- 不推荐 (Not recommend): <40% met or red flags

### Step 4: Conditions & Follow-up

**If conditional approval:**

| Condition | Owner | Deadline |
|-----------|-------|----------|
| e.g., 管理层尽调确认 | [Name] | [Date] |
| e.g., 估值上限确认 | [Name] | [Date] |
| e.g., 监管可行性确认 | [Name] | [Date] |

## China-Specific Considerations

### Decision-Making Context

| Factor | China Context |
|--------|--------------|
| Decision speed | Can be faster or slower depending on SOE vs private |
| Approval layers | Multiple for large deals (>1亿 threshold) |
| Policy alignment | 产业政策 alignment important |
| Relationship | 关系 (guanxi) influences deal flow and terms |
| Documentation | Detailed Chinese documentation required |

### Common IC Discussion Points

- 退出确定性 (Exit certainty)
- 估值谈判空间 (Negotiation room)
- 业绩对赌可行性 (Earnout practicality)
- 董事会席位 (Board representation)
- 反稀释保护 (Anti-dilution)
- 优先清算权 (Liquidation preference)
- 监管审批风险 (Regulatory risk)

### Red Flags for IC

| Red Flag | Typical IC Reaction |
|----------|-------------------|
| 实际控制人不明 | Require ownership clarification |
| 关联交易占比高 | Require ring-fencing |
| 大额质押 | Require investigation |
| 持续经营能力质疑 | Require CF projections review |
| 估值显著高于同行 | Require premium justification |
| 退出路径不清晰 | Require exit analysis |
| 管理层不稳定 | Require retention analysis |

## Quality Checks

Before presenting:
- [ ] Memo structure complete
- [ ] Investment thesis compelling
- [ ] Valuation analysis thorough
- [ ] Risks comprehensively identified
- [ ] Mitigations documented
- [ ] Exit strategy clear
- [ ] Conditions specific and measurable
- [ ] Recommendation supported by analysis
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
