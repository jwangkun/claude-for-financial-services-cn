---
name: china-skill-creator
description: Create new China-specific financial skills following the established patterns and conventions. Use this meta-skill to scaffold new china-* skills that integrate with iFind MCP (Tier-1) and AkShare MCP (Tier-2 fallback), follow CAS accounting standards, and adapt workflows for the Chinese market. Triggers on "创建中国skill", "新建A股skill", "create china skill", "new china-skill", "制作skill", or when creating any new china-* skill.
---

# china-skill-creator

## Purpose

Create new **china-* skills** — scaffold and template new skills for the China financial services plugin ecosystem.

## When to Use

Use this skill when:
- Creating a new china-* skill from scratch
- Adapting an existing plugins/ skill to China context
- Extending the china/ directory with new capabilities
- Ensuring consistency with existing china-* skill patterns

## Skill Creation Pattern

### Step 1: Choose Vertical

**Vertical mapping:**

| Original Vertical | China Vertical | Path |
|-------------------|----------------|------|
| `financial-analysis/` | `china-finance/` | `china/vertical-plugins/china-finance/skills/` |
| `equity-research/` | `china-finance/` | `china/vertical-plugins/china-finance/skills/` |
| `investment-banking/` | `investment-banking/` | `china/vertical-plugins/investment-banking/skills/` |
| `private-equity/` | `private-equity/` | `china/vertical-plugins/private-equity/skills/` |
| `wealth-management/` | `wealth-management/` | `china/vertical-plugins/wealth-management/skills/` |
| `fund-admin/` | `fund-admin/` | `china/vertical-plugins/fund-admin/skills/` |
| `operations/` | `operations/` | `china/vertical-plugins/operations/skills/` |

### Step 2: Name Convention

**Naming rules:**
- All China skills prefix: `china-`
- Mirror original skill name: `china-[original-name]`
- Lowercase with hyphens: `china-3-statement-model`
- Directory matches skill name

**Examples:**
| Original | China Version |
|----------|--------------|
| `comps-analysis` | `china-comps-analysis` |
| `earnings-analysis` | `china-earnings-analysis` |
| `client-report` | `china-client-report` |

### Step 3: Frontmatter Template

**Required frontmatter:**

```yaml
---
name: china-[skill-name]
description: [Chinese + English description]. Triggers on "A股[keywords]", "[Chinese keywords]", "[English keywords]", or "[example usage]".
---
```

**Frontmatter rules:**
- `name`: lowercase with hyphens, prefixed `china-`
- `description`: Include Chinese trigger words and English fallback
- Must include `---` delimiters

### Step 4: SKILL.md Structure Template

**Standard structure:**

```markdown
---
name: china-[skill-name]
description: [description with triggers]
---

# china-[skill-name]

## Purpose

[One-line description in Chinese + English]

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据） / AkShare（Tier-2 免费备选）

\```python
get_quote(ticker)                     → [what it returns]
get_financials(ticker, "income")      → [what it returns]
\```

### Secondary Sources
- 巨潮 — [usage]
- 上交所/深交所 — [usage]
- Wind / Choice — [usage]

## Workflow

### Step 1: [Step Name]

[Content]

### Step 2: [Step Name]

[Content]

[... more steps ...]

## China-Specific Considerations

### [Topic]

[China-specific guidance]

## Quality Checks

Before delivering:
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]
```

### Step 5: China Adaptation Checklist

When adapting from original skill:

| Adaptation Area | China-Specific Changes |
|----------------|----------------------|
| Data sources | Replace Western sources with iFind/AkShare/巨潮/同花顺 |
| Accounting | US GAAP → CAS |
| Tax | US tax → 25% China corporate tax |
| Currency | USD → CNY (¥) |
| Units | $M → 万元 / 亿元 |
| Terminology | English → Chinese (归母净利润, etc.) |
| Market | US markets → A-share (主板/创业板/科创板) |
| Regulations | SEC → CSRC / 证监会 |
| Industry | US sectors → 东方财富 categories |
| Reporting | 10-K/Q → 年报/季报 |

### Step 6: Required Sections

Every china-* SKILL.md must include:

| Section | Required? | Content |
|---------|-----------|---------|
| `name` | ✓ | Frontmatter, `china-` prefix |
| `description` | ✓ | Chinese + English, triggers |
| `## Purpose` | ✓ | One-line description |
| `## Data Sources` | ✓ | iFind MCP (primary) + AkShare (fallback) |
| `## Workflow` | ✓ | Step-by-step process |
| `## China-Specific Considerations` | ✓ | China adaptations |
| `## Quality Checks` | ✓ | Pre-delivery checklist |

### Step 7: Data Source Tool Reference (iFind + AkShare)

**Commonly used tools:**

```python
# Market data
get_quote(ticker)                    → Current quote
get_historical_data(ticker)          → Historical prices
get_index_data(index_code)           → Index data
get_market_overview()                → Market summary

# Financials
get_financials(ticker, "income")     → Income statement
get_financials(ticker, "balance")    → Balance sheet
get_financials(ticker, "cashflow")   → Cash flow

# Industry & peers
get_industry_stocks(industry="...")   → Industry peers
get_stock_info(ticker)               → Company info

# Funds
get_fund_data(fund_code)             → Fund data

# News (china-news MCP — separate server)
get_stock_news(ticker="{{TICKER}}")         → Individual stock news
get_market_headlines(top_n=20)              → Market headlines
```

### Step 8: Common Patterns

**CAS Accounting terms to use:**
- 营业收入 (Revenue, net of VAT)
- 营业成本 (COGS)
- 归母净利润 (Net income to parent)
- 扣非净利润 (Non-GAAP net income)
- 经营现金流 (Operating CF)
- 资本支出 (CapEx)
- EPS (每股收益)
- ROE (净资产收益率)
- 毛利率 (Gross margin)
- 净利率 (Net margin)

**A-share conventions:**
- Stock codes: 6-digit (e.g., "600519", "000001")
- No exchange prefix
- 主板/创业板/科创板/北交所
- 涨跌停: ±10% (±20% for 创业板/科创板)
- 千元 / 万元 / 亿元 units

**Tax conventions:**
- Corporate tax: 25% (15% for 高新技术企业)
- VAT: 13% (standard), excluded from revenue
- Stamp duty: 0.05% on seller
- Dividend tax: 20% (10% for >1 year holding)

### Step 9: Forbidden Patterns

**Never use in china-* skills:**

Western data sources, indices, and filing systems must be replaced with China-native equivalents (iFind / AkShare / 巨潮 / 上交所 / 深交所 / 中证指数 / 东方财富 / 企查查 / 晨星中国). The `check-china.py` validation script enforces this — any skill containing these patterns will fail validation.

See the "China Adaptation Checklist" (Step 5) for the full mapping.

### Step 10: Validation

**After creating a new skill:**

```bash
# Check for forbidden patterns
cd china && python3 scripts/check-china.py

# Sync to agent bundles
python3 scripts/sync-china-skills.py
```

## Quick-Start Template

```markdown
---
name: china-[name]
description: [Chinese description with triggers].
---

# china-[name]

## Purpose

[Chinese + English description]

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据） / AkShare（Tier-2 免费备选）

\```python
get_quote(ticker) → [description]
\```

### Secondary Sources
- 巨潮 — [usage]

## Workflow

### Step 1: [Name]

[Content]

### Step 2: [Name]

[Content]

## China-Specific Considerations

[Content]

## Quality Checks

Before delivering:
- [ ] [Check 1]
- [ ] [Check 2]
```

## Example: Creating a New Skill

**Scenario:** Create `china-portfolio-optimization`

1. **Choose vertical:** `china-finance` (financial analysis)
2. **Create directory:** `china/vertical-plugins/china-finance/skills/china-portfolio-optimization/`
3. **Create SKILL.md:** Use template above
4. **Add China adaptations:**
   - Use A-share universe
   - Consider 涨跌停 limits
   - Factor in 北向资金 flows
   - Use 东方财富 sector classifications
5. **Sync:** Run `sync-china-skills.py`
6. **Validate:** Run `check-china.py`
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
