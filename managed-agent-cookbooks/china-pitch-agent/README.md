# China Pitch Agent — managed-agent cookbook

## Overview

Comps, precedents, DCF, LBO → branded pitch deck for A-share targets, end to end. Same source as the [`china-pitch-agent`](../../agent-plugins/china-pitch-agent) Cowork plugin — this directory is the Managed Agent cookbook for `POST /v1/agents`.

## Deploy

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export AKSHARE_MCP_URL=...
../../scripts/deploy-managed-agent.sh china-pitch-agent
```

## Steering events

See [`steering-examples.json`](./steering-examples.json).

## Security & handoffs

Task-decomposition split — less about untrusted inputs (data comes from iFind / AkShare MCP), more about parallelism and artifact isolation. Exactly one worker holds `Write`:

| Leaf | Tools | Connectors |
|---|---|---|
| `researcher` | `Read`, `Grep` | iFind / AkShare (read-only) |
| `modeler` | `Read`, `Bash` (sandboxed) | iFind / AkShare (read-only) |
| **`deck-writer`** (Write-holder) | `Read`, `Write`, `Edit` | None |

Artifacts land in `./out/pitch-<target>.pptx` and `./out/model.xlsx` via `pptx-author` / `xlsx-author`.

**Handoff:** to rebuild the model after a thesis change, the orchestrator emits a `handoff_request` for `china-model-builder`; `scripts/orchestrate.py` (or your workflow engine) routes it as a new steering event. See the script for the allowlist + payload-validation pattern.
