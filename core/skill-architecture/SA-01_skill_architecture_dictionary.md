# Skill Architecture — Dictionary

**Document ID:** SA-01  
**Status:** Normative skill-architecture terminology baseline  
**Suite version:** 5.0.0-rc.1  
**Part:** Skill Architecture  
**Parent:** ADS-00  
**Language baseline:** LMC

## 1. Purpose

This dictionary defines shared concepts whose correctness depends on the governed artifact being a reusable agent skill.

General language, meaning, evidence, requirement, and terminology rules remain in Part I.

## 2. Product and identity terms

| Term | Definition |
|---|---|
| **skill** | An independently owned agent capability package with a defined task boundary. |
| **canonical package** | The maintained source package from which supported host projections are derived. |
| **canonical source** | The authoritative maintained source location for a canonical package. |
| **projection** | A host-specific installed representation derived from a canonical package. |
| **host** | An agent harness or runtime that discovers and executes a skill. |
| **host adapter** | Logic that maps a canonical package into a host discovery and runtime model without owning domain behavior. |
| **domain behavior** | Skill-specific rules, algorithms, transformations, and workflows that provide the skill's unique capability. |
| **skill URI** | The publisher-qualified URI that identifies one skill lineage across versions, hosts, installations, and projects. |
| **publisher namespace** | A short author- or publisher-chosen namespace discriminator. It is not verified publisher identity. |
| **local skill name** | The host-facing skill name used as the second component of the skill URI. |
| **Skill API** | The mandatory machine-readable public skill interface in root `skill-api.json`. |

## 3. Applicability and capability terms

| Term | Definition |
|---|---|
| **applicability** | Conditions that determine whether a skill is eligible to handle a request. |
| **usage enabler** | One qualifying scenario in `when_to_use`. |
| **applicability exclusion** | One scenario in `when_not_to_use` that disables activation. |
| **implemented capability** | A function the skill actually provides and declares in its Skill API. |
| **capability ID** | A stable local identifier for one implemented capability within a skill lineage. |
| **desired outcome** | An observable result that a successful capability invocation is intended to produce. |
| **outcome ID** | A stable local identifier for one desired outcome within a skill lineage. |
| **capability justification** | The traceable engineering reason an implemented capability is required. |

## 4. Installation and operation terms

| Term | Definition |
|---|---|
| **discovery** | Host behavior that locates a skill and makes it eligible for activation. |
| **installation** | The operation that places or wires a skill where a host can discover it. |
| **global installation** | An installation that makes an immutable skill package discoverable from more than one project. |
| **project installation** | An installation whose discovery projection is stored inside one project. |
| **operations guide** | `references/operations.md`, containing installation, upgrade, verification, recovery, and applicable configuration or lifecycle procedures. |
| **configuration** | Externally supplied settings that influence skill behavior without representing lifecycle readiness. |
| **project binding** | Runtime resolution connecting a stateful skill to project authority. |
| **runtime metadata** | Skill-owned derived data used to operate efficiently or determine readiness. |

## 5. Lifecycle and persistence terms

| Term | Definition |
|---|---|
| **stateful skill** | A skill that persists mutable project-scoped runtime state across operations. |
| **stateless skill** | A skill that does not persist mutable project-scoped runtime state across operations. |
| **configurable skill** | A skill that supports externally supplied settings that influence behavior. |
| **non-configurable skill** | A skill whose behavior accepts no persistent project configuration beyond invocation inputs. |
| **initialization** | The stateful operation that establishes and validates project scope, required bindings, and initial runtime state. |
| **reinitialization** | Initialization repeated because prior state or binding is absent, stale, migrated, or invalid. |
| **UNINITIALIZED** | Required stateful project scope and initial runtime state are not established. |
| **READY** | Required stateful scope, bindings, and runtime state are resolved and validated. |
| **STALE** | Previously valid stateful runtime context requires revalidation because relevant context changed. |
| **BLOCKED** | A required prerequisite cannot currently be resolved or validated. |
| **project-derived data** | Data whose value is created, selected, updated, or persisted because of work in a specific project. |
| **project-local persistent data** | Project-derived data that persists and is stored inside the active project. |
| **readiness evidence** | Project-scoped evidence used to determine whether a stateful skill is READY. |

## 6. Machine-readable and communication terms

| Term | Definition |
|---|---|
| **skill-local schema** | A schema owned by one skill for a domain-specific artifact. |
| **common schema** | A reusable schema owned by Skill Architecture or another designated common contract owner. |
| **schema bundle** | A self-contained set of schemas including every transitive dependency needed for validation. |
| **role-to-skill communication** | An addressed request from an agent role to a target skill. |
| **skill-to-skill communication** | An addressed request from one skill to another skill. |
| **skill communication envelope** | The common schema-covered message structure for addressed skill requests. |
| **identity collision** | A condition in which a host can resolve a display name to a different skill URI or unintended version. |

## 7. Versioning terms

Skill releases, ADS releases, and ADS-owned schemas use Semantic Versioning under SA-05.

The skill public contract includes the Skill API, externally relied-on domain behavior, machine-readable contracts, lifecycle behavior, configuration behavior, stable operations, and required-host guarantees.
