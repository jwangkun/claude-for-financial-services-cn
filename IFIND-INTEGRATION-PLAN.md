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
