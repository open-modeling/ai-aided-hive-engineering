# AI Aided Hive Engineering — Joint Backlog

Status: canonical development backlog for proposal evolution after 0.60.

Priority is execution order. Severity is consequence if unresolved. Rows are sorted by priority, then severity, then ID. Completed, superseded, and retired rows are retained for stable references and change-history continuity.

Severity meanings:

- **Critical** — leaves a central claim unsupported or makes the model unsafe to implement;
- **Major** — a core mechanism is unsound, untestable, materially incomplete, or undefined;
- **Minor** — a local inconsistency or omission that does not require changing the central model;
- **Editorial** — drafting, organization, rendering, or release hygiene.

## Canonical backlog

| ID | Priority | Severity | Status | Backlog item | Completion criterion / scope |
|---|---|---|---|---|---|
| **BL-02** | **P0** | **Critical** | Open | **State-commit consistency** | Define source-State qualification, dependency/affected semantic footprint, stale-result detection, overlapping-change conflict semantics, and required ordering/atomicity without introducing a universal Candidate Delta object. Must use context-qualified Engineering State. |
| **BL-08** | **P0** | **Critical** | Partial | **Information ingress, trust, and execution containment** | Human-originated classification and HWP semantics are corrected. Remaining work: common ingress trust levels, provenance integrity, instruction/data isolation, adversarial/exploitation handling, and an authorized out-of-band suspension path that does not become semantic `HumanOverride`. |
| **BL-03** | **P0** | **Major** | Open | **AX-6 concurrent-evolution formalization** | Remove untestable probability wording; express allowed divergence/convergence properties, include materialized-state replacement, and connect commitment semantics to BL-02. |
| **BL-04** | **P0** | **Major** | Completed | **Engineering History versus Space semantics** | Completed in 0.60: context-qualified State is established and Product Evolution History is no longer required to be a subset of the current State/Space. |
| **BL-05** | **P0** | **Major** | Open | **Contract lifecycle rework** | Re-derive Contract runtime lifecycle from Contract identity/revision, hard Issuer/Executor/delegate separation, Assignment, participants, HWP/Work Product contribution and submission, Acceptance, rework, reassessment, discontinuation, and history. Existing FSM counterexamples are regression cases; do not continue row-by-row guard patching. |
| **BL-06** | **P0** | **Major** | Open | **Rollback Closure semantics** | Define deterministic dependency closure, separate closure from alternative validity-restoration choices, and resolve cross-Layer dependency/core-element cases. |
| **BL-07** | **P0** | **Major** | Open | **Formal argument and NS-1 repair** | Resolve NS-1 circularity; decide theorem versus design principle; move non-implications out of places where they are presented as constraints and retain genuine anti-properties as explicit countermodel/anti-pattern statements. |
| **BL-09** | **P0** | **Major** | Completed | **Feasibility and Trade Space core calculus** | Completed in 0.60: Feasibility is a context/time/problem-qualified Feasible Region under set calculus, not `Feasible(...)`; the core links Solution Universe, Solution Space, active constraints, Feasible Region, Trade Space Analysis, Evidence, and Decision; expansion/recovery semantics are explicit. |
| **BL-29** | **P0** | **Major** | Completed | **Canonical mathematical data model** | `proposal/DATA_MODEL.md` establishes the development consistency baseline. Every future reusable concept/signature must map to or explicitly extend it before proposal mathematics is accepted. |
| **BL-15** | **P1** | **Critical** | Open | **Engineering Economy and retention model** | Complete Resource Cost and Rollback Cost; governance/boundary/retention cost; identity resolution/deduplication; retention/compaction; Reward/Penalty semantics; checkable invention rule. Provide the economic basis consumed by BL-32. |
| **BL-10** | **P1** | **Major** | Partial | **Check Cascade semantics** | Feasibility is explicitly excluded. Remaining work: property-specific/applicability-aware gating; required/pass/fail/not-applicable semantics; unrelated failures must not block unrelated properties. Preserve its role in conformity, Acceptance, re-check, and rework. |
| **BL-11** | **P1** | **Major** | Open | **Boundary assurance and revalidation** | Require transfer/projection fidelity Evidence; root-cause aggregation/escalation classes through Project Profile; validator independence; revalidation triggers after materially relevant model/tool/validator changes. |
| **BL-13** | **P1** | **Major** | Open | **Scale and Magnification semantic consistency** | Re-audit current Scale, Layer, Domain, adjacency, Band, Magnification, transfer, and propagation semantics against the data model. Old 0.40 counterexamples are historical unless reproduced. Executable/Alloy work belongs to BL-16. |
| **BL-14** | **P1** | **Major** | Open | **Project Profile language formalization** | Define machine-addressable Profile syntax/semantics, parameter applicability, defaults/absence rules, validation, composition, inheritance/override, versioning/migration, compatibility, extension points, and the boundary between Project Profile policy and common-model semantics. |
| **BL-32** | **P1** | **Major** | Open | **Project Profile feasibility-control policy** | Define trajectory-time feasibility control under bounded economy/resources: exploration/research budget, economic stopping, capability/technology/resource/domain requests, constraint-relaxation requests, production baseline, timeline limits, escalation, and recovery. Must not redefine core Feasible Region calculus. |
| **BL-12** | **P1** | **Minor** | Open | **Decision propagation typing and disposition** | Give Decision Blast Radius and Decision Extent compatible explicit types/comparison semantics; correct owner-context containment; represent cancelled/superseded/rejected disposition without conflating disposition with the minimal lifecycle. |
| **BL-17** | **P2** | **Critical** | Open | **Evaluation plan and reference Project Profile** | Publish one reference Profile and one end-to-end example across at least two Layers; define falsifiable hypotheses, metrics, governance-cost measurements, and a pilot against an event-driven non-polling baseline. |
| **BL-19** | **P2** | **Major** | Open | **Traceability dimensions** | Define distinct traceability relation types/dimensions, directionality, and applicable semantics rather than one undifferentiated traceability concept. |
| **BL-20** | **P2** | **Major** | Open | **Conformance surface and requirement traceability** | Establish compact stable conformance-obligation IDs and map them to defining clauses and validation evidence without numbering every sentence. |
| **BL-21** | **P2** | **Major** | Open | **Inter-Hive and global operational patterns** | Define Hive-to-Hive handoff/delegation, responsibility, information transfer, convergence, and coordination boundaries without a default global controlling Hive. |
| **BL-23** | **P2** | **Major** | Open | **Safety-critical framework alignment** | Map Evidence, Decision, authority, escalation, traceability, verification, and Acceptance semantics to applicable safety-critical frameworks; document incompatibilities without hard-coding one domain into the common model. |
| **BL-22** | **P2** | **Minor** | Open | **ADS/LMC baseline update and conformance evidence** | Rebase to the accepted project baseline, reconcile terminology/schema changes, and produce required LMC evidence where conformance is claimed. |
| **BL-16** | **P3** | **Minor** | Open | **Executable formal validation / Alloy** | After semantic stabilization, add bounded formal models/runners and formal-source consistency checks to repository validation. Formal tools validate the model; they do not define it. |
| **BL-24** | **P3** | **Minor** | Open | **Proposal structural compaction and lightweight Contract presentation** | Reduce duplicated/disproportionate Contract material and provide a compact Contract view without creating a second semantic Contract model. |
| **BL-25** | **P3** | **Minor** | Open | **Related-work and research-positioning consolidation** | Recheck stabilized semantics against the accepted related-work families and complete publication-grade source/metadata verification before strengthening research-gap wording. |
| **BL-26** | **P3** | **Minor** | Open | **V-model alignment** | Map Hive engineering concepts to V-model development/verification structure without making the V-model normative for Hive. |
| **BL-27** | **P3** | **Minor** | Open | **Automotive SPICE alignment** | Map applicable Contracts, Work Products, Evidence, traceability, verification, Acceptance, and governance semantics to Automotive SPICE and document gaps. |
| **BL-30** | **P3** | **Minor** | Open | **Retracted-section analysis** | Review `proposal/RETRACTIONS.md` after replacement semantics stabilize and recover only general rules not already covered by the common model. |
| **BL-28** | **P3** | **Editorial** | Open | **Release and editorial hygiene** | Fix residual numbering/heading/order/source-release defects and remove closed legacy audit residue rather than carrying it indefinitely. |

## Preserved detailed scope from the 0.50 backlog

The following details are retained from the 0.50 backlog and are governed by the canonical IDs above.

### BL-25 — related work and publication positioning

- Maintain three explicit strata: related work/alignment without presumed ancestry; engineering toolbox/implementation instrumentation; and proposal-specific synthesis.
- Distinguish peer-reviewed research, formal standards/specifications, established engineering methods, recent preprints, industrial research, and implementation/framework documentation.
- Map each related-work family only to semantics it actually supports or contrasts; keep implementation precedent separate from foundational equivalence.
- Continue migration of Draft 0.14 research positioning against the current model rather than importing it verbatim.
- Keep universal Candidate Delta out of the common-model research-positioning spine.
- Treat typed/schema-constrained LLM output and neuro-symbolic computation as implementation mechanisms unless a stronger common-model dependency is established.
- Treat calibration, selective classification, and conformal prediction as computation-level uncertainty methods rather than prior art for Hive Confidence.
- Preserve the historical lineage through shared-state coordination, truth maintenance/design rationale, commitment/governance, assurance/provenance, Trade Space engineering, and resource-bounded reasoning.
- Recheck digital thread, MBSE, lifecycle engineering information, boundary objects/cross-discipline interpretation, artifact-centric lifecycle models, SACM, W3C PROV, PPMN, Agent Contracts, Agent Behavioral Contracts, and Proof-Carrying Agent Actions.
- Keep SysML v2, Alloy, solver interfaces, and similar instrumentation in the Engineering Toolbox unless common-model dependence is established.
- Keep research positioning separate from legal novelty or patentability claims.

### BL-13 — Scale / Magnification / Domain follow-up

The 0.50 topology package is accepted: rectangular Scale-Domain projection, Magnification Bands, Layer Band homogeneity, governed Band compaction, sparse Domain adjacency, and the no-fold invariant remain the baseline.

Follow-up scope:

- assess graph transformation, algebraic graph transformation, order/topology-preserving refinement, sparse multiscale modelling, and related independent work against the stabilized model;
- maintain counterexample cases for imported graph defects, invalid Layer merges, diagonal relations, and Magnification Conflicts;
- keep Alloy/SAT materialization under BL-16 rather than allowing it to redefine Scale semantics.

### BL-21 — Inter-Hive/global operations

Cover Team API-connected Hive topology; source identity and provenance continuity; receiving-Hive context establishment; exchange continuation; boundary failure and Gap semantics; interaction between independently governed Scale systems; Authority and Evidence locality; Contract relationships; global traversal and traceability without semantic collapse; and multiple cooperating Hives/external Actors.

Do not assume one global Engineering State, one global Scale, shared Authority, or global Evidence applicability unless separately established.

### BL-08 — information ingress

Define representation, classification, qualification, validation, and admission of information entering Hive. Conversational forms such as questions, requests, or clarifications remain non-binding content unless explicitly promoted into common-model vocabulary through a reviewed change.

### BL-15 — Engineering Economy

Consolidate economic objective, Resource Cost, Rollback Cost, exploration versus materialization cost, Decision ordering under concurrency, Decision Blast Radius/Decision Extent economics, over-commitment, resource depletion, staged resource expenditure, retention cost, and the economic basis required by feasibility-control policy.

### BL-05 — Contract lifecycle and realization

The full redesign must also cover progression from lightweight Solution Exploration through planning, Work Product materialization, integration, and where applicable physical-world realization. Preserve one Contract semantic model rather than creating a second realization lifecycle.

### BL-19 — traceability

Refine operational/metadata and materialized engineering dimensions of the common Product graph while preserving one relation algebra and explicit directionality/qualification.

### BL-14 — Project Profile DSL

Include semantic types, declarations, references, composition, inheritance/override, validation, versioning/migration, compatibility, extension points, and conformance semantics.

### BL-24 — structural compaction

Continue removing duplicated semantics, unnecessary section depth, and implementation-oriented detail only through bounded reviewed packages. Contract compaction must follow BL-05 rather than pre-empt its data-model redesign.

### BL-22 — ADS/LMC baseline

Rebase to the accepted ADS/LMC baseline and retain only proposal-specific language specialization locally. Keep common Example/Illustration semantics owned by the imported language standard where applicable.

### BL-26 / BL-27 / BL-23 — external alignment

Assess V-model, Automotive SPICE, and safety-critical frameworks as external engineering frameworks. Do not imply common-model conformance or import external semantics before the corresponding assessment is completed.

## Superseded or retired items

| ID | Previous priority | Severity | Status | Disposition |
|---|---|---|---|---|
| **BL-01** | P0 | Major | Superseded | Former formal-source/Human-transformation repair package. Human-specific transformation/composability semantics were retracted; remaining concerns moved into BL-05, BL-08, BL-16, and BL-29. |
| **BL-18** | P2 | Major | Superseded | Contract realization phases are absorbed into the full Contract lifecycle rework in BL-05. |
| **BL-31** | P0 | Major | Retired | Legacy §13 metric proposal removed. The proposal retains only the measurable Prescriptiveness calculus. Historical source is preserved in `proposal/RETRACTIONS.md`. |
