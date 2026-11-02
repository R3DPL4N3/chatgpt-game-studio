"""Preview or install the small workflow bundle. Python 3.11+, stdlib only."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("game-plan-feature", "game-implement-feature", "game-review-test", "game-studio")
COPY_PLAN = {
    "AGENTS.md": "AGENTS.md",
    "templates/PROJECT.md": "studio/PROJECT.md",
    "templates/FEATURE.md": "studio/templates/FEATURE.md",
    "templates/EVIDENCE.md": "studio/templates/EVIDENCE.md",
    "docs/engines/unity.md": "studio/engines/unity.md",
    "docs/engines/unreal.md": "studio/engines/unreal.md",
    "docs/INSTALLATION.md": "studio/WORKFLOW.md",
    "LICENSE": "studio/LICENSE",
    "THIRD_PARTY_NOTICES.md": "studio/THIRD_PARTY_NOTICES.md",
    **{f".agents/skills/{name}/SKILL.md": f".agents/skills/{name}/SKILL.md" for name in SKILLS},
}
AGENT_IDS = ('accessibility-specialist', 'ai-programmer', 'analytics-engineer', 'art-director', 'audio-director', 'community-manager', 'creative-director', 'devops-engineer', 'economy-designer', 'engine-programmer', 'game-designer', 'gameplay-programmer', 'godot-csharp-specialist', 'godot-gdextension-specialist', 'godot-gdscript-specialist', 'godot-shader-specialist', 'godot-specialist', 'lead-programmer', 'level-designer', 'live-ops-designer', 'localization-lead', 'narrative-director', 'network-programmer', 'performance-analyst', 'producer', 'prototyper', 'qa-lead', 'qa-tester', 'release-manager', 'security-engineer', 'sound-designer', 'systems-designer', 'technical-artist', 'technical-director', 'tools-programmer', 'ue-blueprint-specialist', 'ue-gas-specialist', 'ue-replication-specialist', 'ue-umg-specialist', 'ui-programmer', 'unity-addressables-specialist', 'unity-dots-specialist', 'unity-shader-specialist', 'unity-specialist', 'unity-ui-specialist', 'unreal-specialist', 'ux-designer', 'world-builder', 'writer')
COPY_PLAN.update({
    ".codex/config.toml": ".codex/config.toml",
    "studio/agents.json": "studio/agents.json",
    "studio/COORDINATION.md": "studio/COORDINATION.md",
    "templates/HANDOFF.md": "studio/templates/HANDOFF.md",
    "scripts/studio.py": "studio/tools/studio.py",
    **{f".codex/agents/{name}.toml": f".codex/agents/{name}.toml" for name in AGENT_IDS},
})


def reject_symlinks(path: Path) -> None:
    for item in (path, *path.parents):
        if item.is_symlink():
            raise ValueError(f"Symlink path is not supported: {item}")


def plan_install(target: Path, source: Path = ROOT) -> list[tuple[Path, Path]]:
    # Check the lexical path before resolve() so symlinks do not disappear.
    target = target.expanduser().absolute()
    reject_symlinks(target)
    target = target.resolve()
    source = source.resolve()
    if not target.is_dir():
        raise ValueError(f"Target must be an existing directory: {target}")
    if target == source or source in target.parents:
        raise ValueError("Target cannot be inside the toolkit repository")
    plan = []
    for relative_source, relative_target in COPY_PLAN.items():
        src = source / relative_source
        dst = target / relative_target
        reject_symlinks(src)
        reject_symlinks(dst)
        if not src.is_file():
            raise ValueError(f"Missing source file: {src}")
        if dst.exists():
            raise ValueError(f"Refusing to overwrite: {dst}. Merge existing instructions manually.")
        for parent in dst.parents:
            if parent.exists() and not parent.is_dir():
                raise ValueError(f"Destination parent is not a directory: {parent}")
        plan.append((src, dst))
    return plan


def install(target: Path, apply: bool = False, source: Path = ROOT) -> list[Path]:
    plan = plan_install(target, source)
    if apply:
        for src, dst in plan:
            # Recheck immediately before writing, and never truncate a file.
            reject_symlinks(dst)
            dst.parent.mkdir(parents=True, exist_ok=True)
            with dst.open("xb") as output:
                output.write(src.read_bytes())
    return [dst for _, dst in plan]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path, help="Existing game repository root")
    parser.add_argument("--apply", action="store_true", help="Write files after full preflight (default: preview only)")
    args = parser.parse_args(argv)
    try:
        paths = install(args.target, args.apply)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        print("If writing had started, inspect for a partial installation before retrying.", file=sys.stderr)
        return 1
    print("Installed:" if args.apply else "Preview only; no files written:")
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
