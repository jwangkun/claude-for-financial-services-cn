---
name: china-dd-meeting-prep
description: Prepare management meeting materials and question lists for A-share investment due diligence. Adapted from the original dd-meeting-prep skill for Chinese business culture and management meeting conventions. Triggers on "A股尽调会议准备", "管理层会议准备", "management meeting China", "DD meeting prep", "管理層访谈准备", or "prepare for management meeting [company]".
---

# china-dd-meeting-prep

## Purpose

Prepare for **A股投资尽调管理层会议** — structured meeting preparation with question lists and material review.

## Data Sources

### Primary: iFind MCP (Tier-1 付费) / AkShare MCP (Tier-2 免费备选)

```python
get_stock_info(ticker)                        → Company overview
get_quote(ticker)                            → Valuation context
get_financials(ticker, "income")             → Financial performance
get_financials(ticker, "balance")            → Balance sheet
get_industry_stocks(industry="...")           → Peer context
```

### Secondary Sources
- 巨潮 — company filings
- 券商研报 — existing research
- 公开信息 — news, announcements

## Workflow

### Step 1: Research the Company

**Pre-meeting research checklist:**

| Item | Source | Notes |
|------|--------|-------|
| 公司历史 | 巨潮年报 | Founding story, milestones |
| 股权结构 | 年报 / 企查查 | Ownership, actual controller |
| 业务模式 | 年报, 官网 | How they make money |
| 财务表现 | AkShare / 巨潮 | Trends, quality |
| 行业地位 | 行业报告 | Market share, positioning |
| 管理层背景 | 年报, 官网 | Experience, track record |
| 近期动态 | 公告, 新闻 | M&A, contracts, disputes |

### Step 2: Prepare Question List

**Categorized questions:**

#### Strategy & Vision (战略)

```
1. 公司未来3-5年的战略规划是什么？
   - 增长驱动因素：有机增长 vs 并购？
   - 重点发展的业务/区域？
   - 竞争策略是什么？

2. 行业整合怎么看？
   - 公司是否有意参与行业整合？
   - 对竞争对手的评估？

3. 技术/产品路线图？
   - 研发投入计划？
   - 核心技术壁垒？
```

#### Financial Performance (财务)

```
1. 收入增长驱动因素分解？
   - 量 vs 价 vs 产品组合？

2. 毛利率趋势？
   - 原材料成本压力？
   - 提价能力？

3. 资本配置优先级？
   - 分红 vs 再投资 vs 还债？

4. 现金流管理？
   - 经营现金流趋势？
   - 资本支出计划？

5. 债务结构？
   - 有息负债规模和期限？
   - 融资渠道？
```

#### Operations (运营)

```
1. 产能利用率？
2. 供应链管理？
   - 关键供应商？
   - 备选方案？
3. 客户结构？
   - 前五大客户占比？
   - 客户留存率？
4. 质量控制体系？
5. 渠道网络？
   - 经销商管理？
   - 直营 vs 经销？
```

#### Management & Organization (管理)

```
1. 管理层背景和经验？
   - 核心团队 tenure？
   -  succession planning？

2. 组织架构？
   - 关键岗位？
   - 人才流失率？

3. 激励机制？
   - 管理层激励？
   - 员工股权？

4. 企业文化？
   - 价值观, 执行力？
```

#### Competitive Position (竞争)

```
1. 核心竞争优势？
   - 护城河是什么？

2. 主要竞争对手？
   - 如何应对竞争？

3. 进入壁垒？
   - 新进入者威胁？

4. 替代品威胁？
   - 技术替代风险？
```

#### Growth & Investment (发展)

```
1. 增长机会？
   - 新产品/新市场？
   - 国际化计划？

2. 并购策略？
   - 是否有并购计划？
   - 整合能力？

3. 资本支出计划？
   - 未来 CapEx 需求？
```

#### Risk & Challenges (风险)

```
1. 关键风险因素？
   - 行业政策风险？
   - 原材料价格波动？
   - 竞争加剧？

2. 挑战应对？
   - 最担心的竞争对手动作？
   - 最大的 operational challenge？

3. 危机管理？
   - 过去遇到的重大挑战及应对？
```

### Step 3: Prepare Presentation Materials

**Materials to request (会前材料):**
- 公司介绍PPT (Company presentation)
- 最近3-5年审计报告 (Audit reports)
- 最近财务预测 (Financial projections)
- 业务数据 (Operational data)
- 组织结构图 (Org chart)
- 产品/服务介绍 (Product overview)

**Materials to bring:**
- Question list (organized by category)
- Industry overview
- Peer comparison data
- Financial model questions
- Specific concerns to address

### Step 4: Meeting Logistics

**Meeting structure (typical 2-3 hour):**

| Time | Segment | Content |
|------|---------|---------|
| 0:00-0:15 | Opening | Introductions, process overview |
| 0:15-0:45 | Management presentation | Company overview by management |
| 0:45-1:45 | Q&A | Structured questioning |
| 1:45-2:15 | Break / informal chat | Relationship building |
| 2:15-2:30 | Wrap-up | Next steps, follow-up items |

### Step 5: Post-Meeting Actions

**Immediate follow-up:**
- [ ] Send thank-you note / follow-up questions
- [ ] Document key learnings
- [ ] Update investment thesis based on meeting
- [ ] Flag any red flags
- [ ] Schedule next steps

**Meeting minutes template:**

```
【管理层会议纪要】[Company] [Date]

参会人员：
  买方：[Names, firms]
  卖方/管理层：[Names, titles]

一、管理层介绍
   [Summary of management presentation]

二、关键问题与回答
   1. [Question]: [Answer summary]
   2. [Question]: [Answer summary]
   ...

三、关键发现
   [Important insights from meeting]

四、红旗事项
   [Red flags or concerns]

五、后续事项
   [Follow-up items, deadlines]

六、投资逻辑更新
   [How meeting impacted thesis]
```

## China-Specific Meeting Considerations

### Business Culture

| Aspect | Implication |
|--------|-------------|
| 关系建立 | Relationship building important before business |
| 层级意识 | Address most senior person first |
| 面子文化 | Avoid confrontation, read between lines |
| 含蓄表达 | "We'll consider it" may mean no |
| 谈判风格 | Patient, relationship-focused |

### Meeting Best Practices

- Arrive on time (punctuality valued)
- Bring senior team members (shows commitment)
- Prepare bilingual materials if needed
- Have local team member present
- Be prepared for indirect answers
- Read non-verbal cues
- Follow up promptly

### Key Questions for Chinese Companies

| Topic | Specific Questions |
|-------|-------------------|
| 实际控制人 | Who is the actual controller? Control structure? |
| 关联交易 | Related party transactions? Arm's length? |
| 政府关系 | Government relationships? Subsidies? |
| 竞争环境 | How do you compete with state-owned peers? |
| 融资能力 | Bank relationships? Credit access? |
| 国际化 | Overseas expansion plans? |
| 接班人 | Succession planning? |

## Quality Checks

Before meeting:
- [ ] Company research complete
- [ ] Question list prioritized
- [ ] Materials organized
- [ ] Team roles assigned
- [ ] Logistics confirmed

After meeting:
- [ ] Minutes documented promptly
- [ ] Key findings captured
- [ ] Follow-ups assigned
- [ ] Thesis updated
- [ ] Red flags addressed
> **Data Source Mode Switch**: Set env var `IFIND_DATA_SOURCE_MODE` to control data source preference.
> - `ifind-only` (strict): Use iFind only, error if unavailable
> - `ifind-fallback` (default): iFind preferred, fallback to AkShare
> - `akshare-only, wind-only (Wind only), wind-fallback (Wind first, fallback to iFind → AkShare)`: Skip iFind, use AkShare only
