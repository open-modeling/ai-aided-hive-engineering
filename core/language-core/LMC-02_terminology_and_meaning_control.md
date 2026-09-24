# Language & Meaning Core — Project Terminology and Meaning Control

**Document ID:** LMC-02  
**Status:** Normative project terminology and interpretation baseline  
**Suite version:** 5.0.0-rc.1  
**Part:** Language & Meaning Core  
**Parent:** ADS-00

## 1. Purpose

This document controls project-specific terminology and interpretation so project-authored information has stable, reviewable meaning.

It does not provide a substitute STE vocabulary.

## 2. Project terminology principles

Use one preferred project term for one project concept.

Define a shared project term before dependent standards use it normatively.

Record recurring project synonyms as non-preferred terms when recognition is necessary.

Keep domain-only terminology in the owning domain standard.

Use project-authorized terminology sources together with the authorized ASD-STE100 vocabulary.

## 3. Common meaning-control terms

| Term | Meaning |
|---|---|
| **fact** | A current condition supported by inspectable evidence. |
| **assumption** | A provisional statement accepted for current work without authoritative confirmation. |
| **decision** | An accepted choice that constrains subsequent work. |
| **evidence** | An inspectable artifact, source, command result, test result, or observation that supports a claim. |
| **requirement** | A normative provision whose requirement level is expressed through the governing normative-language system. |
| **precondition** | A required condition before an action can execute correctly. |
| **postcondition** | A required condition after successful completion. |
| **invariant** | A condition required to remain true throughout a defined scope or operation. |
| **acceptance criterion** | An objective condition used to decide whether a result is acceptable. |
| **scope** | The boundary inside which a statement, requirement, decision, or effect applies. |
| **authority** | The project-recognized source that can establish a fact, policy, decision, or controlled value. |

## 4. Meaning construction

State the actor when responsibility can otherwise be unclear.

State the object directly when multiple referents are possible.

State critical conditions before the dependent action or requirement.

State scope explicitly when a requirement is not universal.

Distinguish fact, assumption, decision, recommendation, and requirement.

Link a material claim to evidence when verification affects execution or release decisions.

Use acceptance criteria for outcomes that require objective verification.

## 5. Normative meaning

Use BCP 14 keywords with the semantics profiled by LMC-01.

A normative provision identifies the subject, required behavior, relevant condition, and scope when those elements are necessary for unambiguous interpretation.

A `SHOULD` or `SHOULD NOT` deviation records a concrete engineering reason and effect.

## 6. Ambiguity control

Resolve a term collision before dependent requirements are released.

Resolve hidden conditions when different readers could select different execution paths.

Resolve conflicting normative levels before release.

Mark unresolved authority as unresolved instead of converting it into an assumed fact.

## 7. Terminology ownership

Part I owns terminology that is reusable independently of skill architecture.

Part II owns skill-architecture terminology.

Domain standards own their domain-only terminology.

An owning domain standard **MUST NOT** redefine a common project term with a different meaning.
