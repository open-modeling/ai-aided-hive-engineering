# AI Aided Hive Engineering Proposal Backlog

This file records unresolved proposal work outside the canonical proposal body.

Items are not proposal semantics until reviewed and integrated into the proposal through an accepted change.

## Priority work

### 1. Literature organisation and related-work positioning

- **Literature architecture:** reorganize related work into three explicitly separated strata:
  1. conceptual foundations;
  2. engineering-model neighbours;
  3. implementation and comparison technologies.
- **Source classification:** distinguish peer-reviewed research, formal standards/specifications, established engineering methods, recent preprints, industrial research, and implementation/framework documentation. Do not present these source classes as equivalent evidence.
- **Proposal-to-literature traceability:** map each related-work family to the current proposal semantics it actually supports or contrasts. Separate established prior art, implementation precedent, comparison systems, and potentially distinctive combinations.
- **Draft 0.14 migration:** update the Draft 0.14 research recap against the current proposal rather than importing it verbatim. In particular:
  - remove universal `Candidate Delta` from the common-model research-positioning spine;
  - treat typed/schema-constrained LLM output and neuro-symbolic computation as implementation mechanisms unless a stronger common-model dependency is established;
  - treat calibration, selective classification, and conformal prediction as computation-level uncertainty methods rather than prior art for Hive `Confidence`, which is an operational-health indication;
  - preserve the strong historical lineage through shared-state coordination, truth maintenance/design rationale, commitment/governance, assurance/provenance, tradespace engineering, and resource-bounded reasoning.
- **Missing related-work families:** assess and add, where supported:
  - digital thread, MBSE, lifecycle engineering information, and SysML v2;
  - boundary objects and cross-discipline interpretation, especially for Exchange Item and `LocalInterpretation`;
  - artifact-centric lifecycle/process models such as Guard-Stage-Milestone;
  - current assurance and provenance standards, including SACM, W3C PROV, and PPMN;
  - Agent Contracts, Agent Behavioral Contracts, and Proof-Carrying Agent Actions as contemporary comparison work rather than foundational equivalence.
- **Reference-section redesign:** after the literature map is accepted, reorganize proposal references so formal-knowledge references, conceptual prior work, engineering-model neighbours, and current implementation comparisons are not conflated.
- **Research-gap statement:** rewrite the Draft 0.14 gap statement around governed Engineering State evolution over bounded State Projections and existing engineering semantics, without depending on a universal change entity.
- **Novelty discipline:** keep research positioning separate from legal novelty or patentability claims. Any stronger novelty claim requires a dedicated systematic academic and patent search.

### 2. Diffeomorphism / graph-topology operations for Scale, Magnification, and Domain evolution

- **Mathematical-model selection:** determine whether `diffeomorphism` is mathematically justified. The current Product graph is discrete, so explicitly compare graph isomorphism, graph homeomorphism/subdivision equivalence, topology-preserving graph rewrite, order-preserving mappings, and any deliberately defined smooth analogue before adopting terminology.
- **Evolution operator:** define the governed graph operation for establishing an intermediate Magnification and Engineering Layer, including its effect on:
  - Domain-local Layer topology;
  - project-wide Scale intervals and Scale deltas;
  - Magnification traversal;
  - cross-Domain same-Scale alignment;
  - State Projections and historical Engineering States.
- **Domain evolution:** define how one Domain can refine its Layer topology without synthesizing Layers in other Domains, while preserving valid cross-Domain alignment at common Scale positions.
- **Topology invariants:** identify and formalize the invariants that must survive topology evolution, including at minimum:
  - existing Layer identity;
  - relative engineering order;
  - project-wide Scale semantics;
  - no diagonal Domain-and-Scale transition;
  - adjacency-constrained cross-Scale transfer;
  - no vertical semantic compaction;
  - historical state-relative Scale relations and deltas.
- **Mapping across Engineering States:** define how engineering objects and relations before and after a topology refinement are compared without retroactively rewriting historical topology.
- **Traceability delta integration:** align traceability-specific Scale-delta semantics with the resulting topology-evolution model and the common relation algebra.
- **Proof obligations and counterexamples:** define valid and invalid refinement cases, including asymmetric Domain refinement, insertion of multiple intermediate Magnifications, deletion/deprecation scenarios if permitted, and interactions with cross-Domain Exchange Items.
- **Related-work search:** once the model is stable, assess graph transformation systems, algebraic graph transformation, dynamic graph topology, order/topology-preserving refinement, multiscale modelling, and model-transformation research for the closest formal precedents.

## Semantic audit corrections

- **Exchange Item cleanup:** remove stale wording that treats a Human input as becoming an Exchange Item or a Decision as materializing into an Exchange Item. Preserve Exchange Item as a distinct governed transfer node.
- **Mandatory `LocalInterpretation`:** correct remaining propagation formulas that shortcut from Exchange Item directly to Decision or other local semantic use.
- **ADS/LMC baseline:** rebase the proposal to the accepted ADS/LMC `5.0.0-rc.2` baseline and keep only proposal-specific Example/Illustration specialization locally.
- **Example/Illustration cleanup:** convert remaining explicit examples into compliant labelled explanatory blocks and extend validator coverage for equivalent phrasings.
- **Formal-vocabulary cleanup:** localize unnecessary formal predicates and register only genuinely reusable common-model symbols/functions.

## Formal model

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
