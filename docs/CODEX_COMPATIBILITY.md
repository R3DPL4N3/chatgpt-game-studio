# Codex compatibility and verification boundary

Checked 2026-11-02 against [official subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents) and [skill documentation](https://learn.chatgpt.com/docs/build-skills).

This toolkit uses project `.codex/agents/*.toml` definitions with `name`, `description` and `developer_instructions`. Project configuration enables agents and caps concurrent child threads at four. It leaves model selection and permissions with the parent. Agent instructions are not a separate filesystem sandbox. Skills live under `.agents/skills/`. Project trust and managed settings may prevent configuration loading.

This is a **current documented format**, not proof every Codex client/version supports it. In your chosen client, confirm custom discovery and execute a small read-only delegation before relying on it. Hosted sessions may not load local TOMLs. The coordinator supports explicit role instructions on available generic children, or clearly labeled sequential role passes when spawning is absent.

No old `[agents.<role>] config_file` entries, Claude tool names, hooks, external model API wrapper or credential configuration are shipped. Do not automatically alter trust, global settings or permission modes to make it run.

## Local acceptance check

1. Open the game root in your chosen Codex client after installation.
2. Ask which custom roles and spawning capabilities it actually sees.
3. Ask `qa-tester` to inspect one existing test file without editing; verify a real separate child and its result.
4. If discovery/spawning fails, use the documented fallback and mark native execution NOT RUN/BLOCKED.

The repository's Python tests validate files and routing only, not model behavior or live agent execution.
