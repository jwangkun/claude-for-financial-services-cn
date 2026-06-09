#!/usr/bin/env python3
"""Check script for china/ directory — validates structure, references, and drift.

Usage:
    python3 scripts/check-china.py

Checks:
1. All vertical-plugins skills have valid YAML frontmatter
2. All agent-plugins agents/*.md have valid YAML frontmatter
3. Agent plugin skills are in sync with their vertical-plugin sources
4. No cross-references to Western data providers
5. All MCP servers have server.py, requirements.txt, and mcp_config.json
6. All .mcp.json files have consistent MCP server registrations
7. All cookbook agent.yaml and subagent yaml have correct MCP references
8. Agent prompts that reference Wind/iFind have matching cookbook config
"""

import json
import os
import re
import sys
from pathlib import Path

CHINA_DIR = Path(__file__).resolve().parent.parent
_ERROR_COUNT = 0

REQUIRED_AGENT_FRONTMATTER = {"name", "description"}
FORBIDDEN_PATTERNS = [
    r"capiq",
    r"factset",
    r"S&P",
    r"Capital IQ",
    r"Bloomberg",
    r"EDGAR",
    r"Daloopa",
    r"Morningstar",
    r"Kensho",
    r"kfinance",
]

MCP_SERVER_CONFIG = {
    "ifind-mcp":  {"config_required": True,  "config_key": "IFIND_AUTH_TOKEN", "mcp_name": "ifind"},
    "wind-mcp":   {"config_required": True,  "config_key": "WIND_API_KEY",     "mcp_name": "wind"},
    "akshare-mcp":{"config_required": False, "config_key": None,               "mcp_name": "akshare"},
    "china-news-mcp": {"config_required": False, "config_key": None,           "mcp_name": "china-news"},
}

ALL_MCP_NAMES = {cfg["mcp_name"] for cfg in MCP_SERVER_CONFIG.values()}


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def log_error(msg: str) -> None:
    global _ERROR_COUNT
    _ERROR_COUNT += 1
    print(f"  ✖  {msg}", file=sys.stderr)


def log_ok(msg: str) -> None:
    print(f"  ✓  {msg}")


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter as a dict (minimal, no pyyaml dep)."""
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    result = {}
    for line in m.group(1).strip().split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            result[key.strip()] = val.strip()
    return result


# ---------------------------------------------------------------------------
# 1. Skill checks
# ---------------------------------------------------------------------------

def check_skills(vertical: str) -> list[str]:
    """Check all skill files in a vertical plugin. Return skill dir names."""
    skill_dir = CHINA_DIR / "vertical-plugins" / vertical / "skills"
    if not skill_dir.exists():
        log_error(f"Missing skills directory: {skill_dir}")
        return []

    found = []
    for entry in sorted(skill_dir.iterdir()):
        if not entry.is_dir():
            continue
        skill_file = entry / "SKILL.md"
        if not skill_file.exists():
            log_error(f"Missing SKILL.md in {entry}")
            continue
        text = skill_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if not fm.get("name"):
            log_error(f"{skill_file}: missing 'name' in frontmatter")
        if not fm.get("description"):
            log_error(f"{skill_file}: missing 'description' in frontmatter")
        for pat in FORBIDDEN_PATTERNS:
            if re.search(pat, text, re.IGNORECASE):
                log_error(f"{skill_file}: contains forbidden pattern '{pat}'")
        found.append(entry.name)
        log_ok(f"skill {vertical}/{entry.name}")
    return found


# ---------------------------------------------------------------------------
# 2. Agent prompt checks
# ---------------------------------------------------------------------------

def check_agent(agent: str) -> list[str]:
    """Check an agent plugin's system prompt and bundled skills."""
    agent_dir = CHINA_DIR / "agent-plugins" / agent
    prompt_file = agent_dir / "agents" / f"{agent}.md"
    if not prompt_file.exists():
        log_error(f"Missing agent prompt: {prompt_file}")
        return []

    text = prompt_file.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    for field in REQUIRED_AGENT_FRONTMATTER:
        if not fm.get(field):
            log_error(f"{prompt_file}: missing frontmatter field '{field}'")

    for pat in FORBIDDEN_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            log_error(f"{prompt_file}: contains forbidden pattern '{pat}'")

    log_ok(f"agent {agent}/{agent}.md")

    # Check for duplicate workflow sections
    workflow_count = len(re.findall(r"(?:Enhanced|Basic)\s+Workflow", text))
    if workflow_count > 1:
        log_error(f"{prompt_file}: contains duplicate workflow sections — remove one")

    # Check guardrails include Wind
    if "UNSOURCED" in text and "iFind" in text and "Wind" not in text:
        log_error(f"{prompt_file}: guardrail mentions iFind/AkShare but not Wind")

    return []


# ---------------------------------------------------------------------------
# 3. Skill drift detection
# ---------------------------------------------------------------------------

def check_skill_drift(vertical: str, agent: str) -> None:
    """Check that agent's bundled skills match the vertical plugin source."""
    vert_skills = CHINA_DIR / "vertical-plugins" / vertical / "skills"
    agent_skills = CHINA_DIR / "agent-plugins" / agent / "skills"
    if not agent_skills.exists():
        log_ok(f"agent {agent}: no bundled skills (ok for now)")
        return

    for agent_entry in sorted(agent_skills.iterdir()):
        if not agent_entry.is_dir():
            continue
        agent_file = agent_entry / "SKILL.md"
        source_file = vert_skills / agent_entry.name / "SKILL.md"
        if not source_file.exists():
            log_error(f"agent {agent}/{agent_entry.name}: no matching source in {vertical}")
            continue
        if not agent_file.exists():
            log_error(f"agent {agent}/{agent_entry.name}: missing SKILL.md")
            continue

        source_text = source_file.read_text(encoding="utf-8")
        agent_text = agent_file.read_text(encoding="utf-8")
        if source_text.strip() != agent_text.strip():
            log_error(f"agent {agent}/{agent_entry.name}: DRIFT from vertical source — run sync-china-skills.py")


# ---------------------------------------------------------------------------
# 4. MCP server file checks
# ---------------------------------------------------------------------------

def check_mcp_servers() -> None:
    """Validate all MCP server directories have required files."""
    mcp_dir = CHINA_DIR / "mcp-servers"
    if not mcp_dir.exists():
        log_error("Missing mcp-servers/ directory")
        return

    for server_name, config in MCP_SERVER_CONFIG.items():
        server_path = mcp_dir / server_name
        if not server_path.is_dir():
            log_error(f"MCP server {server_name}: directory missing")
            continue

        for required_file in ["server.py", "requirements.txt"]:
            if not (server_path / required_file).exists():
                log_error(f"MCP server {server_name}: missing {required_file}")

        if config["config_required"]:
            if (server_path / "mcp_config.json").exists():
                log_ok(f"MCP server {server_name}/mcp_config.json")
            else:
                log_error(f"MCP server {server_name}: missing mcp_config.json")
        else:
            log_ok(f"MCP server {server_name} (no config needed)")


# ---------------------------------------------------------------------------
# 5. .mcp.json consistency check
# ---------------------------------------------------------------------------

def check_mcp_json() -> None:
    """Verify all .mcp.json files register the expected MCP servers consistently.

    All vertical-plugins that reference Wind should also have ifind (Tier-1),
    akshare (Tier-2), and china-news (Tier-3) for complete fallback chains.
    """
    vert_dir = CHINA_DIR / "vertical-plugins"
    for entry in sorted(vert_dir.iterdir()):
        if not entry.is_dir():
            continue
        mcp_json = entry / ".mcp.json"
        if not mcp_json.exists():
            continue

        try:
            config = json.loads(mcp_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            log_error(f"{mcp_json}: invalid JSON — {e}")
            continue

        servers = config.get("mcpServers", {})
        registered = set(servers.keys())
        missing = ALL_MCP_NAMES - registered

        if missing:
            log_error(f"{mcp_json}: missing MCP servers: {', '.join(sorted(missing))}")
        else:
            log_ok(f".mcp.json {entry.name}: all 4 MCP servers registered")

        # Check Wind has env block
        if "wind" in servers and "env" not in servers["wind"]:
            log_error(f"{mcp_json}: wind entry missing 'env' block — add WIND_API_KEY forwarding")


# ---------------------------------------------------------------------------
# 6. Cookbook checks
# ---------------------------------------------------------------------------

def _agent_prompt_needs_mcp(cb_name: str) -> dict[str, bool]:
    """Check agent prompt to see which MCP servers are referenced."""
    needs = {name: False for name in ALL_MCP_NAMES}
    prompt_file = (
        CHINA_DIR / "agent-plugins" / cb_name / "agents" / f"{cb_name}.md"
    )
    if not prompt_file.exists():
        return needs
    text = prompt_file.read_text(encoding="utf-8")
    for mcp_name in ALL_MCP_NAMES:
        patterns = [f"mcp__{mcp_name}__", f"{mcp_name}-mcp", f"mcp_server_name: {mcp_name}"]
        if any(p in text for p in patterns):
            needs[mcp_name] = True
    return needs


def _check_yaml_mcp_refs(yaml_text: str, yaml_path: Path) -> dict[str, bool]:
    """Check which MCP servers are configured in a yaml file."""
    present = {}
    for mcp_name in ALL_MCP_NAMES:
        pattern = re.compile(rf"mcp_server_name:\s*{re.escape(mcp_name)}(\s*[,}}]|$)")
        if pattern.search(yaml_text):
            present[mcp_name] = True
        else:
            present[mcp_name] = False
    return present


def check_cookbooks() -> None:
    """Validate cookbook agent.yaml and subagent yaml MCP configurations."""
    cookbooks_dir = CHINA_DIR / "managed-agent-cookbooks"
    if not cookbooks_dir.exists():
        log_error("Missing managed-agent-cookbooks/ directory")
        return

    for cb_entry in sorted(cookbooks_dir.iterdir()):
        if not cb_entry.is_dir():
            continue

        agent_yaml = cb_entry / "agent.yaml"
        if not agent_yaml.exists():
            log_error(f"cookbook {cb_entry.name}: missing agent.yaml")
            continue

        yaml_text = agent_yaml.read_text(encoding="utf-8")
        present = _check_yaml_mcp_refs(yaml_text, agent_yaml)
        needs = _agent_prompt_needs_mcp(cb_entry.name)

        # Only flag missing MCP if the agent prompt actually references it
        for mcp_name in ALL_MCP_NAMES:
            if needs[mcp_name] and not present[mcp_name]:
                log_error(
                    f"cookbook {cb_entry.name}/agent.yaml: agent prompt references "
                    f"'{mcp_name}' but mcp_toolset is missing. "
                    f"Add: {{ type: mcp_toolset, mcp_server_name: {mcp_name}, default_config: {{ enabled: true }} }}"
                )
            elif present[mcp_name]:
                log_ok(f"cookbook {cb_entry.name}: {mcp_name} MCP configured")

        # Check subagent yamls
        subagents_dir = cb_entry / "subagents"
        if not subagents_dir.exists():
            continue
        for sub_yaml in sorted(subagents_dir.glob("*.yaml")):
            sub_text = sub_yaml.read_text(encoding="utf-8")
            sub_present = _check_yaml_mcp_refs(sub_text, sub_yaml)

            # Subagents that already use MCP should inherit Wind/iFind if parent uses them
            has_any_mcp = any(sub_present.values())
            if has_any_mcp:
                for mcp_name in ["wind", "ifind"]:
                    if present.get(mcp_name) and not sub_present.get(mcp_name):
                        log_error(
                            f"cookbook {cb_entry.name}/subagents/{sub_yaml.name}: "
                            f"parent agent has '{mcp_name}' but subagent does not. "
                            f"Add mcp_toolset for '{mcp_name}'."
                        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("\n── China Plugin Validation ──\n")

    # 1. Check vertical plugins
    print("[1/6] Vertical plugins")
    vert_skills = {}
    vert_dir = CHINA_DIR / "vertical-plugins"
    for entry in sorted(vert_dir.iterdir()):
        if entry.is_dir():
            skills = check_skills(entry.name)
            vert_skills[entry.name] = skills

    # 2. Check agent plugins
    print("\n[2/6] Agent plugins")
    agent_dir = CHINA_DIR / "agent-plugins"
    for entry in sorted(agent_dir.iterdir()):
        if entry.is_dir():
            check_agent(entry.name)
            if "china-finance" in vert_skills:
                check_skill_drift("china-finance", entry.name)

    # 3. Check MCP servers
    print("\n[3/6] MCP server integrity")
    check_mcp_servers()

    # 4. Check .mcp.json consistency
    print("\n[4/6] .mcp.json consistency")
    check_mcp_json()

    # 5. Check cookbooks
    print("\n[5/6] Cookbook MCP configuration")
    check_cookbooks()

    # 6. Summary
    print("\n[6/6] Summary")
    if _ERROR_COUNT:
        print(f"\n── {_ERROR_COUNT} error(s) found ──\n", file=sys.stderr)
        return 1

    print("\n── All checks passed ──\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
