# Codex Game Studio — 49 specialists

A Codex-native game-development studio toolkit: **49 custom agent definitions**, a coordinator skill, bounded team routing, explicit file ownership, and evidence before “done.” Inspired by Claude-Code-Game-Studios and adapted to Codex rather than blindly renaming Claude configuration.

This is independent software, not an OpenAI product, game engine or guarantee of working games. **49 available roles does not mean 49 agents running at once.** Native spawning must be supported by the actual Codex client.

## What's included

- 49 project-scoped `.codex/agents/*.toml` definitions using the upstream role taxonomy: creative/technical direction, production, design, programming, art, audio, narrative, QA, release and Unity/Unreal/Godot specialists.
- A native project configuration with a four-child concurrency cap and no model or permission overrides.
- `game-studio` coordination plus three focused skills for planning, implementation and review.
- A role registry, task routing helper and handoff template; the coordinator owns dependencies, file ownership and integration.
- Preview-first non-overwriting installation, dependency-free tests, English docs and a [Türkçe başlangıç rehberi](docs/QUICKSTART_TR.md).

[All 49 roles](docs/AGENT_ROSTER.md) · [Coordination protocol](studio/COORDINATION.md) · [Compatibility](docs/CODEX_COMPATIBILITY.md) · [Test evidence](docs/TEST_REPORT.md)

## Quick start

Python **3.11+** is required for the tooling and TOML validation. A compatible Codex client and actual game repository are required for live use. Engine/toolchain installation is separate.

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/studio.py list
python scripts/studio.py route --area network --engine unreal
python scripts/install.py --target /path/to/game
# Review the preview, then:
python scripts/install.py --target /path/to/game --apply
```

On Windows use `py -3` if necessary. Quote paths containing spaces. Existing instructions, config or agent files cause a conflict before writes; **manually merge them, do not delete them to satisfy the installer**. No global settings, secrets, game assets, paid services or external API runner are installed. See [installation](docs/INSTALLATION.md).

Open the **game root** in a fresh Codex session, fill `studio/PROJECT.md` with actual engine/version/build commands, and ask Codex which custom agents and spawning tools it sees. Native role discovery depends on client support, project trust and managed configuration. Never change trust or permissions automatically to force it.

## First mission: a showable vertical slice

> Use game-studio. Inspect this project's actual engine, working systems and licensed assets. Build a small, polished top-down extraction demo: enter a compact ruin, fight one enemy type, loot a chest and reach an extraction zone before time expires. Include smooth right-click/held movement, camera zoom, one attack and one special ability, readable health feedback, atmospheric lighting/audio, and clear win/death/retry flow. Preserve existing working controls and multiplayer; do not rebuild networking or add accounts, matchmaking or auction systems. Keep the main session as coordinator. Select relevant specialists from the 49; use at most four children concurrently, disjoint file ownership and independent QA when available. First give a brief implementation order, then implement within this scope. Ask before a major architectural change, new paid dependency or scope expansion. Deliver runnable increments, explain changed files, actually play and test each flow where tools allow, and show captured evidence. Label unavailable tests NOT RUN. Make the playable result impressive, not the amount of code or paperwork.

A fresh toolkit is not itself a game project. If no game is present, stop to ask for the target project/engine rather than pretending to run it. Cut optional presentation work if needed to finish the core loop first.

## How coordination works

1. Main session acts as producer/coordinator and selects a small relevant team.
2. Design/architecture inputs precede dependent implementation; independent research can run in parallel.
3. Each writable file has one owner. Shared/binary assets and editor actions are serialized.
4. Reviewers examine the integrated revision; a genuine separate reviewer is distinguished from self-review.
5. Coordinator resolves defects, reruns checks and delivers one concise report with PASS, FAIL, BLOCKED and NOT RUN.

The routing helper **only prints suggestions and handoff skeletons**. Codex's native tools perform real delegation. If custom discovery is unavailable but spawning exists, pass selected role instructions explicitly to supported generic children. If no spawning exists, use labeled sequential role passes. Never fabricate49 agent activity.

For small work, keep using `game-plan-feature`, `game-implement-feature` and `game-review-test` directly. Full studio capability does not require a committee for each tiny edit.

## Limits and credit

Local tests validate the registry, native TOML files, installer and deterministic routing. Live Codex discovery/spawning, Windows/macOS and Unity/Unreal/Godot gameplay have **not been tested** in this environment. No CI workflow is configured. Successful toolkit tests are not a game acceptance test.

[MIT license](LICENSE) · [Upstream attribution and pinned provenance](THIRD_PARTY_NOTICES.md). The49 taxonomy/role descriptions are adapted from upstream; this is not a port of all74 upstream skills or Claude hooks. Commercial assets and engine licenses remain separate.
