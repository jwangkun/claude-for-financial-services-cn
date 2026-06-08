#!/usr/bin/env python3
"""Check script for china/ directory — validates structure, references, and drift.

Usage:
    python3 scripts/check-china.py

Checks:
1. All vertical-plugins skills have valid YAML frontmatter
2. All agent-plugins agents/*.md have valid YAML frontmatter
3. Agent plugin skills are in sync with their vertical-plugin sources
4. No cross-references to non-China paths
"""

import os
import re
import sys
from pathlib import Path

CHINA_DIR = Path(__file__).resolve().parent.parent

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
FORBIDDEN_HINTS = ["west financial", "western data"]


def log_error(msg: str) -> None:
    print(f"  ✖  {msg}", file=sys.stderr)


def log_ok(msg: str) -> None:
    print(f"  ✓  {msg}")


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
    return []


def check_skill_drift(vertical: str, agent: str) -> None:
    """Check that agent's bundled skills match the vertical plugin source."""
    vert_skills = CHINA_DIR / "vertical-plugins" / vertical / "skills"
    agent_skills = CHINA_DIR / "agent-plugins" / agent / "skills"
    if not agent_skills.exists():
        log_ok(f"agent {agent}: no bundled skills (ok for now)")
        return

    for agent_entry in agent_skills.iterdir():
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
            log_error(f"agent {agent}/{agent_entry.name}: DRIFT from vertical source")


def main() -> int:
    print("\n── China Plugin Validation ──\n")

    # 1. Check vertical plugins
    vert_skills = {}
    vert_dir = CHINA_DIR / "vertical-plugins"
    for entry in sorted(vert_dir.iterdir()):
        if entry.is_dir():
            skills = check_skills(entry.name)
            vert_skills[entry.name] = skills

    # 2. Check agent plugins
    agent_dir = CHINA_DIR / "agent-plugins"
    for entry in sorted(agent_dir.iterdir()):
        if entry.is_dir():
            check_agent(entry.name)
            # Check skill drift from china-finance (primary source for agent-bundled skills)
            if "china-finance" in vert_skills:
                check_skill_drift("china-finance", entry.name)

    # 3. Check MCP servers exist
    mcp_dir = CHINA_DIR / "mcp-servers"
    for entry in sorted(mcp_dir.iterdir()):
        if entry.is_dir():
            server_file = entry / "server.py"
            req_file = entry / "requirements.txt"
            config_file = entry / "mcp_config.json"
            if server_file.exists():
                log_ok(f"MCP server {entry.name}/server.py")
            else:
                log_error(f"MCP server {entry.name} missing server.py")
            if not req_file.exists():
                log_error(f"MCP server {entry.name} missing requirements.txt")
            # ifind-mcp and other API-based servers should have config template
            if entry.name == "ifind-mcp":
                if config_file.exists():
                    log_ok(f"MCP server {entry.name}/mcp_config.json")
                else:
                    log_error(f"MCP server {entry.name} missing mcp_config.json")

    # 4. Check agent.yaml references ifind MCP when agent prompt uses mcp__ifind__*
    cookbooks_dir = CHINA_DIR / "managed-agent-cookbooks"
    if cookbooks_dir.exists():
        for cb_entry in sorted(cookbooks_dir.iterdir()):
            if not cb_entry.is_dir():
                continue
            agent_yaml = cb_entry / "agent.yaml"
            if not agent_yaml.exists():
                continue
            yaml_text = agent_yaml.read_text(encoding="utf-8")
            if "ifind" in yaml_text:
                log_ok(f"cookbook {cb_entry.name}: ifind MCP configured")
            else:
                log_error(f"cookbook {cb_entry.name}: agent.yaml missing ifind MCP reference")

    print("\n── Done ──\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
