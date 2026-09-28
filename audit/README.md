# Audit records

This directory stores human-readable audit records for specific committed repository states.

Audit records are evidence and rationale, not canonical proposal semantics and not a substitute for Git history or release tags. They explain what was checked, what was found, and why a repository state was accepted, rejected, or left with known issues.

Audit records are repository records and are not included in proposal release archives unless the release policy is changed explicitly.

## 1. Audit target

An audit MUST identify an immutable committed repository state.

Record at least:

- audited commit SHA;
- proposal version, where applicable;
- audit date;
- audit type and scope;
- checks performed;
- findings and limitations;
- external or third-party tool execution relevant to that state.

Do not describe an uncommitted working tree as an audited repository state. If repository infrastructure must change before an audit can be performed, commit that infrastructure first and audit the resulting commit.

An audit record SHOULD target the commit immediately preceding the commit that adds the record. This avoids claiming that a record audits its own addition.

Recommended filename form:

`YYYY-MM-DD_<scope>_<audited-commit>.md`

## 2. Adding an audit

1. Start from a clean working tree.
2. Identify the committed state and the exact audit scope.
3. Run the applicable repository checks and semantic review without modifying the audited state.
4. Record both passing areas and findings. Do not omit known limitations or failed checks.
5. Distinguish local checks from external research, external services, or third-party tool execution.
6. Add the audit record in `audit/` only after the reviewed state is fixed by commit identity.
7. Run repository validation on the record addition before committing it.

If an external tool materially contributes to an audit result, record enough information for a human to understand and repeat the check where practical: tool or service name, version or dated identity, command or configuration, target state, and outcome. Large generated logs should not replace the human-readable audit rationale.

## 3. Finding lifecycle

A finding belongs to the audited state. It MUST NOT be rewritten later to make an old state appear clean.

Use these logical states when processing a finding:

`OPEN -> CHANGE PROPOSED -> ACCEPTED -> IMPLEMENTED -> VERIFIED -> CLOSED`

The states are process states, not fields that must be retroactively edited into old audit records.

- **OPEN:** the audit identifies the issue.
- **CHANGE PROPOSED:** a bounded correction is prepared for review.
- **ACCEPTED:** the human reviewer explicitly agrees to the correction direction or exact change.
- **IMPLEMENTED:** the accepted change exists in a committed repository state.
- **VERIFIED:** a re-check confirms that the committed change resolves the finding without introducing a conflicting defect.
- **CLOSED:** a later audit or re-check record identifies the original finding as resolved.

If a proposed correction is rejected, the finding remains OPEN unless the audit itself is shown to be incorrect. A factual error in an audit record is corrected by a new superseding audit note or record; do not silently rewrite committed audit evidence.

## 4. Change control from audit findings

An audit finding does not authorize a semantic change by itself.

For each correction:

1. identify the finding and affected files/sections;
2. define the minimum viable correction and expected invariants;
3. show the proposed change for review when proposal semantics are affected;
4. obtain explicit agreement before committing semantic changes;
5. keep unrelated corrections out of the same change where practical;
6. run repository validation and finding-specific checks;
7. commit with a message that states the rationale, not only the edited file;
8. re-check the committed state and record closure separately when the finding is materially important.

A correction MAY reveal a larger model problem. In that case, stop expanding the patch, record or backlog the larger issue, and keep the accepted correction boundary explicit.

## 5. Audit control rules

- **State fidelity:** findings and conclusions apply only to the identified commit unless explicitly re-verified on a later state.
- **No silent closure:** removing a backlog item or changing wording does not prove an audit finding closed.
- **No semantic authority:** audit text, backlog text, and tool reports do not become proposal semantics unless separately integrated into the canonical proposal.
- **Traceability:** later corrections SHOULD reference the audit finding or audit record that motivated them.
- **Repeatability:** mechanical checks SHOULD record the actual command or validator used when it matters to the conclusion.
- **Source separation:** local repository evidence, external literature, and third-party tool results MUST be distinguishable.
- **Failure preservation:** a failed check remains part of the audit evidence even if a later change fixes it.
- **Release separation:** audit records remain outside proposal release artifacts unless release policy is deliberately changed.
- **History separation:** repository evolution is reconstructed from Git commits and tags, not from an audit ledger.

## 6. Re-audit after changes

A re-audit SHOULD be performed when a change:

- resolves a High or Medium semantic finding;
- changes formal model semantics or registered vocabulary;
- changes repository governance, validators, release rules, or imported core baselines;
- changes Scale/Magnification/Domain topology rules;
- changes Exchange Item, receiving-layer decomposition, Evidence, authority, Contract, Acceptance, or terminal handoff semantics;
- materially changes the literature-based research-positioning claims.

A re-audit may be narrow when the correction is narrow, but it MUST include all invariants that the correction could reasonably affect.

## 7. Relationship to backlog and proposal

The backlog records unresolved work and accepted future directions. It is not an audit ledger.

Audit findings MAY create or update backlog items. Closing a backlog item and closing an audit finding are separate operations:

- backlog closure means the planned work is no longer outstanding;
- audit closure means a committed state has been verified against the original finding.

The canonical proposal remains `proposal/AI_Aided_Hive_Engineering.md`. Audit records and backlog entries remain non-canonical unless their content is separately reviewed and integrated there.
