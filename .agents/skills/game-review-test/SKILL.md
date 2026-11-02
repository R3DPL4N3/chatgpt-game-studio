---
name: game-review-test
description: Review a game change and verify its acceptance checks with honest evidence. Use for testing or reviewing implemented features, not for claiming unobserved gameplay success.
---

1. Read the requested outcome, relevant instructions, changed files, and acceptance criteria. Identify whether this is independent review or self-review.
2. Check correctness, scope, engine/version compatibility, asset references, lifecycle cleanup, repeat/release/cancel behavior, and any trust boundaries.
3. Run the project's documented checks. Record exact commands, exit status, relevant output, engine/build configuration, and current commit or working-tree state.
4. For visible gameplay, run and observe the actual scenario where tools allow. Capture useful screenshots/video or logs without secrets. If unable, mark NOT RUN or BLOCKED and explain the smallest next step.
5. For multiplayer, test the affected authoritative server, owning client, and observing client separately. A standalone run is not network acceptance. Inspect synchronization, authority, validation, and repeat/reconnect paths relevant to the feature.
6. Report findings by severity with file/location, reproduction, and consequence. No findings does not prove absent bugs. Separate PASS, FAIL, BLOCKED, NOT RUN, and not-applicable checks.
7. After fixes, rerun affected checks against the final state. Do not reuse evidence from a superseded revision as final proof.

Use `studio/templates/EVIDENCE.md` if installed or `templates/EVIDENCE.md` in this toolkit when a durable test record helps. Never fabricate reviewer approval, run logs, screenshots, or performance numbers.
