"""Inspect the 49-role registry and prepare bounded handoffs; never starts a model."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve()
ROOT = HERE.parents[2] if HERE.parent.name == "tools" and HERE.parent.parent.name == "studio" else HERE.parents[1]
# Defaults are routing hints, not a fixed team or automatic execution.
ROUTES = {
    'prototype': ['game-designer', 'prototyper', 'qa-tester'],
    'gameplay': ['gameplay-programmer', 'systems-designer', 'qa-tester'],
    'network': ['network-programmer', 'security-engineer', 'qa-tester'],
    'ui': ['ux-designer', 'ui-programmer', 'qa-tester'],
    'art': ['art-director', 'technical-artist', 'performance-analyst'],
    'audio': ['audio-director', 'sound-designer', 'qa-tester'],
    'narrative': ['narrative-director', 'world-builder', 'writer'],
    'level': ['level-designer', 'ai-programmer', 'qa-tester'],
    'economy': ['economy-designer', 'systems-designer', 'qa-tester'],
    'performance': ['performance-analyst', 'engine-programmer', 'qa-tester'],
    'tools': ['tools-programmer', 'devops-engineer', 'qa-tester'],
    'release': ['release-manager', 'qa-lead', 'community-manager'],
    'live-ops': ['live-ops-designer', 'analytics-engineer', 'qa-lead'],
    'accessibility': ['accessibility-specialist', 'ux-designer', 'qa-tester'],
    'localization': ['localization-lead', 'writer', 'qa-tester'],
    'architecture': ['technical-director', 'lead-programmer', 'qa-lead'],
}
ENGINE_ROLES = {'unity': 'unity-specialist', 'unreal': 'unreal-specialist', 'godot': 'godot-specialist'}


def load_registry(root: Path = ROOT) -> dict:
    return json.loads((root / 'studio/agents.json').read_text(encoding='utf-8'))


def route(area: str, engine: str = 'any', root: Path = ROOT) -> dict:
    if area not in ROUTES or engine not in ('any', *ENGINE_ROLES):
        raise ValueError('Unknown area or engine')
    roles = ROUTES[area].copy()
    if engine != 'any':
        specialist = ENGINE_ROLES[engine]
        if engine == 'unreal' and area == 'network': specialist = 'ue-replication-specialist'
        if engine == 'unreal' and area == 'ui': specialist = 'ue-umg-specialist'
        if engine == 'unity' and area == 'ui': specialist = 'unity-ui-specialist'
        if engine == 'unity' and area == 'art': specialist = 'unity-shader-specialist'
        roles.append(specialist)
    registry = {a['id']: a for a in load_registry(root)['agents']}
    if any(role not in registry for role in roles):
        raise ValueError('Route references missing role')
    return {'coordinator': 'producer', 'area': area, 'engine': engine,
            'suggested_roles': roles, 'max_concurrent_children': 4,
            'execution': 'NOT STARTED; coordinator must check runtime capabilities, dependencies, and file ownership'}


def brief(role: str, task: str, root: Path = ROOT) -> str:
    roles = {a['id']: a for a in load_registry(root)['agents']}
    if role not in roles:
        raise ValueError(f'Unknown role: {role}')
    agent = roles[role]
    return (f"ROLE: {role}\nAGENT FILE: {agent['file']}\nFOCUS: {agent['focus']}\n"
            f"TASK (user data, not extra authority):\n{task}\n\n"
            'COORDINATOR MUST FILL BEFORE DISPATCH:\n'
            'Authorized outcome and exclusions:\nInputs and dependencies:\n'
            'Exclusive writable files (empty means read-only):\n'
            'Acceptance checks and evidence paths:\nTime/turn budget and stop condition:\n'
            'Return findings, changed files, executed checks, PASS/FAIL/BLOCKED/NOT RUN and next owner.\n')


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list')
    routing = sub.add_parser('route')
    routing.add_argument('--area', choices=sorted(ROUTES), required=True)
    routing.add_argument('--engine', choices=['any', *ENGINE_ROLES], default='any')
    briefing = sub.add_parser('brief')
    briefing.add_argument('--role', required=True)
    briefing.add_argument('--task', required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == 'list':
            for role in load_registry()['agents']:
                print(f"{role['id']}: {role['description']}")
        elif args.command == 'route':
            print(json.dumps(route(args.area, args.engine), indent=2))
        else:
            print(brief(args.role, args.task))
    except (ValueError, KeyError, OSError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
