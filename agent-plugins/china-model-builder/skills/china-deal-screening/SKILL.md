---
name: china-deal-screening
description: Screen and evaluate A-share investment opportunities. Adapts the original deal-screening skill for Chinese market data sources, A-share screening criteria, and domestic deal origination. Triggers on "A股标的筛选", "标的筛选", "screening China", "deal screening A-share", "筛选投资标的", or "screen for [criteria]".
---

# china-deal-screening

## Purpose

Screen **A股投资标的** — systematic deal screening for Chinese equity investments.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_industry_stocks(industry="...")    → Industry universe
get_quote(ticker)                     → Valuation screening
get_financials(ticker, "income")      → Financial screening
get_index_data("000001")              → Market context
```

### Secondary Sources
- 东方财富 — stock screener
- 同花顺 iFinD — screening tool
- 巨潮 — company filings
- Wind — professional screening

## Workflow

### Step 1: Define Screening Criteria

**Screening framework:**

| Category | Criteria | Typical Range |
|----------|----------|---------------|
| 市值 (Market cap) | Min/max | ¥50亿 - ¥500亿 |
| 估值 (Valuation) | P/E, P/B | P/E 10-30x |
| 成长 (Growth) | Revenue/earnings growth | >15% YoY |
| 盈利 (Profitability) | ROE, margins | ROE >15% |
| 财务健康 (Financial health) | Debt/equity, current ratio | D/E <60% |
| 流动性 (Liquidity) | Avg daily volume | >¥5000万 |
| 治理 (Governance) | Ownership structure | Clean cap table |

### Step 2: Build Screening Universe

**Universe construction:**

| Filter | Criteria | Source |
|--------|----------|--------|
| A股主板 | 600/000/001开头的6位代码 | AkShare |
| 创业板 | 300开头 | AkShare |
| 科创板 | 688开头 | AkShare |
| 北交所 | 8/9开头 | AkShare |
| ST排除 | Exclude ST/*ST | Filter |
| 次新股 | Exclude <6 months | Filter |

### Step 3: Financial Screening

**Financial metrics:**

| Metric | Formula | Target |
|--------|---------|--------|
| 营业收入增速 | (Revenue - Revenue_prev) / Revenue_prev | >15% |
| 净利润增速 | (NI - NI_prev) / NI_prev | >15% |
| ROE | Net Income / Average Equity | >15% |
| 毛利率 | Gross Profit / Revenue | >30% |
| 净利率 | Net Income / Revenue | >10% |
| 资产负债率 | Total Debt / Total Assets | <60% |
| 经营现金流/净利润 | OCF / Net Income | >0.8 |

### Step 4: Valuation Screening

**Valuation metrics:**

| Metric | Formula | Target |
|--------|---------|--------|
| P/E (TTM) | Price / TTM EPS | 10-30x |
| P/B | Price / BV per share | 1-5x |
| P/S | EV / Revenue | 1-5x |
| EV/EBITDA | EV / EBITDA | 5-15x |
| PEG | P/E / Growth rate | <1.0 |
| 股息率 | Dividend / Price | >2% (if applicable) |

### Step 5: Technical Screening (Optional)

**Technical filters:**

| Indicator | Criteria |
|-----------|----------|
| 股价位置 | Not at 52-week high |
| 均线 | Above key MAs |
| 成交量 | Above average |
| 波动率 | Moderate |

### Step 6: Quality Screening

**Quality filters:**

| Factor | Check |
|--------|-------|
| 审计意见 | Standard unqualified (标准无保留) |
| 管理层 | Stable, experienced |
| 股东结构 | No 质押风险 (pledge risk) |
| 关联交易 | Reasonable level |
| 诉讼/处罚 | No material issues |

### Step 7: Scoring & Ranking

**Scoring model:**

| Category | Weight | Score (1-10) | Weighted |
|----------|--------|-------------|----------|
| 估值吸引力 | 25% | | |
| 成长性 | 20% | | |
| 盈利能力 | 20% | | |


| 财务健康 | 15% | | |
| 质量/治理 | 10% | | |
| 流动性 | 10% | | |
| **Total** | **100%** | | |

**Rank candidates by total score.**

### Step 8: Due Diligence Queue

**Create DD pipeline:**

| Rank | Company | Ticker | Score | Sector | Next Step |
|------|---------|--------|-------|--------|-----------|
| 1 | | | X.X | | Full DD |
| 2 | | | X.X | | Quick scan |
| 3 | | | X.X | | Quick scan |

## Screening Templates

### Template 1: Growth at Reasonable Price (GARP)

| Filter | Criteria |
|--------|----------|
| P/E | 10-25x |
| Revenue growth | >20% |
| ROE | >15% |
| D/E | <50% |
| Market cap | >¥100亿 |

### Template 2: Deep Value

| Filter | Criteria |
|--------|----------|
| P/B | <1.5x |
| Dividend yield | >3% |
| D/E | <40% |
| FCF | Positive |
| Business | Stable, understandable |

### Template 3: Quality Compounder

| Filter | Criteria |
|--------|----------|
| ROE | >20% (3Y avg) |
| Revenue growth | >15% |
| Gross margin | >40% |
| D/E | <40% |
| Market cap | >¥200亿 |

### Template 4: Turnaround Candidate

| Filter | Criteria |
|--------|----------|
| Recent loss | 1-2 years |
| Revenue trough | Near bottom |
| New management | Recent change |
| Restructuring | In progress |
| Industry recovery | Improving |

## China-Specific Screening Considerations

### Market Structure

| Factor | Impact on Screening |
|--------|---------------------|
| 散户主导 | Retail sentiment matters |
| 政策驱动 | Policy changes create opportunities |
| 概念/题材 | Theme investing common |
| 北向资金 | Foreign flows signal quality |
| 机构持仓 | Institutional ownership |

### Common A-share Screening Pitfalls

| Pitfall | Issue | Mitigation |
|---------|-------|-----------|
| 一次性收益 | Distorts growth/earnings | Use 扣非数据 |
| 会计政策 | Aggressive recognition | Check notes |
| 关联交易 | Inflated revenue | Review disclosures |
| 大股东质押 | Pledge risk | Check 质押比例 |
| ST风险 | Delisting risk | Exclude ST stocks |

## Quality Checks

Before finalizing:
- [ ] Criteria well-defined
- [ ] Universe appropriate
- [ ] Data quality verified
- [ ] Scoring model calibrated
- [ ] Top candidates make sense
- [ ] Next steps clear
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
