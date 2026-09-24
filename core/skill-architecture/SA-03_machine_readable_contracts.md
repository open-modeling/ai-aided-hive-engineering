# Skill Architecture — Machine-Readable Contracts

**Document ID:** SA-03  
**Status:** Normative machine-readable contract baseline release candidate  
**Suite version:** 5.0.0-rc.1  
**Date:** 2026-09-13  
**Parent:** ADS-00  
**Language baseline:** LMC  
**Terminology baseline:** SA-01

## 1. Purpose

This standard defines mandatory schema coverage for machine-readable artifacts used by AI DevMode skills and Skill Architecture release evidence.

It also defines schema identity, ownership, reuse, composition, resolution, versioning, validation, and permitted distribution copies.

## 2. Coverage requirement

Every machine-readable artifact produced, consumed, exchanged, or persisted by a skill **MUST** be covered by an identified machine-checkable schema or interface definition.

Coverage applies to artifacts such as:

- `skill-api.json`;
- structured role-to-skill and skill-to-skill messages;
- YAML or JSON frontmatter and manifests;
- configuration files and structured settings;
- state and runtime metadata;
- project-binding records;
- indexes and registries;
- machine-readable handoffs;
- migration records;
- conformance records;
- structured inter-process or network payloads.

Executable source code is not a machine-readable artifact under this standard.

Root `CHANGELOG.md` is human-readable release documentation and is not a machine-readable artifact.

A machine-readable example **MUST** conform to its declared schema unless it is explicitly labeled as invalid test input.

## 3. Schema identity

Every schema **MUST** have a canonical absolute URI identifier.

Every ADS-owned or skill-owned schema **MUST** have a semantic version under SA-05.

A JSON Schema **MUST** use `$schema` and `$id`.

A schema `$id` **MUST** be an absolute URI under RFC 3986.

ADS-owned schemas **MUST** identify their schema semantic version in `x-ads-schema-version`.

A skill-owned schema **SHOULD** expose equivalent machine-readable version metadata when its schema language permits it.

An artifact **SHOULD** identify its schema URI or schema version when the representation supports that metadata without unnecessary duplication.

## 4. Schema ownership

A common contract used by multiple skills **SHOULD** have one canonical common schema owner.

A domain-specific contract **MUST** remain owned by the skill that owns the domain behavior.

A skill **MUST NOT** duplicate a shared concept only to avoid a common schema dependency when a compatible common schema exists.

A shared schema **MUST NOT** absorb skill-specific domain semantics only to increase reuse.

## 5. Schema reuse and composition

Compatible common schemas **SHOULD** be reused across skills.

Schema composition **SHOULD** be used when a skill adds domain-specific constraints to a shared structure.

A skill-local schema **MAY** reference a canonical common schema directly during development and integrated operation.

A skill-local schema **MAY** reference a vendored common schema copy during self-contained distribution.

The final effective schema **MUST** constrain the complete machine-readable artifact that the skill relies on.

An envelope schema with an unconstrained domain payload **MUST** be composed with or accompanied by the payload schema before the payload is relied on.

## 6. Schema-bundle resolution

A self-contained distribution **MUST** include every transitive schema dependency required for offline validation.

Before validating an artifact, the validator **MUST** build or use a schema registry that maps each packaged canonical `$id` to its packaged schema content.

Internal absolute `$ref` values **MUST** resolve through that registry without network access.

A package **MUST NOT** claim self-contained schema validation when a required internal `$ref` cannot resolve from packaged content.

A schema bundle **MUST NOT** contain two different schema documents with the same canonical `$id`.

A validator **MUST** report the unresolved reference and the affected artifact when resolution fails.

The ADS reference validation script in `scripts/validate_ads_bundle.py` implements this registry model for the suite.

A skill **MAY** reuse that script or implement an equivalent validator.

## 7. Distribution copies

A skill **MAY** copy a common schema into its package when self-contained distribution or offline validation requires it.

A vendored schema copy **MUST** preserve:

1. canonical schema URI;
2. canonical schema version;
3. source traceability;
4. license or notice requirements when applicable.

A skill **MUST NOT** modify a vendored common schema while retaining the canonical identifier.

A modified contract **MUST** receive a new schema identity and clear ownership.

A packager **SHOULD** verify that each vendored schema copy matches the expected canonical content.

## 8. Format-specific schema mechanisms

Use the natural machine-checkable contract mechanism for the artifact format.

| Artifact form | Preferred contract mechanism |
|---|---|
| JSON | JSON Schema Draft 2020-12 |
| YAML with JSON-compatible data model | JSON Schema Draft 2020-12 |
| XML | W3C XML Schema or another required machine-checkable XML contract |
| HTTP API | OpenAPI with complete request and response schemas |
| Protocol Buffers | `.proto` interface definition |
| Relational data | DDL plus required constraints and migration definitions |
| Other structured formats | Equivalent machine-checkable grammar, IDL, or schema |

A skill **MAY** use another schema mechanism when it provides equivalent machine-checkable coverage and the choice is documented.

## 9. Validation contract

A skill **MUST** validate a machine-readable artifact before relying on it.

A producer **MUST** validate an artifact before persisting or emitting it.

A stateful skill **MUST** validate mutable state before mutation and after a successful mutation.

A configurable skill **MUST** validate configuration before applying it.

A Skill API **MUST** pass both JSON Schema validation and semantic reference checks before activation verification passes.

A structured skill communication envelope **MUST** validate before dispatch.

When the resolved target capability declares `request_schema_uri`, `payload_schema_uri` **MUST** equal that declared URI.

The payload **MUST** validate against the resolved target capability's declared request schema before the target skill relies on it. A caller-selected alternate schema **MUST NOT** replace the target contract.

A schema validation failure **MUST** identify the artifact, schema URI, failed condition, affected capability, and recovery action.

A skill **MUST NOT** silently coerce schema-invalid data into valid data unless an explicit migration contract permits that transformation.

## 10. Cross-field and semantic constraints

A schema intended as conformance evidence **MUST** encode logically enforceable relationships between its fields when JSON Schema can express those relationships.

The common skill conformance-record schema **MUST** enforce these rules:

- unconditional gates cannot be `N/A`;
- configuration gate applicability follows configuration classification;
- lifecycle gate applicability follows lifecycle classification;
- stateful classification implies persistent project data;
- persistence gate applicability follows whether project-derived data is persisted;
- a passing host-compatibility gate requires both host results to pass;
- a passing changelog gate requires changelog evidence to pass;
- a passing Skill API gate requires Skill API evidence to pass;
- a final passing result requires every applicable mandatory gate to pass;
- `PASS WITH SHOULD DEVIATIONS` requires at least one recorded deviation;
- `PASS` requires no recorded `SHOULD` deviation.

Semantic relationships that JSON Schema cannot express **MUST** be checked by deterministic validation code or tests.

The conformance-record validator **MUST** verify that `skill_name` equals the local skill-name component of `skill_uri`.

When the applicable `skill-api.json` is available, the conformance-record validator **MUST** verify matching `skill_uri`, skill name, semantic version, lifecycle classification, and configuration classification.

The addressed-message validator **MUST** verify that the target capability exists, each expected outcome is linked to that capability, and the payload contract matches the capability's declared request schema when one is declared.

## 11. Schema evolution and compatibility

A schema change **MUST** be versioned under SA-05.

Before a shared schema changes, the owner **MUST** assess producer and consumer compatibility.

A backward-compatible schema extension **SHOULD** increment MINOR when it adds supported structure or semantics.

A schema-only correction that changes no accepted instance set and no defined semantics **SHOULD** increment PATCH.

A backward-incompatible shared-schema change **MUST** increment the schema MAJOR version and trigger review of consuming skills.

A skill that persists artifacts across versions **MUST** provide migration when the new implementation cannot directly consume the previous supported schema.

A migration **MUST** identify source schema, target schema, validation, and recovery behavior.

## 12. Common schema catalog

Skill Architecture provides reusable schemas in `schemas/`.

| Schema | Purpose |
|---|---|
| `ads-common-definitions.schema.json` | Shared URI, classification, lifecycle, version, project, gate, and token definitions. |
| `skill-frontmatter.schema.json` | Common cross-host `SKILL.md` frontmatter contract. |
| `skill-api.schema.json` | Mandatory Skill API contract for identity, applicability, capabilities, and outcomes. |
| `skill-message-envelope.schema.json` | Common addressed role-to-skill and skill-to-skill communication envelope. |
| `stateful-runtime-envelope.schema.json` | Reusable project-local stateful runtime envelope. |
| `skill-conformance-record.schema.json` | Machine-readable ADS 5.0.0-rc.1 skill release-candidate and gate evidence. |

A skill **SHOULD** reuse these schemas when it uses the corresponding common concepts.

A skill **MAY** vendor required common schemas into its package under Section 7.

## 13. Skill schema inventory

Each skill **MUST** maintain a human-readable schema inventory in its domain specification, operations guide, or schema README.

The inventory **MUST** identify:

1. artifact name;
2. artifact purpose;
3. schema URI and semantic version;
4. canonical schema owner;
5. producer and consumer;
6. persistence scope when applicable;
7. migration rule when applicable.

If a skill creates a machine-readable schema registry or catalog, that registry **MUST** have its own schema.

## 14. Conformance

Schema conformance is a mandatory release gate under SA-07.

A release **MUST NOT** pass with an uncovered machine-readable artifact.

A release **MUST NOT** pass with an artifact that fails its declared schema.

A release **MUST NOT** pass with an unresolved required schema reference.

A release **MUST NOT** pass with a silently modified vendored common schema.

A release **MUST NOT** pass when conformance evidence can represent a logically impossible PASS state as schema-valid.

## 15. Related documents

- Governance: [../00_governance_and_bootstrap.md](../00_governance_and_bootstrap.md)
- Skill Architecture dictionary: [SA-01_skill_architecture_dictionary.md](SA-01_skill_architecture_dictionary.md)
- Architecture: [SA-02_skill_architecture_framework.md](SA-02_skill_architecture_framework.md)
- Language & Meaning: [../language-core/README.md](../language-core/README.md)
- Development gates: [SA-07_skill_development_and_conformance.md](SA-07_skill_development_and_conformance.md)
- Standards basis: [../language-core/LMC-01_language_standards_profile.md](../language-core/LMC-01_language_standards_profile.md)
- Required-host compatibility: [SA-04_required_host_compatibility.md](SA-04_required_host_compatibility.md)
- Versioning policy: [SA-05_versioning_and_evolution.md](SA-05_versioning_and_evolution.md)
- Skill API and communication: [SA-06_skill_api_and_communication.md](SA-06_skill_api_and_communication.md)
