---
name: china-break-trace
description: Forensic financial analysis for A-share fund holdings and portfolio companies. Adapts the original break-trace skill for fund administration context and Chinese market standards. Triggers on "基金持仓核查", "持仓异常", "forensic fund analysis China", "持仓质量分析", or "investigate [fund] holdings".
---

# china-break-trace

## Purpose

Conduct **基金持仓核查** — forensic analysis of fund holdings and portfolio company financials for fund administrators.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_financials(ticker, "income")     → Portfolio company P&L
get_financials(ticker, "balance")    → Portfolio company BS
get_financials(ticker, "cashflow")   → Portfolio company CF
get_fund_data(fund_code)              → Fund holdings
```

### Secondary Sources
- 巨潮 — portfolio company filings
- 基金季报/年报 — fund holdings disclosure
- 审计报告 — audit opinions

## Workflow

### Step 1: Review Fund Holdings

**Holdings analysis:**

| Security | Ticker | Sector | Allocation | Rating | Risk Flags |
|----------|--------|--------|-----------|--------|-----------|
| | | | | | |

**Concentration analysis:**

| Metric | Value | Limit | Status |
|--------|-------|-------|--------|
| Top 10 holdings % | XX% | Typically <50% | |
| Single stock max | XX% | Typically <10% | |
| Sector concentration | XX% | | |

### Step 2: Portfolio Company Analysis

**For each significant holding:**

| Check | Result | Notes |
|-------|--------|-------|
| Revenue quality | Pass/Warn/Fail | |
| Profit quality | Pass/Warn/Fail | |
| Cash flow | Pass/Warn/Fail | |
| Balance sheet | Pass/Warn/Fail | |
| Related party | Pass/Warn/Fail | |
| Governance | Pass/Warn/Fail | |

### Step 3: Red Flag Identification

**Red flag categories:**

| Category | Red Flags |
|----------|-----------|
| 财务质量 | Revenue inflation, profit manipulation, cash flow divergence |
| 关联交易 | High related party %, non-arm's length |
| 治理问题 | Ownership concentration, pledge risk |
| 合规问题 | Regulatory penalties, sanctions |
| 流动性 | Low liquidity, suspension risk |

### Step 4: Deep Dive on Concerns

**Investigation protocol:**

| Flag | Investigation | Resolution |
|------|--------------|-----------|
| 应收账款异常 | Review aging, allowance | |
| 存货异常 | Review turnover | |
| 关联交易 | Review agreements | |
| 资金占用 | Review related party balances | |
| 减值波动 | Review timing and amounts | |

### Step 5: Valuation Sanity Check

**Holding valuation review:**

| Security | Price Source | Last Price | Valuation Method | Concern? |
|----------|-------------|-----------|-----------------|----------|
| | | | | |

**Valuation concerns:**
- 停牌股票 (Suspended stocks)
- ST股票 (Distressed)
- 流动性不足 (Low liquidity)
- 估值异常 (Unusual multiples)

### Step 6: Compliance Review

**Regulatory compliance:**

| Check | Fund | Status |
|-------|------|--------|
| Investment scope | Per contract | |
| Concentration limits | Per regulation | |
| Single stock limits | Typically <10% | |
| Sector limits | Per contract | |
| Liquidity requirements | Liquid assets % | |
| Derivatives use | If applicable | |

### Step 7: Action Recommendations

**Recommendations:**

| Priority | Action | Security | Reason |
|----------|--------|----------|--------|
| High | | | |
| Medium | | | |
| Low | | | |

### Step 8: Report

**Report format:**

```
【持仓核查报告】[Fund Name] [Date]

一、持仓概览
   [Holdings summary]

二、风险持仓识别
   [Flagged securities]

三、深度分析
   [Detailed findings]

四、合规检查
   [Compliance status]

五、建议措施
   [Recommendations]
```

## China-Specific Considerations

### Fund Disclosure Requirements

| Requirement | Content |
|-------------|---------|
| 季报/半年报/年报 | Full holdings disclosure |
| 重大事项公告 | Material changes |
| 临时公告 | Ad-hoc disclosures |

### Common Fund Holdings Issues

| Issue | Detection | Action |
|-------|-----------|--------|
| 持仓集中 | Top 10 > 50% | Review |
| 停牌股票 | Suspended positions | Valuation review |
| 退市风险 | Delisting risk | Consider exit |
| ST持仓 | Distressed securities | Review necessity |
| 流动性不足 | Hard to exit | Assess impact |

## Quality Checks

Before completing:
- [ ] All holdings reviewed
- [ ] Red flags investigated
- [ ] Compliance verified
- [ ] Recommendations actionable
- [ ] Report complete
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only`: Skip iFind, use AkShare only
