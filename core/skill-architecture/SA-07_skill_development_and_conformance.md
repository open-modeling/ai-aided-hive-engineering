# Skill Architecture — Development and Conformance

**Document ID:** SA-07  
**Status:** Normative development and release guide release candidate  
**Suite version:** 5.0.0-rc.1  
**Date:** 2026-09-13  
**Parent:** ADS-00  
**Language baseline:** LMC  
**Terminology baseline:** SA-01  
**Architecture baseline:** SA-02  
**Schema baseline:** SA-03  
**Host compatibility baseline:** SA-04  
**Versioning baseline:** SA-05  
**Skill API baseline:** SA-06

## 1. Purpose

This guide defines the required workflow for creating, aligning, reviewing, and releasing AI DevMode skills.

This guide is governed by the Language & Meaning Core. A skill release uses the same common language and meaning foundation as this guide. Skill-specific language rules are limited to skill-domain extensions.

The workflow converts the shared framework into repeatable engineering and release gates.

## 2. Development workflow

### Step 1 — Define the domain boundary

Write one short domain contract.

State the skill purpose, governed tasks, inputs, outputs, integrations, side effects, and persistent project-derived data.

Keep the domain boundary independently testable.

### Step 2 — Assign canonical skill identity

Assign one canonical `skill_uri` under SA-06.

Use `skill:<publisher>.<skill-name>`.

Choose a short publisher namespace that makes same-name skills from different publishers visibly distinct.

Use 1-64 lowercase ASCII letters, digits, or hyphens. Start and end the publisher namespace with a letter or digit. Do not use consecutive hyphens or `.`.

The publisher namespace is author-supplied. Do not validate DNS ownership, legal identity, organization registration, publisher registry membership, or global uniqueness.

Keep the URI stable across versions, hosts, installations, and projects.

Record the same URI in `SKILL.md`, `skill-api.json`, release evidence, and addressed communication.

### Step 3 — Classify lifecycle and configuration

Declare the skill as **stateful** or **stateless**.

Declare the skill as **configurable** or **non-configurable**.

A stateful classification **MUST** include an initialization and reinitialization contract.

A stateless classification **MUST NOT** include initialization or reinitialization.

### Step 4 — Define the Skill API

Create root `skill-api.json`.

Define at least one `when_to_use` scenario.

Define `when_not_to_use` exclusions when a neighboring task can be confused with this skill.

Declare every public implemented capability.

For each capability, state `where_it_helps`, `does`, and linked outcome IDs.

Define each desired outcome with `what_to_expect` and testable acceptance criteria.

Validate capability-to-outcome references.

### Step 5 — Justify capabilities

Create a capability justification for every implemented capability, command, script, integration, configuration surface, persistent resource, and host hook.

A public capability in the implementation **MUST** appear in the Skill API.

A capability in the Skill API **MUST** exist in the implementation.

Remove any capability that has no current justification.

### Step 6 — Reuse the Skill Architecture dictionary

Review SA-01 before defining shared terms.

Add only domain-specific terms that are not already common concepts.

A domain glossary **MUST** reference SA-01 as its parent vocabulary.

### Step 7 — Inventory machine-readable artifacts

List every machine-readable artifact that the skill produces, consumes, exchanges, or persists.

Map every artifact to an identified schema or interface definition.

Reuse a compatible common schema before creating a duplicate.

Include every transitive schema dependency required for offline validation when the package is self-contained.

### Step 8 — Create the canonical package

Create one `<skill-name>/` directory.

Include these universal artifacts:

1. `SKILL.md`;
2. `skill-api.json`;
3. `CHANGELOG.md`;
4. `references/operations.md`.

Add `scripts/`, `schemas/`, `assets/`, and other resources only when they support justified behavior.

### Step 9 — Write the activation contract

Use only `name` and `description` in canonical frontmatter.

Validate frontmatter against the common frontmatter schema.

Verify that the canonical package directory name equals the `SKILL.md` frontmatter `name`. Verify that `skill-api.json` uses the same `name`.

Reject a name reserved by a required host, including Claude Code `synced` in the current host profile.

Keep `SKILL.md` compact.

State the canonical `skill_uri` in the body.

Route the agent to `skill-api.json` and `references/operations.md`.

Make the description consistent with Skill API applicability.

Apply LMC during authoring.

### Step 10 — Write the universal operations guide

Create `references/operations.md` for every skill.

Write separate executable agent and human procedures for each applicable operation.

Include Codex installation and verification.

Include Claude Code installation and verification.

Include upgrade, identity verification, semantic-version reporting, changelog serving, validation, and recovery.

For a configurable skill, include configuration procedures.

For a stateful skill, include initialization and reinitialization procedures.

### Step 11 — Define configuration when supported

For a configurable skill, define project-local sources, scope, precedence, defaults, validation, migration, and reset behavior.

Cover each configuration artifact with a schema.

Store every persistent configuration instance inside the active project.

Keep configuration separable from generated state and runtime metadata.

Allow project policy to choose whether configuration is committed or ignored.

### Step 12 — Define stateful project scope and lifecycle when applicable

For a stateful skill, define:

1. project scope resolution;
2. project authority and binding resolution;
3. state schema;
4. initialization behavior;
5. staleness triggers;
6. reinitialization behavior;
7. BLOCKED recovery;
8. state placement;
9. concurrency control;
10. readiness evidence bound to `skill_uri` and the active project.

### Step 13 — Implement both required host adapters

Implement Codex and Claude Code adapters for the same canonical package version and `skill_uri`.

For each host, define discovery, placement, collision detection, verification, upgrade, and removal behavior.

Enumerate visible same-name skills before claiming identity verification.

Verify which `skill_uri` and version the host actually resolves.

Do not make required domain behavior depend on a host-only extension.

### Step 14 — Implement deterministic validation

Validate package shape, frontmatter, Skill API, routed resources, schema resolution, configuration, state, migrations, and host identity.

Preload packaged schemas by canonical `$id` before resolving internal absolute `$ref` values.

A failing check **MUST** produce a precise diagnostic and recovery action.

### Step 15 — Implement project-local persistence and concurrency

For every skill that persists project-derived data, keep every persistent write inside the active project.

For a configurable skill, verify that persistent configuration is not reused across projects.

For a stateful skill, verify that state and readiness evidence are not reused across projects.

For a stateful skill, use atomic or optimistic concurrency control.

Detect conflicting writes before overwrite.

Do not use a process-wide or cross-project blocking lock.

### Step 16 — Implement addressed skill communication

Use `skill_uri` as the target identity in formal role-to-skill communication.

Use source and target skill URIs in skill-to-skill communication.

Use the common skill communication envelope for structured addressed messages.

A caller **MAY** set `requested_target_version` to one exact semantic version. Use no version range because SA-06 defines no range syntax.

The resolver **MUST** record `resolved_target_version` before target execution.

When `requested_target_version` exists, the resolved version **MUST** equal it.

Validate the target capability ID, expected outcome IDs, payload schema, applicability, configuration, and lifecycle readiness before execution.

### Step 17 — Obtain Language & Meaning conformance evidence

Run the LMC-04 review process for project-authored human-readable skill content.

Use the project-designated checker or designated review authority.

Retain the machine-readable Language & Meaning conformance record and supporting evidence.

Resolve blocking language or meaning findings before broader release testing.

### Step 18 — Test operational paths

For every skill, test clean installation, a representative applicable invocation, schema validation, upgrade, Codex compatibility, Claude Code compatibility, Skill API routing, and addressed role-to-skill dispatch.

For a configurable skill, test absent configuration, valid configuration, invalid configuration, update, and reset when supported.

For a stateful skill, test initialization, deferred initialization, READY operation, staleness, reinitialization, BLOCKED recovery, project isolation, and concurrent operations.

For a stateless skill, verify that no initialization or reinitialization path exists.

### Step 19 — Classify semantic version impact

Compare the candidate release with the previous public contract.

Include Skill API applicability, capabilities, outcomes, schemas, communication contracts, host behavior, configuration, and lifecycle semantics in the comparison.

Select the next `MAJOR.MINOR.PATCH` version under SA-05.

Changing `skill_uri` creates a new identity and **MUST NOT** be represented only as a version increment.

### Step 20 — Update the changelog

Update root `CHANGELOG.md` before release.

Create one entry for the candidate semantic version and release date.

Record every notable change.

State compatibility impact and required migration or operator action when applicable.

### Step 21 — Package and release

Build a standalone archive with one top-level skill directory.

Include required schema dependencies for self-contained validation.

Install the archive into clean Codex and Claude Code test environments.

Run every applicable conformance gate.

Release only after every mandatory gate passes.

## 3. Required conformance gates

### Gate G1 — Terminology

Verify these conditions.

- Common terms match SA-01.
- Domain terms have stable definitions.
- No domain term redefines a common term.
- Canonical identity uses **skill URI** terminology.

Any meaning-changing terminology conflict blocks release.

### Gate G2 — Language & Meaning conformance evidence

Verify these conditions.

- A machine-readable Language & Meaning conformance record exists.
- The record validates against the Part I conformance schema.
- The record identifies the project-designated checker or review authority.
- The record contains retained evidence locations.
- Applicable project-authored prose was reviewed under the authorized ASD-STE100 Issue 9 resources.
- BCP 14 semantics were reviewed where normative prose is present.
- Project terminology and meaning-control results pass.
- Protected/imported content preservation passes when applicable.

A failing Language & Meaning result blocks release.

### Gate G3 — Package conformance

Verify these conditions.

- The archive has one top-level skill directory.
- The top-level directory name equals the `SKILL.md` frontmatter `name` and the Skill API `name`.
- Root `SKILL.md` exists.
- Root `skill-api.json` exists.
- Root `CHANGELOG.md` exists.
- `references/operations.md` exists.
- Frontmatter contains only `name` and `description`.
- Every routed resource exists.
- Every packaged resource supports a justified purpose.

### Gate G4 — Machine-readable schema conformance

Verify these conditions.

- Every machine-readable artifact has an identified schema.
- Every artifact validates before use.
- Shared concepts reuse common schema definitions when compatible.
- Schema identifiers are valid absolute URIs.
- Every ADS-owned or skill-owned schema has a semantic version.
- Every vendored common schema preserves canonical identity and content.
- Every transitive internal schema reference resolves from the packaged schema bundle.
- `python scripts/validate_ads_bundle.py` or an equivalent deterministic resolver completes without unresolved ADS-owned references.
- Conformance-record adversarial tests reject logically impossible PASS records.
- Semantic conformance-record validation rejects a `skill_name` that does not match the local name in `skill_uri`.
- When Skill API evidence is available, semantic conformance-record validation matches identity, version, and classifications to that Skill API.

Any uncovered or unresolved machine-readable contract blocks release.

### Gate G5 — Routing conformance

Test representative prompts that are expected to activate the skill.

Test nearby prompts that are expected not to activate the skill.

Verify that `SKILL.md` description and Skill API applicability agree.

Verify that any matching `when_not_to_use` exclusion disables activation.

Test explicit invocation where the host supports it.

### Gate G6 — Installer and operations-guide conformance

For Codex and Claude Code, verify:

- clean installation;
- repeated installation;
- upgrade from a previous version;
- discovery and actual executed identity;
- preservation of unrelated files;
- correct resource location type;
- installed `skill_uri` and semantic version are reported;
- `CHANGELOG.md` is reachable;
- applicable changelog information is served.

Verify that agents and human operators can execute every applicable operations-guide procedure.

### Gate G7 — Configuration conformance

This gate applies only to a configurable skill.

Verify:

- documented project-local sources and scope;
- no persistent user-global or cross-project configuration;
- deterministic precedence;
- schema validation;
- developer-selectable commit or ignore policy;
- valid absent-configuration behavior when configuration is optional;
- valid update and reset behavior when supported;
- executable agent and human procedures.

For a non-configurable skill, record `N/A`.

### Gate G8 — Stateful lifecycle conformance

This gate applies only to a stateful skill.

Verify:

- installed and UNINITIALIZED state;
- explicit and deferred initialization;
- repeated initialization;
- READY governed operation;
- project B remains non-READY after only project A is initialized;
- staleness and reinitialization;
- BLOCKED recovery;
- migration after a relevant upgrade;
- readiness evidence matches the active project and `skill_uri`;
- executable agent and human lifecycle procedures.

For a stateless skill, record `N/A` and verify that initialization and reinitialization do not exist.

### Gate G9 — Project-local persistence, isolation, and concurrency

This gate applies when the skill persists project-derived data.

Verify:

- every persistent project-derived artifact is inside the active project;
- a global installation remains read-only during project operation;
- no shared registry stores project configuration, state, readiness, bindings, caches, indexes, logs, or runtime metadata;
- project A configuration is not used in project B;
- project A readiness cannot make project B READY;
- configuration can be committed or ignored independently of generated state;
- different project scopes proceed independently.

For a stateful skill, also verify concurrent-write safety and absence of cross-project or process-wide blocking locks.

When the skill persists no project-derived data, record `N/A`.

### Gate G10 — Independence conformance

Verify:

- the skill installs alone in Codex;
- the skill installs alone in Claude Code;
- the skill operates and tests alone in both hosts;
- a stateful skill initializes alone;
- one skill can upgrade without forcing an unrelated skill upgrade;
- shared schema reuse does not create domain-logic coupling;
- addressed communication uses explicit skill URIs.

### Gate G11 — Capability justification

Verify every public capability and supporting capability.

Each item **MUST** trace to a domain, lifecycle, validation, interoperability, operator, or conformance need.

Every public implemented capability **MUST** appear in the Skill API.

Every Skill API capability **MUST** exist in the implementation.

An unjustified or falsely advertised capability blocks release.

### Gate G12 — Release evidence

The release record **MUST** identify:

- skill name;
- canonical `skill_uri`;
- skill semantic version;
- previous released version when one exists;
- version impact;
- lifecycle classification;
- configuration classification;
- whether the skill persists project-derived data;
- tested hosts;
- schema-bundle metaschema, offline-resolution, and conformance-self-test results;
- Skill API schema, identity, applicability, capability, outcome, and communication results;
- changelog results;
- applicable gate results;
- documented `SHOULD` deviations.

A conditional gate can be `N/A` only when its stated applicability condition is false.

### Gate G13 — Required-host compatibility

Verify the same canonical `skill_uri` and package version in Codex and Claude Code.

Verify in both hosts:

- project discovery;
- global discovery when provided;
- activation;
- required reference and script loading;
- Skill API availability;
- project-local configuration when configurable;
- project-local lifecycle behavior when stateful;
- diagnostics and recovery;
- changelog access and serving;
- actual identity resolution when same-name skills are visible;
- required-host reserved-name validation;
- the intended `skill_uri` and version are the package actually executed.

Any mandatory behavior that passes in only one host blocks release.

### Gate G14 — Semantic versioning conformance

Verify:

- the release version conforms to Semantic Versioning 2.0.0;
- the public contract is identified;
- the selected increment matches compatibility impact;
- deprecation increments at least MINOR;
- backward-incompatible public-contract change increments MAJOR;
- released versions are immutable;
- schema versions follow SA-03 and SA-05;
- Skill API changes are included in version-impact analysis;
- a pre-release is not presented as stable.

### Gate G15 — Changelog conformance

Verify:

- root `CHANGELOG.md` exists;
- the candidate release entry has a semantic version and absolute date;
- every notable change has a curated record;
- compatibility and required operator action are stated when applicable;
- Codex and Claude Code projections preserve changelog access;
- clean installation serves the installed version and current entry;
- upgrade serves the required entry range.

A missing, stale, or unserved changelog blocks release.

### Gate G16 — Skill API, identity, and communication conformance

Verify:

- `skill-api.json` validates against the common Skill API schema;
- `skill_uri` uses `skill:<publisher>.<skill-name>` and remains consistent across package artifacts;
- the publisher namespace is present and stable;
- publisher ownership is not an external validation dependency;
- at least one `when_to_use` scenario exists;
- applicability exclusions override matching enablers;
- capability IDs and outcome IDs are unique and valid;
- every capability links to existing outcomes;
- outcome acceptance criteria are inspectable;
- structured role-to-skill communication uses `target_skill_uri`;
- structured skill-to-skill communication uses source and target skill URIs;
- message capability and outcome references exist in the target Skill API;
- when the target capability declares `request_schema_uri`, message `payload_schema_uri` equals that URI;
- message payload validates against the target capability's declared request schema;
- an addressed request cannot bypass target applicability or lifecycle rules;
- `requested_target_version`, when present, contains one exact semantic version;
- `resolved_target_version` is present before target execution;
- an exact requested target version equals the resolved target version;
- explicit host invocation cannot override an applicability exclusion;
- same-name or same-URI version collisions are resolved before PASS.

Any identity, Skill API, or addressed-communication mismatch blocks release.

## 4. Language & Meaning review integration

Use LMC-04 for the common language and meaning review.

This Skill Architecture guide adds only these skill-domain checks:

1. verify skill-architecture terms against SA-01;
2. verify lifecycle and configuration classifications;
3. verify skill URI terminology and identity consistency;
4. verify applicability, implemented capability, and desired outcome semantics under SA-06;
5. verify agent and human operational procedures against the skill contract;
6. retain the Part I Language & Meaning conformance record as G2 evidence.

This section does not reproduce the ASD-STE100 Issue 9 rules or the common Part I review procedure.

## 5. Suggested automated checks

A linter **SHOULD** automate rules that can be checked reliably.

Suitable checks include:

- frontmatter whitelist and schema validation;
- reserved host skill names;
- missing `skill-api.json`, `CHANGELOG.md`, or `references/operations.md`;
- invalid or inconsistent `skill_uri`;
- missing schema coverage;
- unresolved packaged schema references;
- invalid semantic versions;
- invalid Skill API capability or outcome references;
- initialization language in a stateless skill;
- project-derived paths outside the active project;
- persistent configuration in global locations;
- global installation directories mutated during project operation;
- same-name identity collisions;
- host-only required behavior;
- blocking-lock patterns where static analysis is practical;
- resources without capability justification.

A linter **MUST NOT** silently rewrite normative meaning.

Human review remains required for ambiguity, domain correctness, applicability, and concurrency semantics.

## 6. Review record template

```text
Skill: <name>
Skill URI: <absolute-uri>
Version: <semantic-version>
Canonical package: <source>
ADS suite: 5.0.0-rc.1
Lifecycle classification: stateful | stateless
Configuration classification: configurable | non-configurable
Persists project data: true | false

Language & Meaning profile: LMC 5.0.0-rc.1
Language review method: designated-checker | designated-review | combined
Language review authority: <authority>
Language review evidence: <evidence location(s)>
Language & Meaning result: PASS | FAIL

Schema metaschema validation: PASS | FAIL
Schema offline resolution: PASS | FAIL
Conformance adversarial self-tests: PASS | FAIL
Skill API schema validation: PASS | FAIL
Skill API identity consistency: PASS | FAIL
Skill API applicability consistency: PASS | FAIL
Skill API capability implementation: PASS | FAIL
Skill API outcome linkage: PASS | FAIL
Communication addressing: PASS | FAIL
Codex compatibility: PASS | FAIL
Claude Code compatibility: PASS | FAIL
Project-local persistence: PASS | FAIL | N/A
Changelog candidate entry: PASS | FAIL
Changelog serving Codex: PASS | FAIL
Changelog serving Claude Code: PASS | FAIL

G1 Terminology: PASS | FAIL
G2 Language & Meaning: PASS | FAIL
G3 Package: PASS | FAIL
G4 Machine-readable schemas: PASS | FAIL
G5 Routing: PASS | FAIL
G6 Installer and operations guide: PASS | FAIL
G7 Configuration: PASS | FAIL | N/A
G8 Stateful lifecycle: PASS | FAIL | N/A
G9 Project-local persistence and concurrency: PASS | FAIL | N/A
G10 Independence: PASS | FAIL
G11 Capability justification: PASS | FAIL
G12 Release evidence: PASS | FAIL
G13 Codex and Claude Code compatibility: PASS | FAIL
G14 Semantic versioning: PASS | FAIL
G15 Changelog: PASS | FAIL
G16 Skill API and communication: PASS | FAIL

SHOULD deviations:
- <rule>: <reason and effect>

Blocking findings:
- <rule>: <condition and recovery action>

Result: PASS | PASS WITH SHOULD DEVIATIONS | FAIL
```

A machine-readable version of this record **MUST** validate against the common conformance-record schema.

The schema **MUST** reject `N/A` for unconditional gates.

The schema **MUST** reject a passing result when any applicable mandatory gate fails.

## 7. Definition of done for a new skill

A new skill is ready for release only when these conditions hold.

- The domain boundary is explicit.
- The canonical `skill_uri` is stable and valid.
- `skill-api.json` is complete and consistent.
- Every public capability is implemented and justified.
- Lifecycle and configuration classifications are declared.
- The canonical package is complete.
- The activation surface is compact.
- The universal operations guide is executable by agents and humans.
- Common terminology conforms to SA-01.
- Human-readable content has passing Language & Meaning evidence under LMC-04.
- Every machine-readable artifact is schema-covered and resolvable.
- Configuration behavior conforms when supported.
- Stateful lifecycle and concurrency conform when applicable.
- Stateless skills contain no initialization or reinitialization lifecycle.
- Codex and Claude Code projections are verified by actual `skill_uri` and version.
- Persistent project-derived data stays inside the active project.
- Addressed skill communication uses canonical skill URIs.
- Release versioning conforms to SA-05.
- Root `CHANGELOG.md` contains the candidate entry.
- Installation serves the applicable changelog in both hosts.
- Every applicable mandatory gate passes.

## 8. Existing-skill alignment procedure

Every existing project skill **MUST** align to the current suite before its next release.

Apply this sequence.

1. Assign a canonical `skill_uri`.
2. Create `skill-api.json`.
3. Classify the skill as stateful or stateless.
4. Classify it as configurable or non-configurable.
5. Inventory and justify capabilities.
6. Inventory machine-readable artifacts and schemas.
7. Add the universal operations guide.
8. Align terminology and Language & Meaning.
9. Align package and installation behavior.
10. Align configuration procedures when applicable.
11. Align lifecycle, isolation, and concurrency when applicable.
12. Remove lifecycle behavior from stateless skills.
13. Implement and verify Codex and Claude Code adapters.
14. Add host identity-collision checks.
15. Align addressed communication with SA-06.
16. Define the public contract and version impact.
17. Align `CHANGELOG.md` and changelog serving.
18. Run every applicable conformance gate.

Framework alignment **MUST NOT** merge independent skills.

## 9. Guide bootstrap and Language & Meaning conformance

This guide **MUST** conform to the Language & Meaning Core.

A future revision **MUST** follow the bootstrap process in ADS-00.

A release claim **MUST** retain designated checker or review evidence under LMC-04.

The guide defines only skill-specific extensions and **MUST NOT** reconstruct a parallel controlled-language standard.

## 10. Related documents

- Suite governance: [../00_governance_and_bootstrap.md](../00_governance_and_bootstrap.md)
- Skill Architecture dictionary: [SA-01_skill_architecture_dictionary.md](SA-01_skill_architecture_dictionary.md)
- Architecture and lifecycle: [SA-02_skill_architecture_framework.md](SA-02_skill_architecture_framework.md)
- Language & Meaning: [../language-core/README.md](../language-core/README.md)
- Standards basis: [../language-core/LMC-01_language_standards_profile.md](../language-core/LMC-01_language_standards_profile.md)
- Schema standard: [SA-03_machine_readable_contracts.md](SA-03_machine_readable_contracts.md)
- Required-host compatibility: [SA-04_required_host_compatibility.md](SA-04_required_host_compatibility.md)
- Versioning policy: [SA-05_versioning_and_evolution.md](SA-05_versioning_and_evolution.md)
- Skill API and communication: [SA-06_skill_api_and_communication.md](SA-06_skill_api_and_communication.md)
