# Operations

## Maintenance scope

Installation, upgrade, packaging, and hook setup maintain this skill and its host integration. During runtime, Conversation Governor processes messages.

## Package identity

Display name: Conversation Governor.
Machine name: `conversation-governor`.
Canonical URI: `skill:ai-devmode.conversation-governor`.
Version authority: `skill-api.json`.

The skill is stateless and non-configurable. Each invocation resolves current project policy and any provided project dictionary.

## Installation

1. Obtain the complete local `conversation-governor/` package or the local standalone ZIP.
2. Place the package in the host's supported skill discovery location.
3. Verify `SKILL.md`, `skill-api.json`, `CHANGELOG.md`, `agents/openai.yaml`, local standards, and schemas.
4. Check the canonical URI, version, and visible skill-name collisions.
5. Verify explicit `$conversation-governor` invocation and representative implicit activation in Codex.
6. Verify native discovery and activation in Claude Code.
7. Record the actual installed package and host behavior.

For Codex, use `.agents/skills/conversation-governor/` in a project or `~/.agents/skills/conversation-governor/` for the user. The installer defaults to the user path. Set `CODEX_HOME` for an existing custom Codex layout, or specify `--dest` for a project installation. Check for older copies under `~/.codex/skills/` before changing a host installation.

For Claude Code, use `.claude/skills/conversation-governor/` in a project or `~/.claude/skills/conversation-governor/` for the user. The same canonical package provides both projections.

Verify skill discovery in the target host. For recurring activation, include an explicit Conversation Governor instruction in the host's project policy (`AGENTS.md` for Codex, `CLAUDE.md` for Claude Code). The visible `✓` marker reports agent-side review. Host invocation and hook results establish actual enforcement.

## Local upgrade

1. Select a versioned local package; check `skill-api.json`, its release entry in `CHANGELOG.md`, and offline ADS and regression tests.
2. Identify the active host's installed path. Check for legacy Codex copies under `~/.codex/skills/`; specify `--dest` for a legacy or project installation. Preserve unrelated skills and host configuration.
3. Run `python3 scripts/install_verbose.py --source <local-package> --dest <installed-skill> --upgrade --verbose --no-hook`. The installer reports the previous and target versions, release notes, and retained backup. Offline smoke tests are synthetic.
4. Verify `installed_current=true`, target version, package content, and retained backup. Restore the backup if verification fails.
5. Review optional advisory hook entries separately and obtain host trust approval. Hook configuration alone is not enforcement evidence.
6. Start a fresh host session; verify first-turn implicit and explicit invocation, then inspect real Agent transport coverage in Codex and Claude Code.
7. Report versions, release entry, backup, tests, and remaining verification limits. Retain the backup until host checks succeed.

An upgrade changes only the selected local skill installation. Project records and unrelated host configuration keep their owners.

## Validation

The canonical package includes `LICENSE`. The packager uses the bundled license for standalone installations and the repository license as a fallback for older source checkouts.

Run `python3 scripts/validate_ads.py` and `python3 -m unittest discover -s tests -v` from the package root. Install the local Python `jsonschema` dependency in the designated test environment. Run `python3 scripts/package_skill.py --repository-root <local-repository> --output <file.zip>` to build a source distribution with its license.

Language conformance requires designated ASD-STE100 review evidence. Host compatibility requires observed Codex and Claude Code tests. Local tests establish component behavior, not host execution.

## Recovery

Restore the retained backup when an upgrade fails verification. Report missing references, unavailable host events, version collisions, and their next corrective action.

The canonical identifier remains `conversation-governor`. The human-facing display name is `Conversation Governor`. A shell that displays only machine identifiers needs separate presentation support.
