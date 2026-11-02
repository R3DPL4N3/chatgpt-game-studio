# Codex Game Studio

A small, inspectable game-development workflow for Codex. **One feature, a small diff, and evidence before “done.”**

This is an independent workflow toolkit, not an OpenAI product, game engine, autonomous studio, or guarantee of working games. It draws inspiration from Claude-Code-Game-Studios without pretending that renamed Claude hooks run in Codex.

## What you get

- Three repo-local skills: plan a feature, implement it, and review/test it.
- Short working agreements in `AGENTS.md`.
- Unity and Unreal playbooks, with explicit editor and multiplayer verification boundaries.
- A non-overwriting installer and dependency-free scaffold checks.
- [Türkçe başlangıç rehberi](docs/QUICKSTART_TR.md).

The three roles are **workflow responsibilities**, not three automatically launched agents. One Codex session can follow them sequentially. If your Codex environment supports subagents, a separate reviewer can inspect the completed diff; this repository does not configure or require that feature.

## Quick start

Requirements: Python 3.10+ for the helper scripts; a Codex environment with access to the game repository. Unity/Unreal and their toolchains are needed only to build or run a real game.

1. Clone or download this repository.
2. Validate the toolkit:

   ```sh
   python scripts/validate.py
   python -m unittest discover -s tests -v
   ```
3. Preview installation into an **existing** game repository:

   ```sh
   python scripts/install.py --target /path/to/game
   ```
4. Review the printed file list, then install:

   ```sh
   python scripts/install.py --target /path/to/game --apply
   ```

On Windows use `py -3` instead of `python` if necessary, and quote paths containing spaces. The installer copies only workflow files, makes no network calls, changes no global Codex settings, and never overwrites an existing destination. Conflicts abort the whole preflight; manually merge existing `AGENTS.md` guidance instead of deleting it. Read [installation details](docs/INSTALLATION.md).

5. Open **the game repository** in Codex and start a new session. Ask it to list the instructions and skills it can see. If skills are unavailable in that client, explicitly ask it to read the three installed `SKILL.md` files; do not assume discovery succeeded.
6. Use this first prompt:

   > Read AGENTS.md and studio/PROJECT.md. Use game-plan-feature to plan one small change. Explain the existing scene/prefab or Blueprint setup and the files you would touch. Do not implement until I approve the plan.

Fill `studio/PROJECT.md` with the actual engine version, paths and commands. Nothing in this toolkit chooses an engine, imports assets, writes gameplay code, or publishes builds for you.

## Everyday loop

1. **Plan:** pick one observable outcome, exclusions, affected files, and acceptance checks.
2. **Implement:** after authorization, make the smallest useful change; preserve editor-owned content and existing architecture.
3. **Review/test:** inspect the diff, run applicable checks, observe gameplay where possible, and disclose blocked tests.
4. **Explain:** say what changed, why, how to test it, and what remains unverified.

Example: “Holding right mouse updates the move target; release keeps the last target.” This is one feature. Inventory, matchmaking, networking replacement, and UI redesign are separate work.

Use [FEATURE.md](templates/FEATURE.md) and [EVIDENCE.md](templates/EVIDENCE.md) when useful; they are not mandatory paperwork for every tiny change.

## Verification limits

The Python checks validate this toolkit and installer, **not a Unity or Unreal game**. No engine runtime, live Codex skill-selection session, multiplayer session, or asset import is certified by those checks. Successful compilation alone does not prove gameplay correctness. See [verification guide](docs/VERIFICATION.md).

## Compatibility and sources

This repository uses documented `AGENTS.md` and `.agents/skills/<name>/SKILL.md` conventions. It does not ship Claude slash commands, hooks, secret/API-key configuration, or a custom agent scheduler. Client capabilities vary; confirm local skill discovery in your actual Codex environment.

- [Codex project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Provenance and upstream credit](THIRD_PARTY_NOTICES.md)

MIT license; see [LICENSE](LICENSE). Commercial game assets and engine licenses are separate and are not included.
