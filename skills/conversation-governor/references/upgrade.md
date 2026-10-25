# Agent-facing upgrade workflow

Run this workflow when the Human requests `$conversation-governor upgrade`, update, or repair. Do not run on ordinary messages.

1. Identify the intended Codex project root and `CODEX_HOME`; inspect the existing installed `skill-api.json` and available update scripts. Preserve unrelated skills and global settings.
2. Preferred: execute `python3 "${CODEX_HOME:-$HOME/.codex}/skills/conversation-governor/scripts/upgrade_from_github.py" --verbose --project <PROJECT_ROOT>` from the shell. The script fetches the canonical repository branch and installs with backup. The user can supply `--ref <commit>` to pin the source. If the updater is missing, use the **bootstrap procedure below**, fetching a standalone updater from the pinned canonical source. Do not assume `$skill-installer` overwrites existing skill files. Verify source identity and the installed destination before replacement.
3. Check exit status and structured JSON. Verify destination metadata, installed diagnostic scripts, offline tests, backup path and advisory hook configuration. Preserve other project hook entries. A hook is not active merely because it is written to `.codex/hooks.json`; normal Codex trust approval is separate. Do not bypass trust or install enforcement.
4. Migration: this skill is stateless and non-configurable. There is no persistent skill data or ledger to migrate, and no skill reinitialization command. Check only local hook files and user-owned extensions before replacing the installation; report any conflicts without overwriting them silently.
5. Reload: tell the Human to start a fresh Codex session if needed for rediscovery and instructions to reload. Never claim that replacing files updated the in-memory skill context in the active session.
6. Report source ref and SHA, installed skill URI/version, backup path, hook preparation/trust state, offline diagnostics, migration `not required`, reload status, and remaining host-verification limitations. Roll back from the retained backup if the install fails or verification does not pass.

## Bootstrap when the installed helper is missing

The updater itself is standalone Python 3 and requires Git. It does not require a local repository checkout or a project-local `.agents/skills` copy. Retrieve it from the exact verified source:

`https://raw.githubusercontent.com/open-modeling/ai-aided-hive-engineering/d728effeaf5d982e0ae2a6a33b6e1cded5f2591b/skills/conversation-governor/scripts/upgrade_from_github.py`

The Agent can download that one file to a temporary directory, review the canonical repository and commit identity, and execute it from there. Example for a shell with `curl` (change `CG_PROJECT` and `CG_DEST` to the discovered project and installed skill directories; do not guess a custom Codex home):

```sh
CG_PROJECT="$(pwd)"
CG_DEST="${CODEX_HOME:-$HOME/.codex}/skills/conversation-governor"
CG_TMP="$(mktemp -d)"
curl --fail --location --silent --show-error \
  'https://raw.githubusercontent.com/open-modeling/ai-aided-hive-engineering/d728effeaf5d982e0ae2a6a33b6e1cded5f2591b/skills/conversation-governor/scripts/upgrade_from_github.py' \
  --output "$CG_TMP/upgrade_from_github.py"
python3 "$CG_TMP/upgrade_from_github.py" \
  --ref 'd728effeaf5d982e0ae2a6a33b6e1cded5f2591b' \
  --dest "$CG_DEST" \
  --project "$CG_PROJECT" --verbose
CG_STATUS=$?
rm -rf "$CG_TMP"
exit "$CG_STATUS"
```

If `curl` is unavailable, use the supported GitHub connector or a Git temporary checkout and invoke `skills/conversation-governor/scripts/install_verbose.py --upgrade --verbose` from the checkout with explicit `--source`, `--dest`, and `--project`. Never remove the old installation before success; the installer retains its full backup.

Once bootstrapped, future `$conversation-governor upgrade` requests use the freshly installed helper. If hooks require approval, use normal Codex trust mechanisms. Restart Codex when a new session is needed to read updated skill instructions.

Do not clone into or delete the active skill directory directly, do not decode opaque Agent payloads, do not update unrelated skills, and do not modify A03–A06.
