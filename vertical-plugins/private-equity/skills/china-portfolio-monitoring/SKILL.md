---
name: china-portfolio-monitoring
description: Track and report on A-share portfolio company performance for China-focused private equity funds. Monitors KPIs, financials, and strategic milestones. Adapted from the original portfolio-monitoring skill for Chinese portfolio companies. Triggers on "A股投后管理", "基金投后监控", "portfolio monitoring China", "monitor portfolio company", "投后报告", or "portfolio company review".
---

# china-portfolio-monitoring

## Purpose

Monitor **A股及中国市场投资组合公司表现** — financial performance, operational KPIs, strategic milestones, and risk indicators.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_quote(ticker)                        → Stock performance
get_historical_data(ticker)              → Price trend
get_financials(ticker, "income")         → Revenue, profit
get_financials(ticker, "balance")        → Balance sheet health
get_financials(ticker, "cashflow")        → Cash generation
get_stock_info(ticker)                   → Company updates
```

### Secondary Sources
- 巨潮公告 — material announcements
- 业绩说明会 — management updates
- Wind / Choice — ownership, institutional data
- 券商研报 — analyst updates

## Workflow

### Step 1: Define KPIs by Company

**Financial KPIs (standard):**

| KPI | Frequency | Target / Benchmark |
|-----|-----------|-------------------|
| Revenue growth (YoY) | Quarterly | >XX% |
| Gross margin | Quarterly | >XX% |
| Net margin | Quarterly | >XX% |
| EBITDA | Quarterly | Growing |
| Net debt/EBITDA | Quarterly | <Xx |
| FCF | Quarterly | Positive |
| ROE | Quarterly / Annual | >XX% |

**Operational KPIs (company-specific):**

| Sector | Key KPIs |
|--------|---------|
| 白酒 | 批价, 动销, 渠道库存, 回款 |
| 半导体 | 产能利用率, 出货量, 良率 |
| 新能源 | 装机量, 产能利用率, 技术参数 |
| 医药 | 研发进度, 临床数据, 集采中标 |
| 消费 | 门店数量, 同店增速, 库存周转 |
| SaaS/科技 | ARR, 客户数, NRR, churn |

### Step 2: Financial Monitoring

**Quarterly review template:**

```
【投后监控】[Company] [Q20XX] 回顾

一、财务表现
   营业收入: [XX亿] (YoY: [X%]) [vs plan: +/-X%]
   毛利率: [XX%] (vs plan: +/-X bps)
   净利润: [XX亿] (YoY: [X%]) [vs plan: +/-X%]
   EBITDA: [XX亿] (Margin: [XX%])
   经营现金流: [XX亿]
   资本支出: [XX亿]
   自由现金流: [XX亿]

二、资产负债表
   现金余额: [XX亿]
   有息负债: [XX亿]
   净债务: [XX亿]
   净资产: [XX亿]
   商誉: [XX亿] (% of equity: [XX%])

三、估值跟踪
   Current price: [¥XX.XX]
   Market cap: [XX亿]
   PE (TTM): [Xx]
   vs Entry valuation: [Premium/Discount X%]
   vs Sector median: [Premium/Discount X%]

四、关键运营指标
   [Sector-specific KPIs with trends]

五、重大事项
   [Announcements, management changes, M&A, etc.]

六、风险预警
   [Risk flags, concerns]

七、下一步
   [Actions, meetings, reviews]
```

### Step 3: Strategic Milestones

**Milestone tracking:**

| Milestone | Target Date | Status | Notes |
|-----------|-------------|--------|-------|
| e.g., New product launch | Q2 2025 | On track | |
| e.g., Capacity expansion | Q3 2025 | Delayed | 1 quarter |
| e.g., Management hire | Q1 2025 | Complete | |
| e.g., IPO filing | Q4 2025 | In progress | |

### Step 4: Value Creation Tracking

**Value creation levers:**

| Lever | Status | Impact |
|-------|--------|--------|
| Revenue growth acceleration | | |
| Margin expansion | | |
| M&A consolidation | | |
| International expansion | | |
| Digital transformation | | |
| Management upgrade | | |

### Step 5: Risk Monitoring

**Red flag indicators:**

| Risk | Indicator | Threshold | Action |
|------|-----------|-----------|--------|
| 经营现金流 | Operating CF | Consecutive quarters negative | Escalate |
| 毛利率 | Gross margin | Decline >500 bps | Review |
| 有息负债 | Net debt/EBITDA | >4.0x | Review |
| 应收账款 | AR days | >120 days | Review |
| 存货 | Inventory days | >90 days | Review |
| 股价 | Share price | -30% from entry | Review |
| 解禁 | Lock-up expiry | <3 months | Monitor |
| 质押 | Pledge ratio | >50% | Flag |

### Step 6: Reporting

**Monthly / Quarterly report structure:**

```
【投后月度/季度报告】[Company]

一、期间概要
   [Executive summary of period]

二、财务更新
   [Financial KPI table with trends]

三、运营更新
   [Operational KPIs, milestones]

四、估值更新
   [Current valuation, mark-to-market]

五、风险与问题
   [Risk flags, mitigation status]

六、下一步行动
   [Board meeting, management call, DD items]
```

## China-Specific Monitoring Considerations

### Market Context

| Factor | Monitoring Implication |
|--------|----------------------|
| 涨跌停 | Price movement constraints |
| 北向资金 | Foreign flow trends |
| 龙虎榜 | Unusual trading activity |
| 政策变化 | Regulatory impact on business |
| 行业景气 | Sector cyclical position |

### Common Issues in A-share Portfolio Companies

| Issue | Warning Signs | Response |
|-------|--------------|----------|
| 商誉减值 | Goodwill >30% of equity | Impairment testing |
| 应收账款积压 | AR growth > revenue growth | Collections push |
| 存货积压 | Inventory days rising | Discounting, write-downs |
| 经营现金流差 | CF < Net income repeatedly | Working capital review |
| 大股东质押 | Pledge ratio rising | Engagement, covenant |
| 关联交易 | Related party revenue high | Monitor for leakage |
| 退市风险 | *ST designation, losses | Exit planning |

### Value Creation Levers (China-specific)

| Lever | Description | Typical Impact |
|-------|-------------|----------------|
| 精益管理 | Operational efficiency | 10-20% margin improvement |
| 渠道优化 | Distribution optimization | 15-30% revenue uplift |
| 数字化转型 | Digital transformation | 20-40% efficiency gain |
| 并购整合 | Add-on acquisitions | 20-50% value creation |
| 国际化 | Overseas expansion | New growth vectors |
| 股权激励 | ESOP implementation | Management alignment |
| 品牌建设 | Brand investment | Pricing power |

## Quality Checks

Before delivering report:
- [ ] All financial data sourced and current
- [ ] KPIs tracked against targets
- [ ] Milestones updated
- [ ] Valuation current
- [ ] Risk flags addressed
- [ ] Action items clear
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
