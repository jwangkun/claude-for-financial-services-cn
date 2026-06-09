---
name: china-returns-analysis
description: IRR and MOIC analysis for China-focused private equity and investment funds. Adapted from the original returns-analysis skill for RMB/USD fund structures, China market conventions, and Chinese portfolio companies. Triggers on "A股基金回报", "IRR分析", "returns China", "MOIC analysis China", "基金业绩分析", or "portfolio returns review".
---

# china-returns-analysis

## Purpose

Analyze and report on **中国私募基金回报表现** using IRR, MOIC, and related metrics.

## Key Metrics

### Core Metrics (Same as Global)

| Metric | Formula | Benchmark |
|--------|---------|-----------|
| IRR (Internal Rate of Return) | Discounted cash flow rate | 15-20%+ for top China PE |
| MOIC (Multiple on Invested Capital) | Total returned / Total invested | 2.0-3.0x typical |
| TVPI (Total Value to Paid-In) | (Distributed + NAV) / Paid-in | >2.0x target |
| DPI (Distributed to Paid-In) | Distributions / Paid-in | 0.5-1.0x early stage |
| RVPI (Residual Value to Paid-In) | NAV / Paid-in | >1.0x for active funds |

### China-Specific Metrics

| Metric | Description | Benchmark |
|--------|-------------|-----------|
| 人民币IRR | Returns in CNY | 12-18% for quality funds |
| 美元IRR | Returns in USD (hedged/unhedged) | 15-25% |
| 项目回报 | Per-investment IRR/MOIC | 20-30% IRR target |
| 基金回报 | Fund-level IRR | Top quartile: 20%+ |
| 现金回款 | Distributions received | Annual yield target |

## Data Sources (Multi-Tier)

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 - iFind (paid)
> When IFIND_AUTH_TOKEN is configured, iFind is the preferred data source.
> For equivalent iFind tools, see `china-market-data` skill.


### Primary Sources

| Data | Source | Notes |
|------|--------|-------|
| 基金估值报告 | Fund administrator | Monthly/quarterly NAV |
| 投资项目数据 | Portfolio company reports | Financials, valuations |
| 交易文件 | Investment agreements | Deal terms, waterfalls |
| 清科 / 投中 | Industry data | Benchmark comparisons |

### Secondary Sources
- 巨潮 — public portfolio company filings
- AkShare — market data for public holdings
- 交易所 — trading data

## Workflow

### Step 1: Fund-Level Summary

**Fund overview table:**

| Fund | Vintage | Size (亿) | Committed | Called | Distributed | NAV | TVPI | IRR |
|------|---------|-----------|-----------|--------|-------------|-----|------|-----|
| Fund I | 2018 | 30 | | | | | | |
| Fund II | 2021 | 50 | | | | | | |

### Step 2: Portfolio-Level Analysis

**By investment:**

| Investment | Date | Cost (亿) | Fair Value (亿) | MOIC | IRR | Status |
|-----------|------|-----------|----------------|------|-----|--------|
| | | | | | | Active / Exited / Written off |

### Step 3: Vintage Analysis

**Vintage year performance:**

| Vintage | IRR | MOIC | # Deals | # Exits | TVPI |
|---------|-----|------|---------|---------|------|
| | | | | | |

**Benchmark comparison:**
- vs 沪深300
- vs 中国PE/VC指数 (if available)
- vs peer fund performance

### Step 4: Sector Analysis

**Returns by sector:**

| Sector | Invested (亿) | Realized (亿) | NAV (亿) | MOIC | IRR |
|--------|--------------|--------------|----------|------|-----|
| 半导体 | | | | | |
| 新能源 | | | | | |
| 医药 | | | | | |
| 消费 | | | | | |

### Step 5: J-Curve Analysis

**Typical China PE J-curve:**
- Year 0-2: Negative DPI (capital called, no distributions)
- Year 3-5: DPI starts building
- Year 5-7: MOIC > 1.0x
- Year 7+: Strong distributions

### Step 6: Sensitivity Analysis

**Sensitivity on key assumptions:**

| Variable | -20% | -10% | Base | +10% | +20% |
|----------|------|------|------|------|------|
| Exit multiple | | | | | |
| EBITDA growth | | | | | |
| Time to exit | | | | | |

## China-Specific Considerations

### Fund Structures

| Structure | Description | Common Use |
|-----------|-------------|-------------|
| 人民币基金 (RMB fund) | Domestic currency | Onshore investments |
| 美元基金 (USD fund) | Offshore currency | Cross-border, tech |
| 双语基金 (Dual currency) | Both RMB and USD | Flexible allocation |
| 母基金 (Fund of funds) | FoF structure | Diversified access |

### Return Expectations

| Fund Type | IRR Target | MOIC Target | Hold Period |
|-----------|-----------|-------------|-------------|
| VC (种子/早期) | 30-40% | 5-10x | 5-8 years |
| Growth equity | 20-30% | 3-5x | 4-7 years |
| Buyout | 15-25% | 2-4x | 4-7 years |
| Distressed | 20-30% | 2-5x | 3-5 years |

### Exit Routes

| Route | Description | Typical Timeline | Multiple |
|-------|-------------|-----------------|----------|
| A股IPO | IPO on A-share market | 5-8 years from investment | 3-10x |
| 并购退出 | Trade sale to strategic | 3-6 years | 2-5x |
| 老股转让 | Secondary sale | 3-5 years | 1.5-3x |
| 借壳上市 | Reverse merger | 3-5 years | 2-6x |
| 回购 | Sponsor/management buyback | 5-8 years | 1.5-2.5x |
| 基金份额转让 | Fund secondary | Ongoing | 0.7-1.2x NAV |

### Benchmark Indices

| Index | Description |
|-------|-------------|
| 沪深300 | Broad A-share market |
| 中证1000 | Small-cap A-share |
| 中国PE/VC指数 | PE/VC performance index |
| 清科指数 | Zero2IPO index |
| 投中指数 | CVSource index |

## Quality Checks

Before delivering:
- [ ] All cash flows documented
- [ ] IRR/MOIC calculations verified
- [ ] Benchmark comparisons included
- [ ] Sector analysis complete
- [ ] Vintage analysis included
- [ ] J-curve position clear
- [ ] Sensitivities run
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
