---
name: china-comps-analysis
description: Comparable company analysis for A-share equities. Adapts the original comps-analysis skill for Chinese market data sources, A-share trading multiples, and domestic peer selection. Triggers on "A股可比公司", "可比分析", "comps China", "peer comparison A-share", "可比公司分析", or "trading comps [industry]".
---

# china-comps-analysis

## Purpose

Build **A股可比公司分析** — peer group multiples comparison adapted for the Chinese equity market.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_quote(ticker)                        → Current multiples (PE, PB, PS)
get_financials(ticker, "income")         → Revenue, net income for calculations
get_financials(ticker, "balance")        → Book value, debt
get_industry_stocks(industry="白酒")       → Industry peers
```

### Secondary Sources
- 东方财富 — industry classifications
- 巨潮 — financial statements
- Wind / Choice — comprehensive multiples
- 券商研报 — peer analysis

## Workflow

### Step 1: Select Peer Group

**Peer selection criteria:**

| Criterion | China Context |
|-----------|---------------|
| Industry | Same 东方财富 industry category |
| Market cap | ±3x of subject company |
| Revenue | ±2x of subject company |
| Growth | Similar revenue growth profile |
| Profitability | Comparable margins |
| Business model | Same/related business model |
| Geography | China-focused (A-share only) |
| Listing status | All A-share (include 北交所 if relevant) |

**Typical peer count:** 8-15 companies

### Step 2: Collect Financial Data

**Data to collect for each peer:**

| Data Item | Source | Notes |
|-----------|--------|-------|
| Current price | AkShare | |
| Market cap | Calculated | Shares outstanding × price |
| Revenue (LTM) | AkShare financials | |
| Net income (LTM) | AkShare financials | |
| EPS ( diluted ) | AkShare | |
| Book value | Balance sheet | |
| EBITDA | Calculate | Net income + tax + interest + D&A |
| EV | Calculate | Market cap + net debt |

### Step 3: Calculate Trading Multiples

**Standard multiples:**

| Multiple | Formula | Typical Range (A-share) |
|----------|---------|------------------------|
| P/E (动态) | Price / 预测EPS | 10-50x |
| P/E (TTM) | Price / TTM EPS | 10-50x |
| P/E (静态) | Price / 上年EPS | 10-50x |
| PB | Price / 每股净资产 | 1-10x |
| PS | EV / Revenue | 1-10x |
| EV/EBITDA | EV / EBITDA | 5-20x |
| PEG | P/E / Growth | 0.5-2.0 |
| 股息率 | Dividend / Price | 0-5% |
| ROE | Net income / Equity | 5-30% |

**Multiples calculation notes:**
- P/E: use 归母净利润 (net income attributable to parent)
- PB: use 归属于母公司股东权益
- EBITDA: approximate as 营业利润 + 折旧摊销 (if D&A not separately stated)

### Step 4: Peer Comparison Table

**Standard comps table:**

| Company | Ticker | Market Cap (亿) | P/E (TTM) | P/B | P/S | EV/EBITDA | Revenue Growth | Net Margin | ROE |
|---------|--------|----------------|-----------|-----|-----|-----------|---------------|------------|-----|
| Subject | | | X.Xx | X.X | X.X | X.X | X% | X% | X% |
| Peer 1 | | | X.Xx | X.X | X.X | X.X | X% | X% | X% |
| Peer 2 | | | X.Xx | X.X | X.X | X.X | X% | X% | X% |
| Peer 3 | | | X.Xx | X.X | X.X | X.X | X% | X% | X% |
| ... | | | | | | | | | |
| Median | | | X.Xx | X.X | X.X | X.X | X% | X% | X% |
| Mean | | | X.Xx | X.X | X.X | X.X | X% | X% | X% |

### Step 5: Identify Outliers

**Outlier analysis:**

| Company | P/E | vs Median | Reason for Premium/Discount |
|---------|-----|-----------|----------------------------|
| | | ±X% | Growth, margin, quality, sentiment |

**Common reasons for A-share premium/discount:**
- 增速 (Growth rate)
- 盈利能力 (Profitability / ROE)
- 行业地位 (Market position)
- 技术壁垒 (Technology moat)
- 管理层质量 (Management quality)
- 流动性 (Liquidity — 北向资金持仓)
- 概念/题材 (Theme / concept premium)
- 治理结构 (Corporate governance)

### Step 6: Valuation Range

**Derive valuation range:**

| Method | Low | Mid | High | Rationale |
|--------|-----|-----|------|-----------|
| P/E | Xx | Xx | Xx | Based on peer range |
| P/B | Xx | Xx | Xx | Based on peer range |
| P/S | Xx | Xx | Xx | Based on peer range |
| EV/EBITDA | Xx | Xx | Xx | Based on peer range |

**Implied price range:**
- Low: ¥XX (using low multiples + conservative assumptions)
- Mid: ¥XX (using median multiples)
- High: ¥XX (using high multiples + optimistic assumptions)

### Step 7: Relative Valuation Conclusion

**Valuation summary:**

```
可比公司估值结论

当前股价: ¥XX
目标价区间: ¥XX - ¥XX
当前估值水平: [Premium/Discount] vs  peers

关键结论:
1. 相对估值: 较同业 [低/中/高]
2. 主要驱动: [Growth / Margin / Quality]
3. 估值折价/溢价原因: [Explanation]

投资建议: [Buy / Hold / Sell]
```

## China-Specific Considerations

### A-share Multiples Quirks

| Issue | Impact | Mitigation |
|-------|--------|-----------|
| 盈利波动大 | TTM earnings volatile | Use 3Y average |
| 一次性损益 | Distorts P/E | Use 扣非净利润 for P/E |
| 亏损公司 | Negative P/E meaningless | Use P/S or EV/EBITDA |
| 新股次新股 | Limited history | Use 静态市盈率 cautiously |
| ST股票 | Distressed | Exclude from peer set |

### Chinese Market Premiums

| Factor | Typical Premium |
|--------|----------------|
| 消费龙头 (Consumer leader) | +20-50% |
| 科技/创新 (Tech/innovation) | +30-100% |
| 医药 (Pharma) | +15-40% |
| 国企 (SOE) | -10 to -30% |
| 高股息 (High dividend) | -5 to +10% |
| 北向资金重仓 | +5-20% |

### 东方财富 Industry Categories

**Common categories for peer selection:**
- 白酒, 啤酒 — Beverages
- 半导体, 芯片 — Semiconductors
- 银行, 证券, 保险 — Financial services
- 创新药, 医疗器械 — Healthcare
- 光伏设备, 锂电池 — New energy
- 汽车整车, 汽车零部件 — Auto
- 软件开发, IT服务 — Software/IT
- 房地产, 建材 — Real estate / Materials

## Quality Checks

Before delivering:
- [ ] Peer group appropriate (similar size, growth, business model)
- [ ] All data sourced from AkShare or 巨潮
- [ ] Multiples calculated correctly
- [ ] Outliers explained
- [ ] Valuation conclusion supported
- [ ] Current price verified
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
