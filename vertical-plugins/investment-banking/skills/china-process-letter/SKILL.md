---
name: china-process-letter
description: Draft process letters and bid instructions for A-share sell-side M&A processes. Covers indication of interest (IOI) instructions, final bid procedures, and management meeting logistics adapted for Chinese market conventions. Triggers on "A股流程函", "投标函", "process letter China", "bid instructions A-share", or "IOI instructions [company]".
---

# china-process-letter

## Purpose

Draft **A股并购流程函/投标函** for sell-side M&A processes — bid instructions, IOI guidelines, and process correspondence.

## Data Sources

### Tier 0 — 万得 Wind（最全面付费数据）
- 覆盖：A股/港美股/基金/指数/债券/宏观/研报/分析（44个工具）
- MCP 服务：`wind-mcp`（需 `WIND_API_KEY` 密钥，以 `ak_` 开头）
- 优势：全市场覆盖面最广、数据最全面、包含研报和量化分析
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### Tier 1 — 同花顺 iFind（付费精确数据）/ AkShare MCP（Tier-2 免费备选）

## Transaction Types

| Process Type | Description | Documentation |
|-------------|-------------|---------------|
| 协议转让 | Private agreement transfer | 股份转让协议 |
| 要约收购 | General/partial offer | 要约收购报告书 |
| 竞标 | Competitive bidding | IOI → FLA → Final bid |
| 吸收合并 | Merger | 合并协议 |
| 重大资产重组 | Major asset restructuring | 重组报告书 |

## Workflow

### Step 1: Determine Letter Type

**Common process letters:**

| Letter | Timing | Purpose |
|--------|--------|---------|
| 第一轮意向函 (IOI) | Initial interest | Non-binding indication |
| 第二轮报价函 (FLA / FBO) | After management meeting | Detailed financial bid |
| 最终投标函 (Final bid) | Final round | Best and final offer |
| 管理层会议邀请 | Pre-FLA | Management presentation |
| 数据室访问邀请 | Due diligence | Data room access |
| 流程时间表 | Process start | Timeline and milestones |

### Step 2: Draft IOI Instructions

**Standard IOI letter structure:**

```
【机密】

致：[潜在买方名称]

关于：[目标公司名称] 股权转让/收购项目

第一轮意向函 (IOI) 指引

一、项目概述
   [Transaction overview, anonymized if teaser phase]

二、IOI 要求
   1. 格式要求
      - 非binding意向
      - 不超过[X]页
      - 中文或英文均可

   2. 内容要求
      - 买方背景介绍
      - 交易兴趣表达
      - 初步估值区间
      - 交易结构设想
      - 预计时间表

   3. 提交要求
      - 截止时间：[Date] [Time]
      - 提交方式：[Email / Data room]
      - 联系人：[Name, Title, Contact]

三、交易时间表
   Phase 1: IOI 提交 — [Date]
   Phase 2: 筛选/会议邀请 — [Date]
   Phase 3: 管理层会议 — [Date]
   Phase 4: FLA 提交 — [Date]
   Phase 5: 尽调访问 — [Date range]
   Phase 6: 最终投标 — [Date]
   Phase 7: 交易完成 — [Date target]

四、保密条款
   [Standard NDA reference]

五、联系方式
   [Advisor contact details]
```

### Step 3: Draft FBO Instructions

**Second-round bid requirements:**

```
第二轮报价函 (FBO) 指引

一、FBO 要求
   1. 必须包含内容:
      - 估值及定价依据
      - 交易结构 (股权/资产/组合)
      - 资金来源说明
      - 交易确定性评估
      - 预计交割时间
      - 先例条件 (conditions precedent)

   2. 估值支持:
      - DCF分析
      - 可比交易
      - 交易倍数

   3. 交易结构:
      - 收购比例
      - 对价支付方式 (现金/股份/组合)
      - 锁定期安排
      - 业绩承诺 (如适用)

二、格式要求
   - [X]页以内
   - Excel估值模型附件
   - 签字页

三、截止时间
   [Date] [Time] (逾期不予受理)
```

### Step 4: Draft Management Meeting Invitation

**Management meeting logistics:**

```
管理层会议邀请

尊敬的[买方名称]:

我们诚挚邀请贵方参加[目标公司]管理层会议。

时间：[Date] [Time]
地点：[Address / Online platform]
形式：[In-person / Virtual / Hybrid]

议程:
  1. 管理层介绍 (公司历史, 战略, 愿景)
  2. 业务深度介绍 (分业务线)
  3. 财务回顾与展望
  4. Q&A环节

参会管理层:
  - [CEO] — 公司战略
  - [CFO] — 财务回顾
  - [COO / 业务负责人] — 运营介绍

材料准备:
  - 管理层演示材料 (会前提供)
  - 问题清单 (会前收集)

注意事项:
  - 保密协议有效期内
  - 材料仅限内部使用
  - 会后24小时内提交问题清单
```

### Step 5: Transaction Timeline

**Standard A-share M&A timeline:**

```
交易时间表

Phase 1: 项目启动
  - Teaser distribution
  - NDA execution
  - IOI submission

Phase 2: 初步筛选
  - IOI review
  - 买方筛选 (通常3-5家)
  - 第一轮会议

Phase 3: 深度尽调
  - Management meetings
  - Data room access (数据室)
  - Management presentations
  - Site visits (如需)

Phase 4: 最终投标
  - FBO submission
  - 卖方评估
  - 排他性谈判 ( exclusivity )

Phase 5: 交易执行
  - 确定性协议 (SPA)
  - 尽调完成
  - 监管审批 (如需)
  - 交割 (Closing)
```

## China-Specific Process Considerations

### Regulatory Timeline

| Approval | Authority | Timeline |
|----------|-----------|----------|
| 经营者集中申报 | SAMR (State Administration for Market Regulation) | 180 days standard |
| 上市公司收购 | CSRC (if listed target) | Varies |
| 外资安全审查 | MOFCOM / NDRC | 30-60 days |
| 国有股权转让 | 国资委 / 产权交易所 | 30-90 days |
| 反垄断审查 | SAMR | 60-180 days |

### NDA Requirements

**Chinese NDA considerations:**
- 适用法律: typically PRC law
- 争议解决: typically 中国国际经济贸易仲裁委员会 (CIETAC)
- 保密期限: typically 2-5 years
- 返还/销毁条款: standard
- 禁止招揽 (no-poach): often included

### Data Room (数据室)

**Common data room content for A-share targets:**

| Category | Documents |
|----------|-----------|
| 公司治理 | 公司章程, 三会议事规则 |
| 财务 | 审计报告, 内控报告, 预算 |
| 业务 | 重大合同, 客户列表, 供应商列表 |
| 法律 | 诉讼, 仲裁, 行政处罚 |
| 人事 | 劳动合同, 股权激励, 社保 |
| 资产 | 土地使用权, 房产证, 知识产权 |
| 税务 | 税务合规证明, 纳税记录 |
| 关联方 | 关联交易清单, 担保情况 |

## Quality Checks

Before sending:
- [ ] Letter type appropriate for process stage
- [ ] Timeline realistic and complete
- [ ] Regulatory approval steps included
- [ ] Confidentiality clearly stated
- [ ] Contact information correct
- [ ] Formatting professional
- [ ] Language appropriate for audience
