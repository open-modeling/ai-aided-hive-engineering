# AI DevMode Standards — Governance and Bootstrap

**Document ID:** ADS-00  
**Status:** Normative umbrella governance, release-candidate baseline  
**Suite version:** 5.0.0-rc.1  
**Date:** 2026-09-13

## 1. Purpose

AI DevMode Standards (ADS) define a common project baseline with two normative parts:

1. **Part I — Language & Meaning Core (LMC)** controls project-authored language, normative meaning, terminology integration, interpretation, protected-source handling, and conformance evidence.
2. **Part II — Skill Architecture (SA)** controls reusable agent-skill identity, package architecture, lifecycle, configuration, machine-readable contracts, hosts, Skill API, communication, and release behavior.

ADS-00 governs both parts and the process used to change them.

## 2. Dependency architecture

The dependency direction is mandatory:

```text
ADS-00 Governance and Bootstrap
        |
        +--> Part I — Language & Meaning Core
        |         ^
        |         |
        |         +---- governs ADS-00, Part II, and other governed project guidelines
        |
        +--> Part II — Skill Architecture
                  depends on Part I
```

Part I **MUST NOT** depend on Part II.

Part II **MUST** use Part I for project-authored prose, normative meaning, terminology integration, information construction, protected-content handling, and language/meaning conformance evidence.

A shared rule belongs in Part I when its correctness does not depend on the governed artifact being a skill.

A skill-specific rule belongs in Part II.

## 3. External language authority

ADS does not create a replacement controlled language.

BCP 14, using RFC 2119 and RFC 8174, governs normative keyword semantics for applicable project-authored normative prose.

ASD-STE100 Issue 9 governs controlled-English vocabulary and writing rules for applicable project-authored English prose through project-authorized STE resources and terminology sources.

Applicable ISO, IEC, and IEEE standards complement those authorities for terminology, information development, drafting discipline, plain language, and conformity-ready requirements as profiled by Part I.

External standards remain authoritative for their own content. ADS references and profiles them; ADS does not reproduce a reduced or expanded substitute.

## 4. Self-bootstrapping requirement

Every new project-guideline update **MUST** be authored and reviewed under the currently released Language & Meaning Core that governs the project.

A candidate revision to Part I **MUST** satisfy two reviews before release:

1. conformance to the previously released Language & Meaning Core used to author the candidate; and
2. self-conformance to the candidate Language & Meaning Core.

A candidate revision to ADS-00 or Part II **MUST** conform to the currently released Language & Meaning Core.

When the same release candidate also changes Part I, ADS-00 and Part II **MUST** additionally conform to the candidate Language & Meaning Core before release.

A guideline **MUST NOT** exempt itself from the Language & Meaning Core solely because it defines or modifies that core.

A rule that intentionally cannot satisfy the prior language baseline **MUST** identify the incompatibility, rationale, migration path, and approving project authority.

## 5. Guideline-update flow

Every governed guideline update uses this sequence:

1. identify the governing released Language & Meaning Core;
2. classify the changed content and language applicability;
3. preserve protected and imported content;
4. apply BCP 14 where normative semantics are present;
5. apply the project-designated ASD-STE100 Issue 9 resources to applicable prose;
6. apply project terminology and meaning-control rules;
7. apply domain-specific rules after the common language/meaning review;
8. collect designated checker or review evidence;
9. determine version impact;
10. release only after every applicable mandatory gate passes.

## 6. Part I scope

Part I contains:

- [LMC-01 — External Language Standards Profile](language-core/LMC-01_language_standards_profile.md)
- [LMC-02 — Project Terminology and Meaning Control](language-core/LMC-02_terminology_and_meaning_control.md)
- [LMC-03 — Information Construction and Applicability](language-core/LMC-03_information_construction_and_applicability.md)
- [LMC-04 — Language and Meaning Conformance](language-core/LMC-04_language_and_meaning_conformance.md)

Part I is independently reusable by Document Governor, harness guidelines, Hive/Swarm material, project engineering policies, documentation-refinement workflows, and other governed project artifacts.

## 7. Part II scope

Part II contains:

- [SA-01 — Skill Architecture Dictionary](skill-architecture/SA-01_skill_architecture_dictionary.md)
- [SA-02 — Skill Architecture Framework](skill-architecture/SA-02_skill_architecture_framework.md)
- [SA-03 — Machine-Readable Contracts](skill-architecture/SA-03_machine_readable_contracts.md)
- [SA-04 — Required-Host Compatibility](skill-architecture/SA-04_required_host_compatibility.md)
- [SA-05 — Versioning and Evolution](skill-architecture/SA-05_versioning_and_evolution.md)
- [SA-06 — Skill API and Communication](skill-architecture/SA-06_skill_api_and_communication.md)
- [SA-07 — Skill Development and Conformance](skill-architecture/SA-07_skill_development_and_conformance.md)

Part II depends on Part I and **MUST NOT** redefine shared language or meaning rules.

## 8. Precedence

Use this precedence when project documents conflict:

1. platform safety and system constraints;
2. current explicit user instructions within those constraints;
3. authoritative project policy;
4. ADS-00 governance and bootstrap rules;
5. Part I for language, normative meaning, terminology integration, and interpretation control;
6. Part II for skill architecture;
7. domain-specific project standards and skill specifications within their defined scope.

A lower-precedence document **MUST NOT** weaken a higher-precedence mandatory requirement.

## 9. Versioning

The ADS suite uses Semantic Versioning.

This restructuring candidate is `5.0.0-rc.1` because separating the suite into reusable Part I and dependent Part II changes normative document ownership, dependency direction, and conformance obligations.

A released ADS version **MUST** remain immutable.

## 10. Bootstrap evidence

Every ADS release candidate **MUST** include bootstrap evidence that identifies:

- the prior governing language baseline;
- the candidate language baseline;
- the reviewed artifact set;
- the designated checker or review method;
- evidence locations;
- unresolved deviations or blockers.

This candidate records that evidence in [BOOTSTRAP_CONFORMANCE.md](BOOTSTRAP_CONFORMANCE.md).
