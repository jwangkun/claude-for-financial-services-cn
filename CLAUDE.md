# CLAUDE.md — China Financial Services Plugins

China-market equivalent of the main `financial-services` repo. All data sourced from Chinese financial data providers (iFind 同花顺 / AkShare / Tushare). iFind is the Tier-1 paid source; AkShare is the Tier-2 free fallback.

## Source of truth

- **Skills** are authored in `vertical-plugins/china-finance/skills/`.
- **Agent system prompts** are at `agent-plugins/<slug>/agents/<slug>.md`.
- Agent plugins bundle vendored copies of their skills. **Never edit bundled copies directly.**

## Core data layer

Three MCP servers (multi-tier architecture):

```bash
# Start the AkShare data server (A-share market data, free)
python3 mcp-servers/akshare-mcp/server.py

# Start the iFind data server (同花顺, paid — requires IFIND_AUTH_TOKEN)
python3 mcp-servers/ifind-mcp/server.py

# Start the China news server (free)
python3 mcp-servers/china-news-mcp/server.py
```

All default to stdio transport. For deployment, use `--transport sse --port <PORT>`.

**Data source priority:**
1. **iFind MCP** (Tier-1 paid) — precise financials, macro/EDB, bonds, HK/US stocks, ESG
2. **AkShare MCP** (Tier-2 free) — basic quotes, industry classification, indices
3. **china-news MCP** (Tier-3 free) — news and announcements

iFind requires an auth token: set `IFIND_AUTH_TOKEN` env var or write to `mcp-servers/ifind-mcp/mcp_config.json`.
Get your key at https://www.51ifind.com (MCP官网 → 个人中心 → 密钥).

AkShare documentation: https://akshare.akfamily.xyz/

## Commands

```bash
# Validate everything before push
python3 scripts/check-china.py

# Test cookbook structure (dry-run deployment)
bash scripts/test-china-cookbooks.sh

# Deploy a cookbook (dry-run or live)
bash scripts/deploy-managed-agent.sh <slug> [--dry-run]

# After editing a skill in vertical-plugins/, propagate to all agents that bundle it
python3 scripts/sync-china-skills.py

# Cross-agent handoff orchestration (reference implementation)
python3 scripts/orchestrate.py

# Validate worker output against a JSON schema
python3 scripts/validate.py <output.json> <schema.json|schema.yaml>
```

## Key conventions

- Agent frontmatter: every `agents/*.md` must have YAML `---` with `name` + `description`.
- Tool references in agent frontmatter use `mcp__akshare__*`, `mcp__ifind__*`, and `mcp__china-news__*` syntax.
- Stock codes follow A-share conventions: 6-digit codes, no exchange prefix (e.g., "600519", "000001").

## Agents (4 China-market)

- `china-pitch-agent` — A-share pitch book (comps, DCF, LBO, deck)
- `china-market-researcher` — A-share sector research
- `china-earnings-reviewer` — A-share earnings analysis
- `china-model-builder` — DCF, LBO, 3-statement for Chinese equities

## Dependencies

Install per-server:
```bash
pip install -r mcp-servers/akshare-mcp/requirements.txt
pip install -r mcp-servers/ifind-mcp/requirements.txt
pip install -r mcp-servers/china-news-mcp/requirements.txt
```
