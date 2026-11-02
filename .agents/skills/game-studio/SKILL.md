---
name: game-studio
description: Coordinate the 49-role game studio for cross-discipline game development, selecting relevant specialists, exclusive file ownership, dependencies and evidence-based review.
---

Use this skill when the user requests studio coordination or a feature spanning disciplines. A tiny single-file change can use the existing focused skills without a committee.

1. Read AGENTS.md, the actual project setup and `studio/COORDINATION.md`. In a game read `studio/PROJECT.md`; in the toolkit read `templates/PROJECT.md` only as a template.
2. Keep the main session as coordinator, using the producer responsibility. Read the compact registry `studio/agents.json`, not all 49 agent instructions into every context. Choose only the roles relevant to the actual engine and task. Use `python scripts/studio.py route` in the toolkit, or `python studio/tools/studio.py route` in an installed game, for deterministic suggestions. Review the suggestion; it is not a scheduler.
3. Verify available native spawning tools and custom role discovery. Use `.codex/agents/<role>.toml` by its registered `name` only when supported. Do not invent tool names or assume files automatically loaded in every hosted client. If native delegation is available but custom discovery is not, read the selected role's `developer_instructions` and pass them explicitly to a supported child agent. If no spawning is available, disclose sequential role passes and do not call the review independent.
4. Plan a small dependency graph. Assign one owner per writable file or binary asset, read-only reviewers, explicit input, acceptance evidence and stop conditions. Use `studio/templates/HANDOFF.md` in an installed game or `templates/HANDOFF.md` here. Do not launch all 49. At most four concurrent children, fewer when limits, budget or file conflicts require it. Close finished children; do not recursively create more agents to evade the cap.
5. Dispatch only ready tasks with disjoint ownership. A programmer must wait for required design/interface decisions. Reviewers inspect the integrated diff, not stale work. Keep engine editor and scene/asset mutation serialized. Main coordinator alone integrates shared files and resolves conflicts.
6. Collect useful findings and blockers promptly. A blocked dependency blocks downstream claims. Request decisions only when authorization, architecture or meaningful scope is missing, not for every small approved edit.
7. Integrate, run actual available checks, obtain independent QA when feasible, fix defects and retest. Report exact checked build/commit, PASS/FAIL/BLOCKED/NOT RUN and a short file explanation. Capture visible gameplay evidence for visual changes when possible. Deliver one consolidated result; never fabricate agent activity or test success.
