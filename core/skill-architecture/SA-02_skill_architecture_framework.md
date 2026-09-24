# Skill Architecture — Framework

**Document ID:** SA-02  
**Status:** Normative architecture and lifecycle baseline  
**Suite version:** 5.0.0-rc.1  
**Date:** 2026-09-13  
**Parent:** ADS-00  
**Language baseline:** LMC  
**Terminology baseline:** SA-01  
**Schema standard:** SA-03  
**Host compatibility standard:** SA-04  
**Versioning standard:** SA-05  
**Skill API standard:** SA-06

## 1. Purpose

This framework defines the common architecture for reusable agent skills in AI DevMode.

It standardizes identity, package structure, classification, discovery, installation, optional configuration, stateful lifecycle behavior, project-local persistence, concurrency, validation, schema use, dual-host compatibility, communication, and operational procedures.

Each skill remains an independent product. Each skill owns its domain behavior, skill-local schemas, optional configuration, state when applicable, migrations, tests, semantic versions, and release lifecycle.

## 2. Framework principles

Every project skill **MUST** follow these principles.

1. Maintain one canonical package.
2. Maintain one canonical `skill_uri` across versions and host projections.
3. Publish one root `skill-api.json` that defines applicability, implemented capabilities, and desired outcomes.
4. Keep domain ownership independent for each skill.
5. Declare stateful or stateless classification.
6. Declare configurable or non-configurable classification.
7. Cover every machine-readable artifact with an identified schema.
8. Reuse compatible common schemas before defining duplicates.
9. Keep the activation surface compact.
10. Use progressive disclosure for detailed material.
11. Keep canonical YAML frontmatter limited to `name` and `description`.
12. Separate installation, configuration, initialization, and reinitialization.
13. Apply initialization and reinitialization only to stateful skills.
14. Persist project-derived data only inside the active project.
15. Keep stateful readiness and mutation inside the active project scope.
16. Make stateful operations thread safe and non-blocking across concurrent operations.
17. Treat a global installation as read-only during project operation.
18. Never use another project's configuration, state, metadata, or readiness evidence for the active project.
19. Let project policy choose whether project-local configuration is committed or ignored.
20. Use deterministic validation and precise diagnostics.
21. Implement only justified capabilities.
22. Provide `references/operations.md` for agents and human operators.
23. Keep one canonical package compatible with Codex and Claude Code.
24. Version every released canonical package under SA-05.
25. Include root `CHANGELOG.md` and serve applicable changelog information during installation and upgrade.
26. Address formal role-to-skill and skill-to-skill communication by canonical skill URI.
27. Apply LMC to every human-readable skill artifact and human-readable machine-data string.

## 3. Skill classification

### 3.1 Lifecycle classification

Every skill **MUST** be classified as **stateful** or **stateless**.

A stateful skill persists mutable project-scoped runtime state across operations.

A stateless skill does not persist mutable project-scoped runtime state across operations.

A stateful skill **MUST** employ the initialization and reinitialization lifecycle in Section 12.

A stateless skill **MUST NOT** employ initialization or reinitialization.

A stateless skill **MUST** validate required invocation preconditions during each operation.

### 3.2 Configuration classification

Every skill **MUST** be classified as **configurable** or **non-configurable**.

A skill **MAY** support configuration regardless of lifecycle classification.

Configuration support **MUST NOT** substitute for stateful lifecycle state.

A configurable skill **SHOULD** operate without a configuration instance when documented defaults satisfy all mandatory preconditions and domain invariants.

A capability **MAY** require configuration when no documented default can satisfy its mandatory preconditions or domain invariants.

### 3.3 Valid combinations

| Lifecycle | Configuration | Required behavior |
|---|---|---|
| stateless | non-configurable | Validate invocation inputs and run. |
| stateless | configurable | Resolve and validate configuration for the invocation, then run. |
| stateful | non-configurable | Use initialization and reinitialization for project-scoped state. |
| stateful | configurable | Resolve configuration and use initialization and reinitialization for project-scoped state. |

## 4. Common architecture

The framework separates nine concerns.

### 4.1 Canonical package

The canonical package is the maintained source of the skill.

Every host projection **MUST** remain traceable to the same canonical package version.

The canonical package **MUST** be host-neutral for required behavior.

### 4.2 Canonical identity

Every skill **MUST** have one canonical `skill_uri` under SA-06.

The canonical form **MUST** be `skill:<publisher>.<skill-name>`.

The publisher namespace **MUST** be author-supplied and stable.

ADS **MUST NOT** require external publisher validation.

The URI **MUST** remain stable across skill versions, hosts, installations, and projects.

The host-facing `name` is a discovery alias and **MUST NOT** replace `skill_uri` as cross-host identity.

### 4.3 Skill API

Every skill **MUST** publish root `skill-api.json` under SA-06.

The Skill API **MUST** separate applicability, implemented capabilities, and desired outcomes.

The Skill API **MUST** match the package name, semantic version, lifecycle classification, configuration classification, and implemented public behavior.

### 4.4 Host adapter

A host adapter maps the canonical package into a host discovery model.

Every skill **MUST** support Codex and Claude Code adapters under SA-04.

A host adapter owns placement, links or copies, host metadata, collision detection, and discovery verification.

A host adapter **MUST NOT** own domain behavior that belongs in the canonical package.

### 4.5 Machine-readable contracts

Every machine-readable artifact produced, consumed, exchanged, or persisted by a skill **MUST** be covered by SA-03.

Common concepts **SHOULD** use common schemas or common schema definitions.

Skill-specific concepts **MAY** use skill-local schemas.

### 4.6 Configuration

Configuration is optional.

When configuration exists, the skill owns its configuration contract, defaults, validation, scope, migration behavior, and project-local storage contract.

Persistent configuration **MUST** remain inside the active project.

Configuration **MUST** remain distinct from lifecycle readiness state.

### 4.7 Project scope and binding

A stateful skill **MUST** resolve the active project scope before state mutation.

A stateful skill **MAY** use a project binding to locate project authority, integrations, paths, or identifiers.

A binding **MUST** point to project authority.

A binding **MUST NOT** replace that authority.

### 4.8 Runtime state

Runtime state exists only for a stateful skill.

Runtime state **MUST** be project-scoped, schema-covered, minimal, and subordinate to project authority.

### 4.9 Domain behavior

Domain behavior is the skill's unique capability implementation.

Each skill **MUST** own its domain behavior independently.

Shared architecture **MUST NOT** create an unnecessary runtime dependency between independent skills.

## 5. Standard package contract

### 5.1 Canonical directory shape

Use this package shape.

```text
<skill-name>/
├── SKILL.md
├── skill-api.json
├── CHANGELOG.md
├── references/
│   └── operations.md
├── scripts/
├── schemas/
├── assets/
└── <skill-owned runtime helpers when justified>
```

`SKILL.md`, `skill-api.json`, `CHANGELOG.md`, and `references/operations.md` are universally required.

Add another resource only when it supports a justified capability, reliability, validation, portability, recovery, or progressive disclosure.

### 5.2 Distribution shape

A standalone skill archive **MUST** contain exactly one top-level skill directory.

```text
<skill-name>.zip
└── <skill-name>/
    ├── SKILL.md
    ├── skill-api.json
    ├── CHANGELOG.md
    ├── references/
    │   └── operations.md
    └── ...
```

### 5.3 Canonical-source rule

Every installed projection **MUST** identify the canonical package version and canonical `skill_uri`.

A host adapter **SHOULD** use links when the host supports them and the link preserves one maintained source.

A versioned copy **MAY** be used when the host or distribution model requires it.

A vendored common schema copy **MAY** be included under SA-03.

### 5.4 Changelog package contract

Every released canonical package **MUST** contain root `CHANGELOG.md`.

The changelog **MUST** conform to SA-05 and LMC.

Every host projection **MUST** preserve access to the changelog for the installed version.

A global installation **MAY** contain the immutable packaged changelog because it is distribution content.

Project operation **MUST NOT** write project-derived information into the packaged changelog.

## 6. `SKILL.md` contract

`SKILL.md` is the activation surface. It is not the full manual.

### 6.1 Frontmatter

Canonical frontmatter **MUST** contain only these fields.

```yaml
---
name: <kebab-case-skill-name>
description: <routing summary of when the skill applies and its important boundary>
---
```

The frontmatter **MUST** conform to the common frontmatter schema.

The canonical frontmatter **MUST** use only the subset accepted by both required hosts.

The parent canonical package directory name **MUST** equal the frontmatter `name` exactly.

The `name` in `skill-api.json` **MUST** equal the same directory and frontmatter name.

### 6.2 Identity and API routing

The body **MUST** identify the canonical `skill_uri`.

The body **MUST** route the agent to root `skill-api.json` for the complete applicability, capability, and outcome contract.

The URI in `SKILL.md` **MUST** match `skill-api.json`.

### 6.3 Description

The description **SHOULD** summarize `skill-api.json` applicability.

The description **SHOULD** state the primary qualifying task early and state an important exclusion when ambiguity is likely.

The description **MUST NOT** contradict `when_to_use` or `when_not_to_use`.

### 6.4 Body

Keep only activation-critical information in the body.

The body **SHOULD** contain only activation-critical information:

1. canonical `skill_uri`;
2. purpose and scope;
3. lifecycle classification;
4. configuration classification;
5. readiness rule for a stateful skill;
6. critical invariants;
7. shortest reliable workflow;
8. routes to `skill-api.json` and `references/operations.md`;
9. failure behavior for unresolved prerequisites.

Move long procedures, examples, schemas, migrations, and edge cases to supporting resources.

### 6.5 Language

All human-readable `SKILL.md` text **MUST** follow the Language & Meaning Core.

The package **MUST** use SA-01 terms for common concepts.

## 7. Skill API contract

Every skill **MUST** comply with SA-06.

`skill-api.json` **MUST** be schema-valid before the host adapter reports installation success.

At least one `when_to_use` scenario **MUST** enable routing before activation.

Any matching `when_not_to_use` scenario **MUST** disable activation.

Every declared capability **MUST** be implemented and justified.

Every public implemented capability **MUST** be declared.

Every desired outcome **MUST** have acceptance criteria.

Capability-to-outcome references **MUST** resolve within the same Skill API.

## 8. Progressive disclosure and operations guide

### 8.1 References

Use `references/` for procedures, policies, examples, edge cases, migrations, and integration-specific guidance.

`SKILL.md` **SHOULD** state the conditions that require loading an important reference.

### 8.2 Universal operations guide

Every released skill **MUST** provide `references/operations.md` for agents and human operators.

The guide **MUST** cover:

1. installation for Codex;
2. installation for Claude Code;
3. upgrade;
4. discovery and identity verification;
5. installed semantic version and changelog serving;
6. validation;
7. recovery from supported installation or verification failures.

A configurable skill **MUST** also cover configuration discovery, creation or update, validation, active-source determination, and reset when supported.

A stateful skill **MUST** also cover initialization, reinitialization, readiness verification, staleness, and BLOCKED recovery.

Each applicable operation **MUST** include an agent procedure and a human procedure.

The human procedure **MUST** be executable without hidden agent-only knowledge.

### 8.3 Scripts

Use `scripts/` when deterministic execution improves reliability.

A script **SHOULD** accept explicit inputs and return useful status. A repeatable script **SHOULD** be idempotent.

### 8.4 Schemas

Use `schemas/` for skill-local schemas and permitted vendored common schema copies.

Schema ownership, reuse, resolution, identifiers, validation, and distribution **MUST** comply with SA-03.

### 8.5 Assets

Use `assets/` for static templates or resources that support the skill.

Do not place activation-critical instructions only in an asset.

## 9. Authority and configuration model

Resolve conflicting project information in this order.

1. Current explicit user instruction, within project and safety constraints.
2. Authoritative project policy and context.
3. Validated project binding that references project authority, when stateful.
4. Valid project-local configuration for the active project.
5. Skill defaults and references.
6. Generic host defaults that do not contain project-derived skill data.

Policy defines what the project requires.

Configuration selects permitted behavior within the skill contract.

Binding defines how a stateful skill locates or interfaces with authority.

Runtime metadata stores derived facts.

Runtime state stores mutable project-scoped state for a stateful skill.

A configuration change that affects a stateful binding or runtime invariant **MUST** be a staleness trigger.

## 10. Configuration contract

### 10.1 Optional support

A skill **MAY** support configuration.

A non-configurable skill **MUST NOT** add unused settings, placeholder settings, or configuration files for symmetry.

### 10.2 Project-local storage

Every persistent configuration instance **MUST** be stored inside the active project.

A configurable skill **MUST NOT** use a user-global, machine-global, shared cross-project, or installation-directory configuration instance as project configuration.

A globally installed skill **MUST** resolve persistent configuration from the active project for each project operation.

Configuration from one project **MUST NOT** satisfy a configuration requirement in another project.

Configuration **MUST** be separable from generated runtime state and runtime metadata.

The developer or authoritative project policy **MUST** decide whether project-local configuration is committed or ignored.

The skill **MUST NOT** force either version-control choice.

An installer **MUST NOT** stage configuration or modify `.gitignore` without explicit user or project instruction.

### 10.3 Configuration schema

Every configuration artifact **MUST** conform to an identified schema under SA-03.

A configuration schema **SHOULD** reuse common schema definitions when concepts are shared.

### 10.4 Configuration scope and precedence

A configurable skill **MUST** define project-local configuration sources.

The skill **MUST** define precedence when more than one project-local source can apply.

Configuration resolution **MUST** be deterministic.

Invocation inputs **MAY** override configuration when the domain contract permits the override.

An invocation override does not become persistent configuration unless it is explicitly written inside the active project.

## 11. Installation contract

### 11.1 Definition

A skill is installed when the target host can discover its canonical package or projection.

Installation establishes discovery. It does not establish stateful readiness and does not imply that configuration exists.

Installation scope does not change persistence scope.

### 11.2 Installer requirements

Every installer **MUST** be runtime-aware, idempotent, preserving, verifiable, diagnostic, and canonical-source preserving.

Every release **MUST** support installation and discovery verification in Codex and Claude Code.

The installer **MUST** validate package shape, `skill-api.json`, schema availability, and `CHANGELOG.md` before reporting success.

The installer **MUST** compare visible same-name skills and verify the intended `skill_uri` and version under SA-04.

The installer **MUST** distinguish skill locations from agent, subagent, MCP, and unrelated configuration locations.

The installer **MUST** serve the installed semantic version and applicable changelog information.

### 11.3 Installation workflow

Use this workflow.

1. Detect or select the host.
2. Resolve a verified discovery location.
3. Validate the canonical package structure.
4. Validate `skill-api.json` and canonical `skill_uri`.
5. Detect reserved names and visible identity or version collisions.
6. Establish the projection by link or copy.
7. Preserve unrelated files.
8. Verify actual discovery and the identity of the package the host will execute.
9. Report canonical source, installed projection, `skill_uri`, and semantic version.
10. Serve the changelog location and applicable release entry or upgrade range.
11. Route the operator to migration, configuration, initialization, or reinitialization only when applicable.

## 12. Stateful initialization and reinitialization lifecycle

This section applies only to a stateful skill.

A stateless skill **MUST NOT** implement these lifecycle states or procedures.

### 12.1 Lifecycle states

| State | Meaning | Required behavior |
|---|---|---|
| **UNINITIALIZED** | Required project scope and initial runtime state are not established. | Initialize before a governed stateful operation. |
| **READY** | Required project scope, binding, and state are validated. | Governed stateful operations can run. |
| **STALE** | Relevant project context changed after validation. | Revalidate or reinitialize before relying on affected state. |
| **BLOCKED** | A required prerequisite cannot be resolved or validated. | Report the prerequisite, affected capability, and recovery action. |

A stateful skill **MAY** store these states in its own schema-covered metadata format.

### 12.2 Initialization contract

Initialization **MUST**:

1. resolve the active project scope;
2. resolve required project authority and bindings;
3. resolve configuration that influences initial state, when applicable;
4. validate required prerequisites;
5. create or migrate schema-valid project-scoped runtime state;
6. record evidence needed to detect staleness;
7. bind readiness evidence to the active project and canonical `skill_uri`;
8. finish in READY or BLOCKED.

Initialization **MUST** be idempotent.

Readiness evidence from another project **MUST NOT** satisfy READY status for the active project.

### 12.3 Reinitialization triggers

A stateful skill **MUST** reinitialize or revalidate when a relevant change can invalidate current state.

Typical triggers include:

- project authority change;
- configuration change that affects state or binding;
- MCP or integration change;
- authoritative path change;
- schema or binding-contract migration;
- state corruption or validation failure;
- project scope change;
- host-specific binding change that affects state validity.

## 13. Stateless execution model

A stateless skill **MUST NOT** create lifecycle readiness state.

A stateless skill **MUST NOT** expose initialization or reinitialization as operational steps.

Before each operation, a stateless skill **MUST** validate inputs, configuration when supported, schemas, applicability, and external prerequisites.

A failed precondition **MUST** produce a direct diagnostic and recovery action instead of a lifecycle transition.

## 14. Project-local persistence and isolation

This section applies to every skill that persists project-derived data.

A skill **MUST NOT** persist project-derived data outside the active project.

Project-derived persistent data includes configuration, runtime state, runtime metadata, project bindings, readiness evidence, generated caches, indexes, registries, logs, and other durable operational records.

A globally installed skill **MUST** treat its global package, projection, and installation directory as read-only during project operation.

A skill **MUST NOT** store project-derived data in user-global, machine-global, enterprise-global, or cross-project storage.

A skill **MUST NOT** maintain a shared registry that records project configuration, readiness, state, bindings, or runtime metadata outside the project.

A stateful skill **MUST NOT** infer active-project readiness from data created for another project.

A configurable skill **MUST NOT** use project A configuration while operating in project B.

The global installation **MAY** contain immutable distribution resources, schemas, templates, code, Skill API data, and changelog data.

Host-managed ephemeral execution storage **MAY** be used only when it is non-authoritative and non-persistent for project semantics.

The skill **MUST** document its project-local persistence root or paths.

Configuration **MUST** remain separable from generated runtime state.

When branches or worktrees can produce conflicting mutable state, project scope **SHOULD** distinguish those contexts.

## 15. Concurrency contract for stateful skills

Every stateful skill **MUST** be thread safe.

A stateful skill **MUST NOT** block concurrent operations with a cross-project or process-wide blocking lock.

State mutations **MUST** use atomic updates, optimistic concurrency, an equivalent non-blocking mechanism, or a combination of these mechanisms.

A stateful skill **MUST** detect conflicting concurrent writes before overwriting newer state.

A conflicting write **SHOULD** return a retryable conflict with current revision evidence.

A stateful skill **MUST** isolate mutable state by project scope.

Operations in different project scopes **MUST** proceed independently.

## 16. Required-host compatibility

Every skill **MUST** be compatible with Codex and Claude Code.

The same canonical package version and `skill_uri` **MUST** provide required domain behavior in both hosts.

The skill **MUST** satisfy SA-04 for discovery, identity resolution, installation, activation, references, scripts, Skill API access, configuration, lifecycle behavior when applicable, diagnostics, changelog serving, and project-local persistence.

Host-specific adapters **MAY** differ in placement and host metadata.

Host-specific adapters **MUST NOT** fork the domain contract or Skill API.

A release **MUST NOT** pass when required behavior works in only one required host.

## 17. Schema contract

Every machine-readable artifact **MUST** comply with SA-03.

A skill **SHOULD** reuse compatible common schemas.

A skill **MAY** copy a common schema into its distribution package when self-contained validation requires it.

A vendored schema copy **MUST** preserve canonical schema identity, version, and source traceability.

A skill **MUST NOT** silently modify a vendored common schema.

A self-contained schema bundle **MUST** resolve all transitive internal schema references offline under SA-03.

## 18. Capability discipline

Every skill-owned capability **MUST** have a capability justification.

Every public implemented capability **MUST** appear in `skill-api.json`.

Every capability declared in `skill-api.json` **MUST** exist in the implementation.

A valid justification connects a capability to at least one of these needs:

- domain behavior;
- required lifecycle behavior;
- configuration management;
- validation or schema enforcement;
- interoperability or host integration;
- required operator recovery;
- conformance evidence.

A skill **MUST NOT** implement or retain an unjustified capability.

## 19. Communication contract

Formal role-to-skill and skill-to-skill communication **MUST** follow SA-06.

An addressed role-to-skill request **MUST** use the target `skill_uri`.

An addressed skill-to-skill request **MUST** use source and target skill URIs.

Structured addressed communication **MUST** conform to the common skill communication envelope.

A target skill **MUST** validate applicability, capability ID, expected outcomes, payload schema, configuration, lifecycle readiness, and project scope before execution.

If the target capability declares `request_schema_uri`, the message `payload_schema_uri` **MUST** equal that declared URI.

The target **MUST** validate the payload against the target capability's declared request schema before execution. Validation against a caller-selected alternate schema **MUST NOT** satisfy this requirement.

A message **MUST NOT** bypass the target skill's applicability or lifecycle contract.

## 20. Validation and diagnostics

Validation **MUST** be deterministic when the same validated inputs and environment are supplied.

A machine-readable artifact **MUST** be schema-validated before a skill relies on it.

A Skill API **MUST** pass schema validation and semantic reference checks before activation verification passes.

A stateful skill **MUST** validate state before mutation and after a successful mutation.

A failing check **MUST** identify:

1. the failed condition;
2. the affected capability;
3. evidence when available;
4. the recovery action.

A skill **MUST NOT** invent missing authority, configuration, state, identity, or schema validity.

## 21. Handoff contract

Operational handoffs **SHOULD** remain compact.

A handoff **SHOULD** contain current facts, active decisions, open work, blockers, evidence, and the next action that satisfies all mandatory preconditions.

A formal handoff that assigns work to a skill **MUST** identify the target `skill_uri` and semantic version.

When the handoff requests a public capability, it **SHOULD** identify the capability ID and desired outcome IDs.

Machine-readable handoff payloads **MUST** conform to an identified schema.

## 22. Related documents

- Suite governance: [../00_governance_and_bootstrap.md](../00_governance_and_bootstrap.md)
- Skill Architecture dictionary: [SA-01_skill_architecture_dictionary.md](SA-01_skill_architecture_dictionary.md)
- Language & Meaning: [../language-core/README.md](../language-core/README.md)
- Development and conformance: [SA-07_skill_development_and_conformance.md](SA-07_skill_development_and_conformance.md)
- Standards basis: [../language-core/LMC-01_language_standards_profile.md](../language-core/LMC-01_language_standards_profile.md)
- Schema governance: [SA-03_machine_readable_contracts.md](SA-03_machine_readable_contracts.md)
- Required-host compatibility: [SA-04_required_host_compatibility.md](SA-04_required_host_compatibility.md)
- Versioning policy: [SA-05_versioning_and_evolution.md](SA-05_versioning_and_evolution.md)
- Skill identity and communication: [SA-06_skill_api_and_communication.md](SA-06_skill_api_and_communication.md)
