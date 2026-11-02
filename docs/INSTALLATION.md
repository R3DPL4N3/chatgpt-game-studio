# Installation and removal

Run `scripts/install.py` from this toolkit. Target an existing game project directory. Default behavior is a dry run. `--apply` writes the listed files only.

Installed layout:

- `AGENTS.md`: concise working agreements.
- `.agents/skills/game-*/SKILL.md`: three instruction-only skills.
- `studio/PROJECT.md`: fill in real engine details.
- `studio/engines/`: Unity and Unreal guides.
- `studio/templates/`: optional feature and evidence records.
- `studio/WORKFLOW.md`: installation/use notes.
- `studio/LICENSE` and `studio/THIRD_PARTY_NOTICES.md`: license and provenance.

No toolkit Python scripts, tests, credentials, global settings, or assets are installed. The copy plan is explicit in `scripts/install.py`.

The helper refuses existing destination files (including identical files), symlinks in the target path or destination ancestry, and paths inside this toolkit. It preflights all destinations before writing. Each file uses exclusive creation. Filesystem failures or concurrent changes can still leave a **partial installation**: review its error and files before retrying. It is not a transactional filesystem or a defense against a hostile concurrent process. Do not run it while another tool modifies the target directories.

Existing instructions/skills: manually merge the small agreements and selected skills after review. Do not remove your project's AGENTS.md merely to satisfy this installer. Installation is deliberately not an automatic migration or update system.

Removal is manual: remove only the files from the printed plan that you installed and have not since customized. Never remove the whole `.agents` directory or unrelated project instructions. No uninstall command is provided because safe removal requires inspecting your changes.

For instructions to take effect, open the target project in a fresh Codex session and ask which instructions and skills are loaded. Client-specific discovery and tool access still need validation.
