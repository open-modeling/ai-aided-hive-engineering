# AI DevMode Standards 5.0.0-rc.1

This release candidate restructures ADS into two normative parts under one bootstrap governance layer.

## Start here

1. [ADS-00 — Governance and Bootstrap](00_governance_and_bootstrap.md)
2. [Part I — Language & Meaning Core](language-core/README.md)
3. [Part II — Skill Architecture](skill-architecture/README.md)
4. [Bootstrap conformance evidence](BOOTSTRAP_CONFORMANCE.md)
5. [Known issues](KNOWN_ISSUES.md)

## Architectural rule

Part I is reusable independently of skills.

Part II depends on Part I.

Part I does not depend on Part II.

Every new governed guideline update, including an ADS update, uses the Language & Meaning Core during authoring and review.

## External language authority

BCP 14 governs normative keyword semantics.

ASD-STE100 Issue 9 governs applicable controlled-English vocabulary and writing rules through project-authorized resources.

Applicable ISO, IEC, and IEEE standards complement those authorities.

ADS profiles applicability and project integration; it does not reconstruct the external standards.

## Validation

Run:

```text
python scripts/validate_ads_bundle.py
```

Stable promotion remains blocked by the issues recorded in `KNOWN_ISSUES.md`, including designated language-review evidence and clean required-host runtime testing.
