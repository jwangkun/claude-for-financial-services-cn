# claude-for-financial-services-cn

🇨🇳 **63 个 Claude Skills，为 A 股金融从业者而生**

基于 Anthropic 官方 [claude-for-financial-services](https://github.com/anthropics/claude-for-financial-services) 深度适配国内市场，现已开源。

---

## 这是什么？

一套可以直接给 Claude 装上的 **金融专业技能包**。装了之后，你跟 Claude 说"帮我写一份茅台年报点评"或者"建一个宁德时代的 DCF 模型"，它就知道 A 股的格式、数据源和会计准则，直接出活儿。

> 一句话：**把 Anthropic 为华尔街投行做的 AI 助手，搬到了 A 股。**

| | 原版 (Wall Street) | 本项目 (A 股) |
|---|---|---|
| 数据 | Bloomberg / FactSet / PitchBook | **Wind**（万得）+ **iFind**（同花顺）+ **AkShare**（免费开源） |
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
| `china-market-data` | Wind + iFind + AkShare 数据查询入口 |
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

# 🔌 数据层

本项目采用 **多级数据源优先级策略**：商业数据源优先，自动降级到免费数据源，确保任何场景都有数据可用。

| 优先级 | 服务 | 类型 | 说明 |
|---|---|---|---|
| **Tier-0** | wind-mcp | 💰 付费 | 万得 Wind — 全市场最全面金融数据（A 股/港美股/基金/指数/债券/宏观/研报/分析） |
| **Tier-1** | ifind-mcp | 💰 付费 | 同花顺 iFind — 覆盖 A 股全量数据（行情/财务/基金/宏观/债券/港美股/指数板块） |
| **Tier-2** | akshare-mcp | 🆓 免费 | AkShare 开源 — 行情 / 财报 / 行业 / 指数（iFind 不可用时自动降级） |
| **Tier-3** | china-news-mcp | 🆓 免费 | 财经新闻和公告（财联社 / 东方财富 / 交易所公告） |

### 🔑 数据源密钥注册

> **所有付费数据源均需注册获取 API Key 才能使用。** 免费数据源（AkShare、china-news）无需密钥，开箱即用。

| 数据源 | 注册/申请地址 | 密钥环境变量 | 说明 |
|---|---|---|---|
| **万得 Wind** | [https://aifinmarket.wind.com.cn/#/home](https://aifinmarket.wind.com.cn/#/home) | `WIND_API_KEY` | 注册后在「AI 金融终端」获取 API Key（以 `ak_` 开头） |
| **同花顺 iFind** | [https://mcp.51ifind.com/](https://mcp.51ifind.com/) | `IFIND_AUTH_TOKEN` | 登录 iFind MCP 平台 → 个人中心 → 密钥管理获取 JWE Token |
| **AkShare** | 无需注册 | — | 🆓 免费开源，直接使用 |
| **财经新闻** | 无需注册 | — | 🆓 免费开源，直接使用 |

<details>
<summary>📖 各数据源注册指南</summary>

#### 万得 Wind — API Key 申请

1. 访问 [Wind AI 金融终端](https://aifinmarket.wind.com.cn/#/home)
2. 注册/登录万得账号
3. 在「API 管理」中创建新的 API Key
4. Key 格式以 `ak_` 开头
5. 配置环境变量：
   ```bash
   export WIND_API_KEY="ak_your-key-here"
   ```
6. 或写入配置文件 `mcp-servers/wind-mcp/mcp_config.json`（已被 `.gitignore` 排除）

#### 同花顺 iFind — Auth Token 申请

1. 访问 [iFind MCP 平台](https://mcp.51ifind.com/)
2. 登录同花顺账号
3. 进入「个人中心」→「MCP 密钥管理」
4. 复制 JWE Token
5. 配置环境变量：
   ```bash
   export IFIND_AUTH_TOKEN="your-jwe-token-here"
   ```
6. 或写入配置文件 `mcp-servers/ifind-mcp/mcp_config.json`（已被 `.gitignore` 排除）

> 💡 **版本说明：**
> - 🆓 **免费版**：支持 stock / bond / index 基础查询（并发 2/s）
> - 💰 **个人版**：解锁 fund / news / edb 全量服务（并发 5/s）
> - 🏢 **企业版**：全量 + 高并发（并发 10/s）

#### AkShare — 免费开源

无需注册，无需密钥，开箱即用。访问 [AkShare 官网](https://akshare.akfamily.xyz/) 了解详情。

#### 财经新闻 — 免费开源

无需注册，无需密钥。数据来源包括财联社、东方财富、交易所公告等公开渠道。

</details>

### iFind 数据源（新增）

iFind MCP 封装了同花顺 iFind 的远程 MCP 服务，提供 **31 个工具**，覆盖 **7 大服务域**：

| 服务域 | 工具数 | 能力 |
|---|---|---|
| **stock** | 8 | 股票搜索、实时行情、历史K线、财务报表、一致预期、股东/机构、公司事件、ESG |
| **fund** | 7 | 基金搜索、基金净值、基金持仓、基金经理、基金对比、业绩归因、基金排名 |
| **edb** | 2 | 宏观经济数据库搜索、指标查询与下载 |
| **news** | 3 | 新闻搜索、热点追踪、公告查询 |
| **bond** | 4 | 债券搜索、债券行情、信用评级、到期收益 |
| **global_stock** | 5 | 港股/美股搜索、全球市场行情、港美股财务、港美股事件、跨市场对比 |
| **index** | 2 | 指数板块搜索、指数成分股 |

#### 安装依赖

```bash
cd mcp-servers/ifind-mcp
pip install -r requirements.txt
```

#### 配置密钥

> 密钥注册详见上方「🔑 数据源密钥注册」章节。

**方式一：环境变量（推荐）**

```bash
export IFIND_AUTH_TOKEN="your-jwe-token-here"
```

**方式二：配置文件**

创建 `mcp-servers/ifind-mcp/mcp_config.json`（已被 `.gitignore` 排除，不会提交）：

```json
{
  "auth_token": "your-jwe-token-here"
}
```

#### 启动服务

```bash
# stdio 模式（本地开发，Claude Desktop / Claude Code 直连）
python3 mcp-servers/ifind-mcp/server.py

# SSE 模式（远程部署，Managed Agent 使用）
python3 mcp-servers/ifind-mcp/server.py --transport sse --port 8002
```

#### Claude Desktop 配置

在 `~/Library/Application Support/Claude/claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "ifind": {
      "command": "python",
      "args": ["/path/to/mcp-servers/ifind-mcp/server.py"],
      "env": {
        "IFIND_AUTH_TOKEN": "your-jwe-token-here"
      }
    }
  }
}
```

#### 使用示例

配置完成后，Claude 会自动调用 iFind 工具获取数据，所有 31 个工具以 `ifind_` 前缀命名：

```
你：查一下贵州茅台最新的财务数据
    → Claude 调用 ifind_get_stock_financials("600519.SH")

你：帮我对比宁德时代和比亚迪的估值
    → Claude 调用 ifind_get_stock_info("300750.SZ,002594.SZ")

你：最近宏观经济数据怎么样？
    → Claude 调用 ifind_search_edb + ifind_get_edb_data

你：搜一下半导体板块有哪些基金
    → Claude 调用 ifind_search_funds("半导体")
```

当 iFind 返回错误或该服务域不可用时（如免费版调用 fund/news），系统自动降级到 AkShare 获取替代数据。若已配置 Wind API Key，Wind 将作为最高优先级数据源（Tier-0）被优先调用。

### Wind 数据源（Tier-0，新增）

Wind MCP 封装了万得的远程 MCP 服务，提供 **44 个工具**，覆盖 **8 大服务域**：

| 服务域 | 工具数 | 能力 |
|---|---|---|
| **stock_data** | 8 | A 股搜索、实时行情、历史K线、财务报表、一致预期、股东机构、公司事件、技术指标 |
| **global_stock_data** | 5 | 港股/美股搜索、全球行情、跨国对比、ADR、GDR |
| **fund_data** | 6 | 基金搜索、净值、持仓、经理、对比、业绩归因 |
| **index_data** | 5 | 指数搜索、成分股、权重、行业分布、指数对比 |
| **bond_data** | 5 | 债券搜索、行情、信用评级、到期收益、利差分析 |
| **financial_docs** | 5 | 研报搜索、公告查询、财报原文、招股书、评级报告 |
| **economic_data** | 5 | 宏观指标搜索、数据下载、国别对比、预测数据、领先指标 |
| **analytics_data** | 5 | 因子分析、回测、风险模型、组合优化、情景分析 |

#### 配置密钥

> 密钥注册详见上方「🔑 数据源密钥注册」章节。

**方式一：环境变量（推荐）**

```bash
export WIND_API_KEY="ak_your-key-here"
```

**方式二：配置文件**

创建 `mcp-servers/wind-mcp/mcp_config.json`（已被 `.gitignore` 排除，不会提交）：

```json
{
  "api_key": "ak_your-key-here"
}
```

#### 安装依赖

```bash
cd mcp-servers/wind-mcp
pip install -r requirements.txt
```

#### 启动服务

```bash
# stdio 模式（本地开发，Claude Desktop / Claude Code 直连）
python3 mcp-servers/wind-mcp/server.py

# SSE 模式（远程部署，Managed Agent 使用）
python3 mcp-servers/wind-mcp/server.py --transport sse --port 8003
```

#### 使用示例

配置完成后，Claude 会自动调用 Wind 工具获取数据，所有 44 个工具以 `wind_` 前缀命名：

```
你：建一个宁德时代的 DCF 模型
    → Claude 调用 wind_get_stock_financials("宁德时代") + wind_get_economic_data("中债10年期")

你：帮我对比中美新能源车企估值
    → Claude 调用 wind_compare_global_stocks("中美新能源车企估值对比")

你：搜一下白酒行业的深度研报
    → Claude 调用 wind_search_research("白酒行业深度研究")

你：沪深300动量因子近一年表现如何？
    → Claude 调用 wind_factor_analysis("沪深300动量因子近一年")
```

当 Wind 不可用时，系统自动降级到 iFind (Tier-1) → AkShare (Tier-2)。可通过 `IFIND_DATA_SOURCE_MODE` 环境变量控制降级策略（`wind-only`, `wind-fallback`, `ifind-fallback`, `akshare-only`）。

### AkShare 数据源（免费备选）

```
python3 mcp-servers/akshare-mcp/server.py     # AkShare — 9 个工具（免费无需密钥）
python3 mcp-servers/china-news-mcp/server.py  # 新闻公告 — 免费无需密钥
```

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
│   ├── wind-mcp/              # 万得 Wind（付费，Tier-0）
│   ├── ifind-mcp/             # 同花顺 iFind（付费，Tier-1）
│   ├── akshare-mcp/           # AkShare（免费，Tier-2）
│   └── china-news-mcp/        # 新闻公告（免费，Tier-3）
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
| 数据 | 商业数据商 API | **Wind (万得) + iFind (同花顺) + AkShare (开源)** |
| 研报 | 欧美投行格式 | **国内卖方研报格式** |
| 模型 | US GAAP | **中国会计准则** |
| 协议 | Apache 2.0 | **Apache 2.0** |

本项目是原版的**中国市场适配分支**，两者架构设计理念相同，数据层和内容层完全独立。

---

## 📜 License

[Apache License 2.0](./LICENSE)

---

<p align="center">
  Made with 🤖 by Claude<br>
  Data by <a href="https://aifinmarket.wind.com.cn/#/home">Wind 万得</a> + <a href="https://mcp.51ifind.com/">iFind 同花顺</a> + <a href="https://akshare.akfamily.xyz/">AkShare</a><br>
  <sub>为 A 股市场的金融从业者打造</sub>
</p>

---

## 🙏 致谢

感谢以下数据服务商为本项目提供数据支持：

- **[万得 Wind](https://aifinmarket.wind.com.cn/#/home)** — 中国金融数据行业的标杆，提供全市场最全面的金融数据覆盖（A 股、港美股、基金、债券、宏观、研报等 44+ 工具），为项目的 Tier-0 核心数据源。
- **[同花顺 iFind](https://mcp.51ifind.com/)** — 国内领先的金融数据终端，提供 31 个专业工具覆盖 7 大服务域（行情/财务/基金/宏观/债券/港美股/指数），为项目的 Tier-1 核心数据源。
- **[AkShare](https://akshare.akfamily.xyz/)** — 优秀的开源金融数据接口库，由 Albert King 及社区维护，提供免费的 A 股行情、财报、行业、指数数据，为项目的 Tier-2 免费备选数据源。

> 没有他们的数据支持，这个项目不可能实现。如果你觉得本项目对你有帮助，也请支持这些优秀的数据服务商。
