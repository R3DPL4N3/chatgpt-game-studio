# Installation and removal

Run `scripts/install.py` from this toolkit. Target an existing game project directory. Default behavior is a dry run. `--apply` writes the listed files only.

Installed layout:

- `AGENTS.md`: concise working agreements.
- `.agents/skills/game-*/SKILL.md`: four workflow skills.
- `.codex/agents/`: 49 native custom agents.
- `.codex/config.toml`: project-scoped four-child concurrency configuration.
- `studio/agents.json` and `studio/COORDINATION.md`: routing registry and coordination rules.
- `studio/tools/studio.py`: local list/route/brief helper (prints only; does not launch models).
- `studio/PROJECT.md`: fill in real engine details.
- `studio/engines/`: Unity and Unreal guides.
- `studio/templates/`: optional feature, handoff and evidence records.
- `studio/WORKFLOW.md`: installation/use notes.
- `studio/LICENSE` and `studio/THIRD_PARTY_NOTICES.md`: license and provenance.

Only the routing Python helper is installed; maintenance scripts and tests stay in the source toolkit. No credentials, global settings or game assets are installed. The copy plan is explicit in `scripts/install.py`.

The helper refuses existing destination files (including identical files), symlinks in the target path or destination ancestry, and paths inside this toolkit. It preflights all destinations before writing. Each file uses exclusive creation. Filesystem failures or concurrent changes can still leave a **partial installation**: review its error and files before retrying. It is not a transactional filesystem or a defense against a hostile concurrent process. Do not run it while another tool modifies the target directories.

Existing instructions/skills: manually merge the small agreements and selected skills after review. Do not remove your project's AGENTS.md merely to satisfy this installer. Installation is deliberately not an automatic migration or update system.

Removal is manual: remove only the files from the printed plan that you installed and have not since customized. Never remove the whole `.agents` directory or unrelated project instructions. No uninstall command is provided because safe removal requires inspecting your changes.

For instructions to take effect, open the target project in a fresh Codex session and ask which instructions, skills, custom agent names and real spawning capabilities are available. Client-specific discovery and tool access still need validation.

## Upgrading from the three-skill version

The installer is not an updater: preserve your customized files and merge changes manually after comparing the new preview. Include the new studio coordinator skill, 49 agent definitions, registry, protocol and handoff template. Merge only the `[agents]` settings you intend into an existing project config; never replace other settings. Keep the original toolkit folder for maintenance tests. In the installed game use `python studio/tools/studio.py list` or `python studio/tools/studio.py route --area gameplay --engine unity`.
