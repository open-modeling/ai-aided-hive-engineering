# Language & Meaning Core — Information Construction and Applicability

**Document ID:** LMC-03  
**Status:** Normative information-construction and source-protection baseline  
**Suite version:** 5.0.0-rc.1  
**Part:** Language & Meaning Core  
**Parent:** ADS-00

## 1. Purpose

This document defines project integration rules for constructing understandable information without replacing the external controlled-language rules in LMC-01.

## 2. Positive construction model

State language principles as positive construction rules when a valid construction can be specified directly.

Use a prohibition when the prohibited action would create a real safety, semantic, contractual, interoperability, or conformance defect.

Build each project-authored statement so its intended interpretation can be determined from the statement, its defined context, and its referenced authority.

## 3. Information types

### 3.1 Normative provisions

Construct normative provisions with BCP 14 semantics and the meaning controls in LMC-02.

Make mandatory provisions objectively inspectable or testable when conformity assessment is required.

### 3.2 Procedures

Construct procedures as ordered actions when sequence matters.

State prerequisites before dependent actions.

Identify the actor when role ownership is not inherent in the procedure.

Identify expected evidence that confirms successful completion.

### 3.3 Diagnostics

State the failed condition.

State the affected capability or result when the effect is not evident.

State the next safe recovery action when one exists.

### 3.4 Handoffs and status information

Record current facts, decisions, blockers, evidence, and next valid actions.

Prefer current state over chronological discussion history.

### 3.5 Explanatory material

Organize explanations around one technical topic at a time.

Use explicit references when multiple possible referents exist.

## 4. Protected and imported content

Preserve quotations, citations, imported requirements, legal text, contractual text, and other project-designated protected source material unchanged during language normalization.

Place project-authored interpretation, mapping, or explanation outside the protected source text.

Preserve identifiers, controlled external names, and literal values when their exact form carries meaning.

## 5. Mathematical and machine syntax

Treat mathematical notation, code, schemas, identifiers, protocol tokens, URI values, commands, and other machine-readable syntax according to their defining formalism.

Apply the language profile to surrounding human-readable prose.

Apply the language profile to human-readable descriptions embedded in machine-readable artifacts when those strings are intended for people.

Do not transform formal syntax merely to satisfy prose-writing rules.

## 6. Artifact applicability

Before normalization or review, classify each content region as one of these types:

1. project-authored prose;
2. protected or imported prose;
3. formal mathematical notation;
4. executable or machine-readable syntax;
5. identifier or literal token;
6. mixed content requiring region-level treatment.

Apply only the rules that govern the classified region.

## 7. Domain profiles

A domain standard may add construction rules that are necessary for its domain.

A domain-specific profile references the common Language & Meaning Core instead of duplicating shared rules.
