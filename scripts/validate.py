"""Check this toolkit's structure, skill metadata, and local Markdown links."""
from __future__ import annotations

import argparse
import json
import tomllib
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

from install import COPY_PLAN, ROOT, SKILLS, AGENT_IDS

REQUIRED = set(COPY_PLAN) | {
    "README.md", "docs/QUICKSTART_TR.md", "docs/VERIFICATION.md",
    "scripts/install.py", "scripts/validate.py", "tests/test_toolkit.py", "tests/test_agents.py",
    "docs/CODEX_COMPATIBILITY.md", "docs/AGENT_ROSTER.md", "docs/TEST_REPORT.md", ".gitignore",
}


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    for relative in sorted(REQUIRED):
        path = root / relative
        if not path.is_file() or path.is_symlink():
            errors.append(f"Missing file or disallowed symlink: {relative}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"Empty file: {relative}")
    for name in SKILLS:
        path = root / f".agents/skills/{name}/SKILL.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n(.+)", text, re.S)
        if not match:
            errors.append(f"Invalid skill front matter: {name}")
            continue
        fields = dict(re.findall(r"^(name|description): (.+)$", match[1], re.M))
        if fields.get("name") != name or not fields.get("description", "").strip():
            errors.append(f"Invalid skill name or description: {name}")
    errors.extend(validate_agents(root))
    for path in root.rglob("*.md"):
        if any(part in (".git", ".venv", "__pycache__") for part in path.relative_to(root).parts):
            continue
        if path.is_symlink():
            errors.append(f"Disallowed Markdown symlink: {path.relative_to(root)}")
            continue
        text = path.read_text(encoding="utf-8")
        # This toolkit uses simple Markdown links; remote URLs/fragments are not fetched.
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if urlparse(target).scheme or target.startswith("#"):
                continue
            relative = unquote(target.split("#", 1)[0])
            destination = (path.parent / relative).resolve()
            if not destination.is_relative_to(root):
                errors.append(f"Link escapes toolkit: {path.relative_to(root)} -> {target}")
            elif not destination.exists():
                errors.append(f"Broken local link: {path.relative_to(root)} -> {target}")
    return errors


def validate_agents(root: Path) -> list[str]:
    errors = []
    try:
        registry = json.loads((root / "studio/agents.json").read_text(encoding="utf-8"))
        agents = registry["agents"]
        ids = [a["id"] for a in agents]
        if len(ids) != 49 or set(ids) != set(AGENT_IDS) or len(set(ids)) != len(ids):
            errors.append("Registry must contain exactly the 49 expected unique agents")
        paths = {p.name for p in (root / ".codex/agents").glob("*.toml")}
        if paths != {name + ".toml" for name in AGENT_IDS}:
            errors.append("Native agent files must exactly match registry")
        for agent in agents:
            name = agent["id"]
            if name not in AGENT_IDS:
                continue
            if agent["file"] != f".codex/agents/{name}.toml":
                errors.append(f"Invalid agent path: {name}")
            lead = agent.get("lead")
            if lead is not None and lead not in AGENT_IDS:
                errors.append(f"Unknown lead: {name}")
            visited = {name}
            leads = {a["id"]: a.get("lead") for a in agents}
            while lead:
                if lead in visited:
                    errors.append(f"Lead cycle: {name}")
                    break
                visited.add(lead)
                lead = leads.get(lead)
            agent_path = root / f".codex/agents/{name}.toml"
            if agent_path.is_symlink():
                errors.append(f"Disallowed native agent symlink: {name}")
                continue
            data = tomllib.loads(agent_path.read_text(encoding="utf-8"))
            if set(data) != {"name", "description", "developer_instructions"}:
                errors.append(f"Unexpected native agent settings: {name}")
            if data.get("name") != name or data.get("description") != agent["description"]:
                errors.append(f"Native agent mismatch: {name}")
            if agent.get("focus", "") not in data.get("developer_instructions", "") or len(agent.get("focus", "")) < 60:
                errors.append(f"Missing meaningful role focus: {name}")
        config = tomllib.loads((root / ".codex/config.toml").read_text(encoding="utf-8"))
        if config != {"agents": {"enabled": True, "max_concurrent_threads_per_session": 4}}:
            errors.append("Unexpected project agent config or concurrency cap")
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as error:
        errors.append(f"Invalid agent system: {error}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        errors = validate(args.root)
    except (OSError, UnicodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: toolkit structure, four skill manifests, 49 native agent definitions, and local Markdown links")
    print("NOT RUN: live Codex discovery, Unity/Unreal builds, and gameplay tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
