# Changelog

## Unreleased

### 0.4.0-dev candidate — 2026-10-26
- Align activation instructions with ADS information-construction and terminology rules.
- Use a connected receive, prepare, and verify workflow with conditional references.
- Align the ADS skill URI location rule with frontmatter metadata.
- Align the human-facing display name across activation and host metadata.
- Enable implicit invocation and retain explicit `$conversation-governor` invocation.
- Reframe the activation procedure around language norms, communication, and validation.
- Add a minimal skill-owned dictionary and locally packaged ADS references.
- Update the public capability contract and provide a local-package upgrade path.
- Retain a designated language review and clean-host runtime verification as release gates.


### Fixed
- Add offline validation of the ADS Skill API and SA-06 addressed communication envelope; reject mismatched targets, capabilities, outcomes, versions, and malformed payload contracts.
- Add vendored ADS 5.0.0-rc.2 schemas and Python CI schema tests.
- Differentiate valid informational processing from action permission; require trusted recipient authority, scope, and conditions for direction acceptance.
- Return a review-required result for ambiguous informational statements, including instructions in later sentences.
- A02 transport audit: replace suffix-based MCP transport detection with exact registered tool identity and message-field mappings, avoiding unrelated messaging tools and supporting verified hyphenated service names through explicit mappings.
- Add receiver-side regression tests for information non-execution, acceptance with trusted authority, and transport classification.
- A02 follow-up: inspect canonical and MCP agent-message transports, flag indirect-action wording and vague instructions, preserve multi-line quotations as escaped JSON strings, and block malformed hook JSON.
- A01: Separate message validity from action approval. REJECT and DEFER now prevent the check from approving execution.
- A02: Check agent messages at recognized tool communication boundaries using the tool name and message text. Require an information or direction label and actionable fields for directions.

### Changed
- Expose the human-readable name `Conversation Governor` in Codex skill metadata without changing the skill identifier.
- Route supported agent-message tool calls through the shared checker; use exact transport mappings and exclude task-list tools.
- Require neutral informational statements, preserve verbatim source commands as quoted text, and validate directional fields.
- Add adversarial cases for disguised instructions, direct instructions, missing fields, and unclassified messages.
- Add regression tests for acceptance decisions, outgoing self-acceptance, and agent-message hook checks.
- Document the supported hook boundary and remaining semantic and host-runtime checks.

## 0.3.0-dev — 2026-10-16

- Replaced continuity-ledger design with stateless communication rules.
- Added the full BCP 14 requirements baseline and explicit directional acceptance.
- Added portable ADS integration, project terminology, and communication checks.
- Added host operations guidance; hook adapters and runtime conformance remain pending.
