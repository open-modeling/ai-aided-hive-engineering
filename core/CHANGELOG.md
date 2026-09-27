# Changelog

All notable changes to AI DevMode Standards are recorded here.

## [Unreleased]

## [5.0.0-rc.2] - 2026-09-26

### Changed

- Defined Examples and Illustrations as explicitly labeled, non-binding explanatory material in LMC-03.
- Required format-native visual distinction for explanatory material in each governed rendered publication.
- Added explanatory-material handling to the LMC-04 review sequence and conformance basis.

### Added

- Added required `explanatory_material` evidence to the Language & Meaning conformance schema.
- Added adversarial validator tests for missing or contradictory explanatory-material conformance evidence.

### Migration

- Language & Meaning conformance records created for `5.0.0-rc.1` must add `explanatory_material` with `PASS`, `FAIL`, or `N/A` before validation against `5.0.0-rc.2`. A record with overall `PASS` permits only `PASS` or `N/A`.

## [5.0.0-rc.1] - 2026-09-13

### Changed

- Split ADS into Part I — Language & Meaning Core and Part II — Skill Architecture with a one-way dependency from Part II to Part I.
- Replaced the former internal controlled-language standard model with an applicability/profile model that keeps BCP 14, ASD-STE100 Issue 9, and applicable ISO/IEC/IEEE standards authoritative.
- Added mandatory self-bootstrapping for every governed guideline update, including dual review when Part I changes.
- Moved shared terminology, meaning control, protected-source handling, mathematical/machine-token applicability, and conformance evidence into Part I.
- Retained skill-specific identity, lifecycle, persistence, schema, host, versioning, Skill API, communication, and release rules in Part II.
- Changed skill conformance evidence so its language gate depends on reusable Part I Language & Meaning conformance evidence.

### Added

- Added `language-core/schemas/language-meaning-conformance.schema.json` for reusable project language/meaning evidence.
- Added `BOOTSTRAP_CONFORMANCE.md` for ADS self-bootstrap evidence.
- Added physical `language-core/` and `skill-architecture/` source trees.

### Migration

- Project documents that previously treated ADS-03 as the controlled-language authority must reference the Language & Meaning Core profile and the project-authorized external standards resources instead.
- Skill implementations keep their existing skill-architecture contracts unless a renamed source reference or new Language & Meaning evidence requirement affects their release workflow.
