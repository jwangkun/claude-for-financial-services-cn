# claude-for-financial-services-cn

🇨🇳 **63 个 Claude Skills，为 A 股金融从业者而生**

基于 Anthropic 官方 [claude-for-financial-services](https://github.com/anthropics/claude-for-financial-services) 深度适配国内市场，现已开源。

---

## 这是什么？

一套可以直接给 Claude 装上的 **金融专业技能包**。装了之后，你跟 Claude 说"帮我写一份茅台年报点评"或者"建一个宁德时代的 DCF 模型"，它就知道 A 股的格式、数据源和会计准则，直接出活儿。

> 一句话：**把 Anthropic 为华尔街投行做的 AI 助手，搬到了 A 股。**

| | 原版 (Wall Street) | 本项目 (A 股) |
|---|---|---|
| 数据 | Bloomberg / FactSet / PitchBook | **iFind**（同花顺）+ **AkShare**（免费开源） |
| 研报 | JPM / GS 英文研报 | **中金 / 中信 / 华泰** 格式 |
| 模型 | US GAAP | **中国会计准则** |
| 无风险利率 | 美债 | **中债** |
| 行业分类 | GICS | **申万 / 中信** |

---

## ⚡ 一分钟上手

```bash
# 1. 装 Claude Code
npm install -g @anthropic-ai/claude-code

# 2. 加插件市场
claude plugin marketplace add jwangkun/claude-for-financial-services-cn

# 3. 装技能包（全量）
claude plugin install china-finance@claude-for-financial-services-cn

# 4. 或按需装单个垂直领域
claude plugin install investment-banking@claude-for-financial-services-cn
claude plugin install private-equity@claude-for-financial-services-cn
claude plugin install wealth-management@claude-for-financial-services-cn
claude plugin install fund-admin@claude-for-financial-services-cn
```

然后直接跟 Claude 对话：

```
你：写一份贵州茅台 2024 年报点评，中金格式
你：建一个比亚迪的 DCF 模型，WACC 用中债 10 年期
你：出一份半导体行业 A 股投资策略
你：帮我做一份路演 PPT
```

---

## 🧰 63 个 Skills 全览

### china-finance（31 个）— A 股研究核心

| 技能 | 干什么 |
|---|---|
| `china-comps` | 可比公司估值（PE/PB/PS） |
| `china-comps-analysis` | 深度可比分析 + 行业洞察 |
| `china-dcf` / `china-dcf-model` | DCF 估值（中债无风险利率） |
| `china-lbo-model` | 杠杆收购模型 |
| `china-3-statement-model` | 三表联动模型 |
| `china-earnings-analysis` | 季度/年度业绩点评 |
| `china-earnings-preview` | 财报前瞻（一致预期 vs 实际） |
| `china-model-update` | 覆盖模型自动更新 |
| `china-sector-overview` | 行业研究综述 |
| `china-catalyst-calendar` | 事件驱动日历 |
| `china-idea-generation` | A 股选股和标的筛选 |
| `china-thesis-tracker` | 投资观点跟踪 |
| `china-morning-note` | 晨会纪要 |
| `china-initiating-coverage` | 首次覆盖报告 |
| `china-deck-refresh` | 刷新 PPT 图表和数据 |
| `china-ib-check-deck` | 路演材料 QC |
| `china-ppt-template-creator` | PPT 模板技能 |
| `china-pptx-author` | 生成 .pptx 文件 |
| `china-xlsx-author` | 生成 .xlsx 文件 |
| `china-audit-xls` | Excel 模型审计 |
| `china-clean-data-xls` | 表格数据清洗 |
| `china-market-data` | iFind + AkShare 数据查询入口 |
| `china-variance-commentary` | 差异分析注释 |
| `china-accrual-schedule` | 应计项目时间表 |
| `china-break-trace` | 差异根因追踪 |
| `china-gl-recon` | 总账对账 |
| `china-roll-forward` | 数据滚动更新 |
| `china-deal-screening` | 项目初步筛选 |
| `china-skill-creator` | 创建自定义技能 |

### investment-banking（10 个）— A 股投行

| 技能 | 干什么 |
|---|---|
| `china-pitch-deck` | 填充 Pitch Deck 模板 |
| `china-merger-model` | 并购模型（ accretive/dilutive ） |
| `china-cim-builder` | CIM 信息备忘录 |
| `china-teaser` | 匿名交易概要页 |
| `china-buyer-list` | 战略/财务买方清单 |
| `china-datapack-builder` | 数据包构建 |
| `china-process-letter` | 竞标流程函 |
| `china-strip-profile` | 一页公司简介 |
| `china-deal-tracker` | 项目进度跟踪 |
| `china-competitive-analysis` | 竞争格局分析 |

### private-equity（9 个）— 私募股权

| 技能 | 干什么 |
|---|---|
| `china-dd-checklist` | 尽职调查清单 |
| `china-ic-memo` | 投委会 memo |
| `china-portfolio-monitoring` | 被投企业 KPI 跟踪 |
| `china-returns-analysis` | IRR/MOIC 回报分析 |
| `china-deal-sourcing` | 标的发现 |
| `china-unit-economics` | 单位经济模型 |
| `china-value-creation-plan` | 投后改善计划 |
| `china-ai-readiness` | AI 就绪度评估 |
| `china-dd-meeting-prep` | 管理层访谈准备 |

### wealth-management（5 个）— 财富管理

| 技能 | 干什么 |
|---|---|
| `china-client-report` | 客户报告 |
| `china-financial-plan` | 理财规划 |
| `china-investment-proposal` | 投资建议书 |
| `china-portfolio-rebalance` | 组合再平衡 |
| `china-tax-loss-harvesting` | 税损收割 |

### fund-admin（6 个）— 基金运营

| 技能 | 干什么 |
|---|---|
| `china-nav-tieout` | 净值核对 |
| `china-accrual-schedule` | 应计项目 |
| `china-break-trace` | 差异追踪 |
| `china-gl-recon` | 总账对账 |
| `china-roll-forward` | 滚动更新 |
| `china-variance-commentary` | 差异注释 |

### operations（2 个）— 运营

| 技能 | 干什么 |
|---|---|
| `china-kyc-doc-parse` | KYC 文档解析 |
| `china-kyc-rules` | KYC 规则引擎 |

---

## 🤖 4 个端到端智能体

技能可以单独用，也可以搭配智能体开箱即用：

| 智能体 | 一句话 |
|---|---|
| **china-pitch-agent** | 投行 Pitch — 从估值建模到路演 PPT 一条龙 |
| **china-market-researcher** | 行业研究 — 行业概览 → 竞争格局 → 标的池 |
| **china-earnings-reviewer** | 业绩点评 — 财报解读 → 模型更新 → 研报输出 |
| **china-model-builder** | 财务建模 — DCF / LBO / 三表，直接出 Excel |

---

## 🔌 数据层

| 服务 | 类型 | 干什么 |
|---|---|---|
| **ifind-mcp** | 付费 Tier-1 | 同花顺 iFind（股票/基金/宏观/债券/港美股/ESG/指数板块） |
| **akshare-mcp** | 免费 Tier-2 | AkShare 数据接口（行情 / 财报 / 行业 / 指数） |
| **china-news-mcp** | 免费 Tier-3 | 财经新闻和公告（财联社 / 东方财富 / 交易所公告） |

```bash
# 启动数据服务
python mcp-servers/akshare-mcp/server.py     # AkShare（免费）
python mcp-servers/ifind-mcp/server.py       # iFind（需密钥）
python mcp-servers/china-news-mcp/server.py  # 新闻（免费）
```

iFind 需要配置密钥：设置 `IFIND_AUTH_TOKEN` 环境变量，或写入 `mcp-servers/ifind-mcp/mcp_config.json`。
获取密钥：https://www.51ifind.com（MCP官网 → 个人中心 → 密钥）

---

## 🗂️ 项目结构

```
├── agent-plugins/              # 4 个智能体（开箱即用）
├── managed-agent-cookbooks/    # Managed Agent 部署模板
├── vertical-plugins/           # Skills 源文件（按垂直领域分）
│   ├── china-finance/          # 31 个 A 股研究技能
│   ├── investment-banking/     # 10 个投行技能
│   ├── private-equity/         # 9 个 PE 技能
│   ├── wealth-management/      # 5 个财富管理技能
│   ├── fund-admin/             # 6 个基金运营技能
│   └── operations/             # 2 个运营技能
├── mcp-servers/                # 数据接口
│   ├── akshare-mcp/           # AkShare（免费）
│   ├── ifind-mcp/             # 同花顺 iFind（付费）
│   └── china-news-mcp/        # 新闻公告（免费）
└── scripts/                    # 校验 / 部署 / 测试
```

---

## 🧪 自检

```bash
# 校验所有 manifest 和交叉引用
python3 scripts/check-china.py

# 测试部署模板
bash scripts/test-china-cookbooks.sh
```

---

## 🔄 与原版的关系

| | claude-for-financial-services | claude-for-financial-services-cn (本项目) |
|---|---|---|
| 定位 | 全球金融服务 | **中国 A 股市场** |
| 数据 | 商业数据商 API | **iFind (同花顺) + AkShare (开源)** |
| 研报 | 欧美投行格式 | **国内卖方研报格式** |
| 模型 | US GAAP | **中国会计准则** |
| 协议 | Apache 2.0 | **Apache 2.0** |

本项目是原版的**中国市场适配分支**，两者架构设计理念相同，数据层和内容层完全独立。

---

## 📜 License

[Apache License 2.0](./LICENSE)

---

<p align="center">
  Made with 🤖 by Claude · Data by <a href="https://www.51ifind.com">iFind</a> + <a href="https://akshare.akfamily.xyz/">AkShare</a><br>
  <sub>为 A 股市场的金融从业者打造</sub>
</p>
