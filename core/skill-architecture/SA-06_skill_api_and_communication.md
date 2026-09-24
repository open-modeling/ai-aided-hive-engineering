# Skill Architecture — Skill API and Communication

**Document ID:** SA-06  
**Status:** Normative skill identity, applicability, and communication baseline release candidate  
**Suite version:** 5.0.0-rc.1  
**Date:** 2026-09-13  
**Parent:** ADS-00  
**Language baseline:** LMC  
**Terminology baseline:** SA-01  
**Architecture baseline:** SA-02  
**Schema baseline:** SA-03

## 1. Purpose

This standard defines the canonical identity and public machine-readable interface for every AI DevMode skill.

It also defines how roles and skills address a skill during role-to-skill and skill-to-skill communication.

The Skill API separates three questions that serve different purposes:

1. **When to use** defines applicability and enables routing.
2. **Where it helps** identifies an implemented capability.
3. **What to expect** identifies a desired observable outcome.

A skill **MUST NOT** use a capability statement or outcome statement as a substitute for an applicability condition.

## 2. Canonical skill identity

Every skill **MUST** have one canonical `skill_uri`.

The canonical form is:

```text
skill:<publisher>.<skill-name>
```

Examples:

```text
skill:openai.document-governor
skill:acme.document-governor
```

The `publisher` segment is a short namespace label that distinguishes same-name skills from different publishers. The author or publisher chooses the label.

The publisher namespace **MUST** contain 1-64 lowercase ASCII letters, digits, or hyphens.

The publisher namespace **MUST** start and end with a letter or digit.

The publisher namespace **MUST NOT** contain consecutive hyphens or `.`.

The project **MUST NOT** treat the publisher namespace as proof of legal identity, DNS ownership, organization registration, registry membership, or global uniqueness.

ADS **MUST NOT** require external publisher validation.

The `skill-name` segment **MUST** equal the canonical package directory name, the `SKILL.md` frontmatter `name`, and the Skill API `name`.

The `skill-name` segment **MUST** satisfy the common required-host skill-name schema.

Canonical `skill_uri` serialization **MUST** use lowercase ASCII. The URI **MUST NOT** use percent encoding, query data, fragments, user information, or authority syntax. Exact string equality determines skill identity.

`skill_uri` **MUST** be an absolute URI under RFC 3986 using the ADS-internal `skill` URI scheme. ADS uses RFC 7595 as design guidance for this private interoperability contract.

The ADS `skill:` scheme is limited to systems that explicitly adopt ADS. ADS does not claim IANA registration for the scheme. An implementation **MUST NOT** assume that a `skill:` URI is publicly dereferenceable or interoperable outside an ADS-aware system.

A canonical `skill_uri` **MUST NOT** contain secrets, user identifiers, project identifiers, configuration values, readiness evidence, or other project-derived data.

The canonical `skill_uri` **MUST** remain stable across skill versions, Codex and Claude Code projections, installation scopes, project scopes, configuration instances, and lifecycle transitions.

A skill version **MUST NOT** be encoded into `skill_uri`. A host-native skill ID, filesystem path, package name, or display name **MUST NOT** replace `skill_uri` as the cross-host identity.

Once a `skill_uri` identifies a released skill lineage, the project **MUST NOT** reassign it to a different skill lineage. Changing the publisher namespace or local skill name creates a new skill identity. It is not a version update of the prior identity.

## 3. Skill API artifact

Every canonical skill package **MUST** contain `skill-api.json` at the package root.

`skill-api.json` **MUST** conform to the common Skill API schema in SA-03.

The Skill API **MUST** identify:

1. the canonical `skill_uri`;
2. the publisher namespace label;
3. the host-facing skill `name`;
4. the skill semantic version;
5. lifecycle classification;
6. configuration classification;
7. the operations guide path;
8. applicability;
9. implemented capabilities;
10. desired outcomes;
11. the common communication-envelope schema.

The `skill_uri`, publisher, `name`, version, and classifications **MUST** agree with the canonical package and release record.

Human-readable string values in `skill-api.json` **MUST** follow the Language & Meaning Core.

## 4. Applicability contract — when to use

`applicability.when_to_use` defines the routing enablers for the skill.

Each `when_to_use` entry **MUST** describe one qualifying usage scenario.

At least one `when_to_use` entry **MUST** match before the skill is considered applicable.

`applicability.when_not_to_use` **MAY** define exclusion scenarios.

If any `when_not_to_use` entry matches, the skill **MUST NOT** activate for that request even when a `when_to_use` entry also matches.

Explicit invocation by host-facing name or canonical `skill_uri` **MUST NOT** override an applicability exclusion or required precondition. Explicit invocation is a routing request, not authority to widen the Skill API contract.

An applicability entry **MUST** describe conditions on the request, project, or required task. It **MUST NOT** merely restate the skill name.

An applicability entry **MUST NOT** promise an outcome that the skill does not implement.

The `SKILL.md` description **MUST** summarize the same applicability boundary without contradicting `skill-api.json`.

## 5. Capability contract — where it helps

Each entry in `capabilities` identifies one implemented capability.

A capability **MUST** have a stable local capability ID within the skill lineage.

`where_it_helps` **MUST** identify the task area or problem where that implemented capability is useful.

`does` **MUST** state what the capability actually performs.

Every public implemented capability **MUST** appear in `skill-api.json`.

Every declared capability **MUST** exist in the implementation.

Every declared capability **MUST** have a capability justification under SA-02.

A capability **MUST** identify at least one desired outcome by outcome ID.

If a capability consumes or emits a structured payload, it **MUST** identify the applicable request or response schema URI when that schema is not already fixed by a higher-level contract.

## 6. Outcome contract — what to expect

Each entry in `outcomes` identifies one desired observable outcome.

An outcome **MUST** have a stable local outcome ID within the skill lineage.

`what_to_expect` **MUST** describe the result that a successful capability invocation is intended to produce.

Each outcome **MUST** include at least one acceptance criterion.

An acceptance criterion **MUST** be directly inspectable or objectively testable.

An outcome **MUST NOT** be written as an activation condition.

A capability **MUST NOT** claim an outcome that the implementation cannot produce under its documented preconditions.

## 7. Skill API consistency

The following representations **MUST** remain consistent:

- `SKILL.md` routing description;
- `skill-api.json` applicability;
- implemented capabilities;
- documented outcomes;
- operations guide procedures;
- machine-readable request and response schemas;
- release and changelog records.

When two representations conflict, the skill **MUST** be treated as non-conforming until the conflict is resolved.

A release **MUST NOT** pass when `skill-api.json` advertises a capability that is absent, hides a public capability that exists, or contradicts the activation boundary.

## 8. Role-to-skill communication

An addressed role-to-skill request **MUST** identify the target with `target_skill_uri`.

A display name **MAY** accompany the URI. The display name **MUST NOT** replace the URI.

A structured role-to-skill request **MUST** conform to the common skill communication envelope in SA-03.

The request **MUST** identify:

1. the source role;
2. the target `skill_uri`;
3. the requested capability ID;
4. the expected outcome IDs;
5. the request intent;
6. the payload schema URI;
7. the payload.

The caller **MAY** set `requested_target_version` to one exact semantic version. SA-06 does not define version-range syntax.

Before target execution, the resolver **MUST** set `resolved_target_version` to the exact version that will execute.

When `requested_target_version` exists, `resolved_target_version` **MUST** equal it.

The target skill **MUST** validate its own applicability before execution. A role request **MUST NOT** bypass `when_to_use` or `when_not_to_use` rules.

If the requested capability declares `request_schema_uri`, `payload_schema_uri` **MUST** equal that URI.

The target **MUST** validate the payload against the requested capability's declared request schema before execution. A caller-selected alternate schema **MUST NOT** substitute for the target contract.

## 9. Skill-to-skill communication

An addressed skill-to-skill request **MUST** identify both source and target skills by canonical skill URI.

A structured skill-to-skill request **MUST** conform to the common skill communication envelope.

The request **MUST** identify the source skill version. The caller **MAY** set `requested_target_version` to one exact target semantic version.

Before target execution, the resolver **MUST** set `resolved_target_version`.

When an exact requested target version exists, the resolved target version **MUST** equal it.

The target capability ID **MUST** exist in the resolved target Skill API.

Each expected outcome ID **MUST** exist in the resolved target Skill API.

Each expected outcome ID **MUST** be linked to the requested capability.

If the target capability declares `request_schema_uri`, `payload_schema_uri` **MUST** equal that URI.

The payload **MUST** validate against the target capability's declared request schema before the target skill relies on it. A caller-selected alternate schema **MUST NOT** substitute for the target contract.

Skill-to-skill communication **MUST NOT** create shared cross-project state or shared project configuration.

A called skill **MUST** apply its own lifecycle, configuration, project-isolation, and authorization requirements.

## 10. Human-readable handoffs

A formal human-readable handoff that assigns work to a skill **MUST** identify the target `skill_uri` and skill version.

When a handoff requests a public capability, it **SHOULD** identify the capability ID and expected outcome IDs.

A handoff **MUST NOT** use only a display name when two visible skills can share that name.

The handoff language **MUST** follow the Language & Meaning Core.

## 11. Identity and host name collisions

The host-facing `name` is an alias for discovery. It is not the canonical identity.

Before installation or activation verification, the host adapter **MUST** inspect visible same-name skills when the host exposes more than one discovery scope.

If two visible packages have the same `name` and different `skill_uri` values, the adapter **MUST** report an identity collision.

If two visible packages have the same `skill_uri` and different versions, the adapter **MUST** verify which version the host actually resolves.

The adapter **MUST NOT** report compatibility PASS until the intended `skill_uri` and version are the package that the host will execute.

An unresolved identity or version collision **MUST** block release verification or installation completion.

## 12. Versioning impact

The Skill API is part of the skill public contract under SA-05.

Removing or incompatibly changing a capability or outcome **MUST** increment MAJOR.

Narrowing applicability so that a previously supported request becomes excluded **MUST** increment MAJOR.

Adding a backward-compatible capability, outcome, or qualifying applicability scenario **MUST** increment MINOR.

Correcting wording without changing applicability, capability semantics, or outcome semantics **MAY** increment PATCH.

Changing `skill_uri` creates a new identity and **MUST NOT** be represented only as a version increment.

## 13. Conformance

Skill API and communication conformance is a mandatory release gate under SA-07.

A release **MUST NOT** pass when:

- `skill-api.json` is missing or schema-invalid;
- `skill_uri` is missing, does not use `skill:<publisher>.<skill-name>`, is unstable, or is inconsistent;
- the Skill API and `SKILL.md` disagree on applicability;
- a declared capability is not implemented or justified;
- an implemented public capability is not declared;
- an outcome is not linked to a capability;
- role-to-skill or skill-to-skill addressing substitutes a display name for `skill_uri`;
- a structured communication payload is not validated against the target capability's declared request schema when one exists;
- a conformance record identifies a `skill_name` that does not match its `skill_uri`;
- a resolved addressed request does not record `resolved_target_version`;
- an exact `requested_target_version` differs from `resolved_target_version`;
- an unresolved same-name or same-URI version collision can select the wrong package.

## 14. Related documents

- Governance: [../00_governance_and_bootstrap.md](../00_governance_and_bootstrap.md)
- Skill Architecture dictionary: [SA-01_skill_architecture_dictionary.md](SA-01_skill_architecture_dictionary.md)
- Common framework: [SA-02_skill_architecture_framework.md](SA-02_skill_architecture_framework.md)
- Language & Meaning: [../language-core/README.md](../language-core/README.md)
- Development and conformance: [SA-07_skill_development_and_conformance.md](SA-07_skill_development_and_conformance.md)
- Standards basis: [../language-core/LMC-01_language_standards_profile.md](../language-core/LMC-01_language_standards_profile.md)
- Schema governance: [SA-03_machine_readable_contracts.md](SA-03_machine_readable_contracts.md)
- Required-host compatibility: [SA-04_required_host_compatibility.md](SA-04_required_host_compatibility.md)
- Versioning and evolution: [SA-05_versioning_and_evolution.md](SA-05_versioning_and_evolution.md)
