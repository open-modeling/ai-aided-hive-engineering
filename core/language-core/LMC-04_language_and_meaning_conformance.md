# Language & Meaning Core — Language and Meaning Conformance

**Document ID:** LMC-04  
**Status:** Normative conformance and bootstrap baseline  
**Suite version:** 5.0.0-rc.1  
**Part:** Language & Meaning Core  
**Parent:** ADS-00

## 1. Purpose

This document defines evidence required to claim Language & Meaning conformance and the bootstrap review used for guideline updates.

## 2. Conformance basis

A Language & Meaning conformance claim identifies:

- the governed artifact and version;
- the applicable LMC version;
- the project-designated checker or review authority;
- the review method;
- evidence locations;
- protected-content handling when applicable;
- project terminology sources used;
- unresolved deviations or blockers;
- the final result.

A conformance claim without designated evidence is incomplete.

## 3. Review sequence

Use this sequence for a governed artifact:

1. classify content applicability under LMC-03;
2. identify protected and imported content;
3. identify normative prose and apply BCP 14 semantics;
4. apply project-authorized ASD-STE100 Issue 9 resources to applicable English prose;
5. apply project-authorized terminology sources;
6. review meaning, scope, actors, conditions, references, and acceptance criteria under LMC-02;
7. apply complementary domain or information standards when relevant;
8. preserve mathematical and machine syntax according to LMC-03;
9. run the project-designated checker or designated review process;
10. retain evidence and record the result.

## 4. Bootstrap review for guideline updates

Every guideline update identifies the previously released LMC baseline used for authoring.

A candidate that changes Part I also performs self-review against the candidate Part I before release.

A candidate that changes only another governed guideline performs review against the currently released Part I.

When one release changes Part I and dependent documents together, dependent documents receive both the prior-baseline review and the candidate-baseline review required by ADS-00.

Bootstrap evidence is part of release evidence.

## 5. Generic machine-readable evidence

The reusable schema is [language-meaning-conformance.schema.json](schemas/language-meaning-conformance.schema.json).

A machine-readable conformance record **MUST** validate against that schema.

A passing record requires designated evidence and passing meaning-control results.

## 6. Conformance classes

| Class | Meaning | Release effect |
|---|---|---|
| **LMC-M** | A mandatory Language & Meaning requirement is not satisfied. | Blocks a conforming release. |
| **LMC-A** | Ambiguity can materially change interpretation or execution. | Blocks release until resolved. |
| **LMC-S** | A documented deviation from a `SHOULD` or `SHOULD NOT` provision. | Allowed with recorded engineering reason and effect. |
| **LMC-E** | Editorial improvement with no normative or semantic effect. | Does not block release. |

## 7. No substitute-standard claim

Passing this project profile does not claim independent certification to an external standard.

When the project claims ASD-STE100 conformance, the claim **MUST** be supported by the project-designated ASD-STE100 checker or review process and its retained evidence.
