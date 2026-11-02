# Verification policy

## Toolkit checks

Run from the toolkit root:

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

The validator checks required files, skill metadata, local Markdown links and installer sources. Unit tests exercise dry-run behavior, successful installation, conflict refusal, symlink refusal, and validation failure cases using temporary directories. No third-party Python packages are required.

## Game acceptance

A feature is not gameplay-verified merely because toolkit checks or a compiler passed. Record the exact game revision, engine version, commands, configuration, test scenario and observed result. Cover relevant repeat, release/cancel, failure and network-role paths. Evidence can include logs, screenshots, or video; ensure files exist and exclude secrets/private information before sharing.

Use these labels consistently:

- PASS: this specific executed check met its expected outcome.
- FAIL: this executed check did not meet its expected outcome.
- BLOCKED: a needed dependency or access prevents execution; state which.
- NOT RUN: no execution was attempted; state why.
- NOT APPLICABLE: explain why the check does not apply.

A self-review is not independent review. Source inspection is not runtime execution. A screenshot can support an observation but not prove an entire test suite. Rerun affected checks after changes.

This initial toolkit has no bundled Unity/Unreal project and no CI that builds a game. Engine integration and real Codex skill discovery require validation in the user's chosen environment.
