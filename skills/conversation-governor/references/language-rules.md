# ADS language and meaning profile (portable extract)

**Source:** AI DevMode Standards `5.0.0-rc.2`, tag `core-v5.0.0-rc.2`. This document embeds the *project integration rules* needed by Conversation Governor. External normative texts retain their own authority.

## LMC-01 — external standards

- BCP 14, RFC 2119 and RFC 8174 define the requirement force of capitalized MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY.
- ASD-STE100 Issue 9 controls applicable project-authored English prose through project-authorized resources and authorized terminology.
- Project prose remains in scope unless a documented applicability rule assigns it to a separate syntax or protected-content class.
- Project terminology complements the authorized ASD-STE100 vocabulary; it has no authority to redefine that vocabulary.
- A full ASD-STE100 conformance claim requires the designated checker or review evidence. A generic word list or local linter is not equivalent.

## LMC-02 — terminology and meaning

- Use one preferred term for one concept.
- Use the common dictionary for shared terms and the owning domain dictionary for domain terms.
- Recognize documented non-preferred synonyms; use the preferred term in agent-authored language.
- When ownership matters, identify the actor. When reference is ambiguous, name the object.
- State material conditions before the dependent instruction; state scope when it differs from the conversation scope.
- Distinguish fact, assumption, decision, recommendation, requirement, and evidence.
- For a material claim, identify inspectable evidence when verification affects execution.
- Resolve term collisions, hidden conditions, conflicting normative levels, and uncertain authority before operational acceptance.

Canonical shared meanings from LMC-02:
- **fact** — current condition supported by inspectable evidence.
- **assumption** — provisional statement accepted for current work without authoritative confirmation.
- **decision** — accepted choice that constrains later work.
- **evidence** — inspectable source, artifact, command result, test, or observation supporting a claim.
- **requirement** — normative provision with a defined level of obligation.
- **precondition** — condition needed before an action can execute correctly.
- **postcondition** — condition required after successful completion.
- **invariant** — condition that remains true throughout its defined scope.
- **acceptance criterion** — objective condition for result acceptability.
- **scope** — the boundary of a statement, action, or decision.
- **authority** — the recognized source able to establish a fact, policy, decision, or controlled value.

## LMC-03 — information construction

- Prefer positive rules that state valid constructions.
- Use prohibitions when needed to protect safety, meaning, contracts, interoperability, or conformance.
- Put procedure prerequisites before ordered actions; include objective completion evidence when needed.
- Present diagnostics as a failed condition, its effect, and a recovery action.
- Mark explanatory content as **Example** or **Illustration** and keep it visibly distinct in a governed publication. These labels establish no normative requirement.
- Preserve quotations, imported requirements, legal text, citations, and project-designated protected content.
- Preserve identifiers, literals, commands, paths, code, mathematical notation, schema keys, and URI values under their own formal syntax rules. Apply language rules to human-readable descriptions around them.
- Classify mixed messages by content region before interpreting or transforming them.

## LMC-04 — language conformance

Review in this order: content applicability; protected text; normative keyword meaning; explanatory labels; authorized STE resources; authorized project terminology; actors, scope, conditions, and evidence; relevant domain standards; syntax protection; designated checker/review.

ADS issue classes:
- **LMC-M** — unsatisfied mandatory requirement.
- **LMC-A** — ambiguity materially affects interpretation or execution.
- **LMC-S** — justified SHOULD deviation with a documented engineering reason and effect.
- **LMC-E** — editorial improvement without normative effect.

A passing ADS or ASD-STE100 claim requires designated review evidence, authority, affected artifact/version, and outstanding limitations.

## Project language lookup during communication

1. Locate project-designated dictionaries and naming conventions from the active project context.
2. Read the relevant term definitions before interpretation or emission.
3. Apply shared LMC terms; apply SA-01 terminology to skill-specific concepts; apply owning domain terms to local concepts.
4. Preserve source wording in quoted/protected incoming material. Normalize the *agent-authored interpretation* for communication.
5. When project sources are unavailable, use explicitly supplied terminology and report material unknown definitions.

## Source links

[LMC-01](https://github.com/open-modeling/ai-aided-hive-engineering/blob/core-v5.0.0-rc.2/core/language-core/LMC-01_language_standards_profile.md) ·
[LMC-02](https://github.com/open-modeling/ai-aided-hive-engineering/blob/core-v5.0.0-rc.2/core/language-core/LMC-02_terminology_and_meaning_control.md) ·
[LMC-03](https://github.com/open-modeling/ai-aided-hive-engineering/blob/core-v5.0.0-rc.2/core/language-core/LMC-03_information_construction_and_applicability.md) ·
[LMC-04](https://github.com/open-modeling/ai-aided-hive-engineering/blob/core-v5.0.0-rc.2/core/language-core/LMC-04_language_and_meaning_conformance.md).
