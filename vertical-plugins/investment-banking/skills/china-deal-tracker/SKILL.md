---
name: china-deal-tracker
description: Track A-share sell-side M&A and deal pipeline with milestones, deadlines, and action items. Adapted from the original deal-tracker skill for Chinese market deal processes. Triggers on "A股交易跟踪", "并购进度", "deal tracker China", "M&A pipeline A-share", or "track progress on [deal]".
---

# china-deal-tracker

## Purpose

Track **A股投行交易/并购进度** with structured milestone tracking, deadline management, and action item follow-up.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

## Workflow

### Step 1: Set Up Deal Record

**Deal setup template:**

```json
{
  "deal_name": "[Target] 股权转让",
  "deal_type": "股权收购 / 资产收购 / 吸收合并 / 借壳",
  "target": "[Company name] ([Ticker])",
  "industry": "[Industry]",
  "mandate_date": "[Date]",
  "expected_close": "[Date]",
  "deal_size": "XX亿",
  "status": "Active / On hold / Completed / Terminated"
}
```

### Step 2: Define Milestones

**Standard A-share M&A milestones:**

| # | Milestone | Typical Duration | Dependencies |
|---|-----------|-----------------|-------------|
| 1 | 委托签约 (Mandate signing) | Day 0 | Client agreement |
| 2 | Teaser 制作 | 3-5 days | Information gathering |
| 3 | 买方筛选 (Buyer screening) | 1-2 weeks | IOI responses |
| 4 | NDA 签署 | 1-3 days | Buyer identification |
| 5 | 管理层会议 (Management meeting) | Week 3-4 | Buyer shortlist |
| 6 | 尽调 (Due diligence) | 2-4 weeks | Data room access |
| 7 | 投标 (Bid submission) | Week 6-8 | DD complete |
| 8 | 谈判 (Negotiation) | 2-4 weeks | Best bid selection |
| 9 | 排他 (Exclusivity) | 2-4 weeks | Term sheet signed |
| 10 | SPA 签署 (Signing) | 4-8 weeks | Approvals obtained |
| 11 | 监管审批 (Regulatory approval) | 1-6 months | Filing complete |
| 12 | 交割 (Closing) | Day 0 of closing | All CPs satisfied |

### Step 3: Track Action Items

**Action item format:**

| # | Action | Owner | Deadline | Status | Notes |
|---|--------|-------|----------|--------|-------|
| 1 | 制作Teaser | [Name] | [Date] | In progress | |
| 2 | 买方联系 | [Name] | [Date] | Not started | 3 target buyers |
| 3 | 管理层会议安排 | [Name] | [Date] | Pending | 需确认日期 |

### Step 4: Weekly Status Update

**Standard status format:**

```
【[Deal Name]】周报 [YYYY-MM-DD]

一、本周进展
   - [Milestone 1]: [Status update]
   - [Milestone 2]: [Status update]

二、下周计划
   - [Action 1]
   - [Action 2]

三、风险与问题
   - [Issue 1]: [Mitigation]
   - [Issue 2]: [Escalation needed?]

四、时间表更新
   [Updated timeline if changed]
```

### Step 5: Deadlines & Alerts

**Critical deadlines to track:**

| Deadline | Alert Level | Action Required |
|----------|-------------|-----------------|
| IOI submission | High | Confirm receipt |
| FBO submission | High | Final review |
| Management meeting | High | Preparation, logistics |
| Regulatory filing | Critical | Prepare documents |
| SPA signing | Critical | Final terms |
| Closing | Critical | Coordination |

### Step 6: Pipeline Overview

**Deal pipeline summary:**

| Deal | Stage | Size | Expected Close | Probability | Next Action |
|------|-------|------|---------------|-------------|-------------|
| | | | | | |

## China-Specific Considerations

### Regulatory Timeline Variations

| Factor | Impact |
|--------|--------|
| 反垄断审查 | Can add 60-180 days |
| 国有股权转让 | Requires 评估 and 产权交易所 |
| 外资安全审查 | 30-60 days if foreign buyer |
| 行业准入 | Sector-specific approvals |

### Common Delays

| Issue | Typical Impact | Mitigation |
|-------|---------------|------------|
| 监管审批延迟 | +30-90 days | Early filing, engage regulators |
| 管理层分歧 | +2-4 weeks | Alignment meetings |
| 买方尽调问题 | +1-2 weeks | Data room preparation |
| 估值差距 | +2-4 weeks | Advisor mediation |
| 审批机关反馈 | Variable | Proactive engagement |

### A-share Specific Items

- **停牌** (Trading halt): Target company stock halt during process
- **信息披露** (Disclosure): Public announcements required at key stages
- **内幕信息管理** (Insider trading): Strict MI management required
- **保密期** (Confidentiality period): Typically 6-12 months

## Quality Checks

Before updating:
- [ ] All milestones defined
- [ ] Owners assigned
- [ ] Deadlines realistic
- [ ] Status accurate
- [ ] Risks flagged
- [ ] Next actions clear
- [ ] Pipeline summary current
