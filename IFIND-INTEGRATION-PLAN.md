# 同花顺 iFind 数据源集成计划

## 背景

当前 `china/` 目录下的金融数据层仅依赖两个免费开源数据源：
- **akshare-mcp** — A 股行情/财报/行业/指数（基于东方财富）
- **china-news-mcp** — 财经新闻和公告

需要集成同花顺 iFind 作为**付费级数据源**，同时保留 AkShare 作为免费备选。架构需支持后续扩展更多数据商（如 Wind、Tushare、聚宽等）。

## 需求分析

### 1. iFind MCP Server
- 在 `china/mcp-servers/ifind-mcp/` 下创建标准 MCP Server
- 复用 `ifind-finance-data-1.1.0/` 的 `call.py` / `call-node.js` 调用逻辑
- 封装为 FastMCP stdio/SSE 服务，与现有 akshare-mcp 架构对齐
- 覆盖 iFind 7 大服务域：stock / fund / edb / news / bond / global_stock / index
- 密钥通过 `mcp_config.json` 管理，支持环境变量覆盖

### 2. Skill 层更新
- 更新 `china-market-data` SKILL.md，增加 iFind 作为 **Tier-1 付费数据源**
- 定义数据源优先级策略：iFind（付费精确数据）> AkShare（免费备选）
- 保持 AkShare 工具不变，确保向后兼容

### 3. Agent Prompt 更新
- 4 个 Agent 的 `tools` frontmatter 增加 `mcp__ifind__*`
- Workflow 中增加 iFind 数据获取指引
- 更新数据源优先级说明

### 4. Managed Agent Cookbook 更新
- 4 个 `agent.yaml` 增加 ifind mcp_toolset 和 mcp_server 配置
- 增加 `IFIND_MCP_URL` / `IFIND_AUTH_TOKEN` 环境变量引用

### 5. 文档与校验更新
- CLAUDE.md 增加 iFind MCP 启动说明
- README.md 更新数据层表格
- check-china.py 增加 ifind-mcp 校验

## 任务清单

| # | 任务 | 文件 | 状态 |
|---|------|------|------|
| 1 | 创建 iFind MCP Server | `china/mcp-servers/ifind-mcp/server.py` | ✅ 完成 |
| 2 | 创建 iFind MCP requirements | `china/mcp-servers/ifind-mcp/requirements.txt` | ✅ 完成 |
| 3 | 创建 iFind MCP config 模板 | `china/mcp-servers/ifind-mcp/mcp_config.json` | ✅ 完成 |
| 4 | 更新 china-market-data skill | `china/vertical-plugins/china-finance/skills/china-market-data/SKILL.md` | ✅ 完成 |
| 5 | 更新 china-earnings-reviewer agent | `china/agent-plugins/china-earnings-reviewer/agents/china-earnings-reviewer.md` | ✅ 完成 |
| 6 | 更新 china-market-researcher agent | `china/agent-plugins/china-market-researcher/agents/china-market-researcher.md` | ✅ 完成 |
| 7 | 更新 china-model-builder agent | `china/agent-plugins/china-model-builder/agents/china-model-builder.md` | ✅ 完成 |
| 8 | 更新 china-pitch-agent agent | `china/agent-plugins/china-pitch-agent/agents/china-pitch-agent.md` | ✅ 完成 |
| 9 | 更新 4 个 managed-agent agent.yaml | `china/managed-agent-cookbooks/*/agent.yaml` | ✅ 完成 |
| 10 | 更新 CLAUDE.md | `china/CLAUDE.md` | ✅ 完成 |
| 11 | 更新 README.md | `china/README.md` | ✅ 完成 |
| 12 | 更新 check-china.py | `china/scripts/check-china.py` | ✅ 完成 |
| 13 | 运行 check-china.py 验证 | — | ✅ 通过 |

## 架构设计：可扩展数据源层

```
mcp-servers/
├── akshare-mcp/       # 免费 — A 股基础数据（保留）
├── china-news-mcp/    # 免费 — 新闻公告（保留）
├── ifind-mcp/         # 付费 — 同花顺 iFind（新增）
└── [future]-mcp/      # 预留 — Wind / Tushare / 聚宽等
```

数据源优先级策略（在 skill 中定义）：
1. **iFind** — 精确财务、宏观经济、债券、港美股、ESG（需密钥）
2. **AkShare** — 基础行情、行业分类、指数（免费无限制）
3. **china-news** — 新闻和公告（免费）

## iFind MCP Server 工具映射

| MCP 工具名 | iFind server_type | iFind tool_name |
|-----------|-------------------|-----------------|
| `ifind_search_stocks` | stock | search_stocks |
| `ifind_get_stock_summary` | stock | get_stock_summary |
| `ifind_get_stock_info` | stock | get_stock_info |
| `ifind_get_stock_shareholders` | stock | get_stock_shareholders |
| `ifind_get_stock_financials` | stock | get_stock_financials |
| `ifind_get_risk_indicators` | stock | get_risk_indicators |
| `ifind_get_stock_events` | stock | get_stock_events |
| `ifind_get_esg_data` | stock | get_esg_data |
| `ifind_search_funds` | fund | search_funds |
| `ifind_get_fund_profile` | fund | get_fund_profile |
| `ifind_get_fund_market_performance` | fund | get_fund_market_performance |
| `ifind_get_fund_ownership` | fund | get_fund_ownership |
| `ifind_get_fund_portfolio` | fund | get_fund_portfolio |
| `ifind_get_fund_financials` | fund | get_fund_financials |
| `ifind_get_fund_company_info` | fund | get_fund_company_info |
| `ifind_search_edb` | edb | search_edb |
| `ifind_get_edb_data` | edb | get_edb_data |
| `ifind_search_news` | news | search_news |
| `ifind_search_notice` | news | search_notice |
| `ifind_search_trending_news` | news | search_trending_news |
| `ifind_bond_basic_info` | bond | bond_basic_info |
| `ifind_bond_market_data` | bond | bond_market_data |
| `ifind_bond_financial_data` | bond | bond_financial_data |
| `ifind_bond_special_data` | bond | bond_special_data |
| `ifind_search_global_stocks` | global_stock | search_global_stocks |
| `ifind_global_stock_profile` | global_stock | global_stock_profile |
| `ifind_global_stock_quotes` | global_stock | global_stock_quotes |
| `ifind_global_stock_financial` | global_stock | global_stock_financial |
| `ifind_global_stock_events` | global_stock | global_stock_events |
| `ifind_index_data` | index | index_data |
| `ifind_sector_data` | index | sector_data |

---

## 万得 Wind 数据源集成（Tier-0）

### 背景

在 iFind 集成完成后，进一步集成万得 Wind 作为最高优先级数据源（Tier-0）。Wind 是中国金融数据行业的标杆，覆盖面最广、数据最全面。

### Wind MCP Server

- 路径：`china/mcp-servers/wind-mcp/`
- 架构：Python FastMCP 封装万得远程 JSON-RPC 2.0 API
- 基地址：`https://mcp.wind.com.cn`
- 认证：`Authorization: Bearer <WIND_API_KEY>`（Key 格式以 `ak_` 开头）
- 工具数：44 个，覆盖 8 大服务域
- SSE 默认端口：8003
- 密钥申请：https://aifinmarket.wind.com.cn/#/home

### 工具映射表

| MCP 工具名 | server_type | 功能 |
|-----------|-------------|------|
| `wind_search_stocks` | stock_data | A股智能选股 |
| `wind_get_stock_info` | stock_data | 股票基本资料/行情 |
| `wind_get_stock_financials` | stock_data | 财务报表/指标 |
| `wind_get_stock_shareholders` | stock_data | 股东/机构 |
| `wind_get_stock_events` | stock_data | 公司事件 |
| `wind_get_stock_consensus` | stock_data | 一致预期 |
| `wind_get_stock_technical` | stock_data | 技术指标 |
| `wind_get_stock_summary` | stock_data | 股票信息摘要 |
| `wind_search_global_stocks` | global_stock_data | 港美股搜索 |
| `wind_get_global_stock_info` | global_stock_data | 港美股行情 |
| `wind_get_global_stock_financials` | global_stock_data | 港美股财务 |
| `wind_get_global_stock_events` | global_stock_data | 港美股事件 |
| `wind_compare_global_stocks` | global_stock_data | 跨市场对比 |
| `wind_search_funds` | fund_data | 基金搜索 |
| `wind_get_fund_info` | fund_data | 基金资料 |
| `wind_get_fund_nav` | fund_data | 基金净值 |
| `wind_get_fund_portfolio` | fund_data | 基金持仓 |
| `wind_compare_funds` | fund_data | 基金对比 |
| `wind_get_fund_performance_attribution` | fund_data | 业绩归因 |
| `wind_search_indices` | index_data | 指数搜索 |
| `wind_get_index_info` | index_data | 指数行情 |
| `wind_get_index_constituents` | index_data | 指数成分股 |
| `wind_get_index_weights` | index_data | 指数权重 |
| `wind_compare_indices` | index_data | 指数对比 |
| `wind_search_bonds` | bond_data | 债券搜索 |
| `wind_get_bond_info` | bond_data | 债券行情 |
| `wind_get_bond_rating` | bond_data | 信用评级 |
| `wind_get_bond_yield` | bond_data | 到期收益 |
| `wind_get_bond_spread` | bond_data | 利差分析 |
| `wind_search_research` | financial_docs | 研报搜索 |
| `wind_get_announcements` | financial_docs | 公告查询 |
| `wind_get_financial_report` | financial_docs | 财报原文 |
| `wind_get_prospectus` | financial_docs | 招股书 |
| `wind_get_credit_report` | financial_docs | 评级报告 |
| `wind_search_economic_indicators` | economic_data | 宏观指标搜索 |
| `wind_get_economic_data` | economic_data | 宏观数据下载 |
| `wind_compare_economic_data` | economic_data | 国别对比 |
| `wind_get_economic_forecast` | economic_data | 预测数据 |
| `wind_get_leading_indicators` | economic_data | 领先指标 |
| `wind_factor_analysis` | analytics_data | 因子分析 |
| `wind_backtest` | analytics_data | 回测 |
| `wind_risk_model` | analytics_data | 风险模型 |
| `wind_portfolio_optimization` | analytics_data | 组合优化 |
| `wind_scenario_analysis` | analytics_data | 情景分析 |

### 数据源优先级（更新后）

1. **Wind** (Tier-0) — 全市场最全面金融数据，44 工具覆盖 8 大服务域
2. **iFind** (Tier-1) — 精确财务、宏观、债券、港美股、ESG
3. **AkShare** (Tier-2) — 免费备选，基础行情/财报/行业/指数
4. **china-news** (Tier-3) — 免费新闻和公告

### 任务清单

| # | 任务 | 文件 | 状态 |
|---|------|------|------|
| 1 | 创建 Wind MCP Server | `mcp-servers/wind-mcp/server.py` | ✅ 完成 |
| 2 | 创建 Wind MCP requirements | `mcp-servers/wind-mcp/requirements.txt` | ✅ 完成 |
| 3 | 创建 Wind MCP config 模板 | `mcp-servers/wind-mcp/mcp_config.json` | ✅ 完成 |
| 4 | 更新 6 个 .mcp.json | `vertical-plugins/*/.mcp.json` | ✅ 完成 |
| 5 | 更新 4 个 agent .md | `agent-plugins/*/agents/*.md` | ✅ 完成 |
| 6 | 更新 4 个 agent.yaml | `managed-agent-cookbooks/*/agent.yaml` | ✅ 完成 |
| 7 | 更新 CLAUDE.md | `CLAUDE.md` | ✅ 完成 |
| 8 | 更新 check-china.py | `scripts/check-china.py` | ✅ 完成 |
| 9 | 更新 README.md | `README.md` | ✅ 完成 |
| 10 | 更新 SKILL.md 文件 | `vertical-plugins/*/skills/*/SKILL.md` | ✅ 完成 |
