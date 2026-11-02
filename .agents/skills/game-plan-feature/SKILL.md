---
name: game-plan-feature
description: Plan one small game feature with acceptance checks before implementation. Use for new gameplay changes or unclear scope, not for implementing an already approved plan.
---

1. Read the project's nearest AGENTS.md and `studio/PROJECT.md` if present. Inspect relevant existing code and editor assets without modifying them.
2. Establish engine/version, input and network architecture, actual file locations, and the user's intended result. Ask only for missing decisions that affect the change.
3. Choose one observable feature. State exclusions explicitly; do not add inventory, matchmaking, new frameworks, or other features just because they are nearby.
4. Explain the smallest design in the user's language. Identify affected code plus scene/prefab/Blueprint configuration, dependency and asset-license implications.
5. Define acceptance checks: happy path, repeated action, cancel/release, relevant failure case, and network roles if applicable. Separate headless checks from editor observations.
6. Give a compact plan and intended next action. If the user requested only planning, stop. If implementation is already clearly authorized, proceed within that scope using game-implement-feature.

Use `studio/templates/FEATURE.md` if installed, or `templates/FEATURE.md` in this toolkit, only when the task needs a durable record. No large document hierarchy is required.
