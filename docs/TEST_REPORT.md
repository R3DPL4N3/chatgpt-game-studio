# 49-agent toolkit verification

Date: 2026-11-02 (UTC). Environment: Linux, Python 3.11+ standard-library checks. No engine or model session used for these tests.

## Executed

- PASS: `python scripts/validate.py` — required files, four skills, 49 native TOML definitions, registry/lead consistency, concurrency configuration and local Markdown links.
- PASS: `python -m unittest discover -s tests -v` — 32 tests, 0 failures, 0 skips.
- PASS: `python -m compileall -q scripts tests` — Python syntax compilation.
- PASS: exact 49 role IDs matched the pinned upstream `.claude/agents/` list; upstream commit verified locally as `05ad7c8a5b8aa2aa86bbd3439ae7cf7295cac418`.
- PASS: installed routing helper invoked from outside the game folder; list returned 49 roles and Unreal network routing selected `ue-replication-specialist`.

Original 16 regression tests remain. New 16 cover native-role count/content, all 64 area/engine route combinations, engine-specific selections, all 49 handoff templates, unknown roles/routes, missing agent files, duplicate registry entries, invalid paths, lead cycles, mismatched native names, disallowed configuration keys, concurrency tampering, preserving an existing config, installed CLI and failure exit behavior.

Installer coverage includes preview without writes, explicit copy manifest, preserving unrelated files, refusing existing files before writes, repeat-install refusal, missing target/source, self-install refusal, path spaces, file/directory conflicts, symlink targets/parents/dangling destinations, and CLI exit statuses. Validator negative cases include missing files, malformed skill metadata, and broken local links.

## Not run

- Live Codex custom-agent discovery, actual spawning, independent model-review behavior or 49-agent execution. Native definitions were parsed and checked, not executed by a model runtime.
- Windows/macOS execution; Windows symlink tests may skip where privileges are absent.
- Unity, Unreal or Godot compilation, editor operations, gameplay, asset imports or multiplayer.
- GitHub-hosted CI; no automated workflow is configured.

These results validate toolkit structure and deterministic helpers, not a completed game or proven model orchestration. Rerun after modifications. The installer is non-overwriting but not a filesystem transaction or hostile-concurrency defense. Routing suggestions and ownership rules are not OS-enforced isolation.
