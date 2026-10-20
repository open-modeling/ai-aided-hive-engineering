# Operations and host coverage

Version: 0.3.0-dev. Canonical URI: skill:ai-devmode.conversation-governor.

## Installation

Codex project: place the canonical package under `.agents/skills/conversation-governor/`. Claude Code project: place the same canonical package under `.claude/skills/conversation-governor/`. Verify each host discovers the same `skill_uri`, version, and `skill-api.json`. Inspect other installed skills for same-name conflicts. Prefer links to a single canonical package where supported.

## Hook policy

Register a supported host hook only after confirming its event schema and observed behavior. The bundled adapter examines recognized agent-message tool names and their message or prompt text. It requires an `[INFORMATION]` or `[DIRECTION]` label; directions require `Action:`, `Target:`, and `Expected-Result:`. Validate inbound prompts and agent-tool messages where hooks provide the source text. Use pre-dispatch hooks when available for directional agent calls; treat response-time hooks as complementary feedback. Apply the instruction-level quality review for messages that cannot be intercepted. Verify hooks with a sample message that includes an instruction-like quotation and a sample directional request. Failures produce a targeted communication correction.

## Upgrade, validation and recovery

Review CHANGELOG.md and the installed version, replace the host projection with the tested canonical release, and verify discovery and relevant hook execution. On missing project dictionary, preserve the supplied term and ask for a definition when necessary. On unsupported hook events, run the in-context checks and report the event-coverage limitation. Stateless operation requires no initialization or reinitialization.

## Conformance

Compare behavior with requirements/BASELINE.md; test each of F01–F08 in both hosts. Verify formal ADS/ASD-STE100 conformance only using designated checker or review evidence. Measure false instruction acceptance and missed clarification in addition to language quality.
