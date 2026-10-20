# Changelog

## Unreleased

### Fixed
- A01: Separate message validity from action approval. REJECT and DEFER now prevent the check from approving execution.
- A02: Check agent messages at recognized tool communication boundaries using the tool name and message text. Require an information or direction label and actionable fields for directions.

### Changed
- Add regression tests for acceptance decisions, outgoing self-acceptance, and agent-message hook checks.
- Document the supported hook boundary and remaining semantic and host-runtime checks.

## 0.3.0-dev — 2026-10-16

- Replaced continuity-ledger design with stateless communication rules.
- Added the full BCP 14 requirements baseline and explicit directional acceptance.
- Added portable ADS integration, project terminology, and communication checks.
- Added host operations guidance; hook adapters and runtime conformance remain pending.
