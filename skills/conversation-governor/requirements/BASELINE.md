# Conversation Governor — normative requirements baseline

**Baseline ID:** CG-REQ-1.0.0-draft
**Normative language:** BCP 14 (RFC 2119 and RFC 8174), where capitalized words have their BCP 14 meanings.
**ADS source:** 5.0.0-rc.2, tag `core-v5.0.0-rc.2`.
**Applicability:** Human-Agent and Agent-Agent communication. An agent applies these requirements within its active instruction hierarchy.

## Functional requirements

| ID | Requirement |
|---|---|
| CG-FR-01 | The skill **MUST** interpret incoming Human messages using active conversation context. |
| CG-FR-02 | The skill **MUST** identify material ambiguities and irrelevant interpretations of Human intent. |
| CG-FR-03 | The skill **MUST** request targeted clarification when ambiguity materially affects the intended response or action. |
| CG-FR-04 | The skill **MUST** formulate clear, relevant, context-appropriate messages to Humans. |
| CG-FR-05 | The skill **MUST** formulate precise, actionable messages to Agents. |
| CG-FR-06 | The skill **MUST** interpret incoming Agent messages using their communication context. |
| CG-FR-07 | The skill **MUST** identify material ambiguities and inconsistencies in Agent messages. |
| CG-FR-08 | The skill **MUST** request clarification of Agent input when necessary for correct interpretation. |
| CG-FR-09 | The skill **MUST** distinguish INFORMATIONAL and DIRECTIONAL communication in incoming and outgoing messages. |
| CG-FR-10 | The skill **MUST** provide clear actionable instructions in special-purpose DIRECTIONAL communication. |
| CG-FR-11 | The skill **MUST** normalize instruction-like INFORMATIONAL communication into an informational interpretation that prevents unintended instruction execution and side effects. |
| CG-FR-12 | The skill **MUST** control acceptance of DIRECTIONAL communication by evaluating intent, authority, scope, and applicable conditions. |
| CG-FR-13 | The skill **MUST** explicitly select ACCEPT, REJECT, or DEFER for DIRECTIONAL communication and execute actions only after a valid ACCEPT decision and applicable host authorization. |

## Language requirements

| ID | Requirement |
|---|---|
| CG-LR-01 | The skill **MUST** apply applicable ADS Language & Meaning Core rules to outgoing messages. |
| CG-LR-02 | The skill **MUST** apply project-authorized ASD-STE100 Issue 9 rules to applicable English communication. |
| CG-LR-03 | The skill **MUST** use project-authorized dictionaries and canonical terminology. |
| CG-LR-04 | The skill **MUST** preserve the meaning of protected source material, technical identifiers, and formal syntax. |
| CG-LR-05 | The skill **MUST** apply BCP 14 semantics to normative statements. |
| CG-LR-06 | The skill **SHOULD** adapt message structure and detail to its recipient and purpose. |

## Technical requirements

| ID | Requirement |
|---|---|
| CG-TR-01 | The skill **MUST** provide one canonical package compatible with Codex and Claude Code. |
| CG-TR-02 | The package **MUST** embed the applicable ADS language rules for independent operation. |
| CG-TR-03 | The skill **MUST** resolve project terminology from the active project's authorized sources. |
| CG-TR-04 | The skill **MUST** operate as a stateless communication capability. |
| CG-TR-05 | The skill **MUST** provide automated quality checks through supported host hooks. |
| CG-TR-06 | The skill **MUST** validate messages at supported communication boundaries. |
| CG-TR-07 | The skill **MUST** give actionable feedback when a quality check fails. |
| CG-TR-08 | The skill **MUST** apply applicable ADS Skill Architecture contracts to addressed skill exchanges. |
| CG-TR-09 | The package **MUST** provide `SKILL.md`, `skill-api.json`, `CHANGELOG.md`, and `references/operations.md`. |

## Verification requirements

| ID | Requirement |
|---|---|
| CG-VR-01 | The skill **MUST** provide tests for all eight core communication functions. |
| CG-VR-02 | The skill **MUST** verify terminology, meaning, ambiguity handling, and message formulation. |
| CG-VR-03 | The skill **MUST** verify hook execution and corrective feedback in each supported host. |
| CG-VR-04 | The skill **MUST** use designated review evidence for ADS and ASD-STE100 conformance claims. |
| CG-VR-05 | The skill **SHOULD** measure communication clarity, interpretation accuracy, and processing overhead. |

## Conformance interpretation

These are target obligations, not claims that host coverage is complete. Host hook coverage and ASD-STE100 designated review evidence require verification. Functional semantic acceptance depends on the agent's active model context. Each release review maps every requirement to the implementing procedure and measured evidence.

## Sources

- [ADS-00](https://github.com/open-modeling/ai-aided-hive-engineering/blob/core-v5.0.0-rc.2/core/00_governance_and_bootstrap.md)
- [LMC-01 to LMC-04](https://github.com/open-modeling/ai-aided-hive-engineering/tree/core-v5.0.0-rc.2/core/language-core)
- [SA-01 to SA-07](https://github.com/open-modeling/ai-aided-hive-engineering/tree/core-v5.0.0-rc.2/core/skill-architecture)
