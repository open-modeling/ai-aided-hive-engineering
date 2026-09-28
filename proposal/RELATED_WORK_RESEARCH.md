# Literature organisation and related-work map

**Status:** research working material; non-canonical supporting data  
**Proposal baseline:** AI Aided Hive Engineering Proposal 0.40  
**Prepared:** 2026-09-27  
**Primary migration input:** `hive_swarm_research_recap_draft_0.14.md`  
**Purpose:** organize independent/parallel related work and optional engineering instrumentation against the current proposal, without implying ancestry or tool authority.

This file is a governed research map, not a bibliography dump and not a novelty opinion. Similarity does not establish ancestry, adoption, dependency, or semantic equivalence. Hive semantics remain proposal-defined; external work is aligned only when a specific mapping or dependency is explicitly accepted.

## 1. Organisation rules

### 1.1 Separation of related work and toolbox

Research organization uses two independent axes:

1. **Related work and alignment** — independent or parallel research used for comparison, corroboration, challenge, or later explicit alignment.
2. **Engineering toolbox** — optional languages, standards, analyzers, frameworks, and exchange/runtime instrumentation. Toolbox entries do not define Hive semantics.

Related work is not presumed to be Hive ancestry. Toolbox representations are derived from Hive semantics when used, not the reverse.

### 1.2 Source classes

Use the following source classes when integrating citations into the proposal:

| Code | Source class | Use |
|---|---|---|
| `STD` | formal standard / specification | normative external definition or mature reference model |
| `PR` | peer-reviewed research | established or reviewed research result |
| `MONO` | research monograph / thesis | established research lineage or formal development |
| `PRE` | recent preprint | emerging comparison; do not present as mature consensus |
| `TECH` | government / industrial technical publication | current engineering practice or implementation evidence |
| `FW` | framework / product / protocol documentation | implementation comparison only |

Source class does not determine correctness. It controls how strongly the proposal may use the source as evidence.

### 1.3 Relation to Hive

Every related-work source should have one explicit relationship state:

- **Parallel** — addresses a similar concern independently; no lineage or dependency is asserted.
- **Compared** — used to clarify similarities, differences, or boundaries.
- **Aligned** — a defined Hive concept or operation deliberately maps to an external concept or mechanism.
- **Dependent** — a defined Hive semantic or conformance rule requires the external specification or mechanism.

A source remains Parallel or Compared unless alignment or dependency is explicitly accepted. Tool selection alone does not create common-model alignment.

### 1.4 Verification status

- `CURRENT` — source identity/status re-checked during the 2026-09-27 organisation pass.
- `MIGRATED` — carried from the Draft 0.14 research recap and retained as relevant, but exact bibliographic metadata should be checked before final proposal publication.
- `DEFER` — family is relevant, but proposal semantics should stabilize before selecting definitive sources.

## 2. Current proposal-to-literature map

| Current proposal concern | Primary related-work families | Relation | Positioning rule |
|---|---|---|---|
| Shared Engineering State as coordination medium; transient computation | Blackboard systems; Linda/tuple spaces; Coordination Artifacts; Agents & Artifacts; stigmergy | Prior art | Do not claim shared-state or environment-mediated coordination as novel. Hive adds typed Product engineering semantics, legitimacy, evidence, authority, Scale, Contract, and lifecycle governance. |
| Persistent reasoning, justification, competing possibilities | TMS; ATMS; QOC/design rationale | Prior art / neighbour | Use to position retained reasons, alternative contexts, and non-destructive correction. Graph reachability remains distinct from legitimate justification. |
| Distributed coordination without a single persistent manager | Contract Net; Partial Global Planning; SharedPlans; commitments/conventions; electronic institutions | Prior art / contrast | Use for coordination comparison. Hive does not derive semantic authority from an agent role or communication hierarchy. |
| Engineering Universe / Space / State / State Projection; persistent identity and lifecycle information | digital thread / model-based enterprise; SysML v2 and Systems Modeling API | Engineering-model neighbour | Add as a first-class family. Hive is not merely a lifecycle integration layer: it adds state legitimacy, locality, Evidence, authority, Contract, and resource-governance semantics. |
| Product evolution, revision, identity, and provenance | W3C PROV; OMG PPMN; digital-thread work | Engineering-model neighbour | Use for provenance and lifecycle identity precedent. Do not imply that provenance alone establishes semantic validity or authority. |
| Exchange Item receiving-layer decomposition and terminal handoff | boundary objects in multidisciplinary engineering; artifact-mediated coordination | Engineering-model neighbour | Boundary-object research is the closest conceptual neighbour for cross-discipline transfer with local meaning. Hive is stricter about transfer identity, local semantic reconstruction, authority, Scale, and terminal handoff. |
| Contract lifecycle, obligations, prerequisites, Acceptance, and Work Product delivery | commitment-oriented MAS; Guard-Stage-Milestone; assume-guarantee/contract-based design; Agent Contracts | Mixed: prior art / neighbour / contemporary comparison | Split the comparison. No one family should be used as if it were equivalent to the proposal Contract. |
| Evidence, assurance, support, sufficiency, and locality | SACM; GSN/CAE; W3C PROV; PPMN | Engineering-model neighbour | Assurance and provenance are established. Hive-specific comparison should focus on Evidence locality, sufficiency, transfer, and authority separation. |
| Trade Space, trajectories, alternatives, outliers | ATMS; set-based concurrent engineering; MATE | Prior art / neighbour | Do not claim preservation of alternatives or tradespace exploration as individually novel. |
| Resource-rated exploration and survival | metareasoning; anytime computation; Agent Contracts | Prior art / contemporary comparison | Distinguish search/resource allocation from Product truth and Acceptance. |
| `Confidence` | metareasoning and operational resource-control literature | Contrast | Hive `Confidence` is an operational-health indication, not probability, calibration, statistical confidence, Evidence sufficiency, truth, or authority. |
| Computation boundary and structured model outputs | TypeChat; schema-constrained outputs; neuro-symbolic methods | Implementation precedent | Keep outside the common-model semantic definition unless a direct semantic dependency is introduced. |
| Formal relation/statement representation | OpenMath; TPTP; OMDoc; SMT-LIB | Reference model | Retain existing proposal §23 role: design references, not serialization dependencies. |
| Scale / Magnification / Domain evolution | graph transformation; topology/order-preserving refinement; multiscale modelling | `DEFER` | Do not select a definitive ancestry until priority-2 topology semantics are stabilized. “Diffeomorphism” is not assumed. |
| Recursive Y-model / pull-driven information flow | boundary objects; digital-thread information flow; coordination artifacts | Neighbour / contrast | Current sources are partial analogues only. Avoid presenting the Y-model as derived from a single external model. |
| Runtime governance of heterogeneous agents | Agent Behavioral Contracts; Proof-Carrying Agent Actions | Contemporary comparison | Use only as recent comparison work. Hive governs engineering-state evolution, not only runtime action admissibility. |
| Conventional LLM multi-agent orchestration | AutoGen and similar agent frameworks | Contrast | Keep in implementation/comparison stratum. These systems should not dominate the proposal's intellectual positioning. |
| Reasoning-search structures | Tree of Thoughts; Graph of Thoughts | Contrast / implementation | Useful for search/exploration comparison, not for engineering-state semantics. |
| Durable execution and external interoperability | Temporal; LangGraph; A2A | Implementation precedent | Relevant to harness implementation, not evidence of common-model semantics. |

## 3. Migration decisions from Draft 0.14

### 3.1 Retain as principal parallel/comparison families

The following Draft 0.14 families remain useful as parallel or comparative work; no ancestry is implied:

- blackboard and environment-mediated coordination;
- Linda / tuple-space decoupling;
- coordination artifacts and Agents & Artifacts;
- stigmergy;
- TMS / ATMS and design rationale;
- commitments, conventions, institutional MAS, and distributed coordination;
- assurance and provenance;
- set-based/tradespace engineering;
- bounded rationality, metareasoning, and anytime computation.

### 3.2 Reclassify

Keep these outside Hive semantic definition and treat them as implementation/toolbox or computation-level comparison:

- typed/schema-constrained LLM output -> implementation precedent;
- TypeChat / structured-output systems -> implementation precedent;
- neuro-symbolic AI -> possible computation implementation;
- calibration, selective classification, and conformal prediction -> computation-level uncertainty methods, not prior art for Hive `Confidence`;
- LangGraph / Temporal / A2A -> runtime/interoperability implementation precedent;
- AutoGen and other LLM-agent frameworks -> comparison systems.

### 3.3 Remove from the common-model positioning spine

Do not use a universal `Candidate Delta` as the bridge between computation and canonical Engineering State. Proposal 0.40 maps retained computation results into existing engineering semantics rather than introducing one universal engineering change entity.

This does not prohibit an implementation from using an internal patch/delta representation. It means such a representation is not the research-positioning center of the common model.

### 3.4 Add as first-class parallel/comparison families

Add these families because the current proposal developed beyond the 0.14 coverage:

- digital thread / model-based enterprise and persistent lifecycle engineering information;
- boundary objects in multidisciplinary and cyber-physical-system engineering;
- artifact-centric lifecycle models, especially Guard-Stage-Milestone;
- current provenance standards, including OMG PPMN alongside W3C PROV;
- contemporary resource/action governance work such as Agent Contracts, Agent Behavioral Contracts, and Proof-Carrying Agent Actions, while keeping their preprint status explicit.

### 3.5 Defer until topology semantics stabilize

Do not make a strong literature-gap or novelty statement for Scale/Magnification/Domain topology yet. The current proposal still has an open asymmetric-refinement defect, so the exact mathematical object being compared is not stable.

After priority 2 defines the transformation semantics, search and compare at least:

- algebraic graph transformation;
- graph subdivision and homeomorphism equivalence;
- order-preserving graph mappings;
- dynamic graph topology;
- multiscale modelling;
- model-transformation and model-evolution theory.

## 4. Source register

### 4.1 Conceptual comparison sources

| ID | Source | Class | Status | Primary use |
|---|---|---|---|---|
| `CF-01` | H. Penny Nii, *The Blackboard Model of Problem Solving and the Evolution of Blackboard Architectures*, 1986. https://onlinelibrary.wiley.com/doi/abs/10.1609/aimag.v7i2.537 | `PR` | `CURRENT` | Shared state, specialist computation, event/state-driven coordination |
| `CF-02` | David Gelernter, *Generative Communication in Linda*, 1985 | `PR` | `MIGRATED` | Asynchronous shared tuple space; spatial/temporal decoupling |
| `CF-03` | Omicini, Ricci, Viroli, Castelfranchi & Tummolini, *Coordination Artifacts: Environment-Based Coordination for Intelligent Agents*, 2004. https://cris.unibo.it/handle/11585/3962 | `PR` | `MIGRATED` | First-class environment-mediated coordination |
| `CF-04` | Ricci et al., Agents & Artifacts / artifact-based MAS work | `PR` | `MIGRATED` | Separation of agents from persistent artifacts/environment |
| `CF-05` | Francis Heylighen, *Stigmergy as a Universal Coordination Mechanism I/II*, 2016. https://www.sciencedirect.com/science/article/pii/S1389041715000327 | `PR` | `CURRENT` | Indirect asynchronous coordination via persistent traces |
| `CF-06` | Jon Doyle, *A Truth Maintenance System*, 1979. https://doi.org/10.1016/0004-3702(79)90008-0 | `PR` | `CURRENT` | Reasons, revision, dependency tracking, explanations |
| `CF-07` | Johan de Kleer, *An Assumption-Based TMS*, 1986. https://doi.org/10.1016/0004-3702(86)90080-9 | `PR` | `CURRENT` | Multiple assumption contexts and simultaneous alternatives |
| `CF-08` | MacLean, Young, Bellotti & Moran, QOC design-rationale work, 1991 | `PR` | `MIGRATED` | Questions/options/criteria and retained design rationale |
| `CF-09` | Reid G. Smith, *The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver*, 1980. https://ieeexplore.ieee.org/document/1675516 | `PR` | `CURRENT` | Contract metaphor for distributed task allocation |
| `CF-10` | Durfee & Lesser, *Using Partial Global Plans to Coordinate Distributed Problem Solvers*, 1987 | `PR` | `CURRENT` | Partial/global coordination without complete global knowledge |
| `CF-11` | Nick R. Jennings, *Commitments and Conventions: The Foundation of Coordination in Multi-Agent Systems*, 1993. https://doi.org/10.1017/S0269888900000205 | `PR` | `CURRENT` | Commitment and monitoring semantics for coordination |
| `CF-12` | Grosz & Kraus, *Collaborative Plans for Complex Group Action*, 1996. https://doi.org/10.1016/0004-3702(95)00103-4 | `PR` | `CURRENT` | SharedPlans, partial knowledge, collaborative planning |
| `CF-13` | Hübner, Sichman & Boissier, MOISE+ organizational model, 2002. https://moise.sourceforge.net/related-papers.html | `PR` | `CURRENT` | Structural, functional, and deontic organization |
| `CF-14` | Electronic Institutions research; formal operational model summarized in *Communicating Open Systems*, 2012. https://doi.org/10.1016/j.artint.2012.03.004 | `PR` | `CURRENT` | Explicit institutional state and interaction governance |
| `CF-15` | Liker, Sobek, Ward & Cristiano, set-based concurrent engineering, 1996. https://doi.org/10.1109/17.509982 | `PR` | `CURRENT` | Engineering reasoning over sets of alternatives |
| `CF-16` | Ross, Hastings, Warmkessel & Diller, *Multi-Attribute Tradespace Exploration as Front End for Effective Space System Design*, 2004. http://hdl.handle.net/1721.1/84152 | `PR` | `CURRENT` | Systematic tradespace generation and evaluation |
| `CF-17` | Russell & Wefald, metareasoning / bounded rational computation | `MONO` | `MIGRATED` | Deciding how to allocate reasoning resources |
| `CF-18` | Dean & Boddy, anytime computation / anytime algorithms | `PR` | `MIGRATED` | Resource/time-sensitive improvement of computation |

### 4.2 Engineering-model neighbours

| ID | Source | Class | Status | Primary use |
|---|---|---|---|---|
| `EN-01` | NIST, *Research Results and Recommendations for Universally Unique Identifiers in Product Data Standards*, 2024. https://www.nist.gov/publications/research-results-and-recommendations-universally-unique-identifiers-product-data | `TECH` | `CURRENT` | Digital thread, authoritative integrated product-lifecycle information, persistent identity |
| `EN-04` | Boundary objects in complex cyber-physical-system engineering, scoping review, 2026. https://doi.org/10.1016/j.heliyon.2026.e44633 | `PR` | `CURRENT` | Cross-discipline artifacts with locally interpreted meaning |
| `EN-05` | Hull et al., *Business Artifacts with Guard-Stage-Milestone Lifecycles*, 2011. https://research.ibm.com/publications/business-artifacts-with-guard-stage-milestone-lifecycles-managing-artifact-interactions-with-conditions-and-events | `PR` | `CURRENT` | Declarative artifact lifecycle, conditions, events, hierarchy, parallelism |
| `EN-06` | OMG Structured Assurance Case Metamodel (SACM) 2.3 formal; 2.4 beta available September 2026. https://www.omg.org/spec/SACM/ | `STD` | `CURRENT` | Claims, argument/evidence structures, assurance-case interchange |
| `EN-07` | W3C PROV family / PROV-O Recommendation, 2013. https://www.w3.org/TR/prov-o/ | `STD` | `CURRENT` | Provenance entities, activities, agents, derivation, responsibility, interchange |
| `EN-08` | OMG Pedigree and Provenance Model and Notation (PPMN) 1.0, formal September 2026. https://www.omg.org/spec/PPMN/1.0 | `STD` | `CURRENT` | Current formal provenance/pedigree modelling neighbour |
| `EN-09` | Assume-guarantee and contract-based compositional verification research | `PR` | `MIGRATED` | Compositional obligations and guarantees; not equivalent to Product Delivery Contract |
| `EN-10` | AGREE, assume-guarantee reasoning environment. https://github.com/loonwerks/AGREE | `FW` | `MIGRATED` | Engineering implementation/reference for compositional contracts |
| `EN-11` | Goal Structuring Notation Community Standard Version 3, 2021. https://scsc.uk/gsn-standard | `STD` | `CURRENT` | Structured engineering assurance arguments and evidence links |

### 4.3 Engineering toolbox candidates

| ID | Tool/specification | Class | Status | Primary use |
|---|---|---|---|---|
| `TB-01` | OMG SysML 2.0. https://www.omg.org/spec/SysML/2.0 | `STD` | `CURRENT` | Optional systems-model materialization |
| `TB-02` | OMG Systems Modeling API and Services 1.0 | `STD` | `CURRENT` | Optional model access/query/update instrumentation |
| `TB-03` | Alloy. https://alloytools.org/ | `FW` | `CURRENT` | Optional derived finite relational model and bounded SAT analysis |
| `TB-04` | OpenMath / OMDoc / TPTP | `STD` | `CURRENT` | Optional mathematical/formal statement representation or interchange |
| `TB-05` | SMT-LIB and compatible solvers | `STD` | `CURRENT` | Optional solver-oriented formal analysis |
| `TB-06` | SACM / W3C PROV / PPMN representations | `STD` | `CURRENT` | Optional assurance/provenance materialization |

Toolbox items are non-normative unless explicitly selected by a governed project decision. Their representations are downstream materializations of Hive semantics.

### 4.4 Implementation and comparison technologies

| ID | Source | Class | Status | Primary use |
|---|---|---|---|---|
| `IC-01` | Microsoft TypeChat. https://github.com/microsoft/TypeChat | `FW` | `CURRENT` | Schema-guided LLM translation, validation, and repair |
| `IC-02` | OpenAI Structured Outputs. https://developers.openai.com/api/docs/guides/structured-outputs | `FW` | `CURRENT` | Schema-constrained model output; computation-boundary precedent |
| `IC-03` | Agent Contracts, 2026. https://arxiv.org/abs/2601.08815 | `PRE` | `CURRENT` | Resource, temporal, I/O, success-criteria and lifecycle constraints for autonomous agents |
| `IC-04` | Agent Behavioral Contracts, 2026. https://arxiv.org/abs/2602.22302 | `PRE` | `CURRENT` | Runtime preconditions, invariants, governance, and recovery |
| `IC-05` | Proof-Carrying Agent Actions, 2026. https://arxiv.org/abs/2606.04104 | `PRE` | `CURRENT` | Portable action authority/approval/evidence certificates across runtimes |
| `IC-06` | AutoGen / message-based LLM-agent systems | `FW` | `MIGRATED` | Conventional conversational multi-agent comparison |
| `IC-07` | Tree of Thoughts, 2023. https://arxiv.org/abs/2305.10601 | `PR` | `MIGRATED` | Reasoning-search tree comparison |
| `IC-08` | Graph of Thoughts, 2024 | `PR` | `MIGRATED` | Reasoning-search graph comparison |
| `IC-09` | LangGraph durable graph execution / persistence | `FW` | `CURRENT` | Runtime durability and orchestration implementation precedent |
| `IC-10` | Temporal. https://docs.temporal.io/ | `FW` | `CURRENT` | Durable long-running workflow execution |
| `IC-11` | Agent2Agent (A2A) protocol. https://a2a-protocol.org/ | `FW` | `CURRENT` | External agent discovery, delegation, and interoperability; not engineering-state semantics |
| `IC-12` | Current neuro-symbolic agentic AI research | `PRE` | `MIGRATED` | Possible implementation of semantic + formal computation boundary |

## 5. Sources intentionally demoted from direct Hive `Confidence` ancestry

Draft 0.14 included calibration, selective classification, and conformal prediction in the broad map. They remain useful when an individual probabilistic model exposes uncertainty, but they SHOULD NOT be cited as if they define Hive `Confidence`.

Current proposal semantics make `Confidence` an operational exploration-health indication. It does not itself establish:

- correctness;
- probability of truth;
- statistical significance;
- Evidence sufficiency;
- authority;
- Acceptance;
- Product materialization.

If these uncertainty-method sources are retained later, place them under computation implementation rather than common-model related work.

## 6. Candidate current research-gap statement for review

The following is working research text, not proposal text:

> Existing research provides mature mechanisms for shared-state coordination, distributed planning, commitment-based interaction, artifact-centric lifecycles, design rationale, provenance, assurance cases, compositional contracts, tradespace exploration, and resource-bounded computation. These mechanisms are usually studied separately or integrated for narrower purposes. AI Aided Hive Engineering investigates their integration into a Product-centred engineering-state model in which transient computational participants operate on bounded State Projections; retained results acquire meaning through existing governed engineering concepts; and Engineering State evolution remains constrained by explicit relation, Evidence, authority, Scale, Contract, Acceptance, Project Profile, provenance, and resource semantics.

Before this wording is moved into the proposal:

1. resolve the open Scale/Magnification/Domain topology semantics;
2. assess inter-Hive and global operational patterns built on the stabilized Exchange Item decomposition and terminal handoff semantics;
3. verify all source metadata selected for proposal citation;
4. keep the statement as research positioning, not a patentability or legal-novelty conclusion.

## 7. Accepted proposal integration architecture

Proposal integration uses two bounded sections:

1. **§23 Related work and alignment** — parallel/comparison work, with explicit Parallel / Compared / Aligned / Dependent status discipline and no presumed ancestry.
2. **§24 Engineering toolbox** — optional instrumentation such as SysML, Alloy, formal interchange, assurance/provenance representations, and runtime frameworks. Toolbox representations are derived from Hive semantics and do not define them.

A stronger research-gap statement remains deferred until inter-Hive/global operational patterns and the selected literature set are rechecked against the stabilized topology and Exchange Item decomposition semantics.

## 8. Next literature actions

Proposal integration for priority 1 is accepted. Remaining literature work is controlled follow-up:

1. verify exact bibliographic metadata for migrated sources before publication-grade release;
2. establish explicit alignment only when a Hive mechanism actually adopts or maps to external work;
3. run the dedicated Scale/Magnification/Domain topology literature search after priority-2 semantics stabilize;
4. revisit the combination-level research-gap statement after the topology and Exchange Item semantics are stable.
