# 49-agent coordination

The main session coordinates; `producer` is its production responsibility, not a mandatory extra child. The 49 native agent files are available specialists, not 49 continuously running processes.

## Capability check

Ask the current Codex client to confirm discovered custom names and available spawning. Project agents are `.codex/agents/*.toml`; the supported fields used here are `name`, `description`, and `developer_instructions`. `.codex/config.toml` sets `[agents] enabled = true` and `max_concurrent_threads_per_session = 4`. Models, credentials and permission settings are inherited, not overridden. Project trust and managed policy can prevent loading; do not automatically change trust or security settings.

If custom roles are unavailable, read the selected TOML instructions and pass them to a supported generic child. If no spawning tools exist, use sequential role passes and disclose that independent review did not occur. Do not replace missing functionality with invented command names or say a simulation launched real agents.

## Small task graph, not paperwork

Record task ID, role, dependency IDs, exclusive writable paths and acceptance evidence in a brief ledger. States: planned → ready → running → review → done; blocked and failed are explicit states, never done. A dependency becomes ready only after its required artifact is available. A reviewer reads the exact integrated revision.

- Design questions: game-designer; formulas: systems-designer; architecture: technical-director/lead-programmer.
- Implementation: gameplay/UI/AI/network programmer plus the actual engine specialist when needed.
- Presentation: art-director/technical-artist, audio-director/sound-designer, narrative-director/writer as relevant.
- Gate: qa-lead defines risk-based checks, qa-tester executes. Security/performance reviews are targeted, not compulsory ceremony.
- The registry records each specialist's coordination lead. This is a routing guide, not authority over the user.

## Ownership and concurrency

At most four active child threads by default. Never spawn all 49 merely to demonstrate activity. Assign disjoint writable files; all others are read-only. Binary assets, scene editing, package manifests and other shared integration points have one owner at a time. Run independent investigation in parallel, dependent implementation sequentially. The coordinator reconciles findings before changing shared interfaces. Do not let children recursively fan out beyond the allocated budget.

On a conflict, stop affected writes, inspect both changes and reassign ownership; never discard another worker's edits. Cancel obsolete children when the user redirects scope. On failure report completed artifacts and exact blocker, then fix or ask only for the missing input. Preserve the user's current project and engine.

## Review gates

1. Scope and relevant engine/version confirmed.
2. Small implementation and changed-file explanation complete.
3. Independent review when a separate agent actually ran; otherwise labeled self-review.
4. Applicable tests executed and observed results attached. Engine absence means NOT RUN, not PASS.
5. Visual/gameplay changes actually played or marked unverified. Multiplayer requires multiple roles/clients, not a standalone screenshot.
6. Publication/deployment only when authorized. No silent paid service, telemetry or asset acquisition.

The routing helper prints suggested teams and handoff skeletons only. It does not execute models, bill an API, or enforce filesystem isolation. Native Codex owns spawning and permissions; the coordinator owns the workflow.
