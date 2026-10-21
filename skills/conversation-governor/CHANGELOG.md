# Changelog

## Unreleased

### Fixed
- A02 transport audit: replace suffix-based MCP transport detection with exact registered tool identity and message-field mappings, avoiding unrelated messaging tools and supporting verified hyphenated service names through explicit mappings.
- Add receiver-side regression tests for information non-execution, acceptance with trusted authority, and transport classification.
- A02 follow-up: inspect canonical and MCP agent-message transports, flag indirect-action wording and vague instructions, preserve multi-line quotations as escaped JSON strings, and block malformed hook JSON.
- A01: Separate message validity from action approval. REJECT and DEFER now prevent the check from approving execution.
- A02: Check agent messages at recognized tool communication boundaries using the tool name and message text. Require an information or direction label and actionable fields for directions.

### Changed
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
