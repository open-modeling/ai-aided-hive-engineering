# Skill Architecture — Required-Host Compatibility

**Document ID:** SA-04  
**Status:** Normative required-host compatibility baseline release candidate  
**Suite version:** 5.0.0-rc.1  
**Date:** 2026-09-13  
**Parent:** ADS-00  
**Language baseline:** LMC  
**Terminology baseline:** SA-01  
**Architecture baseline:** SA-02  
**Versioning baseline:** SA-05  
**Identity baseline:** SA-06

## 1. Purpose

This standard defines mandatory compatibility for AI DevMode skills in Codex and Claude Code.

Every released skill **MUST** provide the same required domain behavior from one canonical package version in both required hosts.

Installation scope affects discovery only. Project-derived persistence remains project-local under SA-02.

## 2. Required hosts

The required hosts are:

1. **Codex**;
2. **Claude Code**.

A release **MUST NOT** claim ADS conformance when required behavior fails in either host.

Compatibility with other Agent Skills hosts **MAY** be provided. Such compatibility does not replace either required host unless project policy changes the required-host set.

## 3. Canonical package contract

The canonical package **MUST** be host-neutral for required behavior.

The canonical package **MUST** use `SKILL.md` as its host activation entry point.

Canonical YAML frontmatter **MUST** contain only `name` and `description`.

The canonical package directory name **MUST** equal the frontmatter `name` and the Skill API `name`.

The package **MUST** contain the same `skill_uri` and semantic version in `skill-api.json` for both host projections.

The canonical `skill_uri` **MUST** use `skill:<publisher>.<skill-name>`. The publisher namespace is a readable discriminator. Required-host verification **MUST NOT** depend on external publisher validation.

The canonical package **MUST NOT** require a host-only frontmatter field, command alias, subagent feature, context-injection mechanism, or tool-grant extension for required domain behavior.

A host-specific extension **MAY** improve usability when all of these conditions hold:

1. the extension is optional;
2. the other required host retains equivalent required behavior;
3. the extension does not change the Skill API public contract;
4. release tests cover both host paths.

## 4. Host projection contract

A host projection is a discovery representation of the canonical package.

Each projection **MUST** remain traceable to the same canonical `skill_uri` and semantic version.

A projection **MUST NOT** contain divergent domain instructions that change required behavior.

When reliable filesystem links are supported, an installer **SHOULD** use links to preserve one maintained source.

A versioned copy **MAY** be used when the host or distribution model requires a copy.

The installer **MUST** verify the identity and version that the host will actually execute after projection.

## 5. Codex compatibility

### 5.1 Project discovery

A Codex project projection **MUST** use the current verified Codex repository skill discovery convention.

For the SA host profile for suite 5.0.0-rc.1, verified on 2026-09-09, Codex scans `.agents/skills` from the current working directory through the repository root.

### 5.2 Global discovery

A Codex global installation **MUST** use a current verified Codex user, admin, or managed skill discovery location.

For the SA host profile for suite 5.0.0-rc.1, verified on 2026-09-09, Codex documents `$HOME/.agents/skills` for user skills and `/etc/codex/skills` for admin skills.

The global package **MUST** remain read-only during project operation.

### 5.3 Same-name behavior

Codex can expose more than one visible skill with the same host-facing `name`.

The installer and verifier **MUST** inspect visible same-name candidates across applicable Codex discovery scopes.

A same-name candidate with a different `skill_uri` **MUST** be reported as an identity collision.

A same-URI candidate with a different semantic version **MUST** be reported as a version collision until the intended executed version is verified.

### 5.4 Verification

Codex compatibility **MUST** verify:

- discovery;
- representative automatic activation;
- explicit invocation when the host surface supports it;
- `skill_uri` and version of the executed package;
- `skill-api.json` loading and validation;
- reference and script loading;
- offline resolution of packaged schemas;
- project-local configuration when configurable;
- project-local initialization, readiness, and reinitialization when stateful;
- role-to-skill and skill-to-skill addressing when used;
- diagnostics and recovery behavior;
- changelog access and installation serving.

## 6. Claude Code compatibility

### 6.1 Project discovery

A Claude Code project projection **MUST** use the current verified Claude Code project skill discovery convention.

For the SA host profile for suite 5.0.0-rc.1, verified on 2026-09-09, the standard project path is `.claude/skills/<skill-name>/SKILL.md`.

### 6.2 Global discovery

A Claude Code global installation **MUST** use the current verified Claude Code personal or managed skill discovery location.

For the SA host profile for suite 5.0.0-rc.1, verified on 2026-09-09, the standard personal path is `~/.claude/skills/<skill-name>/SKILL.md`.

The global package **MUST** remain read-only during project operation.

### 6.3 Reserved names

A skill `name` **MUST NOT** use a host-reserved name for a required host.

For the SA host profile for suite 5.0.0-rc.1, verified on 2026-09-09, Claude Code reserves the skill folder name `synced` in any capitalization for skills synchronized from claude.ai.

The common `skillName` schema **MUST** reject `synced` for the SA host profile for suite 5.0.0-rc.1.

A future host-reserved name change **MUST** be incorporated into compatibility validation before release.

### 6.4 Same-name resolution

Claude Code can load same-name skills or commands from enterprise, personal, project, nested-project, added-directory, plugin, synced, bundled, and legacy command sources.

For the SA host profile for suite 5.0.0-rc.1, verified on 2026-09-09, enterprise takes precedence over personal, and personal takes precedence over project for `/name`. A project-root skill and a nested skill can both remain visible. Plugin skills use a plugin-qualified command name. A local skill takes precedence over a same-name synced skill.

Before compatibility PASS, the verifier **MUST** enumerate every visible same-name source that can affect the tested automatic or explicit invocation path.

When a visible candidate is ADS-aware, the verifier **MUST** identify its `skill_uri` and semantic version. When a visible candidate is not ADS-aware, the verifier **MUST** record its source and host-visible identity.

The verifier **MUST** identify the actual package or command that the tested invocation resolves to.

A candidate that can intercept the tested invocation with a different `skill_uri`, an unintended version, or an unknown ADS identity **MUST** block compatibility PASS until the collision is resolved.

The verifier **MUST NOT** assume that a project-local projection overrides another same-name source.

### 6.5 Verification

Claude Code compatibility **MUST** verify:

- discovery;
- representative automatic activation;
- direct `/skill-name` invocation when applicable;
- `skill_uri` and version of the executed package;
- `skill-api.json` loading and validation;
- reference and script loading;
- offline resolution of packaged schemas;
- project-local configuration when configurable;
- project-local initialization, readiness, and reinitialization when stateful;
- role-to-skill and skill-to-skill addressing when used;
- diagnostics and recovery behavior;
- changelog access and installation serving.

## 7. Identity and collision verification

The host-facing `name` **MUST** be treated as a discovery alias, not canonical identity.

Before installation completion and release verification, each required-host adapter **MUST** determine:

1. every visible candidate with the target `name` in relevant host scopes or command sources;
2. each ADS-aware candidate `skill_uri`;
3. each ADS-aware candidate semantic version;
4. the source and host-visible identity of each non-ADS candidate that can affect resolution;
5. the candidate the host will execute for automatic and explicit invocation paths that are tested.

The intended package **MUST** be selected unambiguously.

An unresolved identity collision or version collision **MUST** block installation completion and release verification.

The operations guide **MUST** provide a recovery procedure for a collision.

## 8. Project-local persistence across both hosts

Codex and Claude Code **MUST** use the same project-local persistence semantics.

A host adapter **MUST NOT** redirect project configuration, state, runtime metadata, bindings, caches, indexes, logs, registries, or readiness evidence to a user-global or shared location.

A global installation **MUST NOT** become READY for project B because project A was initialized.

A configurable global installation **MUST NOT** use project A configuration while operating in project B.

Installation directories **MUST NOT** be mutated with project-derived data during project operation.

## 9. Configuration portability

A configurable skill **MUST** use a host-independent project-local configuration contract unless its domain contract requires host-specific values.

When host-specific values are necessary, they **MUST** be represented inside the same project-local configuration contract or in clearly separated project-local host sections.

The developer or project policy **MUST** be able to commit or ignore project-local configuration.

The host adapter **MUST NOT** force a version-control choice.

## 10. Stateful lifecycle portability

A stateful skill **MUST** preserve SA-02 lifecycle semantics in both hosts.

`UNINITIALIZED`, `READY`, `STALE`, and `BLOCKED` **MUST** have the same meaning in Codex and Claude Code.

Readiness evidence **MUST** be project-local and bound to the canonical `skill_uri`.

A host change **MUST NOT** make a project READY when project-local readiness evidence is missing or invalid.

If a host-specific binding affects state validity, that binding **MUST** be included in staleness detection.

## 11. Skill API portability

Both hosts **MUST** use the same packaged `skill-api.json` for the same skill version.

The `SKILL.md` description **MUST** summarize the applicability boundary in `skill-api.json` without contradiction.

A host-specific extension **MUST NOT** widen applicability beyond `skill-api.json`.

A host-specific extension **MUST NOT** advertise a capability or outcome absent from the Skill API.

Explicit host invocation **MUST NOT** bypass Skill API applicability exclusions or required preconditions.

## 12. Changelog delivery across both hosts

The same packaged `CHANGELOG.md` **MUST** be available from Codex and Claude Code projections of the same canonical package version.

A clean installation **MUST** serve the installed semantic version, changelog location, and current release entry.

An upgrade **MUST** serve the changelog entries after the previously installed version through the target version.

When a served entry requires migration, configuration change, initialization, or reinitialization, the installer or agent **MUST** route the operator to the applicable procedure before dependent operation continues.

## 13. Operations guide requirements

Every released skill **MUST** provide `references/operations.md`.

The operations guide **MUST** explain installation, upgrade, discovery verification, identity verification, version verification, changelog serving, and collision recovery for both Codex and Claude Code.

For a configurable skill, the guide **MUST** explain how each host locates the same project-local configuration contract.

For a stateful skill, the guide **MUST** explain how each host initializes, reinitializes, and verifies project-local readiness.

The guide **MUST** identify any optional host-specific extension and state that required behavior remains available without it.

## 14. Compatibility test matrix

Every release **MUST** execute each applicable cell in this matrix.

| Capability | Codex | Claude Code |
|---|---|---|
| Project installation | PASS | PASS |
| Global installation, when provided | PASS | PASS |
| Discovery | PASS | PASS |
| Automatic activation | PASS | PASS |
| Explicit invocation, when supported | PASS | PASS |
| Executed `skill_uri` and version | PASS | PASS |
| Same-name collision detection | PASS | PASS |
| `skill-api.json` loading and validation | PASS | PASS |
| Reference loading | PASS | PASS |
| Script execution, when used | PASS | PASS |
| Offline schema resolution | PASS | PASS |
| Project-local configuration, when configurable | PASS | PASS |
| Initialization and reinitialization, when stateful | PASS | PASS |
| Cross-project isolation | PASS | PASS |
| Project-local persistence | PASS | PASS |
| Skill communication, when used | PASS | PASS |
| Diagnostics and recovery | PASS | PASS |
| Changelog access and serving | PASS | PASS |

A mandatory cell that fails **MUST** block release.

## 15. Host-version changes

Host discovery conventions, precedence, reserved names, and supported Agent Skills features can change.

Before each release, the project **MUST** verify current Codex and Claude Code skill documentation for changed discovery paths, precedence, reserved names, or required package constraints.

A host change that breaks a mandatory compatibility cell **MUST** block release until the adapter or package is corrected.

A host-specific compatibility repair **MUST NOT** weaken project-local persistence, schema coverage, Language & Meaning, identity, Skill API semantics, or domain independence.

A host-compatibility repair that preserves the public contract **MAY** be released as PATCH.

A host-driven change that breaks the public contract **MUST** use a MAJOR increment under SA-05.

## 16. Conformance

Required-host compatibility is a mandatory release gate under SA-07.

A release **MUST NOT** pass when either required host executes a package with the wrong `skill_uri` or semantic version.

A release **MUST NOT** pass with an unresolved same-name identity or version collision.

A release **MUST NOT** pass when a host-reserved name prevents skill discovery.

A release **MUST NOT** pass when host-specific behavior contradicts the Skill API.

## 17. Related documents

- Governance: [../00_governance_and_bootstrap.md](../00_governance_and_bootstrap.md)
- Skill Architecture dictionary: [SA-01_skill_architecture_dictionary.md](SA-01_skill_architecture_dictionary.md)
- Architecture: [SA-02_skill_architecture_framework.md](SA-02_skill_architecture_framework.md)
- Language & Meaning: [../language-core/README.md](../language-core/README.md)
- Development and conformance: [SA-07_skill_development_and_conformance.md](SA-07_skill_development_and_conformance.md)
- Standards basis: [../language-core/LMC-01_language_standards_profile.md](../language-core/LMC-01_language_standards_profile.md)
- Schema governance: [SA-03_machine_readable_contracts.md](SA-03_machine_readable_contracts.md)
- Versioning policy: [SA-05_versioning_and_evolution.md](SA-05_versioning_and_evolution.md)
- Skill identity and communication: [SA-06_skill_api_and_communication.md](SA-06_skill_api_and_communication.md)
