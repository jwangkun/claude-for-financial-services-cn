---
name: china-break-trace
description: Forensic financial analysis for A-share companies. Identifies discrepancies, potential irregularities, and earnings quality issues in Chinese financial statements. Adapted from the original break-trace skill for CAS accounting and Chinese market red flags. Triggers on "A股财务核查", "财务异常", "forensic analysis China", "财务舞弊", "earnings quality China", or "investigate [company] financials".
---

# china-break-trace

## Purpose

Conduct **A股财务核查** — forensic analysis to identify potential issues in Chinese financial statements.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "income")     → Revenue, profit trends
get_financials(ticker, "balance")    → Balance sheet anomalies
get_financials(ticker, "cashflow")   → Cash flow quality
```

### Secondary Sources
- 巨潮 — filings, notes
- 审计报告 — auditor opinion, emphasis of matter
- 公告 — unusual transactions
- 证监会/交易所 — inquiries, penalties

## Workflow

### Step 1: Revenue Quality Analysis

**Revenue red flags:**

| Indicator | Check | Red Flag |
|-----------|-------|----------|
| 应收账款/收入 | AR / Revenue | >40% or rising fast |
| 应收账款增速 vs 收入增速 | Growth comparison | AR growing >> Revenue |
| 经营活动现金流/净利润 | OCF / Net Income | <0.5 or negative |
| 收入确认政策 | Notes review | Aggressive recognition |
| 客户集中度 | Top customers | >30% from one customer |
| 关联交易 | Related party | High % of revenue |

**Revenue quality score:**

| Metric | Score (1-5) | Notes |
|--------|-------------|-------|
| OCF/NI ratio | | 5 = OCF >> NI |
| AR days | | 5 = low/stable |
| Revenue concentration | | 5 = diversified |
| Growth quality | | 5 = organic, recurring |
| Cash conversion | | 5 = excellent |

### Step 2: Profit Quality Analysis

**Profit red flags:**

| Indicator | Check | Red Flag |
|-----------|-------|----------|
| 营业利润 vs 净利润 | Operating profit vs net | Large gap |
| 非经常性损益 | Non-recurring items | >20% of profit |
| 政府补助 | Government subsidies | High % of profit |
| 资产减值 | Impairments | Irregular timing |
| 投资收益 | Investment income | Unsustainable |
| 毛利率趋势 | Gross margin | Unexplained changes |

**Profit decomposition:**

```
净利润 = 营业利润 + 营业外收支 - 所得税

分析重点:
1. 营业利润占比 (营业利润/净利润): 应>80%
2. 非经常性损益: 识别一次性项目
3. 政府补助依赖度: 补助/净利润
4. 减值损失波动: 是否平滑利润?
```

### Step 3: Cash Flow Quality

**Cash flow analysis:**

| Metric | Formula | Healthy | Concern |
|--------|---------|---------|---------|
| OCF/NI | OCF / Net Income | >1 | <0.5 |
| FCF | OCF - CapEx | Positive | Negative |
| OCF/Revenue | OCF / Revenue | >5% | <0% |
| 投资活动现金流 | Investing CF | Outflows (growth) | Large inflows (asset sales?) |

**Cash flow quality score:**

| Indicator | Healthy | Warning |
|-----------|---------|---------|
| OCF consistently positive | ✓ | Negative OCF |
| OCF tracks NI | ✓ | Large divergence |
| CapEx sustainable | ✓ | CapEx >> OCF |
| No frequent asset sales | ✓ | Asset disposal income |

### Step 4: Balance Sheet Anomalies

**Balance sheet checks:**

| Area | Red Flags |
|------|-----------|
| 货币资金 | Large cash + high debt (possible restriction) |
| 应收账款 | Rapid growth, aging issues |
| 其他应收款 | Unusually large (possible tunneling) |
| 存货 | Rapid growth, no explanation |
| 在建工程 | Never completed (capitalized costs?) |
| 商誉 | High % of equity (>30%) |
| 长期待摊费用 | Unusually large |
| 负债 | Off-balance sheet items |

**Specific balance sheet ratios:**

| Ratio | Formula | Concern |
|-------|---------|---------|
| 有息负债/净资产 | Interest-bearing debt / Equity | >100% |
| 货币资金/有息负债 | Cash / Interest-bearing debt | <0.3 |
| 商誉/净资产 | Goodwill / Equity | >30% |
| 其他应收款/资产 | Other receivables / Total assets | >5% |
| 存货周转天数 | Inventory days | Sudden increase |

### Step 5: Related Party Analysis

**Related party red flags:**

| Indicator | Check |
|-----------|-------|
| 关联交易金额 | % of revenue/costs |
| 关联交易定价 | Arm's length? |
| 关联应收应付 | Balances with related parties |
| 资金占用 | Funds tied up with related parties |
| 担保 | Guarantees for related parties |

**Common tunneling mechanisms:**
- 预付账款 to related parties
- 其他应收款 from related parties
- 资金拆借 without interest
- Asset sales to related parties at non-arm's length prices
- 担保 for related party debt

### Step 6: Earnings Management Detection

**Earnings management indicators:**

| Method | Detection |
|--------|-----------|
| 费用资本化 | CapEx unusual, D&A low |
| 收入提前确认 | AR rising, 预收账款 falling |
| 费用延后确认 | AP falling, accrued expenses low |
| 减值选择性计提 | Timing of impairments |
| 会计政策变更 | Policy change benefits |
| 估计变更 | Reserve changes |

**Beneish M-Score (adapted for China):**

| Variable | Calculation |
|----------|------------|
| DSRI | Days sales in receivables change |
| GMI | Gross margin deterioration |
| AQI | Asset quality index |
| SGI | Sales growth index |
| DEPI | Depreciation index |
| SGAI | SG&A index |
| LVGI | Leverage index |
| TATA | Total accruals / Total assets |

### Step 7: Auditor & Filing Analysis

**Audit report review:**

| Item | Review |
|------|--------|
| 审计意见 | Standard / Modified / Adverse |
| 强调事项段 | Any emphasis of matter? |
| 关键审计事项 | Key audit matters |
| 审计师变更 | Recent change? |
| 审计费用 | Unusual changes? |

**Filing review:**
- 年报 vs 中报 consistency
- Notes completeness
- Segment disclosures
| Related party disclosures
| Commitments and contingencies

### Step 8: Regulatory Signals

**Regulatory red flags:**

| Source | Signals |
|--------|---------|
| 交易所问询函 | Inquiry letters |
| 证监会关注函 | Regulatory attention |
| 行政处罚 | Fines, penalties |
| 交易所纪律处分 | Disciplinary actions |
| 投资者诉讼 | Shareholder lawsuits |

## Common A-share Fraud Patterns

| Pattern | Description | Detection |
|---------|-------------|-----------|
| 虚增收入 | Fictitious revenue | AR anomaly, tax mismatch |
| 虚减成本 | Understate costs | Margin anomaly |
| 关联交易非关联化 | Related party disguised | Customer/supplier analysis |
| 资金循环 | Round-tripping | Cash flow analysis |
| 资产置换 | Asset swapping | Unusual asset changes |
| 会计估计操纵 | Estimate manipulation | Reserve changes |

## Quality Checks

Before delivering report:
- [ ] All red flags investigated
- [ ] Evidence documented
- [ ] Severity assessed
- [ ] Conclusions supported
- [ ] Regulatory signals checked
- [ ] Report structured clearly
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
