# Skill Architecture — Versioning and Evolution

**Document ID:** SA-05  
**Status:** Normative versioning and release-evolution baseline release candidate  
**Suite version:** 5.0.0-rc.1  
**Date:** 2026-09-13  
**Parent:** ADS-00  
**Language baseline:** LMC  
**Terminology baseline:** SA-01  
**Conformance baseline:** SA-07  
**Identity baseline:** SA-06

## 1. Purpose

This standard defines semantic versioning and release changelog requirements for AI DevMode skills, the ADS suite, and ADS-owned schemas.

It converts compatibility impact into a deterministic release-version decision.

## 2. Normative basis

This standard adopts Semantic Versioning 2.0.0 as the version syntax and increment model.

Normative keyword semantics are inherited from the Language & Meaning Core.

When this standard and SemVer differ in skill-architecture terminology, SA-01 controls project terminology and this document controls the Skill Architecture adoption of SemVer.

## 3. Release units

These release units **MUST** use Semantic Versioning:

1. each released skill canonical package;
2. the released ADS suite baseline;
3. each ADS-owned schema;
4. each skill-owned schema that is independently identified and evolved.

A host projection that contains no independent contract **MUST** use the canonical skill package version.

A release unit **MAY** have an independent version stream when its contract evolves independently.

## 4. Version syntax

A released version without a pre-release identifier **MUST** use `MAJOR.MINOR.PATCH`.

Each component **MUST** be a non-negative integer without leading zeroes.

A pre-release version **MAY** append a hyphen and valid SemVer pre-release identifiers.

Build metadata **MAY** append a plus sign and valid SemVer build identifiers.

Build metadata **MUST NOT** change compatibility interpretation or version precedence.

## 5. Public contract

A versioned skill **MUST** define the public contract used for version-impact analysis.

The public contract includes externally relied-on elements such as:

- canonical `skill_uri` lineage identity;
- `skill-api.json` applicability, capability, and outcome contracts;

- domain inputs, outputs, and required behavior;
- activation and routing behavior when clients rely on it;
- configuration keys, defaults, scopes, and precedence;
- stateful lifecycle semantics and supported migration behavior;
- persisted and exchanged machine-readable schemas;
- commands or operator procedures that are documented as stable interfaces;
- required Codex and Claude Code behavior under SA-04;
- documented error or diagnostic contracts when consumers rely on them.

Internal refactoring, private helper structure, and implementation detail are outside the public contract when no conforming consumer relies on them.

A release review **MUST** evaluate compatibility against the previous supported release, not only against author intent.

## 6. MAJOR increment

A release **MUST** increment MAJOR when it introduces a backward-incompatible public-contract change.

Examples include:

- removing or incompatibly changing required domain behavior;
- removing a supported input, output, configuration key, or command without a compatible replacement;
- changing lifecycle classification between stateful and stateless;
- changing persisted data semantics so existing supported data cannot be consumed or migrated transparently;
- changing a schema so previously conforming artifacts become invalid or change meaning without compatible migration;
- dropping required Codex or Claude Code behavior;
- changing an established operator procedure so existing automation requires changes.

A host-facing skill `name` change **MAY** remain in the same identity lineage when `skill_uri` is unchanged. A rename that changes documented invocation behavior **MUST** be classified by its public-contract impact.

Changing `skill_uri` creates a new skill identity and **MUST NOT** be represented as a version update of the previous lineage.

When MAJOR increments, MINOR and PATCH **MUST** reset to zero.

## 7. MINOR increment

A release **MUST** increment MINOR when it adds backward-compatible public functionality.

A release **MUST** increment at least MINOR when it introduces a deprecation.

Examples include:

- adding a backward-compatible Skill API capability, outcome, or applicability enabler while preserving existing behavior;
- adding an optional configuration key with a backward-compatible default;
- adding a backward-compatible machine-readable field or operation;
- adding an additional supported integration that does not alter existing required behavior.

When MINOR increments, PATCH **MUST** reset to zero.

## 8. PATCH increment

A release **MUST** increment PATCH when it contains only backward-compatible corrections that do not add required public functionality.

Examples include:

- correcting incorrect implementation while preserving the documented contract;
- fixing a Codex or Claude Code adapter without changing required behavior;
- correcting documentation, diagnostics, or Language & Meaning wording without changing normative meaning;
- correcting schema annotations or metadata without changing accepted instances or defined semantics.

## 9. Initial development and stable release

A release unit **MAY** use `0.y.z` during initial development.

A `0.y.z` release **MUST NOT** be presented as a stable public contract.

The first release intended as a stable supported contract **MUST** use version `1.0.0` or greater.

## 10. Pre-release and build metadata

A pre-release identifier **MAY** be used for alpha, beta, release-candidate, or other unstable builds.

A pre-release version **MUST NOT** be presented as satisfying the stability guarantee of the associated version without a pre-release identifier.

Build metadata **MAY** identify build provenance, commit identity, or packaging information.

Build metadata **MUST NOT** be used to distinguish incompatible public contracts.

## 11. Release immutability

A released version **MUST** be immutable.

The project **MUST NOT** replace package content, schema content, or normative ADS content while retaining the same released semantic version.

Any post-release modification **MUST** use a new version.

A vendored schema copy **MUST** continue to match the canonical content for its declared version.

## 12. Skill and schema version independence

A skill version and a schema version are independent release units unless the project explicitly binds them.

A schema MAJOR increment does not automatically require a skill MAJOR increment when the skill transparently migrates or supports the previous contract and preserves its own public contract.

A schema change that forces skill consumers or project operators to change **MUST** be included in the skill public-contract impact analysis.

Persisted artifacts **MUST** identify the applicable schema version when SA-03 requires that identity.

## 13. Configuration and state evolution

A configurable skill **MUST** classify configuration-contract changes under this standard.

A stateful skill **MUST** classify persisted-state contract changes under this standard.

When a new release cannot directly consume a previously supported project-local configuration or state artifact, the skill **MUST** provide migration or classify the change as backward incompatible.

Migration behavior **MUST** remain project-local under SA-02.

## 14. Host compatibility evolution

A repair for a changed Codex or Claude Code host convention **MAY** be PATCH when required skill behavior remains backward compatible.

A host-driven change that requires users to change the skill public contract **MUST** receive the corresponding MINOR or MAJOR increment.

Host documentation changes **MUST** be evaluated before release under SA-04.

## 15. Skill identity and Skill API evolution

The canonical `skill_uri` identifies a skill lineage and **MUST** remain stable across versions in that lineage.

Changing `skill_uri` creates a new identity and **MUST NOT** be represented only by a MAJOR, MINOR, or PATCH increment of the previous identity.

`skill-api.json` is part of the skill public contract.

Removing or incompatibly changing a public capability or desired outcome **MUST** increment MAJOR.

Narrowing applicability so a previously supported request becomes excluded **MUST** increment MAJOR.

Adding a backward-compatible capability, outcome, or applicability enabler **MUST** increment MINOR.

Correcting Skill API wording without changing applicability, capability semantics, outcome semantics, or acceptance criteria **MAY** increment PATCH.

A capability ID or outcome ID that has been published **MUST NOT** be reassigned to a different semantic meaning within the same `skill_uri` lineage.

## 16. ADS suite versioning

The ADS suite **MUST** use one suite semantic version across all normative ADS documents in a released baseline.

A change to a mandatory conformance obligation that makes previously conforming skills non-conforming **MUST** increment the suite MAJOR version.

A backward-compatible new framework capability or optional rule **SHOULD** increment MINOR.

A clarification or correction that changes no normative meaning **SHOULD** increment PATCH.

The current working suite version is `5.0.0-rc.1`. The intended stable baseline is `4.0.0` after every mandatory release gate passes.

## 17. Skill changelog contract

Every released skill canonical package **MUST** contain `CHANGELOG.md` at the package root.

The changelog **MUST** be human-readable.

The changelog **MUST** follow the Language & Meaning Core.

Each released version without a pre-release identifier **MUST** have one release entry that identifies:

1. the released semantic version;
2. the absolute release date;
3. every notable change in that release;
4. compatibility impact when the effect is not obvious from the version increment;
5. required migration, configuration, initialization, reinitialization, schema, or operator action when applicable.

Release entries **SHOULD** use consistent categories such as `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security`.

A changelog **MAY** contain an `Unreleased` section for accepted work that is not yet part of a released version.

A change record **MUST** describe an externally relevant effect. A raw commit message, ticket identifier, branch name, or implementation detail alone **MUST NOT** satisfy the change-record requirement.

Purely internal implementation changes with no externally relevant effect **MAY** be omitted unless project policy, security, or conformance reporting requires disclosure.

A MAJOR release **MUST** include migration guidance for each backward-incompatible change that can be migrated.

A release that introduces deprecation **MUST** identify the deprecated element and the supported replacement or migration path when one exists.

A configuration, state, or schema change **MUST** identify any required migration and resulting initialization or reinitialization action.

A Codex-only or Claude Code-only compatibility repair **MUST** name the affected host.

Released package content, including its changelog, remains immutable under Section 11. A later release **MAY** correct a historical changelog statement, but the current release entry **MUST** record that correction.

### 17.1 Installation serving

The packaged changelog **MUST** be served with installation in both required hosts.

For a clean installation, the installer or agent **MUST** provide:

1. the installed semantic version;
2. the changelog location;
3. the release entry for the installed version.

For an upgrade, the installer or agent **MUST** provide:

1. the previous installed version when known;
2. the target version;
3. the changelog location;
4. the release entries after the previous version through the target version;
5. any required migration or lifecycle action before dependent operation continues.

A non-interactive installer **MAY** serve the changelog through deterministic output that identifies the exact packaged path and applicable release entry range.

Merely copying `CHANGELOG.md` without identifying it to the operator **MUST NOT** satisfy the served-changelog requirement.

## 18. Release procedure

Before release, the maintainer **MUST**:

1. identify the previous released version;
2. identify the public contract;
3. enumerate externally observable changes;
4. classify each change as backward compatible or backward incompatible;
5. select the required MAJOR, MINOR, or PATCH increment;
6. classify independently versioned schemas;
7. run SA-07 conformance gates;
8. record migrations and deprecations;
9. update `CHANGELOG.md` with the candidate release entry;
10. verify installation serves the applicable changelog information in Codex and Claude Code;
11. verify `skill_uri` continuity and Skill API compatibility impact;
12. publish an immutable release.

## 19. Conformance

Semantic-version conformance is a mandatory release gate under SA-07.

A release **MUST NOT** pass when its version understates compatibility impact.

A release **MUST NOT** pass when a released version identifier is reused for modified content.

A release **MUST NOT** pass when a pre-release is represented as stable.

A release **MUST NOT** pass when `CHANGELOG.md` is missing, stale, inconsistent with the candidate semantic version, or not served by installation in either required host.

## 20. Related documents

- Governance: [../00_governance_and_bootstrap.md](../00_governance_and_bootstrap.md)
- Skill Architecture dictionary: [SA-01_skill_architecture_dictionary.md](SA-01_skill_architecture_dictionary.md)
- Architecture: [SA-02_skill_architecture_framework.md](SA-02_skill_architecture_framework.md)
- Language & Meaning: [../language-core/README.md](../language-core/README.md)
- Development and conformance: [SA-07_skill_development_and_conformance.md](SA-07_skill_development_and_conformance.md)
- Standards basis: [../language-core/LMC-01_language_standards_profile.md](../language-core/LMC-01_language_standards_profile.md)
- Schema governance: [SA-03_machine_readable_contracts.md](SA-03_machine_readable_contracts.md)
- Required-host compatibility: [SA-04_required_host_compatibility.md](SA-04_required_host_compatibility.md)
- Skill identity and communication: [SA-06_skill_api_and_communication.md](SA-06_skill_api_and_communication.md)
