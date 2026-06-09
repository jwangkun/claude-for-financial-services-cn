---
name: china-3-statement-model
description: Three-statement financial model for A-share stocks. Adapts the standard 3-statement-model methodology for Chinese accounting standards (CAS), Chinese GAAP differences, and AkShare-sourced financials. Use instead of the original 3-statement-model skill when building integrated IS/BS/CF models for Chinese listed companies.
---

# china-3-statement-model

## Purpose

Build institutional-quality three-statement models (Income Statement / Balance Sheet / Cash Flow) for A-share equities, adapted for Chinese Accounting Standards (CAS) and the Chinese market context.

## Key Differences from US 3-Statement Models

| Parameter | US Model | China Model |
|-----------|----------|-------------|
| Accounting standard | US GAAP / IFRS | CAS (企业会计准则) |
| Tax rate | 21% federal | 25% standard (高新技术企业 15%) |
| Currency | USD | CNY (人民币) |
| Fiscal year | Varied | Mostly Dec 31 year-end |
| Revenue recognition | ASC 606 | CAS 14 (similar principles) |
| Goodwill | Indefinite life (no amortization) | CAS 8 — goodwill amortized or tested |
| R&D capitalization | Typically expensed | Can be capitalized under CAS |
| VAT treatment | Sales tax separate | 增值税 often embedded in revenue/sales |
| Unit reporting | USD | Often 千元 (thousands CNY) — verify |

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_financials(ticker, "income", "annual")   → 利润表
get_financials(ticker, "balance", "annual")  → 资产负债表
get_financials(ticker, "cashflow", "annual") → 现金流量表
get_quote(ticker)                            → 实时行情
get_historical_data(ticker)                  → 历史价格
get_stock_info(ticker)                       → 公司基本信息
```

### Secondary Sources (when AkShare insufficient)
- 巨潮资讯 (cninfo.com.cn) — mandatory disclosure filings
- 上交所 / 深交所 — listed company announcements
- 上证e互动 / 深交所互动易 — IR Q&A
- 公司官网投资者关系页面

## Workflow

### Step 1: Data Retrieval

Pull 3-5 years of historical financials from AkShare.

**Verify units carefully:**
- Some statements report in 元 (CNY)
- Others in 千元 (thousands CNY)
- Normalize to consistent unit before modeling

```python
# Pull all three statements
get_financials(ticker, "income", "annual")
get_financials(ticker, "balance", "annual")
get_financials(ticker, "cashflow", "annual")
```

### Step 2: Historical Analysis

Document key trends:

- **Revenue growth**: YoY %, CAGR over 3-5 years
- **Gross margin**: 毛利率 — track expansion/contraction
- **Operating margin**: 营业利润率
- **Net margin**: 净利率
- **Tax rate**: 所得税率 — flag if below 25% (likely 高新技术企业)
- **Effective tax rate**: vs statutory rate
- **D&A**: 折旧与摊销 as % of PPE
- **CapEx**: 资本支出 from cash flow statement
- **Working capital**: 应收账款、存货、应付账款 trends
- **Debt structure**: 有息负债 composition

### Step 3: Build the Model

Follow standard 3-statement modeling methodology, adapted for CAS:

#### Income Statement (利润表)

Key line items (Chinese naming):
- 营业收入 (Revenue)
- 营业成本 (COGS)
- 税金及附加 (Taxes and surcharges — includes 消费税、城建税等)
- 销售费用 (Selling expenses)
- 管理费用 (G&A)
- 研发费用 (R&D expenses — must be separated per CAS)
- 财务费用 (Financial costs — net of interest income)
- 营业利润 (Operating profit)
- 营业外收入/支出 (Non-operating income/expenses)
- 利润总额 (Profit before tax)
- 所得税费用 (Income tax expense)
- 净利润 (Net income)
- 归属于母公司股东的净利润 (Net income attributable to parent)

#### Balance Sheet (资产负债表)

Key line items:
- 货币资金 (Cash & equivalents)
- 交易性金融资产 (Trading financial assets)
- 应收账款 (Accounts receivable)
- 预付款项 (Prepayments)
- 存货 (Inventory)
- 其他流动资产 (Other current assets)
- 流动资产合计 (Total current assets)
- 固定资产 (Fixed assets / PPE)
- 在建工程 (Construction in progress)
- 无形资产 (Intangible assets)
- 商誉 (Goodwill — flag if >30% of equity)
- 非流动资产合计 (Total non-current assets)
- 资产总计 (Total assets)
- 短期借款 (Short-term borrowings)
- 应付账款 (Accounts payable)
- 预收款项/合同负债 (Advance receipts / contract liabilities)
- 一年内到期非流动负债 (Current portion of LT debt)
- 流动负债合计 (Total current liabilities)
- 长期借款 (Long-term borrowings)
- 应付债券 (Bonds payable)
- 非流动负债合计 (Total non-current liabilities)
- 负债合计 (Total liabilities)
- 股本 (Share capital)
- 资本公积 (Capital reserve)
- 盈余公积 (Surplus reserve)
- 未分配利润 (Retained earnings)
- 归属于母公司股东权益合计 (Parent equity)
- 少数股东权益 (Minority interest)
- 所有者权益合计 (Total equity)
- 负债和股东权益总计 (Total liabilities + equity)

#### Cash Flow Statement (现金流量表)

Chinese indirect method:
- 经营活动现金流量 (Operating CF):
  - Start from 净利润
  - Adjust: D&A, 财务费用, 投资收益, 营运资本 changes
  - 经营活动产生的现金流量净额
- 投资活动现金流量 (Investing CF):
  - 购建固定资产/无形资产 (CapEx)
  - 处置收回 (Asset sales)
  - 投资支付/收回 (Investment purchases/sales)
- 筹资活动现金流量 (Financing CF):
  - 吸收投资 (Equity issuance)
  - 取得借款 (Borrowings)
  - 偿还债务 (Debt repayment)
  - 分配股利 (Dividends)
- 现金净增加额 (Net change in cash)
- 期末现金余额 (Ending cash balance)

### Step 4: Balance Checks

**CRITICAL — Chinese-specific checks:**

1. **Cash reconciliation**: 货币资金 (BS) = 期末现金余额 (CF) ± restricted cash
2. **BS balancing**: 资产总计 = 负债和股东权益总计
3. **RE roll-forward**: 期初未分配利润 + 本期净利润 - 提取盈余公积 - 现金分红 = 期末未分配利润
4. **CF-IS linkage**: 净利润 (IS) → starting point for 经营CF
5. **CapEx check**: 购建固定资产 (CF) ≈ 固定资产增加 (BS) + 累计折旧增加 (BS)
6. **Debt check**: 借款变动 (CF) = 短期借款变动 + 长期借款变动 (BS)
7. **Tax check**: 所得税费用 (IS) vs 实际缴纳 (CF indirect method add-back)

### Step 5: Scenario & Sensitivity

- Base / Bear / Bull scenarios
- Sensitivity on revenue growth, gross margin, tax rate
- Key drivers: 毛利率, 期间费用率, 营运资本效率

## China-Specific Modeling Conventions

### 增值税 (VAT)
- Listed companies report 营业收入 net of VAT
- 税金及附加 includes 消费税 but not VAT
- VAT is off-balance-sheet in most models

### 商誉 (Goodwill)
- Common from M&A, especially 2015-2016 boom
- Flag if 商誉 > 30% of 归母权益
- Note annual impairment testing requirements

### 研发费用 (R&D)
- CAS requires R&D to be expensed (not capitalized like IFRS allows)
- Some companies disclose R&D capitalization in notes — check if >5% of revenue

### 折旧 (Depreciation)
- Chinese companies often use straight-line over longer lives
- Typical ranges:
  - Buildings: 20-40 years
  - Equipment: 5-10 years
  - Vehicles: 4-6 years

### 存货 (Inventory)
- LIFO not permitted under CAS (FIFO or weighted average only)
- 存货计价 affects margin comparability across years

### 应收款项 (Receivables)
- 应收账款 often high for industrial companies — check DSO
- 应收票据 (notes receivable) vs 应收账款 (trade AR) — treat separately
- 坏账准备 (allowance for doubtful accounts) varies by company

### 借款 (Debt)
- 短期借款 often high for leveraged companies
- 长期借款 may include 一年内到期非流动负债
- 应付债券 for corporate bond issuers
- Interest expense in 财务费用 (net of interest income)

## Excel Formatting (OpenPyXL / Office JS)

Follow the same professional conventions as the base `xlsx-author` skill, with China-specific adaptations:

- **Section headers**: Dark blue `#1F4E79` with white bold text
- **Column headers**: Light blue `#D9E1F2` with black bold text
- **Input cells**: Blue font (RGB: 0,0,255) — all hardcoded inputs
- **Formula cells**: Black font (RGB: 0,0,0)
- **Sheet links**: Green font (RGB: 0,128,0)
- **Currency**: CNY (¥) with thousands separator
- **Percentages**: 0.0% format
- **Cell comments**: "Source: AkShare, [date], [field], [ticker]"

### Number Format Conventions

| Item | Format | Example |
|------|--------|---------|
| Revenue | ¥#,##0 | ¥12,345 |
| Percentages | 0.0% | 15.3% |
| Ratios | 0.00x | 2.50x |
| Dates | YYYY | 2024 |
| Stock price | ¥#,##0.00 | ¥158.50 |

## Quality Checks

Before delivering:

- [ ] All three statements balance correctly
- [ ] Cash from CF = Cash on BS
- [ ] Retained earnings roll-forward ties
- [ ] CapEx/Depreciation logic consistent
- [ ] Debt changes tie between BS and CF
- [ ] Tax rate reasonable (20-28% unless 高新技术企业)
- [ ] All hardcoded inputs have cell comments
- [ ] All formulas reference cells, no hardcodes in formulas
- [ ] Scenario blocks structured correctly (Bear/Base/Bull)
- [ ] Sensitivity analysis included

## Common Pitfalls

1. **Unit mismatch**: Mixing 元 and 千元 — always normalize
2. **VAT confusion**: Double-counting VAT in revenue or COGS
3. **Goodwill spike**: Forgetting large goodwill from acquisitions
4. **Tax rate variance**: Assuming 25% when company is 高新技术企业 (15%)
5. **R&D understatement**: CAS expenses all R&D, but some companies capitalize in notes
6. **Receivables inflation**: 应收账款 much higher than revenue growth — flag
7. **Short-term debt**: 短期借款 often high; don't miss current portion of LT debt
8. **Minority interest**: 少数股东权益 can be significant for conglomerates

## Data Source Priority

1. **AkShare MCP** (primary) — real-time and historical A-share data
2. **巨潮资讯** (cninfo.com.cn) — mandatory disclosures
3. **交易所公告** — SH/SZ exchange filings
4. **公司官网/IR** — supplementary data
5. **Web search** — only if above insufficient, mark `[UNSOURCED]`

## Output Checklist

- [ ] Three-statement model fully linked (IS → BS → CF)
- [ ] All balance checks pass
- [ ] Historical + projected years included
- [ ] Scenario analysis (Bear/Base/Bull)
- [ ] Sensitivity tables
- [ ] All hardcoded inputs sourced and commented
- [ ] CAS conventions documented
- [ ] Currency consistent (CNY)
- [ ] File named: `[Ticker]_3StatementModel_[Date].xlsx`
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
