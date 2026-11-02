"""Check this toolkit's structure, skill metadata, and local Markdown links."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

from install import COPY_PLAN, ROOT, SKILLS

REQUIRED = set(COPY_PLAN) | {
    "README.md", "docs/QUICKSTART_TR.md", "docs/VERIFICATION.md",
    "scripts/install.py", "scripts/validate.py", "tests/test_toolkit.py", ".gitignore",
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
    print("PASS: toolkit structure, three skill manifests, and local Markdown links")
    print("NOT RUN: live Codex discovery, Unity/Unreal builds, and gameplay tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
