# Operations

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

For Codex, a project installation uses `.agents/skills/conversation-governor/`. For Claude Code, a project installation uses `.claude/skills/conversation-governor/`. The same canonical package provides both projections.

## Local upgrade

1. Select a tested local skill package.
2. Inspect the installed version and read `CHANGELOG.md`.
3. Use `python3 scripts/install_verbose.py --source <local-package> --dest <installed-skill> --upgrade --no-hook` to preserve a backup.
4. Validate the resulting installation and its host-visible identity.
5. Review project-local advisory hook entries and request host trust approval when required.
6. Start a new host session when discovery requires reloading package instructions.
7. Report the installed version, backup, tests, and remaining host-verification conditions.

An upgrade operates on local package content. Existing unrelated skills and host configuration retain their owners.

## Validation

Run `python3 scripts/validate_ads.py` and `python3 -m unittest discover -s tests -v` from the package root. Install the local Python `jsonschema` dependency in the designated test environment. Run `python3 scripts/package_skill.py --repository-root <local-repository> --output <file.zip>` to build a source distribution with its license.

Language conformance requires designated ASD-STE100 review evidence. Host compatibility requires observed Codex and Claude Code tests. Local tests establish component behavior, not host execution.

## Recovery

Restore the retained backup when an upgrade fails verification. Report missing references, unavailable host events, version collisions, and their next corrective action.

The canonical identifier remains `conversation-governor`. The human-facing display name is `Conversation Governor`. A shell that displays only machine identifiers needs separate presentation support.
