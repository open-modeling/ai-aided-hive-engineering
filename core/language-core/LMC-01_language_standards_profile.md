# Language & Meaning Core — External Language Standards Profile

**Document ID:** LMC-01  
**Status:** Normative project applicability profile  
**Suite version:** 5.0.0-rc.1  
**Part:** Language & Meaning Core  
**Parent:** ADS-00

## 1. Purpose

This document defines how established language and information standards apply to AI DevMode project-authored material.

It does not replace, reconstruct, or reproduce those standards.

## 2. Authoritative external basis

### 2.1 BCP 14

RFC 2119 and RFC 8174 govern the semantics of uppercase `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` in applicable project-authored normative prose.

Project material uses those keywords with BCP 14 meaning.

### 2.2 ASD-STE100 Issue 9

ASD-STE100 Issue 9 governs controlled-English vocabulary and writing rules for applicable project-authored English prose.

Authors and checkers **MUST** use project-authorized ASD-STE100 Issue 9 resources and authorized terminology sources.

Project material **MUST NOT** reconstruct the complete ASD-STE100 dictionary or create a parallel authoritative STE dictionary.

LMC documents define applicability and integration behavior only where project-specific decisions are necessary.

### 2.3 Complementary standards

The project uses applicable ISO, IEC, and IEEE standards to complement BCP 14 and ASD-STE100 in these areas:

- ISO 704, ISO 1087, ISO 10241-1, and ISO 860 for terminology work and harmonization;
- ISO 24495-1 for plain-language principles;
- ISO/IEC Directives, Part 2 for drafting discipline and verifiable provisions;
- ISO/IEC/IEEE 26514 and 26515, and IEC/IEEE 82079-1, for information development and information for use;
- ISO/IEC 17007 for conformity-assessment-ready normative requirements.

The project profile **MUST** preserve the authoritative scope and meaning of each external standard.

## 3. Applicability classes

Project-authored English prose is in scope for ASD-STE100 Issue 9 unless an explicit applicability rule excludes the content type.

Project-authored normative prose is in scope for BCP 14 when the project uses normative requirement levels.

Human-readable prose embedded inside machine-readable artifacts remains prose and uses the applicable language profile.

The following content is handled by explicit applicability rules rather than prose rewriting:

- mathematical notation;
- executable code;
- schema and protocol tokens;
- identifiers and URI values;
- literal commands and paths;
- machine-readable syntax.

Protected source material is preserved under LMC-03.

## 4. Project terminology integration

Project terminology complements, rather than replaces, the authorized STE vocabulary.

Project-specific technical names and domain terms use project-authorized terminology sources.

A domain-specific standard defines only the terminology extensions required by that domain.

Shared project terminology belongs in LMC-02 or another project-authorized common terminology source.

## 5. Evidence rule

A language-conformance claim requires evidence from the project-designated checker, designated review process, or an approved combination of both.

A local checklist without designated evidence **MUST NOT** be represented as full language conformance.

## 6. External-standard updates

When an authoritative external standard changes, the project **SHOULD** review the applicable profile before the next affected guideline release.

A profile update records the project integration change without copying the external standard into ADS.
