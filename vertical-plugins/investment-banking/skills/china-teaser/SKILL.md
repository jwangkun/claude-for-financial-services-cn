---
name: china-teaser
description: Draft anonymous one-page company teasers for A-share sell-side M&A processes. Creates compelling blind profiles without revealing the company's identity, adapted for Chinese market conventions. Triggers on "A股Teaser", "盲审材料", "blind profile China", "anonymous teaser A-share", or "sell-side teaser".
---

# china-teaser

## Purpose

Draft **A股并购盲审Teaser /  teaser** for sell-side M&A processes — anonymous one-page profiles designed to gauge buyer interest before NDA execution.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
# Anonymized financial metrics
get_industry_stocks(industry="...")     → Industry context, peer benchmarks
get_quote(ticker)                       → Valuation ranges (anonymized)
get_financials(ticker, "income")        → Revenue, margins (anonymized)
```

### Secondary Sources
- 巨潮 — target company filings (anonymized data extraction)
- Wind / Choice — industry benchmarks
- 券商研报 — sector overviews for context

## Workflow

### Step 1: Anonymize Target Information

**Strip identifying information:**
- Company name → "Leading [Industry] Player"
- Ticker → "[Listing Board] -listed Company"
- Exact location → "Headquartered in [Region]"
- Specific products → Product categories only
- Customer names → "Major domestic/international clients"
- Management names → Titles only

**Preserve:**
- Industry/sector
- Revenue scale (ranges)
- Margin profile
- Growth trajectory
- Market position (leader/challenger)
- Geographic footprint (regions, not cities)
- Deal rationale

### Step 2: Structure the Teaser

**Standard A-share teaser format:**

```
[CONFIDENTIAL — FOR DISCUSSION PURPOSES ONLY]

[ANONYMOUS TARGET]
[Industry Category] | [Listing Board] | [Region]

═══════════════════════════════════════════

INVESTMENT HIGHLIGHTS

• Leading position in [industry] with ~[X%] market share
• Revenue of ~[XX]亿 RMB with [XX%] YoY growth
• [Gross/Operating] margin of [XX%], above sector average
• Strong [competitive advantage: brand/technology/distribution]
• Established [customer base / channel network / R&D platform]
• Attractive valuation at [X]x EV/EBITDA vs peers at [Y]x

═══════════════════════════════════════════

COMPANY OVERVIEW

Business: [Description without names]
Founded: [Year]
Headquarters: [Region]
Employees: ~[XXX]
Listing: [Board] since [Year]

Core Business:
• [Segment 1]: [XX%] of revenue
• [Segment 2]: [XX%] of revenue
• [Segment 3]: [XX%] of revenue

═══════════════════════════════════════════

MARKET POSITION

• #X player in China [industry] market (~[XX]亿 RMB TAM)
• Strong presence in [region/segment]
• Key competitive advantages: [bullet points]
• [XX%] market share in core segment

═══════════════════════════════════════════

FINANCIAL SNAPSHOT

(RMB 亿元)

                   2022    2023    2024E
Revenue            XX      XX      XX
YoY Growth         XX%     XX%     XX%
Gross Profit       XX      XX      XX
Gross Margin       XX%     XX%     XX%
EBITDA             XX      XX      XX
EBITDA Margin      XX%     XX%     XX%
Net Income         XX      XX      XX
Net Margin         XX%     XX%     XX%

═══════════════════════════════════════════

TRANSACTION RATIONALE

• Industry consolidation opportunity — top [X] players control [XX%]
• Synergies: [cost savings / revenue enhancement]
• Attractive valuation vs transaction comps
• Strong [cash flow / growth] supporting leverage capacity

═══════════════════════════════════════════

CONFIDENTIALITY
This teaser is prepared solely for discussion purposes and is subject to a
Non-Disclosure Agreement. All information is provided on a confidential basis
and may not be reproduced or distributed without prior written consent.

[Advisor Name] | [Date]
```

### Step 3: Financial Anonymization

**Ranges to use:**

| Actual | Display As |
|--------|-----------|
| 15.2亿 | ~15亿 |
| 23.7亿 | ~20-25亿 |
| 156.3亿 | ~150亿 |
| 0.98% | ~1% |
| 15.23% | ~15% |

**Multiple rounding:**
- 8.3x → ~8x
- 12.7x → ~12-13x
- 23.45x → ~23x

### Step 4: Design

**Layout:**
- Single page (A4 or letter)
- Clean, professional design
- Firm branding (logo, colors)
- No company-specific imagery
- Generic industry imagery acceptable

**Visual elements:**
- Company logo: Anonymous icon or generic placeholder
- Charts: Revenue growth, margin trends (anonymized)
- Market share: Industry context without naming

### Step 5: Distribution Protocol

**Distribution rules:**
1. Only to qualified, vetted buyers
2. Under mutual NDA
3. Version control (track who received which version)
4. No forwarding without approval
5. Digital: PDF with disabled printing/editing preferred

## China-Specific Considerations

### A-share Market Context

| Feature | Teaser Consideration |
|---------|----------------------|
| 涨跌停限制 | Mention as market characteristic |
| 散户投资者 | Note retail participation level |
| 政策驱动 | Highlight policy tailwinds/risks |
| 北向资金 | Foreign ownership trend |
| 外资准入 | Foreign investment restrictions if applicable |

### Anonymization Best Practices

**Do NOT include:**
- Exact company name or ticker
- Specific city names (use region: 华东, 华南, 华北)
- Customer/supplier names
- Specific product brand names
- Management names
- Exact address

**DO include:**
- Industry sector (e.g., 白酒, 半导体)
- Revenue range
- Margin profile
- Growth trajectory
- Market position (# rank)
- Geographic region (broad)
- Competitive strengths (general)

### China M&A Market Context

**Typical teaser distribution:**
- 5-20 potential buyers
- Mix of strategic and financial
- 国企买家 often requires longer relationship-building
- 外资买家 may need additional regulatory context

**Valuation context to include:**
- A-share market multiples
- Recent comparable transactions
- Control premium range
- Market sentiment

## Quality Checks

Before distributing:
- [ ] All identifying information removed
- [ ] Financial data anonymized appropriately
- [ ] Industry context clear
- [ ] Investment thesis compelling
- [ ] Design professional
- [ ] Distribution list approved
- [ ] NDA in place for all recipients
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
