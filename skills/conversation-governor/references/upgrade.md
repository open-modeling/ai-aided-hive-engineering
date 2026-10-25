# Agent-facing upgrade workflow

Run this workflow when the Human requests `$conversation-governor upgrade`, update, or repair. Do not run on ordinary messages.

1. Identify the intended Codex project root and `CODEX_HOME`; inspect the existing installed `skill-api.json` and available update scripts. Preserve unrelated skills and global settings.
2. Preferred: execute `python3 "${CODEX_HOME:-$HOME/.codex}/skills/conversation-governor/scripts/upgrade_from_github.py" --verbose --project <PROJECT_ROOT>` from the shell. The script fetches the canonical repository branch and installs with backup. The user can supply `--ref <commit>` to pin the source. If the updater is missing, retrieve the installer from the canonical repository through supported GitHub tools or a temporary checkout; do not assume `$skill-installer` overwrites files. Verify source identity before replacement.
3. Check exit status and structured JSON. Verify destination metadata, installed diagnostic scripts, offline tests, backup path and advisory hook configuration. Preserve other project hook entries. A hook is not active merely because it is written to `.codex/hooks.json`; normal Codex trust approval is separate. Do not bypass trust or install enforcement.
4. Migration: this skill is stateless and non-configurable. There is no persistent skill data or ledger to migrate, and no skill reinitialization command. Check only local hook files and user-owned extensions before replacing the installation; report any conflicts without overwriting them silently.
5. Reload: tell the Human to start a fresh Codex session if needed for rediscovery and instructions to reload. Never claim that replacing files updated the in-memory skill context in the active session.
6. Report source ref and SHA, installed skill URI/version, backup path, hook preparation/trust state, offline diagnostics, migration `not required`, reload status, and remaining host-verification limitations. Roll back from the retained backup if the install fails or verification does not pass.

Do not clone into or delete the active skill directory directly, do not decode opaque Agent payloads, do not update unrelated skills, and do not modify A03–A06.
