# Operations and host coverage

Version: 0.3.0-dev. Canonical URI: skill:ai-devmode.conversation-governor.

## Installation

Codex project: place the canonical package under `.agents/skills/conversation-governor/`. Claude Code project: place the same canonical package under `.claude/skills/conversation-governor/`. Verify each host discovers the same `skill_uri`, version, and `skill-api.json`. Inspect other installed skills for same-name conflicts. Prefer links to a single canonical package where supported.

## Verbose installation and opt-in A02 probe

The upstream Codex `$skill-installer` copies files only; it does not register communication hooks. The package provides an independent, project-owned helper:

```sh
python3 skills/conversation-governor/scripts/install_verbose.py --verbose --project .
```

With `--verbose`, setup also prepares a project-local advisory `PreToolUse` hook for Codex trust review; use `--no-hook` to omit this. The hook is not active until Codex trusts it. This installs the local skill into `${CODEX_HOME:-~/.codex}/skills/conversation-governor` when absent, validates its manifest, runs a synthetic hook probe, and checks registered/excluded/unverified local mappings. It does not create configuration in default verbose mode or imply any real host invocation. To use an already installed skill as the source, run `python3 ~/.codex/skills/conversation-governor/scripts/install_verbose.py --verbose --source ~/.codex/skills/conversation-governor --project .`.

You can explicitly add the **temporary, nonblocking project-local** diagnostic with `--prepare-hook` outside verbose mode. It edits only `.codex/hooks.json`, preserves existing unrelated entries, and needs separate trust approval via `/hooks` before any live call. `--remove-hook` removes only the helper's diagnostic. Do not use it to infer execution permission or automatically register enforcement. A separate real collaboration-tool event is necessary to establish hook invocation, readable fields, and pre-dispatch ordering. Existing installed destination is retained unless explicitly upgraded. If an older installation lacks diagnostic scripts, `--verbose` tests the source separately and reports `requires_upgrade: true`; it does not claim the old installation passed. Use `--upgrade --verbose` to atomically replace that installation and preserve a full backup. Add `--prepare-hook` only if local hook configuration is also desired; Codex trust and actual invocation remain separate.

## Upgrade directly from a Codex shell

From any working directory, once the updater is installed:

```sh
python3 "${CODEX_HOME:-$HOME/.codex}/skills/conversation-governor/scripts/upgrade_from_github.py" --verbose --project .
```

The updater fetches the canonical repository's `feature/conversation-governor-communication-only` branch into a temporary checkout, runs the tested installer with `--upgrade`, preserves the previous package as a backup, and prepares a project-local advisory hook for Codex trust approval. Pin `--ref <full-commit-sha>` for reproducibility. Use `--no-hook` to omit hook installation. The `--project` argument refers to the directory where local `.codex/hooks.json` belongs; specify that explicitly if the current shell is not inside the intended project. The updater does not claim actual host activation.

**Bootstrap for an older installation without the updater:** follow the standalone pinned-source recovery in [`references/upgrade.md`](upgrade.md). It fetches a temporary copy of `upgrade_from_github.py` and runs it with explicit `--dest` and `--project`, without requiring a project-local skill or deleting the installed version first. Remote fetch requires Git and access to GitHub.

## Hook policy

Register a supported host hook only after confirming its event schema and observed behavior. The bundled adapter uses explicit tool-to-message-field mappings and the shared message checker. Verify each tool name, event schema, and command registration in the active host. It requires an `[INFORMATION]` or `[DIRECTION]` label; directions require `Action:`, `Target:`, and `Expected-Result:`. Validate inbound prompts and agent-tool messages where hooks provide the source text. Use pre-dispatch hooks when available for directional agent calls; treat response-time hooks as complementary feedback. Apply the instruction-level quality review for messages that cannot be intercepted. Verify hooks with a sample message that includes an instruction-like quotation and a sample directional request. Failures produce a targeted communication correction.

## Upgrade, validation and recovery

Review CHANGELOG.md and the installed version, replace the host projection with the tested canonical release, and verify discovery and relevant hook execution. On missing project dictionary, preserve the supplied term and ask for a definition when necessary. On unsupported hook events, run the in-context checks and report the event-coverage limitation. Stateless operation requires no initialization or reinitialization.

## Conformance

Compare behavior with requirements/BASELINE.md; test each of F01–F08 in both hosts. Verify formal ADS/ASD-STE100 conformance only using designated checker or review evidence. Measure false instruction acceptance and missed clarification in addition to language quality.

## Communication quality verification

Use `python3 -m unittest discover -s tests -v` at the canonical package root. Verify actual PreToolUse event routing and tool name mappings in each required host. Validate A01 acceptance and A02 source-safe information, directive messages, and unsupported transports. The local test suite is only component evidence; host runtime verification remains a separate mandatory gate.

## Current runtime limitation

The receiving-agent assessment is an explicit callable interface. An incoming host boundary MUST supply the trusted recipient verification result. The installed host's post-tool events might not cover all agent messages, and post-tool checks cannot undo a completed tool action. No end-to-end enforcement claim applies until the host integration tests pass.

## Automated ADS contract verification

The package contains exact copies of the ADS 5.0.0-rc.2 Skill API, envelope, and common definitions schemas under `schemas/ads/`. Run `python3 -m pip install 'jsonschema>=4.20,<5'` in an isolated test environment, then run `python3 -m unittest discover -s tests -v`. Run `python3 scripts/validate_ads.py` from the package root to validate the local Skill API. The `check_envelope` function validates addressed requests against the local API and offline schema bundle. This does not establish the caller's authority or execute payloads. A payload that has its own declared request schema still requires validation against that target schema.

## Opaque collaboration messages

Codex CLI 0.164.0 tests showed that `collaborationspawn_agent.message` and `collaborationsend_message.message` reached `PreToolUse` as opaque-looking strings. The adapter treats these as uninspectable, issues advisory context without a permission decision, and does not claim content validation. The `collaborationfollowup_task` alias is a candidate pending field testing. Classification and receipt-side acceptance remain the responsibility of the communicating agents and trusted host boundaries. Neither advisory hook setup nor delivery of a marker proves enforcement.
