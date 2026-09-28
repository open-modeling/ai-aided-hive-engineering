# AI Aided Hive Engineering Proposal Backlog

This file records unresolved proposal work outside the canonical proposal body.

Items are not proposal semantics until reviewed and integrated into the proposal through an accepted change.

## Priority work

### 1. Literature organisation and related-work positioning

**Status:** accepted and integrated into proposal §§23–24. `proposal/RELATED_WORK_RESEARCH.md` remains non-canonical research support; publication-grade metadata verification and future explicit alignments remain follow-up work.

- **Literature architecture:** reorganize related work into three explicitly separated strata:
  1. related work and alignment without presumed ancestry;
  2. engineering toolbox and implementation/comparison instrumentation.
- **Source classification:** distinguish peer-reviewed research, formal standards/specifications, established engineering methods, recent preprints, industrial research, and implementation/framework documentation. Do not present these source classes as equivalent evidence.
- **Proposal-to-literature traceability:** map each related-work family to the current proposal semantics it actually supports or contrasts. Separate established prior art, implementation precedent, comparison systems, and potentially distinctive combinations.
- **Draft 0.14 migration:** update the Draft 0.14 research recap against the current proposal rather than importing it verbatim. In particular:
  - remove universal `Candidate Delta` from the common-model research-positioning spine;
  - treat typed/schema-constrained LLM output and neuro-symbolic computation as implementation mechanisms unless a stronger common-model dependency is established;
  - treat calibration, selective classification, and conformal prediction as computation-level uncertainty methods rather than prior art for Hive `Confidence`, which is an operational-health indication;
  - preserve the strong historical lineage through shared-state coordination, truth maintenance/design rationale, commitment/governance, assurance/provenance, tradespace engineering, and resource-bounded reasoning.
- **Missing related-work families:** assess and add, where supported:
  - digital thread, MBSE, and lifecycle engineering information;
  - keep SysML v2, Alloy, solver interfaces, and similar instrumentation in the Engineering Toolbox rather than treating them as Hive semantic foundations;
  - boundary objects and cross-discipline interpretation, especially for Exchange Item receiving-layer decomposition and inter-Hive handoff;
  - artifact-centric lifecycle/process models such as Guard-Stage-Milestone;
  - current assurance and provenance standards, including SACM, W3C PROV, and PPMN;
  - Agent Contracts, Agent Behavioral Contracts, and Proof-Carrying Agent Actions as contemporary comparison work rather than foundational equivalence.
- **Reference-section redesign:** completed in proposal §§23–24: related work/alignment is separated from optional Engineering Toolbox instrumentation.
- **Research-gap statement:** Scale/Magnification topology and Exchange Item decomposition are now stabilized; defer stronger wording until inter-Hive/global operational patterns and the selected literature set are rechecked against the integrated model.
- **Novelty discipline:** keep research positioning separate from legal novelty or patentability claims. Any stronger novelty claim requires a dedicated systematic academic and patent search.

### 2. Scale / Magnification / Domain topology and no-fold evolution

**Status:** accepted and integrated. The formal model now uses a rectangular Scale-Domain projection, Magnification Bands, Layer Band homogeneity, governed Band compaction, sparse Domain adjacency, and a no-fold invariant. Diffeomorphism is retained only as a continuous analogy; the common model remains discrete. Alloy/SAT materialization remains downstream Engineering Toolbox work.

Follow-up work:

- derive the accepted mathematics into Alloy and define bounded SAT checks without allowing the Alloy representation to redefine proposal semantics;
- assess graph transformation, algebraic graph transformation, order/topology-preserving refinement, sparse multiscale modelling, and related independent work against the stabilized model;
- add topology-specific counterexample suites for imported graph defects, invalid Layer merges, diagonal relations, and Magnification Conflicts.

## Semantic audit corrections

- **ADS/LMC baseline:** rebase the proposal to the accepted ADS/LMC `5.0.0-rc.2` baseline and keep only proposal-specific Example/Illustration specialization locally.
- **Formal-vocabulary cleanup:** localize unnecessary formal predicates and register only genuinely reusable common-model symbols/functions.

## Formal model

- **Inter-Hive and global operational patterns:** formalize operational composition of independently governed Hives now that adjacent-Layer exchange decomposition and terminal Team API handoff semantics are established. Cover Team API-connected Hive topology; source identity and provenance continuity; receiving-Hive context establishment; exchange continuation; boundary failure and Gap semantics; interaction between independently governed Scale systems; Authority and Evidence locality; Contract relationships; global traversal and traceability without semantic collapse; and operational patterns involving multiple cooperating Hives and external Actors. Do not assume one global Engineering State, one global Scale, shared Authority, or global Evidence applicability unless separately established.
- **Information ingress model:** define how information entering Hive is represented, classified, validated, and admitted into Engineering State. The current common model intentionally does not specify conversational or ingress-form taxonomies such as questions, requests, or clarifications. Until an ingress form is explicitly specified, it can appear only as non-binding content inside a labelled Example or Illustration and must not be used as common-model vocabulary, a formal role, or a conformance requirement.
- **Engineering Economy consolidation:** consolidate the economic objective, Resource Cost, Rollback Cost, exploration versus materialization cost, Decision ordering under concurrency, Decision Blast Radius/Decision Extent economics, over-commitment, resource depletion, and staged resource expenditure.
- **Contract realization phases:** formalize progression from lightweight Solution Exploration through planning, Work Product materialization, integration, and where applicable physical-world realization.
- **Traceability dimensions:** refine operational/metadata and materialized engineering dimensions of the common Product graph while preserving one relation algebra.
- **Project Profile language formalization:** formalize Project Profile as a domain-specific language with semantic types, declarations, references, composition, inheritance/override, validation, versioning/migration, compatibility, extension points, and conformance semantics.

## Proposal structure and language

- **Proposal structural compaction:** continue removing duplicated semantics, unnecessary section depth, and implementation-oriented detail after each bounded compaction package is reviewed.
- **Related-work publication integration:** integrate accepted literature organisation into the proposal only after the literature map, source classification, and research-gap wording are reviewed as one bounded package.

## External engineering alignment assessment

- **V-model:** assess the proposal against established V-model concepts without importing V-model semantics into the common model by default.
- **Automotive SPICE:** assess relevant proposal semantics against Automotive SPICE as an external engineering framework.
- **Safety-critical frameworks:** assess relevant proposal semantics against safety-critical engineering frameworks generally, without implying common-model conformance or support before that assessment is performed.
