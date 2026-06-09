---
name: china-nav-tieout
description: Net asset value (NAV) reconciliation and tie-out for Chinese funds and investment portfolios. Adapts the original nav-tieout skill for A-share holdings, Chinese fund accounting standards, and domestic custody arrangements. Triggers on "A股净值核对", "NAV计算", "NAV tie-out China", "基金净值", "net asset value [fund]", or "portfolio valuation [date]".
---

# china-nav-tieout

## Purpose

Perform **A股投资组合净值核算** — comprehensive NAV reconciliation and valuation for Chinese investment portfolios.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

```python
get_quote(ticker)                     → Latest prices for holdings
get_fund_data(fund_code)              → Fund NAV data
get_index_data("000001")              → Benchmark data
```

### Secondary Sources
- 基金公司 — fund NAV calculations
- 托管行 — custody valuations
- Wind / Choice — portfolio analytics
- 交易所 — closing prices

## Workflow

### Step 1: Gather Portfolio Holdings

**Holdings snapshot:**

| Security | Ticker | Type | Quantity | Market Value | Cost | Unrealized P/L |
|----------|--------|------|----------|--------------|------|----------------|
| | | | | | | |
| Cash | | | | | | |
| Receivables | | | | | | |
| Payables | | | | | | |
| **Total NAV** | | | | | | |

### Step 2: Value Each Holding

**Valuation methodology:**

| Security Type | Valuation Method | Source |
|---------------|-----------------|--------|
| A股上市股票 | Closing price (收盘价) | 交易所 |
| A股停牌股票 | Last closing / 估值 | 中基协 guidelines |
| 基金 (ETF/LOF) | NAV / market price | 基金公司 |
| 债券 | 中债估值 / 收盘价 | 中债/交易所 |
| 逆回购 | Principal + interest | Calculated |
| 存款 | Principal + interest | Bank |
| 衍生品 | Mark-to-market | Exchange/Counterparty |

**A-share valuation rules:**
- 上市股票: 收盘价 (closing price)
- 停牌股票: 
  - <1 month: last closing
  - 1-3 months: 中基协 AMAC guidelines
  - >3 months: independent valuation
- 涨跌停股票: Ceiling/floor price

### Step 3: Calculate NAV

**NAV calculation:**

| Component | Amount | Notes |
|-----------|--------|-------|
| Market value of securities | ¥XX | |
| Cash and cash equivalents | ¥XX | |
| Accrued income | ¥XX | Dividends, interest |
| Receivables | ¥XX | |
| Other assets | ¥XX | |
| **Gross Assets** | **¥XX** | |
| | | |
| Payables | ¥XX | |
| Accrued expenses | ¥XX | Management fees, etc. |
| Other liabilities | ¥XX | |
| **Total Liabilities** | **¥XX** | |
| | | |
| **Net Assets** | **¥XX** | |
| | | |
| Shares outstanding | XX 份 | |
| **NAV per share/unit** | **¥X.XXXX** | |

### Step 4: Income Accruals

**Accrued income:**

| Type | Security | Amount | Ex-date | Pay-date |
|------|----------|--------|---------|----------|
| 现金股息 | | | | |
| 股票股息 | | | | |
| 债券利息 | | | | |
| 基金分红 | | | | |
| 逆回购利息 | | | | |
| **Total accrued income** | | | | |

### Step 5: Expense Accruals

**Accrued expenses:**

| Type | Amount | Calculation Basis |
|------|--------|-------------------|
| 管理费 (Management fee) | ¥XX | AUM × annual rate × days/365 |
| 托管费 (Custodian fee) | ¥XX | AUM × annual rate × days/365 |
| 交易佣金 (Trading commission) | ¥XX | Actual trades |
| 税费 (Taxes) | ¥XX | |
| 其他费用 | ¥XX | |
| **Total accrued expenses** | | |

### Step 6: Reconciliation

**Reconciliation checklist:**

| Item | Portfolio System | Custodian | Difference | Resolved |
|-------|-----------------|-----------|------------|----------|
| Securities holdings | | | | |
| Cash balance | | | | |
| Accrued income | | | | |
| Accrued expenses | | | | |
| Total NAV | | | | |

**Common reconciling items:**
- Trade date vs settlement date differences
- 在途交易 (Trades in transit)
- 分红在途 (Dividends pending)
- 费用计提差异 (Accrual timing)

### Step 7: Performance Calculation

**Performance metrics:**

| Metric | Period Return | Annualized |
|--------|--------------|------------|
| Portfolio return | X.XX% | X.XX% |
| Benchmark return | X.XX% | X.XX% |
| Active return | X.XX% | X.XX% |
| Volatility | X.XX% | X.XX% |
| Sharpe ratio | | X.XX |
| Max drawdown | X.XX% | |
| Best period | | X.XX% |
| Worst period | | X.XX% |

### Step 8: Compliance Checks

**Fund compliance (China):**

| Check | Requirement | Status |
|-------|-------------|--------|
| 投资范围 | Within mandate | |
| 投资比例 | Per fund contract | |
| 集中度 | Single stock limit | |
| 流动性 | Liquid assets ratio | |
| 杠杆率 | Leverage limits | |
| 关联交易 | Within limits | |
| 估值方法 | Per regulations | |

### Step 9: Reporting

**NAV report format:**

```
【净值报告】[Fund Name] [Date]
报告日期: YYYY年MM月DD日
单位净值: ¥X.XXXX
累计净值: ¥X.XXXX
日涨跌幅: +/-X.XX%

资产组合:
  股票投资: ¥XX亿 (XX%)
  债券投资: ¥XX亿 (XX%)
  现金及等价物: ¥XX亿 (XX%)
  其他: ¥XX亿 (XX%)
  合计: ¥XX亿

净值计算人: _________
复核人: _________
```

## China-Specific Considerations

### Fund Types

| Type | Regulation | Valuation |
|------|-----------|-----------|
| 公募基金 (Public fund) | 证监会 | Daily NAV |
| 私募基金 (Private fund) | 中基协 | Weekly/Monthly |
| 券商资管 | 证监会 | Per contract |
| 信托计划 | 银保监会 | Per contract |
| 保险资管 | 银保监会 | Per contract |

### Valuation Standards

| Standard | Source |
|----------|--------|
| 基金会计核算 | 财政部 / 证监会 |
| 估值指引 | 中基协 AMAC |
| 证券投资基金 | 基金合同 |
| 托管协议 | 托管行 |

### Common Issues

| Issue | Resolution |
|-------|-----------|
| 停牌股票估值 | AMAC guidelines |
| 汇率折算 | PBOC rate |
| 费用计提 | Per fund contract |
| 分红处理 | Ex-dividend adjustment |

## Quality Checks

Before finalizing:
- [ ] All holdings priced correctly
- [ ] Income and expenses accrued
- [ ] Reconciliation complete
- [ ] Performance calculated accurately
- [ ] Compliance verified
- [ ] Documentation complete
- [ ] Sign-offs obtained
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
> - `wind-only`: Wind only, error if unavailable
> - `wind-fallback`: Wind first, fallback to iFind → AkShare
