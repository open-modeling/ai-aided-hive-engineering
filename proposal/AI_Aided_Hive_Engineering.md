---
title: "AI Aided Hive Engineering Proposal"
subtitle: "Formal Proposal - Draft 0.40"
author: "Julia (Ilya) Lebedev <ilya@lebedev.net>"
copyright: "© 2026 Julia (Ilya) Lebedev"
date: "24 September 2026"
---

[[STATIC_TOC]]

# Part I - Proposal in plain terms

## 1. Abstract and intent

This proposal originates from a practical problem observed in AI-assisted engineering: a substantial part of computation can be spent coordinating agents, replaying context, polling execution, and maintaining an artificial organization around the engineering work. These problems largely originate from applying human-like organizational, reasoning, and consensus models directly to AI execution.

Orchestration frameworks and role models shaped like real organizations inherit many of the same deficiencies: locked waits, polling, administrative and coordination work, and context pollution by intermediate thinking. AI makes these losses directly visible because they immediately appear as computational and execution cost.

This proposal does not aim to build a better virtual organization or incrementally improve orchestration processes. It proposes a different coordination and synchronization model whose purpose is to reduce overall engineering cost while preserving engineering rigor.

**Hive** is a form of distributed intelligence in which orchestration is performed through coordinated multi-agent operations rather than through a persistent human-like organization. To an observer, it acts as one coherent engineering intelligence while retaining distributed specialization internally.

Engineering meaning is held in explicit shared state rather than in conversations or private agent memory. At its foundation, this state is represented as a multidimensional temporal graph that preserves project entities, evidence, relationships, and evolution without requiring the whole history to participate in every task.

Hive engineering is intentionally concurrent and non-deterministic. Starting from the same initial engineering basis, separate valid Hive executions can explore different Solution Space regions, commit Decisions in different orders, materialize different Work Products, and converge to different Product realizations. The governance model establishes engineering validity, traceability, authority, convergence, and resource control. It does not define Product development as deterministic reproduction of one trajectory or one Product realization.

The intended result is faster and more stable engineering delivery through lower coordination overhead, less context pollution, controlled rework and exploration, preserved engineering evidence, and economically justified use of computational and engineering resources. The proposal complements established engineering lifecycles, processes, and standards rather than replacing them.

## 2. Why a Hive/Swarm architecture

### 2.1 Three orchestration paradigms

| Property | Organization-mimetic agent harness | Reasoning-mimetic harness | Hive/Swarm proposal |
|---|---|---|---|
| Primary abstraction | Role-bearing agents, managers, teams, tasks | Reasoning steps, thought chains, trees, graphs, planner-reflector loops | Hive execution model, canonical semantic state, task-assigned Swarms, Clusters, Decisions, trajectories |
| Persistent identity | Common | Often one reasoning process or persistent planner | Not required for computation; provenance is retained instead |
| Coordination | Delegation, handoffs, messages, shared conversation | Sequential or branching thought generation and evaluation | Typed relations, bounded state projections, candidate semantic deltas |
| State carrier | Agent/session memory, task state, conversation | Reasoning trace and search structure | Addressable Proposition state and materialized Engineering Objects |
| Specialized computation | Specialist agents or tools | Specialized reasoning stages | Task-assigned Swarms of cheap specialized participants, solvers, simulations, tools, and humans |
| Authority | Often coupled to agent role or workflow | Usually implicit in reasoning control | Explicit in Contract, Decision scope, relation semantics, and Project Profile |
| Truth | Often selected/summarized by orchestrator | Often selected by self-evaluation or search score | Never owned by an agent; accepted through formal validators, evidence, and obligations |
| Search | Task/workflow execution | Deliberate reasoning-space search | Trade-space exploration with persistent outcomes and resource-rated active trajectories |
| Communication cost risk | Repeated delegation, messaging, status polling, history replay | Repeated long reasoning and branch evaluation | Small bounded State Projections and explicit engineering results by default |
| Failure handling | Retry, handoff, escalation | Backtrack, reflect, branch | Preserve outcome, update trajectory rating, post-mortem, reallocate resources |
| Engineering traceability | Added by application | Usually outside the reasoning method | Native part of the state and relation algebra |
| Cross-layer authority | Workflow-dependent | Usually not modeled | Explicitly blocked unless materialized and locally reconciled |

::: {custom-style="Illustration"}
**Illustration - established patterns.** Current agent frameworks commonly expose manager/worker, agents-as-tools, handoff, crew, task, process, memory, and conversation concepts. OpenAI Agents SDK and CrewAI are examples of this family. Tree of Thoughts and Graph of Thoughts are examples of deliberate reasoning-space search. These examples illustrate the comparison categories; they do not define proposal conformance.
:::

### 2.2 Project evidence for communication cost

The project resource analysis is supporting evidence for the architecture choice, not proof of a universal law. Direct polling/status activity accounted for 19.9% of measured input. Supporting orchestration accounted for another 10.5%. Root/orchestrator sessions carried 97.9% of measured input while sub-agents carried 2.1%.

| Observation | Measured value | Design implication |
|---|---:|---|
| Direct polling/status waste | 19.9% of measured input | Do not use repeated wait/list/status interactions as a core coordination method |
| `wait_agent` alone | 15.7% of measured input | Prefer event/state change and semantic completion conditions |
| Supporting orchestration | 10.5% of measured input | Minimize messages, follow-up task restatement, spawn overhead, and interruption |
| Root/orchestrator share | 97.9% of measured input | Reduce central context replay and long orchestration sessions |
| Sub-agent share | 2.1% of measured input | Cheap specialists are not the main measured cost; coordination/context is |

The measured archive does not contain exact model identifiers for all sub-agents and its phase timing includes explicit proxy values. The proposal therefore uses these data as a decision input, not as a universal performance benchmark.

## 3. Why this proposal is needed and what it contains

The proposal addresses a coordination problem rather than a lack of AI capability. Modern models can already perform substantial analysis, design, implementation, and validation work. The remaining problem is how to coordinate that work without reproducing the cost, loss of information, loss of decision reasoning, loss of decision history and participants, and overall instability of a large human organization.

### 3.1 Operational reasons

- Coordination should not become a major part of execution. Waiting, polling, task tracking, responsibility assignment and reassignment, status reporting, synchronization, repeated handoffs, and duplicated context consume capacity without directly improving the Product.
- Intermediate reasoning should not continuously pollute the working context. Only information that remains relevant to engineering state should survive beyond the computation that produced it.
- Independent work should proceed in parallel and without unnecessary blocking.
- Decisions should propagate through changed engineering information and affected Product elements, not through organizational waiting chains.
- Bottom-up findings should be handled first at the nearest affected level. Higher levels should remain undisturbed when the change can be resolved locally.
- This allows unaffected work to continue in parallel and prevents local changes from triggering unnecessary synchronization or replanning across the Hive.
- Independent specialists should be able to contribute without requiring a persistent organizational hierarchy around every task.
- The execution model should preserve continuity when participants, tools, models, or external services change.
- Human participation should remain possible without making routine engineering dependent on continuous human approval.

### 3.2 Engineering reasons

- Engineering decisions should remain traceable to the information, evidence, constraints, alternatives, and authority that justified them.
- Incomplete knowledge should remain visible. A known gap is safer than an apparently complete but unjustified engineering chain.
- Failure should be exposed early. Fast failure followed by reassessment is healthier than forced continuation after an engineering path has become unsound, because forced execution accumulates rework, invalid evidence, and downstream cost.
- Engineering information exists at different levels of Product decomposition and abstraction. Their relations must remain explicit without allowing detailed local reasoning to acquire unintended authority elsewhere.
- Alternatives, rejected directions, outliers, and the reasoning behind past Decisions are valuable engineering knowledge. Good projects already record part of this information, for example through ADRs in software engineering, but those records often become large, weakly structured collections with poor evolution, visibility, and traceability to the Product elements they affected.
- Decision history should therefore remain connected to the relevant Product state, evidence, alternatives, and later changes instead of becoming detached documentation.
- The model should support software, physical products, mixed systems, and established engineering lifecycles without assuming one artifact taxonomy or organizational structure.

### 3.3 Economic reasons

- Engineering cost includes more than model execution. It includes human attention, computation, elapsed time, coordination, rework, physical work, external services, supplier effort, and the cost of changing already-developed results.
- Cheap exploration is valuable before expensive engineering work is committed. Exploration itself becomes waste when additional investigation has little expected value compared with the resources available and the value of the Decision being improved.
- Fast recognition of an invalid direction usually costs less than preserving activity merely because resources have already been invested in it.
- Local improvement should be evaluated against its effect on the wider Product. A technically better local solution can be economically worse when it creates extensive rework elsewhere.
- Unnecessary upward propagation of change creates avoidable Decision rework, analysis, coordination, Work Product rework, and repeated validation.
- When a committed Decision has to be cancelled, Rollback preserves compatible parallel engineering and removes the same-Layer materialized continuation required for complete cancellation. Cross-Layer consequences remain governed by ordinary adjacent-Layer engineering.
- In many current AI harnesses, a human directive becomes effectively undisputable once entered into execution. A seemingly simple intervention can therefore trigger major downstream rework without systematic assessment of its effect on the existing solution space.
- Human intervention should instead be assessed against current alternatives, constraints, evidence, affected Product elements, and expected cost before commitment wherever the applicable authority allows that assessment.
- Trade-space analysis is a basis for informed and data-driven decision making. It preserves viable alternatives and their consequences so that human and autonomous Decisions do not lose the information generated during exploration.
- The objective is reliable Product delivery within explicitly available project resources, not unlimited search for a theoretical global optimum.

### 3.4 Logical reasons

Engineering information cannot be treated as true merely because it is connected, repeated, agreed by several participants, produced by a capable model, or prescribed by a human.

The proposal therefore needs a consistent foundation for identity, relations, evidence, time, scope, authority, uncertainty, change, and the boundaries between different parts of the Product.

This foundation separates engineering meaning from the temporary computation used to discover it and makes both the current engineering state and the reasoning that led to it inspectable after participants or reasoning sessions disappear.

### 3.5 What the proposal contains

The proposal is organized around five complementary concerns:

- a **language and terminology foundation** that keeps engineering concepts stable and unambiguous;
- a **mathematical foundation** for entities, relations, graph structure, temporal evolution, reasoning, and Product decomposition;
- an **operational and data model** that preserves engineering state independently from individual agents, tools, and conversations;
- an **engineering governance model** for Decisions, trade-space exploration, evidence, Contracts, validation, traceability, Product delivery, human intervention, resource use, and supporting engineering processes;
- a **Project Profile and conformance model** that keeps domain-, lifecycle-, organization-, and standard-specific choices outside the universal foundation.

The remaining parts of the proposal formalize these concerns while leaving implementation technology and project-specific engineering practice open.

# Part II - Language and Meaning Profile

## 4. Language and Meaning Profile

### 4.1 Governing baseline

This proposal applies the relevant governance provisions of **AI DevMode Standards (ADS) 5.0.0-rc.1** and **Part I - Language & Meaning Core (LMC)**.

The applicable Language & Meaning Core provides the common rules for:

- external language standards;
- normative meaning;
- terminology and meaning control;
- information construction;
- protected-source handling;
- Language & Meaning conformance.

This section provides the proposal-specific language and meaning profile required by the formal Hive engineering model.

#### 4.1.1 External language standards

External language and information standards apply through the project profile established by LMC-01.

This includes BCP 14 normative keyword semantics, ASD-STE100 Issue 9 controlled-English rules, and the complementary terminology, plain-language, drafting, information-development, and conformity guidance identified by LMC-01.

Each external standard remains authoritative for its own content.

#### 4.1.2 Terminology and meaning

Common project terminology and meaning follow LMC-02.

Common terms retain the meanings established by the applicable common terminology source.

Proposal-specific terminology extends that vocabulary with concepts required by the Hive engineering model.

The proposal dictionary in §4.4 defines proposal-specific concepts and the reusable mathematical symbols of the common model.

Changes to common terminology follow the governance of the applicable common terminology source.

#### 4.1.3 Language and Meaning conformance

A Language & Meaning conformance claim for this proposal follows LMC-04.

The conformance record identifies:

- proposal revision;
- applicable LMC revision;
- designated checker or review authority;
- review method;
- evidence locations;
- terminology sources;
- unresolved deviations or blockers;
- final result.

An ASD-STE100 conformance claim requires evidence from the project-designated checker or review process.

Language & Meaning conformance evaluates the proposal as technical information.

Engineering-model Conformance Evaluation in §4.3.3 evaluates an implementation, engineering state, process configuration, or another subject against the engineering model and applicable Project Profile.

### 4.2 Proposal-specific applicability

The proposal applies the content classification established by LMC-03.

Project-authored prose follows the applicable Language & Meaning Core.

Protected and imported content follows the applicable source-protection rules.

Mathematical notation, formal expressions, identifiers, and machine-readable syntax follow the semantics of their defining formalism.

Each region of mixed content follows the rule applicable to its information type.

The following clauses define proposal-specific treatment required by the formal engineering model.

#### 4.2.1 Illustrations

Illustrations provide explanation, demonstration, and context for proposal concepts.

An Illustration can contain:

- representative engineering situations;
- examples;
- example values;
- possible implementations;
- explanatory scenarios.

Definitions, axioms, relation semantics, Project Profile defaults, Contract obligations, conformance criteria, and other formal properties are established by their designated proposal clauses.

Illustrations are visually separated from formal proposal content and explicitly identified as **Illustration**.

#### 4.2.2 Normative provisions

Project-authored normative prose uses BCP 14 with the semantics established by LMC-01.

Uppercase `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` identify normative requirement levels where those distinctions are material to interpretation or conformance.

Definitions, mathematical statements, axioms, assumptions, lemmas, theorems, derived properties, conjectures, and explanatory architecture carry meaning through their declared formal role.

A separate normative provision uses the applicable BCP 14 keyword where requirement level is material.

Quoted and imported normative material retains the normative semantics of its source.

#### 4.2.3 Mathematical content

Mathematical content expresses the formal structure of the proposal through definitions, relations, predicates, sets, functions, equations, invariants, and derived properties.

Mathematical statements use consistent notation and preserve the distinction between:

- **Definition** - introduces the meaning of a mathematical object or term;
- **Axiom** - establishes a foundational proposition accepted by the model;
- **Assumption** - states a condition under which a result applies;
- **Lemma** - establishes an intermediate result used by another formal statement;
- **Theorem or Derived Property** - follows from definitions, axioms, assumptions, or previously established results;
- **Conjecture** - states a proposition whose establishment remains open.

Engineering semantics are assigned to structural mathematical operations through explicit definitions.

Mathematical notation in the Markdown master uses a representation that preserves clean source evolution and supports accurate conversion into native mathematical notation in derived Word and PDF representations.

**Mathematical expression style.** Mathematics is the primary formal language of this proposal. Sets, relations, mappings, order, algebra, topology, and temporal qualification are preferred when they express the engineering concept directly. Computer-science notation is used where it contributes engineering meaning to computation or execution boundaries. Ordinary mathematical structure remains preferred where it already expresses the concept.

The proposal distinguishes:

- mathematical structure;
- engineering semantics assigned to that structure;
- implementation mechanisms.

An implementation can realize the mathematical model through software structures while the common formal model remains expressed through its defined mathematical and engineering semantics.

##### Formal identifier control

Reusable mathematical symbols are defined in the §4.4 mathematical-symbol dictionary.

Reusable common-model relations, predicates, and functions are defined in the Formal Vocabulary Registry in §21.

A section can introduce a local variable or local helper expression when its meaning is declared at the point of use.

A local identifier remains scoped to that formal construction.

Project Profile-defined operators are identified explicitly as Project Profile extensions.

Each reusable identifier carries one mathematical type and one semantic meaning throughout the common model.

### 4.3 Proposal-specific interpretation

The following clauses define proposal-specific concepts required by the formal Hive engineering model.

#### 4.3.1 Dimension-bounded set terminology

The proposal uses **Universe**, **Space**, **State**, and **State Projection** as successively bounded concepts.

A **Universe** establishes the theoretical domain before Product-, project-, material-, contextual-, or temporal bounds are applied.

A **Space** applies material and contextual bounds to a Universe.

A **State** applies a temporal bound within a Space.

A **State Projection** applies an operation-specific information bound to one State.

Conceptually:

$$Universe
\supseteq
Space
\supseteq
State
\supseteq
StateProjection.$$

`Unbounded` in this terminology refers to unapplied bounding dimensions.

Mathematical cardinality is independent of this usage.

The dimensions have distinct origins:

- Universe - theoretical domain;
- Space - material and contextual bounds;
- State - observation time;
- State Projection - purpose of one bounded operation.

#### 4.3.2 Project Profile

The Project Profile supplies formal project-specific values where the common proposal leaves parameters open.

A Project Profile can define:

- project-specific terminology;
- relation vocabularies;
- validation rules;
- authority structures;
- engineering topology;
- resource models;
- lifecycle predicates;
- independence requirements;
- construction strategies;
- other parameters identified by the proposal.

Project Profile content specializes the common model within its defined project context.

#### 4.3.3 Conformance Evaluation

Conformance Evaluation determines whether an implementation, engineering state, process configuration, or other evaluated subject satisfies:

- the common requirements of this proposal; and
- the applicable Project Profile.

Conformance Evaluation applies the engineering rules established by the proposal and the applicable Project Profile to the evaluated subject.

### 4.4 Dictionary

The dictionary is intentionally compact. A term definition may reference another defined term rather than repeating its semantics. Project-specific specializations belong in the Project Profile.

| Term | Definition |
|---|---|
| **Acceptance** | Contract-governed process that assesses Contract fulfilment and the resulting Work Product against the applicable Acceptance rules and records the resulting disposition. |
| **Check Cascade** | Cost-ordered sequence of applicable checks in which a more expensive check is entered only after all applicable cheaper checks have passed. |
| **Assignment** | Contract relation that identifies the Actor responsible for execution of that Contract. A valid Assignment establishes that Actor as the Executor in the Contract context. Assignment is part of the Contract state, not a separate Engineering Object. |
| **Authority** | Explicit, externally established permission for an Actor to perform a governed operation within a defined Scope, time, and context. Authority is operation-specific and does not imply correctness, Evidence sufficiency, or engineering feasibility. |
| **Actor** | Human, Hive, external organization, or other authority-capable participant. Computational micro-agents are not Actors unless a Project Profile grants that role. |
| **Agent** | Computational participant that performs a bounded operation. Agent identity does not create semantic authority. |
| **Baseline** | Configuration Management reference state created only when the applicable Configuration Management process defines it. |
| **Binding** | Scoped and time-qualified prescriptive force of an obligatory Decision. Binding applies to Decisions, not Work Products or Exchange Items. |
| **Cluster** | Set of sufficiently independent contributions within a Swarm that support one Decision for one task/problem statement. A Decision can then preserve or direct a trajectory. |
| **Confidence** | Time-varying operational health indicator produced by the Hive for an active task, exploration, trajectory, or scoped Decision context. It summarizes the Hive's current weighted assessment of whether the ongoing exploration/development process is trending toward a useful outcome under the available information and Resource Envelope. Confidence is not truth, probability, precision, Evidence, authority, Decision, Acceptance, Back-off, or a property of a Work Product. |
| **Conformance Evaluation** | Formal check of implementation/state against this model plus the applicable Project Profile. |
| **Contract** | Durable governed record that defines a Product target, required Work Product, Issuer, Assignment, Resource Envelope, execution topology, Acceptance rules, enforcement, and the information required to preserve execution and fulfilment history. |
| **Decision** | Rationale-bearing Proposition node kind that preserves or directs a possible course of exploration or behavior. In lifecycle-specific text, the same Decision is stated as **Decision Candidate** while commitment remains open and as **Decision** after commitment. Both terms refer to the same Proposition node identity. |
| **Decision Blast Radius** | Calculated propagation reach of a **Decision Candidate** over the currently available engineering state before commitment. Decision Blast Radius supports feasibility and engineering-economy assessment and does not itself change Engineering State. |
| **Decision Extent** | Propagation reach already materialized by a **Decision** in the Engineering State at a stated time. |
| **Deprecation** | Ordinary forward engineering evolution in which later engineering supersedes, replaces, or makes earlier materialized engineering obsolete while continuing Product development from that history. |
| **Delusive Traceability** | Apparently complete traceability created through semantically invalid, fabricated, or unjustified relations. |
| **Domain Nature** | Classification of an Engineering Domain as **Prescriptive** or **Engineered**. A Prescriptive Domain develops or interprets conditions imposed on Product engineering. An Engineered Domain develops Product or project solutions.<br><br>**Examples:**<br>Prescriptive — legal, regulatory, certification, natural-law.<br>Engineered — customer development, UX, Product engineering, ordering, architecture, implementation, manufacturing. |
| **Engineering Domain** | Project-defined engineering concern whose Decisions, Contracts, Work Products, Evidence, and other engineering information evolve through Domain-local Engineering Layers on the common Scale. |
| **Engineering Layer** | Domain-local engineering context established for engineering information at one Magnification. Engineering Layers occupy relative positions on the common Scale. Additional Layers can be established when engineering information requires an intermediate Magnification. An Engineering Layer can contain an execution sub-scale without creating another Engineering Layer. |
| **Engineering Universe** | Theoretical domain of engineering elements, relations, configurations, and outcomes expressible by the common model before Product-, project-, material-, contextual-, or temporal bounds are applied. |
| **Engineering Space** | Materially and contextually bounded subset of the Engineering Universe applicable to one Product or engineering context. Its bounds can include Product scope, engineering domains, Project Profile, physical constraints, available capability, enabling technology, applicable external constraints, and other non-temporal engineering dimensions. |
| **Engineering State** | Temporally bounded subset of an Engineering Space containing the governed engineering elements and relations addressable at one observation point together with their applicable identity, revision, Scope, lifecycle or status, provenance, temporal qualification, and applicability. |
| **Engineering Object** | Materialized project entity with tool, repository, physical, or document identity. It can carry or materialize one or more Propositions. |
| **Evidence** | Recorded information used by a defined validator or argument to support a Proposition. Evidence is scope- and role-specific. |
| **Exchange Item** | Addressable Proposition node that represents a governed engineering transfer and preserves that transfer for traversal and traceability. An Informational Exchange Item delivers a boundary-relative projection of a Decision or Evidence Proposition. An Objective Exchange Item delivers a Work Product. The Exchange Item retains identity distinct from its transferred content. |
| **Executor** | Actor responsible for fulfilment of an assigned Contract, including delivery of the required Work Product or explicit reporting that fulfilment cannot be completed. A Human can be an Executor when assigned responsibility for a Contract result. |
| **Exploration** | Bounded computational attempt to extend, test, compare, or refine the current Solution Space. |
| **Extremum Exploration** | Exploration intended to discover a different local extremum or challenge whether a materially better region exists outside the current search neighborhood. |
| **Feasible Region** | Subset of a Solution Space satisfying the constraints applicable under a stated Engineering State and engineering context. |
| **Future Action** | Explicit deferred engineering activity that resolves or closes a Known Gap after its required prerequisites become available. It identifies the responsible party, trigger, expected result, required artifacts, execution method or reference, readiness conditions, and completion conditions. |
| **Gap** | Explicitly known missing relation, evidence, content, capability, or result required for a stated purpose. |
| **Hive** | Complete execution model that maintains engineering state, governance, Contracts, resources, and execution topology and commands Swarms assigned to bounded tasks. |
| **Hive Mind** | Distributed/federated intelligence paradigm in which the Hive operates as one coherent intelligence for an external observer while participating actors retain individual traits, properties, and behaviours. |
| **Human Arbitrary Input (HAI)** | Exogenous human input that can arrive at any time and can preempt the current continuation without erasing history. |
| **Human Prescriptive Choice (HPC)** | Human choice required when an obligatory Decision cannot be committed by the Hive. |
| **Human Voluntary Choice (HVC)** | Optional human choice made while autonomous Hive continuation remains possible. |
| **Human Work Product (HWP)** | Work Product supplied by a Human or human organization. Human origin does not bypass validation. |
| **High-profile Assessment** | Open semantic or logical assessment used only for properties that cannot yet be established adequately by cheaper checks. |
| **Instrumental Check** | Deterministic or mechanically executable check over explicit engineering data, structure, or rules. |
| **Integrator** | Executor of an integration Contract that constructs a coherent same-scale Work Product from applicable partial Work Products and evidence. |
| **Issuer** | Actor that, under applicable authority, creates or revises a Contract and assigns its execution. Originating an input, request, Choice, or human directive does not by itself make an Actor an Issuer. |
| **Justification** | Valid relation/evidence structure that satisfies the applicable validators for using a Proposition as a decision, trace, or commitment basis. |
| **Known Gap** | Gap whose existence and scope are known and recorded. |
| **Local Optimum / Local Extremum** | Best/extreme candidate relative to a declared neighborhood or currently explored region, not the entire theoretical Solution Space. |
| **Low-profile Assessment** | Bounded, semi-instrumented semantic assessment using explicit checklists, questions, local rules, or similar structures. |
| **Materialized Product State** | Product content materially realized at a stated observation point. |
| **Magnification** | Operator on Scale used to locate engineering information by relative engineering order and to perform bounded traversal toward applicable coarser or finer engineering information. Magnification uses the Scale relations established among Engineering Layers and does not create missing engineering content. |
| **Micro-agent** | Short-lived, specialized, low-Resource-Cost Agent used for one narrow exploration or validation operation. |
| **Negotiability** | Classification of a Y Branch as **Negotiable** or **Fixed** for one Product engineering reconciliation. Information from a Prescriptive Domain is Fixed. Information from an Engineered Domain is normally Negotiable and can be Fixed when applicable engineering conditions make source change economically ineffective for the current reconciliation. Both classifications support governed feedback. |
| **Obligation** | Responsibility of an Executor for the complete result of an assigned Contract. The Executor delivers the required result or explicitly reports inability to fulfil the Contract to the authoritative party or parties. Obligation is Contract semantics, not necessarily a separate stored object. |
| **Outlier** | Discovered outcome or trajectory with low current cluster support. It remains recorded even when active allocation is zero. |
| **Overthinking** | Reasoning expenditure whose expected information or decision value is lower than its Resource Cost, or reasoning applied to a result that deterministic state/algebra can establish directly. |
| **Product** | Coherent engineered subject and primary top-level scope/intent of Hive operation. The Product identifies what the Hive is working to establish, evolve, analyze, verify, realize, or deliver and bounds the corresponding engineering context. Actual Product development is bounded by available Hive capabilities, enabling technology, authority, and resources. |
| **Product Delivery** | Specialization of Contract fulfilment in which fulfilment requires satisfaction of an explicit Product target state in addition to Acceptance of the required Work Product. |
| **Product Evolution History** | Temporally ordered governed history of Product engineering, including Decisions, Evidence, Contracts, Work Products, exploration outcomes, supersession, deprecation, Rollback, Gaps, and other retained engineering information. |
| **Project Profile** | Formal project input that defines open parameters such as relation vocabulary, scale topology, Work Product schemas, validators, authority, resource models, lifecycle predicates, and validation independence. |
| **Proposition** | Core addressable semantic element of the solution model. It is not an Engineering Object by default. It can later be materialized, carried, or realized by Engineering Objects. |
| **Relation** | Typed semantic or structural association between addressable elements, qualified by scope, revision, time, and Project Profile semantics. |
| **Reshuffling** | Primarily vertical Decision rework caused when an Engineering Layer committed downstream constraints without sufficient exploration to support delivery through affected downstream layers. A downstream finding becomes Reshuffling when it cannot be absorbed locally and requires Decision change at an adjacent or higher Engineering Layer. |
| **Resource Cost** | Multi-dimensional consumption caused by an operation, exploration, Contract, trajectory, or change. |
| **Resource Envelope** | Declared availability/limits for relevant resource dimensions such as context, model calls, compute, wall time, money, human effort, energy, equipment, and external capacity. It is not a universal scalar. |
| **Rollback** | Evidence-supported engineering activity that completely cancels one previously committed Decision on one Engineering Layer. Rollback removes from current materialization the same-Layer engineering consequences that cannot remain valid after cancellation of that Decision, while retaining compatible parallel engineering and historical addressability. |
| **Rollback Closure** | Least same-Layer set of Decisions, Contracts, and Work Products that have to be cancelled or rematerialized together for a Rollback to completely cancel its target Decision while leaving a valid same-Layer remainder. |
| **Rollback Contract** | Contract governing one Rollback. It identifies the committed Decision being cancelled, applicable Evidence, the Rollback Closure, the expected resulting state, required Work Product, and Acceptance conditions. |
| **Rollback Cost** | Resource Cost attributable to exploration, realization, verification, integration consequences, or other engineering work caused by a Rollback. Its complete economy semantics are deferred to the Engineering Economy backlog package. |
| **Scale of measurement** | Established measurement-theory classification defining which comparisons and algebraic operations are meaningful for a measured property. Common scales of measurement are nominal, ordinal, interval, and ratio. The proposal uses these established meanings and does not redefine them. |
| **Scale** | Project-wide interval Scale that establishes relative engineering order and interval distance among Engineering Layers according to Magnification. Scale has no mandatory absolute numerical coordinates. Adjacent Engineering Layers are separated by one applicable Scale interval; additional intermediate Layers can be inserted while preserving adjacent-interval semantics. |
| **Solution Universe** | Theoretical domain of possible solution configurations for an applicable class of engineering problem before the material and contextual bounds of a particular Product or problem are applied. |
| **Solution Space** | Materially and contextually bounded subset of a Solution Universe for a stated Product or engineering problem. Its bounds can include Product intent, Product boundary, physical constraints, available capability, enabling technology, and applicable external constraints. |
| **State Projection** | Purpose-bounded subset of one Engineering State selected for a stated computation, query, analysis, Contract, Decision, traversal, or other engineering operation while preserving the applicable qualifications of the selected engineering information. |
| **Swarm** | Population of specialized computational participants assigned by the Hive to one bounded task. Swarm contributions can form Clusters supporting Decisions. |
| **Team API** | Governed cross-Actor or cross-Hive communication boundary used to coordinate Product evolution and Contract execution through applicable Work Products, Exchange Items, and communication Propositions. |
| **Trade Space** | Project-visible subset of a Solution Space represented for comparison or exploration for one bounded engineering problem at a stated observation point. |
| **Trajectory** | Temporally ordered path of exploration outcomes and Decisions through a Trade Space. |
| **UNKNOWN** | Required information whose value, validity, applicability, or result has not been established. |
| **Waste** | Resource consumption that creates neither required governance/validation effect nor reusable progress, evidence, knowledge, or Product value for the active objective. |
| **Work Product** | Complete required Contract result prepared under a defined schema and Acceptance rule. A Work Product can be an input to another Contract. |
| **Y Branch** | Consumer-established information flow from an Engineering Domain for a particular Product engineering need. The flow participates in a Y-model reconciliation on the Fixed or Negotiable branch according to Domain Nature and applicable engineering conditions. |

#### Mathematical symbols

Mathematical symbols are part of the proposal dictionary. This table is authoritative for reusable mathematical symbols in the common model. Section-local variables are declared where they are introduced.

| Symbol | Meaning |
|---|---|
| $t$ | Time or temporally ordered observation point. |
| $t_1,t_2$ | Two ordered observation points. |
| $H$ | Hive. |
| $P$ | One Product. |
| $p$ | One Proposition. |
| $\mathbb P$ | Set of Propositions. |
| $\mathbb O$ | Set of Engineering Objects. |
| $\mathbb C$ | Set of Contracts. |
| $PP$ | Applicable Project Profile. |
| $PP^m$ | Revision $m$ of a Project Profile. |
| $\beta$ | Engineering branch or historical lineage identifier. |
| $X^\beta_t$ | Engineering State on branch $\beta$ at observation point $t$. |
| $\rho_{(\beta,t)\rightarrow(\beta',t')}$ | Partial revision mapping from $X^\beta_t$ to $X^{\beta'}_{t'}$. |
| $D$ | Set of Decisions in the stated context; lifecycle qualification is stated where material. |
| $D^*$ | Same bounded Decision set compared across trajectories. |
| $d$ | One Decision node. Where pre-commit lifecycle qualification is material, the same node is written $d^{candidate}$. |
| $d_0$ | Committed Decision targeted by a Rollback. |
| $D_L$ | Decisions belonging to Engineering Layer $L$. |
| $C$ | Contract. |
| $C^k$ | Revision $k$ of Contract $C$. |
| $C_I$ | Integration Contract. |
| $C_R$ | Rollback Contract. |
| $C_0$ | Contract context associated with the initial Rollback target. |
| $C_L$ | Contracts belonging to Engineering Layer $L$. |
| $W$ | Set of Work Products in the stated context. |
| $w$ | One Work Product. |
| $w^r$ | Revision $r$ of Work Product $w$. |
| $w_0$ | Initial materialized Work Product associated with Rollback target $d_0$. |
| $w_I$ | Integrated Work Product. |
| $W_L$ | Work Products belonging to Engineering Layer $L$. |
| $W_I$ | Required materialized input Work Product set for Integration Contract $C_I$. |
| $W^{ready}_{C_I}$ | Work Products ready for integration under $C_I$. |
| $\mathbf W_a,\mathbf W_b$ | Ordered materialized Work Product sequences of compared trajectories. |
| $L$ | Engineering Layer. |
| $L_R$ | Engineering Layer of Rollback Contract $C_R$. |
| $X_t$ | Engineering State at observation point $t$. |
| $X_0$ | Common initial Engineering State used when comparing trajectories. |
| $K_t$ | Product Evolution History accumulated by observation point $t$. |
| $P^{mat}_t$ | Materialized Product State at observation point $t$. |
| $P^{mat}_a,P^{mat}_b$ | Materialized Product States reached by compared trajectories. |
| $R_t(C_R)$ | Subset of $P^{mat}_t$ removed from active materialization by successful Rollback Contract $C_R$. |
| $\mathcal U_E$ | Engineering Universe. |
| $\mathcal E_\kappa$ | Engineering Space applicable to engineering context $\kappa$. |
| $\Omega$ | Solution Universe. |
| $\mathcal S_\kappa$ | Solution Space applicable to engineering context $\kappa$. |
| $\mathcal F(X_t)$ | Feasible Region under Engineering State $X_t$. |
| $q$ | Bounded engineering problem or query. |
| $\Pi_q(X_t)$ | State Projection of $X_t$ selected for problem $q$. |
| $T(q,t)$ | Trade Space for problem $q$ at observation point $t$. |
| $\sigma$ | Scope. |
| $\kappa$ | Engineering context. |
| $\tau$ | Engineering trajectory. |
| $\tau_a,\tau_b$ | Two compared engineering trajectories. |
| $\pi$ | Ordering or permutation. |
| $\pi_a,\pi_b$ | Two Decision commitment orderings. |
| $\Gamma_R(C_R)$ | Rollback Closure of Rollback Contract $C_R$. |
| $\mathcal D_C(t)$ | Contract-dependency relation on $\mathbb C$ applicable at time $t$. |
| $G$ | Graph-structured State Projection of addressable engineering elements and relation instances. |
| $V_G$ | Vertex set of graph-structured State Projection $G$. |
| $E_G$ | Edge/relation-instance set of graph-structured State Projection $G$. |
| $r$ | Typed relation family. |
| $S_r,T_r$ | Source and target sets of relation $r$. |
| $x,y,z$ | Locally typed arbitrary elements. |
| $i,j,k,m,n$ | Local indices or revision counters. |
| $a,b$ | Labels distinguishing compared cases when used as subscripts. |
| $\langle\cdot\rangle$ | Ordered tuple. |
| $\subseteq,\subset,\cup,\cap,\setminus,\in,\varnothing$ | Standard set operators and the empty set. |
| $=,\neq,\Rightarrow,\Leftrightarrow,\forall,\exists,\neg,\land,\lor$ | Standard equality and logical operators. |
| $<,>$ | Standard order operators where the participating domain defines an order. |
| $\times$ | Cartesian product. |
| $\rightarrow$ | Directed progression or mapping where defined by context. |
| $\{\cdot\}$ | Set notation. |
| $\ldots$ | Omitted additional elements of the same locally defined structure. |

# Part III - Foundation

## 5. Foundation

### 5.1 Preface - reasoning before mathematics

The model starts from five non-technical observations.

First, a graph edge is not truth. Engineering traceability fails if the model treats any path as semantic justification.

Second, missing information must remain visible. A false trace is more dangerous than an explicit unresolved item because it hides the need for work.

Third, engineering has scale. A component-level decision and a Product-level decision can both be valid without one inheriting the other's authority.

Fourth, autonomy has an authority boundary. A Hive should decide when a feasible choice is inside its authority and should ask for human prescription only when the missing commitment requires it.

Fifth, exploration has a cost. The Hive should preserve discoveries but should not keep spending resources on every trajectory or promise a global optimum when Contract fulfilment does not require one.

The mathematics below exists to make those observations testable. Sets represent candidate spaces. Relations represent typed associations. Graphs provide projections for navigation. Validators decide whether a relation can be used semantically. Time and revision preserve history. Resource vectors control active computation without deleting knowledge.

### 5.2 Formal statement roles

Formal statement roles follow §4.2.3 and remain independent of mathematical expression syntax or serialization.

OpenMath supports mathematical objects, symbols, Content Dictionaries, and Formal Mathematical Properties. OMDoc and TPTP explicitly represent statement roles. The proposal uses the role distinction without requiring one serialization format.

An **Invariant** is a property that holds in every valid state of a specified Scope. Its logical basis can be an Axiom, Theorem, Contract rule, or Project Profile rule.

A formal statement record conceptually contains:

$$(id,role,intent,statement,scope,dependencies,evidence,validation).$$

The tuple identifies conceptual fields only and introduces no reusable mathematical symbol.

### 5.3 Core set, relation, and graph algebra

The common semantic algebra distinguishes Propositions and Engineering Objects inside the Engineering Universe:

$$\mathbb P\subseteq\mathcal U_E$$

and:

$$\mathbb O\subseteq\mathcal U_E.$$

Their types remain distinct.

A materialization relation can connect them:

$$Materializes\subseteq\mathbb P\times\mathbb O.$$

A Proposition can have several materializations and one Engineering Object can carry several Propositions.

A typed binary relation $r$ has source and target sets:

$$r\subseteq S_r\times T_r.$$

Its converse is:

$$r^{\smile}=\{(y,x)\mid(x,y)\in r\}.$$

The converse is a mathematical view of the same relation. It does not create a second independent semantic fact.

The common structural algebra includes domain, range, image, inverse image, restriction, converse, set union/intersection/difference, and relational composition. Structural composition is:

$$r\circ s=\{(x,z)\mid\exists y:(x,y)\in s\land(y,z)\in r\}.$$

Structural composition creates a path relation. It does not create semantic entailment unless the Project Profile defines a sound semantic composition rule for the relation family.

A graph $G=(V,E)$ is a graph-structured State Projection of addressable elements and relation instances used for navigation and analysis. Graph reachability is therefore weaker than semantic justification:

$$Reachable_G(a,b)\not\Rightarrow Justifies(a,b).$$

A relation validator has the generic form:

$$V_r(e,\kappa)\in\{\top,\bot,?\},$$

where $\kappa$ contains the applicable scope, revision, time, Project Profile, authority, and other relation-specific context.

### 5.4 Engineering State and computation boundary

For bounded engineering problem:

$$q,$$

at observation point:

$$t,$$

the applicable computational input is the State Projection:

$$\Pi_q(X_t)\subseteq X_t.$$

The projection selects the governed engineering information required for the problem according to the applicable:

- Scope;
- Scale;
- Magnification;
- Contract context;
- authority;
- revision;
- Project Profile;
- information boundary.

The selected information retains its semantic identity and applicable qualification from:

$$X_t.$$

Computation can derive, compare, simulate, optimize, infer, or explore additional information from that projection.

Intermediate hypotheses, reasoning branches, simulation states, model outputs, temporary relations, candidate structures, and other intermediate results constitute **temporary computational material**.

Information selected for engineering retention is recorded using the common-model concept corresponding to its meaning.

A prospective Decision is represented as a Proposition with the applicable Decision status.

Potential Evidence is represented through the Evidence role.

An unresolved finding is represented as an UNKNOWN or Gap.

Required future engineering activity is represented through the applicable Request, Future Action, or Contract mechanism.

Material engineering output is represented as an Engineering Object and can become a Work Product according to the Work Product definition.

A relation is recorded through the applicable typed relation family.

The computation boundary therefore maps retained results into the existing engineering ontology rather than through an additional universal change entity.

#### 5.4.1 Deterministic operations before semantic computation

A State Projection can contain properties whose values follow directly from explicit engineering information and the formal algebra.

Applicable deterministic operations are performed before unresolved semantic reasoning where this reduces Resource Cost.

Such operations can establish:

- set membership;
- relation domain and range;
- relation type compatibility;
- converse and inverse-image results;
- bounded reachability;
- Scope intersection;
- revision lookup;
- supersession status;
- schema conformance;
- known dependency structure;
- Scale and Magnification compatibility;
- other mechanically decidable Project Profile rules.

Semantic computation addresses engineering questions remaining unresolved after the applicable deterministic operations.

The applicable engineering method can additionally require semantic assessment of a mechanically established property.

#### 5.4.2 Temporary computational material

Temporary computational material supports one bounded computation.

Its engineering persistence is determined by whether a resulting item carries continuing engineering value.

Selected results enter Product Evolution History through their corresponding common-model concepts and retain their actual disposition.

Such dispositions can include:

- prospective;
- committed;
- accepted;
- rejected;
- deferred;
- superseded;
- deprecated;
- cancelled;
- unresolved;
- non-selected.

This preserves useful engineering discovery while retaining the semantic distinction between exploration, Decision commitment, Evidence, Contract state, Work Product Acceptance, and Product materialization.

#### 5.4.3 Engineering State evolution

For:

$$t_1<t_2,$$

consider:

$$X_{t_1}$$

and:

$$X_{t_2}.$$

When the applicable Space-defining context remains:

$$\kappa,$$

both satisfy:

$$X_{t_1}\subseteq\mathcal E_\kappa$$

and:

$$X_{t_2}\subseteq\mathcal E_\kappa.$$

Product Evolution History grows monotonically:

$$K_{t_1}\subseteq K_{t_2}.$$

The historical increment:

$$K_{t_2}\setminus K_{t_1}$$

contains the governed engineering history established between the observations.

It can include:

- new or revised Propositions;
- Decision states;
- Evidence;
- relations;
- Contracts and Contract events;
- Engineering Objects;
- Work Products;
- Gaps;
- UNKNOWNs;
- Future Actions;
- provenance;
- Rollback information;
- other governed engineering information.

Each retained element carries its applicable temporal and lifecycle/status qualification.

The relation:

$$X_{t_1}\rightarrow X_{t_2}$$

represents temporal Engineering State evolution.

Concurrent engineering activities can contribute multiple governed events between these observation points.

A material or contextual change of the Space-defining context can establish:

$$\kappa'$$

with:

$$X_{t_2}\subseteq\mathcal E_{\kappa'}$$

and:

$$\mathcal E_{\kappa'}\neq\mathcal E_\kappa.$$

Product Evolution History preserves the engineering history spanning that transition.

#### 5.4.4 Operation-specific state effects

Different governed operations produce distinct Engineering State effects.

**Decision commitment** records the committed Decision together with its rationale, Evidence basis, applicable authority, and context in Product Evolution History. It can change constraints, the Feasible Region, Contract topology, and subsequent engineering choices.

**Contract creation, revision, or lifecycle transition** changes the applicable Contract definition or Contract history according to Contract semantics.

**Work Product creation, submission, verification, or Acceptance** changes the applicable Work Product and Contract history according to Work Product and Acceptance semantics.

**Product realization** changes Materialized Product State according to the applicable engineering process.

**Rollback** changes Materialized Product State according to §10.4 and records the Rollback activity in Product Evolution History.

Each governed operation therefore contributes to Engineering State according to its own formal semantics.

#### 5.4.5 State-relative reassessment

A computational result is interpreted against the Engineering State from which its material inputs were selected.

Its applicability continues while the relevant:

- assumptions;
- relations;
- constraints;
- Evidence conditions;
- authority conditions;
- Product state;
- Contract basis;
- validation dependencies

remain materially equivalent.

A material change in one of these dependencies triggers reassessment of the affected validation against the later Engineering State.

The original result and provenance remain associated with their original temporal context.

The reassessment establishes applicability in the later Engineering State.

#### 5.4.6 Computational participants and implementation mechanisms

Agents, micro-agents, Humans, simulations, solvers, and tools can perform bounded computation over State Projections.

Engineering continuity is carried by the retained Engineering State and provenance.

Provenance identifies the applicable computational source and context where origin is material.

Decision authority, Contract authority, Acceptance authority, Evidence sufficiency, and Product-materialization authority follow their respective governance models.

Implementation mechanisms can batch or transport engineering information through transactions, patches, commits, deltas, messages, database operations, or similar structures.

The engineering semantics remain those of the common-model elements and relations carried by those mechanisms.

### 5.5 Human ingress and choice set

Human interaction is a known set before delegated-autonomy rules are applied:

$$H=\{HAI,HVC,HPC,HWP\}.$$

- `HAI` = HUMAN_ARBITRARY_INPUT.
- `HVC` = HUMAN_VOLUNTARY_CHOICE.
- `HPC` = HUMAN_PRESCRIPTIVE_CHOICE.
- `HWP` = HUMAN_WORK_PRODUCT.

These classes describe how Human-originated information enters Hive operation. They do not define authority.

For Human $h$ and Human-originated input $x$:

$$HumanOrigin(x,h)\not\Rightarrow Authorized(h,x).$$

`HAI` can arrive asynchronously and can project a successor engineering universe. It can be controversial or outside the current Hive recommendation. It does not erase prior state and does not by itself create Binding, Contract revision, Assignment, or another authoritative effect.

`HVC` is optional while autonomous continuation remains possible. A Human-selected candidate is assessed against the current Solution Space before commitment.

`HPC` is required only for an obligatory Decision when no Hive-committable choice remains or when that Decision authority is explicitly human. Requesting a Human prescription does not make any responding Human authoritative automatically.

`HWP` is a Work Product supplied by a Human or human organization. Human origin provides provenance but does not bypass Work Product, information-boundary, traceability, Evidence, validation, or Acceptance rules.

Binding remains restricted to qualifying obligatory Decisions:

$$Binding\subseteq Decision\times Scope\times Time.$$

#### 5.5.1 Explicit Human authority

Authority is an externally established governance property consumed by the Hive.

Let:

$$AuthorizedFor(a,o,x,\sigma,t,\kappa)$$

mean that Actor $a$ is authorized to perform governed operation $o$ on governed subject $x$, within Scope $\sigma$, at time $t$, in engineering context $\kappa$.

Authority therefore has one common signature:

$$Actor\times Operation\times Subject\times Scope\times Time\times Context.$$

An authority fact can be represented conceptually as:

$$AuthorityFact=(Source,Actor,Operation,Subject,Scope,Time,Conditions,Provenance).$$

Authority sources are explicit Project Profile inputs. They can originate from applicable law or regulation, contractual authority, enterprise governance, Product ownership, delegated authority, project governance, or another recognized source. These categories do not establish one universal precedence order.

Title, seniority, Confidence, expertise, social cues, and organizational visibility are not authority sources. Authority is established from an explicit authority source applicable to the governed operation, subject, Scope, time, and context.

Expertise can be relevant to Evidence, assessment, or participant selection.

#### 5.5.2 Authority does not create correctness or feasibility

Authority permits a governed effect. It does not prove that the effect is correct, feasible, or sufficiently evidenced:

$$AuthorizedFor(a,o,x,\sigma,t,\kappa)\not\Rightarrow Correct(x)$$

$$AuthorizedFor(a,DecisionCommitment,d,\sigma,t,\kappa)\not\Rightarrow Feasible(d)$$

$$AuthorizedFor(a,DecisionCommitment,d,\sigma,t,\kappa)\not\Rightarrow EvidenceSufficient(d).$$

Human authority cannot change physical, mathematical, technical, or logical feasibility.

#### 5.5.3 Authority kinds and role separation

At minimum, authority can be required to commit an obligatory Decision, create a Contract, revise a Contract, establish or revise Assignment, delegate Acceptance assessment, or perform another explicitly governed operation.

Authority for one operation does not imply another:

$$AuthorizedFor(a,ContractIssue,C,\sigma,t,\kappa)\not\Rightarrow AuthorizedFor(a,DecisionCommitment,d,\sigma,t,\kappa)$$

and:

$$AuthorizedFor(a,DecisionCommitment,d,\sigma,t,\kappa)\not\Rightarrow AuthorizedFor(a,Assignment,C,\sigma,t,\kappa).$$

Contract Issuer, Executor, Acceptance delegate, Human Decision authority, request originator, Work Product producer, and Engineering Layer participant remain distinct roles.

For example:

$$Executor(C)=a\not\Rightarrow Issuer(C)=a$$

$$Executor(C)=a\not\Rightarrow DecisionAuthority(a,C)$$

$$AcceptanceDelegate(a,C)\not\Rightarrow DesignAuthority(a,C)$$

and:

$$OriginatesRequest(a,C)\not\Rightarrow Issuer(C)=a.$$

One Actor can carry several roles where the Project Profile and required independence rules permit that combination.

#### 5.5.4 Multi-layer and Contract-boundary locality
#### 5.5.4 Multi-layer and Contract-boundary locality

A Human can participate in several Engineering Layers without creating cross-layer authority:

$$Participates(h,L_i)\land Participates(h,L_j)\not\Rightarrow AuthorityPropagation(h,L_i,L_j).$$

Knowledge acquired in one Engineering Layer can inform reasoning but does not become an implicit Decision in another layer:

$$Knows(h,p,L_i)\land Participates(h,L_j)\not\Rightarrow Decision_j(p).$$

Authority also does not propagate through Contract topology:

$$ParentContract(C_i,C_j)\not\Rightarrow AuthorityInheritance(C_i,C_j)$$

$$DependsOn(C_i,C_j)\not\Rightarrow AuthorityInheritance(C_i,C_j)$$

$$Integrates(C_i,C_j)\not\Rightarrow AuthorityInheritance(C_i,C_j).$$

Where information must affect another Engineering Layer or Contract context, it follows the applicable Decision, Exchange Item, feedback, Contract, or other explicit materialization mechanism.

#### 5.5.5 Delegation

Authority can be delegated only where the authority source permits delegation.

Let:

$$Delegates(a,b,o,\sigma,I)$$

mean Actor $a$ delegates operation $o$ within Scope $\sigma$ and applicability interval $I$ to Actor $b$.

Delegation is explicit and bounded. It does not imply unlimited transfer:

$$DelegatedAuthority(b)\subseteq DelegableAuthority(a)$$

unless another independent authority source establishes broader authority for $b$.

Delegation does not create Contract Assignment automatically:

$$Delegates(a,b,o)\not\Rightarrow Executor(C)=b.$$

Authority can expire or be revoked. Later authority change does not rewrite the authority state under which earlier governed operations occurred.

#### 5.5.6 Human input semantic classification

Every Human-originated item is classified by what it is, not merely by who supplied it.

A Human input can become, as applicable, a Question, Request, Clarification, candidate Proposition, Decision candidate, Exchange Item, Work Product, Evidence candidate, Contract revision request, or another Project Profile-defined role.

Therefore:

$$HumanOrigin(x)\not\Rightarrow DecisionKind(x,\kappa).$$

Human provenance does not replace semantic typing.

#### 5.5.7 Human inputs as Engineering State transformations

Authority qualification determines whether a Human input is permitted to act. When its applicable authority and semantic role are established, its engineering effect can transform the current engineering state.

Let the current Engineering State be:

$$X_t.$$

The corresponding feasible continuation is:

$$\mathcal F(X_t)\subseteq\mathcal S_\kappa.$$

For Human input $A$ with applicable authority, define a potentially partial transformation:

The transformation can change constraints, objectives, Product intent, trajectories, Contracts, capability assumptions, or other governed information and thereby produce a successor Engineering State.

A partial transformation is used because a Human input can change the structure or cardinality of the space and can also be non-composable with the state produced by another input.

Authority and transformation remain separate:

$$AuthorizedInput(A)\Rightarrow EligibleToApply(\Phi_A)$$

but:

$$AuthorizedInput(A)\not\Rightarrow Feasible(\Phi_A(X_t)).$$

#### 5.5.8 Sequential Human input algebra

For readability define:

$$X_t+A\equiv\Phi_A(X_t).$$

Sequential inputs are evaluated from left to right:

$$X_t+A+B=\Phi_B(\Phi_A(X_t)).$$

Human-input composition is not assumed commutative:

$$A+B\neq B+A$$

in general, equivalently:

$$\Phi_B\circ\Phi_A\neq\Phi_A\circ\Phi_B.$$

The first input can change the context in which the second input is interpreted. It can remove candidates, introduce constraints, create Contracts, change Product intent, open a new Solution Space region, or change the Engineering Layer or Scale at which the second input becomes material.

Human input is therefore state-dependent:

$$\Phi_A(X_1)\neq\Phi_A(X_2)$$

in general.

For an ordered Human-input sequence:

$$\Sigma_H=(A_1,A_2,\ldots,A_n)$$

let:

$$\Phi_{\Sigma_H}=\Phi_{A_n}\circ\cdots\circ\Phi_{A_2}\circ\Phi_{A_1}.$$

A permutation $\pi(\Sigma_H)$ does not generally preserve the resulting engineering state:

$$\Phi_{\pi(\Sigma_H)}(X_t)\neq\Phi_{\Sigma_H}(X_t).$$

The temporal order of Human inputs is therefore semantically material and remains part of historical state.

#### 5.5.9 Retraction and supersession are not inverse operations

Removing, retracting, superseding, or reversing Human input $A$ does not mean applying $\Phi_A^{-1}$.

Define a governed retraction operation:

$$R_A.$$

Then in general:

$$B+A-A\neq B$$

and:

$$R_A\circ\Phi_A\circ\Phi_B\neq\Phi_B.$$

After $A$ has been applied, subsequent Engineering States can already contain new Decisions, Evidence, Contracts, completed work, Product realization, Work Product revisions, resource expenditure, external commitments, discovered constraints, and later inputs.

Therefore:

$$Retract(A)\neq HistoricalErasure(A).$$

Likewise, explicit supersession:

$$Supersedes(B,A,\sigma,t)$$

controls continuing applicability of $A$ in the stated Scope and time but does not imply:

$$B=A^{-1}$$

or restoration of the state that existed before $A$.

#### 5.5.10 Composable Human inputs

After applicable authority is established, multiple Human inputs are evaluated through their engineering composition; no additional governance-dispute primitive is introduced.

Define:

When:

$$Composable(A,B,X_t),$$

let:

$$X_{AB}=\Phi_B(\Phi_A(X_t)).$$

The resulting feasible region is non-empty when:

$$\mathcal F(X_{AB})\neq\varnothing,$$

both inputs can participate in a valid successor engineering state. Their joint effect can narrow, broaden, restructure, or redirect the active Solution Space.

#### 5.5.11 Non-composable Human inputs

The first failure mode occurs when the transformations cannot produce a sufficiently defined successor engineering state:

$$\neg Composable(A,B,X_t).$$

Using partial-function notation:

$$\Phi_B(\Phi_A(X_t))\uparrow.$$

This is an input-composition failure. Authority qualification has already been resolved before transformation application.

When:

$$\neg Composable(A,B,X_t),$$

the composed successor Engineering State is undefined:

$$\Phi_B(\Phi_A(X_t))\uparrow.$$

A Decision candidate space for that undefined successor state is therefore not constructed.

The Hive preserves both inputs, provenance, authority qualification, previous engineering state, the failed composition attempt, and the reason composition could not be established. Truthful incompleteness applies.

#### 5.5.12 Composable inputs with empty feasible space

A distinct failure mode occurs when the transformations compose successfully but the resulting feasible region is empty.

Let:

$$X_{AB}=\Phi_B(\Phi_A(X_t)).$$

Then it is possible that:

$$Composable(A,B,X_t)\land\mathcal F(X_{AB})=\varnothing.$$

Here the successor engineering state is defined, and its Decision Space can be calculated, but no currently feasible continuation exists:

$$\mathcal D_{feasible}(X_{AB})=\varnothing.$$

This differs fundamentally from non-composition. In the non-composable case the successor state and corresponding Decision Space are undefined; in the empty-feasible-space case they are defined and explicitly infeasible.

Because Human-input composition is order-sensitive, define the reverse ordering:

$$X_{BA}=\Phi_A(\Phi_B(X_t)).$$

It is possible that:

$$\mathcal F(X_{AB})\neq\varnothing$$

while:

$$\mathcal F(X_{BA})=\varnothing,$$

or that one ordering is composable while another is not.

An empty feasible space means that autonomous commitment is unavailable:

$$\mathcal F(X_t)=\varnothing\Rightarrow\neg AutonomousCommitmentAvailable.$$

Recovery can require revision or relaxation of an input, another Human input, Product-intent revision, capability or enabling-technology acquisition, Contract revision, Resource Envelope change, external capability, or another newly explored trajectory. Human authority still does not manufacture engineering feasibility.

If a Human input changes a Space-defining material or contextual bound, the resulting state is evaluated under the resulting context:

$$X_{t+1}\subseteq\mathcal E_{\kappa'}$$

with corresponding:

$$\mathcal S_{\kappa'}.$$

#### 5.5.13 Binding and Contract lifecycle effect

For a Human response to create Binding, Decision semantics and applicable authority must both hold:

$$Binding(d,\sigma,t)\Rightarrow DecisionKind(d,\kappa)\land AuthorizedFor(a,DecisionCommitment,d,\sigma,t,\kappa)\land ApplicableDecisionConditionsSatisfied(d,\kappa).$$

The common model does not introduce a generic `HumanOverride` primitive. A Human can cause a major change through ordinary governed concepts such as Human ingress, Decision, Contract revision, Assignment, Work Product, Product transition, and successor Engineering State.

A Human input or authority change that materially revises a Contract feeds the existing revision-aware Contract FSM. It does not create a separate Human lifecycle.

Human intervention never destructively rewrites prior engineering history:

$$X_t\rightarrow X_{t+1}$$

preserves $X_t$ as an addressable historical State.

### 5.6 AX-1 - Semantic legitimacy

**Intent.** Prevent a graph, document link, or path from becoming engineering truth only because it exists.

**Statement.** A relation can support a justification or commitment only when every applicable validator for that relation is established in the current context.

$$UseForJustification(r,\kappa)\Rightarrow TypeValid(r,\kappa)\land SemanticValid(r,\kappa)\land ScaleValid(r,\kappa)\land StateValid(r,\kappa).$$

$$Reachable_G(a,b)\not\Rightarrow Justifies(a,b).$$

**Boundary.** AX-1 does not state that a Proposition is true merely because all relation validators pass. It states that invalid relations cannot be used as a justification path.

**Validation.** Remove AX-1 and an arbitrary edge can satisfy a trace requirement without semantic evidence. The resulting model admits false trace closure. The axiom is therefore necessary for the proposal's trace semantics.

### 5.7 AX-2 - Truthful incompleteness

**Intent.** Preserve missing information instead of hiding it behind a plausible but unsupported relation.

**Statement.** When a required justification, evidence item, relation, or result cannot be established, the model records the unresolved state explicitly and does not fabricate completion.

$$Required(x,\kappa)\land\neg Established(x,\kappa)\Rightarrow ExplicitUnresolved(x,\kappa).$$

A project can classify the unresolved state as `ORPHAN`, `UNKNOWN`, `KNOWN_GAP`, `CONFLICT`, or another Project Profile category. The category must preserve the fact that the required item is unresolved.

**Boundary.** AX-2 does not require every unknown to block every activity. Materiality and commitment rules remain project- and Contract-specific.

**Validation.** Remove AX-2 and the model can improve apparent completeness by inventing links or suppressing gaps. That directly conflicts with truthful traceability.

### 5.8 AX-3 - Scale locality

**Intent.** Prevent visibility, graph reachability, Human participation, or engineering convenience from creating direct semantic, evidential, or authority relations across incompatible engineering orders.

**Statement.** Every direct engineering relation operates between elements at the same Scale position:

$$DirectSemanticUse(x,y,\kappa)\Rightarrow Scale(x)=Scale(y).$$

Scale equality and Scale distance are relative engineering properties. They do not require permanently assigned numerical coordinates.

A consequence moving between Engineering Layers is propagated only through the applicable adjacent Engineering Layer boundary, using an Exchange Item or Feedback Exchange Item followed by local interpretation.

$$CrossScaleEffect\Rightarrow AdjacentLayerTransfer\land LocalInterpretation.$$

A direct relation must not bypass an Engineering Layer that is intermediate under the current Scale and Magnification relations.

A cross-domain relation must not simultaneously change domain and Scale level.

**Human locality.** One Human can participate in several Engineering Layers, but Human identity does not create a cross-layer authority, Evidence, support, or Decision path.

$$Participates(h,L_i)\land Participates(h,L_j)\not\Rightarrow AuthorityPropagation(h,L_i,L_j).$$

Each Human Decision remains subject to the engineering artifacts, authority, and semantic conditions applicable at its own Engineering Layer.

**Boundary.** The proposal defines one project-wide interval Scale. Magnification establishes the relative Scale placement of Engineering Layers, while Scale establishes their interval relations and deltas. The occupied Layer structure can evolve as engineering work establishes additional Magnifications. The Project Profile defines Domain topology, Magnification interpretation, adjacent-layer transfer semantics, and cross-Domain alignment rules.

**Validation.** Without AX-3, a local Decision, Evidence item, or Human action can silently become authoritative at remote engineering levels and produce the authority/evidence sphere that the proposal is intended to prevent.

### 5.9 AX-4 - Delegated autonomy

**Intent.** Let the Hive act without routine human approval while preserving explicit human authority boundaries.

For problem $q$ define:

$$HiveSpace(q)=Feasible(q)\cap HiveAuthorized(q).$$

**Statement.** If $HiveSpace(q)$ is non-empty, the Hive can continue autonomously. If an obligatory Decision is required, feasible choices exist, and none can be committed by the Hive, HUMAN_PRESCRIPTIVE_CHOICE is required. If no feasible choice exists, human authority cannot make the solution feasible; the conflict remains explicit until the problem changes.

$$HiveSpace(q)\neq\varnothing\Rightarrow AutonomousContinue(q).$$

$$Feasible(q)\neq\varnothing\land HiveSpace(q)=\varnothing\land NeedsObligatoryDecision(q)\Rightarrow HPC(q)=REQUIRED.$$

$$Feasible(q)=\varnothing\Rightarrow PreserveConflict(q).$$

**Boundary.** AX-4 does not block HAI, HVC, or HWP while autonomous continuation is possible.

**Validation.** Remove AX-4 and either all commitments require human approval or the Hive can make commitments outside its authority. Both outcomes violate the delegated-autonomy objective.

### 5.10 AX-5 - Resource-rated exploration

**Intent.** Preserve all discoveries while concentrating active resources on trajectories that justify continued expenditure.

Every discovered outcome is retained with provenance and status:

$$Discovered(o,q,t)\Rightarrow Preserve(o,q,t).$$

Active resource allocation is separate from preservation:

$$Allocation(o,t)=Rate(o,Progress,Novelty,Evidence,Independence,RollbackCost,DeliveryValue,ResourceEnvelope).$$

$$Allocation(o,t)=0\not\Rightarrow Delete(o).$$

The Hive seeks a satisfactory Contract/Product path under the declared Resource Envelope. It does not promise a global optimum unless a Contract explicitly requires and defines such an objective. Outliers can remain in the semi-latent Solution Space even when their active allocation is zero.

The Hive MUST NOT spend production effort on invention until known means are exhausted and the applicable invention allocation is approved.

**Boundary.** AX-5 does not limit the number of discovered outcomes and does not treat majority support as truth. It limits only active expenditure.

**Validation.** Remove AX-5 and the model can either discard low-support discoveries or consume unlimited resources on persistent trajectories. Both conflict with the intended resource and post-mortem behavior.

### 5.11 AX-6 - Concurrent non-deterministic Product evolution

**Intent.** Represent Product development as concurrent exploration with preserved history, order-sensitive commitment, and non-deterministic realization.

#### Common origin and divergent trajectories

Two valid Hive executions can begin from the same Engineering State $X_0$. Let their engineering trajectories be $\tau_a$ and $\tau_b$. They share their common origin:

$$X_0\in\tau_a\cap\tau_b.$$

They can also share later Decisions, Evidence, Contracts, Work Products, and intermediate engineering states. When their engineering progression differs:

$$\tau_a\neq\tau_b.$$

Thus Product evolution supports intersecting but distinct trajectories.

#### Decision ordering is material

Let $D^*$ be the same bounded set of Decisions committed in two trajectories, with two different commitment orders:

$$\pi_a\neq\pi_b.$$

The most probable outcome is that different admissible commitment orders produce different trajectories:

$$\tau_a\neq\tau_b.$$

Their ordered materialized Work Product sequences are correspondingly different:

$$\mathbf W_a\neq\mathbf W_b.$$

The Work Product sets can still intersect because both trajectories can reuse or independently reach common materialized results. The model treats distinct trajectories and distinct materialized Product states as the most probable outcome. Equality remains a special convergence case. The proposal assigns no universal numeric probability to either outcome.

#### Resulting Materialized Product State

For two valid Hive executions starting from the same initial Engineering State and committing the same bounded Decision set, the most probable outcome is distinct Materialized Product States:

$$P^{mat}_a\neq P^{mat}_b.$$

Equality:

$$P^{mat}_a=P^{mat}_b$$

remains possible when the particular trajectories converge to engineering-equivalent realizations. Where that equality matters, it is established for the particular trajectories rather than assumed from common origin or common Decision membership.

#### Decision commitment ordering

The Hive explores Decisions concurrently where applicable. Decisions can require different amounts of exploration, Evidence, realization, verification, and other engineering work. Their readiness for commitment can therefore emerge in an order different from the order in which the underlying engineering questions were introduced.

Product evolution is governed by engineering validity and economy rather than by a universal submission queue.

#### Decisions and Contract dependencies

The common model does not define a general Decision-to-Decision execution-dependency relation. Contract dependencies remain part of Contract topology:

$$\mathcal D_C(t)\subseteq\mathbb C\times\mathbb C.$$

A committed Decision can change Product or Contract state and thereby change that topology:

$$\mathcal D_C(t_1)\neq\mathcal D_C(t_2).$$

Decision ordering and Contract dependencies therefore remain distinct concepts.

#### Product Evolution History

Product Evolution History grows monotonically. For:

$$t_1<t_2,$$

$$K_{t_1}\subseteq K_{t_2}.$$

New Decisions, Evidence, Contracts, Work Products, Gaps, Rollbacks, deprecations, supersessions, and exploration outcomes extend the historically addressable Product evolution.

#### Materialized Product State

Materialization has different semantics. No monotonic inclusion relation is assigned to $P^{mat}_t$. A later Decision can add Product content:

$$P^{mat}_{t_1}\subset P^{mat}_{t_2},$$

or remove previously materialized Product content:

$$P^{mat}_{t_2}\subset P^{mat}_{t_1}.$$

Both are ordinary Product evolution.

#### Solution Universe, Solution Space, Feasible Region, and Trade Space

The solution hierarchy is:

$$\mathcal F(X_t)\subseteq\mathcal S_\kappa\subseteq\Omega.$$

The Solution Universe:

$$\Omega$$

provides the theoretical solution domain.

The engineering context:

$$\kappa$$

establishes the material and contextual bounds of:

$$\mathcal S_\kappa.$$

Engineering State:

$$X_t$$

establishes the state-dependent constraints used to determine:

$$\mathcal F(X_t).$$

A Decision, Evidence result, Contract constraint, Human input, Product realization, or another governed state change can therefore change:

$$\mathcal F(X_t).$$

The Trade Space:

$$T(q,t)$$

contains the part of the applicable Solution Space currently represented for comparison or exploration for problem $q$.

Exploration can enlarge or restructure:

$$T(q,t)$$

while the Space-defining bounds of:

$$\mathcal S_\kappa$$

remain stable.

A material change of Product boundary, capability, enabling technology, physical constraints, or another Space-defining condition can establish a changed context:

$$\kappa'$$

and therefore:

$$\mathcal S_{\kappa'}\neq\mathcal S_\kappa.$$

#### Engineering Universe, Engineering Space, and Engineering State

The engineering hierarchy is:

$$X_t\subseteq\mathcal E_\kappa\subseteq\mathcal U_E.$$

The Engineering Universe provides the theoretical engineering domain.

Engineering context:

$$\kappa$$

establishes the material and contextual bounds of:

$$\mathcal E_\kappa.$$

Observation point:

$$t$$

establishes the temporal bound of:

$$X_t.$$

For two observations under the same Engineering Space:

$$t_1<t_2,$$

Product Evolution History satisfies:

$$K_{t_1}\subseteq K_{t_2},$$

while active Materialized Product State can grow:

$$P^{mat}_{t_1}\subset P^{mat}_{t_2},$$

or contract:

$$P^{mat}_{t_2}\subset P^{mat}_{t_1}.$$

A change in the material or contextual bounds can establish:

$$\mathcal E_{\kappa'}\neq\mathcal E_\kappa.$$

Product Evolution History preserves temporal continuity across the corresponding Engineering States.

**Boundary.** AX-6 does not remove Contract prerequisites, integration gates, verification, Acceptance, authority, or other engineering constraints. It defines the global evolution model in which those constraints operate.

**Validation.** Without AX-6, the model can be misread as deterministic sequential transformation from a fixed input to a unique Product realization, or as monotonically accumulating Product materialization. Both interpretations conflict with concurrent Hive exploration, order-sensitive Decision commitment, and explicit Product rollback.

# Part IV - Formal Proposal

## 6. Operational state, data structure, and roles

### 6.1 Engineering Universe, Engineering Space, Engineering State, and State Projection

The formal engineering model uses four successively bounded sets:

$$\Pi_q(X_t)\subseteq X_t\subseteq\mathcal E_\kappa\subseteq\mathcal U_E.$$

#### Engineering Universe

$$\mathcal U_E$$

is the theoretical domain of engineering elements, relations, configurations, and outcomes expressible by the common model.

Product-, project-, contextual-, material-, and temporal bounds select progressively narrower subsets from this domain.

#### Engineering Space

For engineering context:

$$\kappa,$$

the Engineering Space:

$$\mathcal E_\kappa$$

contains the engineering domain established by the applicable material and contextual bounds.

These bounds can include:

- Product boundary;
- engineering domains;
- physical constraints;
- capability;
- enabling technology;
- Project Profile;
- applicable external constraints.

A material change in these bounds can establish a changed context:

$$\kappa'$$

and:

$$\mathcal E_{\kappa'}\neq\mathcal E_\kappa.$$

#### Engineering State

At observation point:

$$t,$$

Engineering State is:

$$X_t\subseteq\mathcal E_\kappa.$$

$X_t$ contains the governed engineering elements and relations addressable at that observation point together with the qualifications required for their interpretation.

These qualifications include, where applicable:

- identity;
- revision;
- Scope;
- lifecycle or status;
- provenance;
- temporal qualification;
- authority applicability;
- relation qualification;
- Project Profile context.

Engineering State includes both current and historical engineering information according to these qualifications.

Product Evolution History:

$$K_t\subseteq X_t$$

contains the accumulated temporal history.

Materialized Product State:

$$P^{mat}_t\subseteq X_t$$

identifies the currently realized Product content.

#### State Projection

For bounded operation or problem:

$$q,$$

the applicable State Projection is:

$$\Pi_q(X_t)\subseteq X_t.$$

It selects the portion of Engineering State required for that operation.

The selected elements retain their applicable:

- semantic identity;
- Scope;
- revision;
- status;
- temporal qualification;
- provenance;
- relations.

A graph query, Contract-local context, Decision-impact context, Work Product context, Magnification traversal, tool context, or computational input can therefore be expressed as a State Projection.

Repositories, authoring tools, model stores, databases, and runtime interfaces can expose State Projections.

Engineering Objects and physical Product elements retain their own defined semantics when accessed through these projections.

Engineering State and its governed relations provide the common semantic reference across those projections.

### 6.2 Proposition and Engineering Object

A Proposition is the core addressable semantic graph node. It can represent a claim, need, candidate structure, Decision, interface intent, expected behavior, constraint, question, request, gap statement, or another addressable semantic unit.

An Engineering Object is a materialized project entity such as a requirement record, document, model element, source file, binary, simulation result, test artifact, physical part, assembly, configuration record, or other tool/physical item.

Materialization is many-to-many:

$$Materializes\subseteq\mathbb P\times\mathbb O.$$

A Decision is a Proposition node kind. It can materialize into an ADR, plan, change request, Product definition, Exchange Item, or another Engineering Object.

Evidence, Question, Request, constraint, expected behavior, interface intent, Gap statement, and other semantic roles specialize Proposition semantics without creating separate semantic universes.

For an engineering context $\kappa$, let:

$$D_{\kappa}=\{p\in\mathbb P\mid DecisionKind(p,\kappa)\}$$

and:

$$E_{\kappa}=\{p\in\mathbb P\mid EvidenceRole(p,\kappa)\}.$$

Therefore:

$$D_{\kappa}\subseteq\mathbb P$$

and:

$$E_{\kappa}\subseteq\mathbb P.$$

A Decision is a Proposition node of Decision kind. An Evidence item is a Proposition playing the Evidence role.

Evidence inherits the common Proposition algebra, including semantic identity, Scope, revision and temporal qualification, provenance, materialization, typed relations, converse relations, image and inverse-image operations, bounded forward and reverse traversal, and historical addressability.

Evidence extends the common Proposition algebra with Evidence-specific relations and validators required to establish relevance, support, sufficiency, independence, representativeness, provenance, and local evidential closure.

Membership in the common Proposition algebra does not imply predicate substitutability. An operation defined for Evidence is valid only when the participating Proposition has the required Evidence role and the applicable relation validators succeed.

### 6.3 Communication Proposition roles

The common minimum communication roles are:

$$CommRole\supseteq\{Question,Request,Clarification\}.$$

Projects can add roles through the Project Profile. Exchange Item is not another conversational role; it is an addressable Proposition node used for governed transfer of a Decision or Evidence projection or a Work Product.

### 6.4 Decision

A Decision is a rationale-bearing Proposition node kind that preserves or directs a possible course of Hive exploration or behavior. Agreement is a relation to a Decision, not the definition of a Decision.

$$DecisionSupport(x,d)$$

$$AgreesWith(x,d).$$

#### 6.4.1 Lifecycle

The common Decision lifecycle has two states.

While commitment remains open, the Decision is stated as a **Decision Candidate**.

After commitment, the same Decision is stated as a **Decision**.

Thus:

**Decision Candidate → Decision**

Commitment changes the lifecycle qualification while preserving the same Proposition node identity.

Decision rationale, provenance, Evidence, relations, revisions, exploration results, and historical addressability remain associated with that identity.

An implementation represents one Decision node across this lifecycle.

### 6.5 Exchange Item

An Exchange Item is an addressable Proposition node that represents a governed engineering transfer.

Its graph identity supports forward and reverse traversal, provenance, traceability, revision and temporal qualification, Scope, and relation qualification.

The Exchange Item and the source or transferred engineering element retain separate identities.

Exchange Items have two common kinds.

#### 6.5.1 Informational Exchange Item

An Informational Exchange Item delivers a boundary-relative projection of one Decision or Evidence Proposition.

The projection contains only the semantic information required by the receiving boundary.

The source Decision or Evidence Proposition remains canonically addressable in its originating engineering context.

The projection preserves sufficient source identity and provenance for reverse traversal and traceability.

An Informational Exchange Item does not convert the source Decision or Evidence into an Engineering Object.

#### 6.5.2 Objective Exchange Item

An Objective Exchange Item delivers a Work Product.

The Work Product remains the Contract-produced Engineering Object.

The Objective Exchange Item represents its governed transfer to another Contract or Engineering Layer and preserves the corresponding graph traversal and traceability.

#### 6.5.3 Boundary semantics

Exchange Item atomicity is boundary-relative.

The receiving context consumes only the Decision projection, Evidence projection, or Work Product applicable to that boundary.

An Exchange Item remains addressable after consumption so that the governed transfer can be traversed in both directions.

### 6.6 Work Product

A Work Product is the Contract-required result offered as complete for the applicable Contract scope.

A Work Product is produced through Contract execution.

A Work Product can subsequently become the transferred content of an Objective Exchange Item when supplied to another Contract or Engineering Layer.

The Work Product remains the complete result of its source Contract. The Objective Exchange Item represents its governed transfer.

Parallel Contracts can produce parallel Work Products independently and concurrently. Their information is exchanged only through applicable governed engineering boundaries.

The Work Product role does not itself prove conformity or Acceptance:

$$WorkProduct(w,C)\not\Rightarrow Conformant(w,C)$$

$$WorkProduct(w,C)\not\Rightarrow Accepted(w,C).$$

Intermediate engineering material is not automatically a Work Product. Partial models, exploratory artifacts, simulations, computational results, internal drafts, and incomplete Engineering Objects retain their applicable roles until intentionally prepared as the complete Contract result.

$$InternalEngineeringMaterial\not\Rightarrow WorkProduct.$$

A Work Product has its own schema, permitted information boundary, applicable checks under Section 8.5, required validation, supplementary information, and Acceptance rule. A lower-level Work Product does not automatically become content of an upper Work Product merely because it exists.

$$IsWorkProduct(w,C)\Rightarrow ConformsToSchema(w,C).$$

A Work Product can become an input to another Contract while remaining the complete result of its source Contract.

#### 6.6.1 Work Product revision qualification

For Work Product revision $w^r$ and Contract revision $C^k$:

$$Submitted(w^r,C^k)$$

and:

$$Accepted(w^r,C^k)$$

apply to those exact revisions.

Therefore:

$$Accepted(w^r,C^k)\not\Rightarrow Accepted(w^{r+1},C^k)$$

and:

$$Accepted(w^r,C^k)\not\Rightarrow Accepted(w^r,C^{k+1}).$$

Unaffected Evidence or validation can be reused only where the applicable Project Profile establishes that the changed revision does not invalidate it.

### 6.7 Product

A Product is the coherent engineered subject and the primary scope and intent anchor for Hive operation.

A Product can be, for example:

- a mobile application;
- a book;
- an SoC;
- a software component;
- an electronic or mechanical component;
- a complex device;
- a vehicle;
- a system-of-systems;
- another project-defined engineered subject.

These examples do not constrain Product kind.

The Product establishes the top-level engineering context within which the Hive operates. Conceptually:

$$Product(P)\rightarrow HiveOperatingContext(H,P).$$

The Product therefore identifies what the Hive is working on and what engineering intent establishes that work. It does not prescribe how the Product is decomposed, architected, implemented, manufactured, written, encoded, integrated, or otherwise realized. Those remain engineering outcomes discovered or established during Product development.

Product structure, Work Product structure, Contract execution topology, Engineering Layer topology, and Hive execution topology represent different concerns.

Product decomposition describes the engineered subject. Work Product structure describes results required by Contracts. Contract decomposition distributes governed execution responsibility. Hive topology describes how the Hive organizes computational execution.

Therefore:

$$ContractDecomposition\not\Rightarrow ProductDecomposition$$

$$ContractDecomposition\not\Rightarrow HiveDecomposition$$

and:

$$ProductDecomposition\not\Rightarrow ContractDecomposition.$$

The common proposal does not prescribe technical interfaces, architecture, protocols, decomposition strategy, or other engineering content of a Product. Such details belong to project engineering work. Where examples are useful for explanation, they are Illustrations and do not establish proposal semantics.

#### 6.7.1 Product as the primary Hive input

Product definition is a primary input to Hive operation. It establishes the initial scope, intent, and subject of Product-oriented Solution Exploration.

Let:

$$Intent(P)$$

represent Product-level intent and:

$$Scope(P)$$

represent the applicable Product scope.

Then initiation of Product-oriented Hive work can be represented conceptually as:

$$(P,Intent(P),Scope(P))\rightarrow InitializeExplorationContext(H,P).$$

This does not require the Product to be fully defined before work begins. The initial Product definition can contain known needs, intended outcomes, constraints, UNKNOWNs, Known Gaps, existing Product state, externally imposed conditions, available capabilities, partial intent, or ambiguous intent. Truthful incompleteness remains applicable.

Therefore:

$$ProductDefined(P)\not\Rightarrow ProductFullySpecified(P).$$

A Product can establish meaningful Hive work while much of its eventual structure remains unexplored.

#### 6.7.2 Product is broader than a Contract target

A Contract operates inside a Product context. The Product provides the overall subject and engineering intent. A Contract governs one bounded execution responsibility related to that Product.

Conceptually, for a Contract belonging to Product $P$:

$$ContractTarget(C)\subseteq ProductContext(P).$$

This does not require the Contract target to represent a physical Product fragment. A Contract can concern Product development, analysis, architecture, verification, Evidence generation, integration, supplier work, documentation, qualification, or another bounded responsibility.

The Product is not created merely by aggregating Contracts:

$$Product(P)\not\equiv\bigcup_i Contract(C_i).$$

Likewise:

$$ProductScope(P)\not\Rightarrow CompleteContractDecomposition(P).$$

The existence of a Product does not imply that every part of its intended development has already been decomposed into Contracts.

#### 6.7.3 Product operating scope

The Product establishes a general scope of work for the Hive.

Let:

$$OperationalScope_H(P,t)$$

be the currently applicable Product-oriented operating scope of Hive $H$. It can contain active engineering questions, active Contracts, Product Decisions, Trade Spaces, Product-relevant Evidence, unresolved Product UNKNOWNs and Gaps, applicable Engineering Layers, enabling capabilities and tools, and Product-related external dependencies.

The operating scope can evolve as the Product becomes better understood:

$$OperationalScope_H(P,t)\rightarrow OperationalScope_H(P,t+\Delta t).$$

Such evolution does not imply that Product identity changes. The Product can remain the same while its known engineering scope expands, contracts, or is restructured.

#### 6.7.4 Product intent and Product state are distinct

The Product includes an engineering intent that establishes Hive operation, but intended state and actual state remain distinct.

Let:

$$DesiredState(P,t)$$

and:

$$ObservedState(P,t)$$

represent those concepts where applicable. Then:

$$DesiredState(P,t)\neq ObservedState(P,t)$$

in general.

The gap between intended and actual state is part of the engineering problem. The Hive operates over that gap rather than treating Product intent as Evidence that the intended state already exists.

#### 6.7.5 Hive capability bounds Product development

Product intent does not imply that the Hive is capable of realizing every possible Product state.

Let:

$$Capability_H(t)$$

represent the engineering capabilities available to Hive $H$ at time $t$. Capability can include reasoning capability, domain knowledge, software-development capability, simulation capability, verification capability, physical-design capability, tooling access, manufacturing access, external specialist capability, Human capability, supplier capability, and other project-defined execution capability.

The Product defines the intended engineering problem. Hive capability restricts what parts of that problem can actually be executed autonomously or through currently available participants.

Therefore:

$$ProductIntent(P)\not\Rightarrow HiveCapable(H,P).$$

#### 6.7.6 Enabling technology bounds Product development

Actual Product development also depends on available enabling technology.

Let:

$$Enablement(P,t)$$

represent the applicable set of technologies, facilities, tools, platforms, infrastructure, processes, and external technical capabilities available for Product development.

Illustrative examples include programming languages and frameworks, EDA/CAD/CAE tools, fabrication technologies, semiconductor process nodes, test equipment, manufacturing methods, simulation environments, laboratories, cloud/compute infrastructure, publishing technologies, third-party platforms, and external engineering services.

A theoretically valid Product solution can remain unavailable when required enabling technology does not exist or is inaccessible. Therefore:

$$TechnicallyConceivable(x)\not\Rightarrow Developable_H(x,t).$$

#### 6.7.7 Product Development Envelope

Hive capability and enabling technology jointly bound the currently reachable development region.

For Product $P$, define:

$$DevelopmentEnvelope_H(P,t)$$

as the currently reachable Product-development region under the applicable Product intent, Hive capabilities, enabling technology, authority, Resource Envelope, and external constraints.

Conceptually:

$$DevelopmentEnvelope_H(P,t)=SolutionSpace(P,t)\cap CapabilityReach_H(t)\cap EnablementReach(P,t)\cap AuthorityReach_H(t)\cap ResourceReach_H(t).$$

This is a conceptual intersection and does not require all dimensions to use the same mathematical representation.

The important invariant is:

$$SolutionSpace(P,t)\not\equiv DevelopmentEnvelope_H(P,t).$$

The Solution Space can contain valid or interesting Product possibilities that the current Hive cannot yet develop.

#### 6.7.8 Capability limitation does not invalidate Product intent

If Product intent lies partly outside the current Development Envelope, the Product itself is not invalid. Instead the Hive exposes the limitation.

For intended state $x$:

$$x\in IntendedProductRegion(P)\land x\notin DevelopmentEnvelope_H(P,t)$$

can lead to capability acquisition, tooling development, external Contract, supplier involvement, Human intervention, enabling-technology development, Product intent revision, deferred work, or explicit inability report.

The model must not silently reduce Product intent merely to make the current Hive appear capable:

$$CapabilityLimit\not\Rightarrow SilentProductScopeReduction.$$

#### 6.7.9 Development Envelope can evolve

Hive capability and enabling technology are temporal. Therefore:

$$DevelopmentEnvelope_H(P,t_1)\neq DevelopmentEnvelope_H(P,t_2)$$

can occur even when Product intent is unchanged.

For example:

$$NewTool\rightarrow ExpandedCapability\rightarrow ExpandedDevelopmentEnvelope$$

or:

$$SupplierUnavailable\rightarrow ReducedEnablement\rightarrow ReducedDevelopmentEnvelope.$$

A Product path that was previously infeasible can later become feasible without changing Product identity. A previously feasible Product path can likewise become unavailable.

#### 6.7.10 Product scope, capability, enablement, and resources

The Product Development Envelope remains distinct from the Resource Envelope.

Product answers what engineered subject and intent establish the work. Capability describes what kinds of engineering action the Hive can perform. Enablement describes what technical means exist and are accessible. Resource Envelope describes how much applicable resource is available.

Therefore:

$$ProductScope\neq Capability\neq Enablement\neq ResourceEnvelope.$$

They interact, but none substitutes for another.

#### 6.7.11 Product and Work Product are independent roles

Product and Work Product describe different semantics.

For subject $x$:

$$ProductRole(x,\kappa)$$

means that $x$ is treated as the engineered subject in context $\kappa$.

For Contract $C$:

$$WorkProductRole(x,C)$$

means that $x$ is the complete Contract-required result.

Neither role implies the other:

$$ProductRole(x,\kappa)\not\Rightarrow WorkProductRole(x,C)$$

and:

$$WorkProductRole(x,C)\not\Rightarrow ProductRole(x,\kappa).$$

The same addressable or material entity can play both roles when the applicable engineering context explicitly establishes both:

$$ProductRole(x,\kappa)\land WorkProductRole(x,C).$$

Role coincidence does not collapse the two concepts.

#### 6.7.12 Product state and Work Product state

Product state and Work Product state are distinct. Let:

$$ProductState(P,t)$$

represent the applicable Product state and:

$$WorkProductState(w,C,t)$$

represent the Contract-relative Work Product state. In general:

$$ProductState(P,t)\neq WorkProductState(w,C,t).$$

A Work Product can change without changing the Product:

$$WorkProductRevised(w)\not\Rightarrow ProductChanged(P).$$

Conversely:

$$ProductChanged(P)\not\Rightarrow WorkProductRevised(w)$$

universally.

Whether a Product change makes a particular Work Product stale is determined through the applicable Contract, traceability, revision, and impact rules. Where the Product change is material to the Work Product or its Acceptance basis, reassessment is required.

#### 6.7.13 Product target and required Work Product

A Contract contains two semantically distinct elements:

1. the Product target - what engineering state the Contract concerns or intends to establish; and
2. the required Work Product - what complete result the Executor must submit for Contract fulfilment.

Conceptually:

$$ProductTarget(C)=(P,\tau_P)$$

and:

$$WPReq(C).$$

These are different Contract semantics. Therefore:

$$ProductTarget(C)\neq WPReq(C)$$

as roles, even when the same material object participates in both roles.

#### 6.7.14 Work Product Acceptance does not create universal Product Acceptance

Acceptance remains Contract-relative. For:

$$Accepted(w^r,C^k)$$

the model establishes that the specified Work Product revision satisfies the applicable Acceptance rules of the specified Contract revision. It does not establish a universal predicate:

$$AcceptedProduct(P).$$

Therefore:

$$Accepted(w,C)\not\Rightarrow GloballyAccepted(P).$$

The common model does not define universal Product Acceptance. Product-level acceptance, qualification, certification, release, manufacturing acceptance, customer acceptance, regulatory approval, or another Product lifecycle predicate can be defined through the Project Profile or an applicable external process.

#### 6.7.15 Acceptance does not automatically mutate Product state

Acceptance is a governance event. A Work Product Acceptance event does not by itself constitute a Product state-transition operation:

$$Accepted(w,C)\not\Rightarrow ProductStateTransition(P).$$

A Product transition occurs only where the Contract or applicable project process establishes that transition.

### 6.8 Product Delivery

Product Delivery is a specialization of Contract fulfilment.

For an ordinary Contract $C$:

$$Fulfilled(C)$$

means that its required Work Product has passed the applicable Acceptance rules. This does not universally imply that the Product itself has moved to a new target state.

For a Product Delivery Contract:

$$ProductDeliveryContract(C)$$

fulfilment additionally requires satisfaction of the applicable Product target. Therefore:

$$ProductDeliveryContract(C)\land Fulfilled(C)\Rightarrow ProductTargetSatisfied(C).$$

For a Contract that is not a Product Delivery Contract:

$$Fulfilled(C)\not\Rightarrow ProductStateTransition(P).$$

A verification, analysis, feasibility, testing, planning, Evidence-generation, or similar Contract can therefore be successfully fulfilled without itself changing the Product.

#### 6.8.1 Product target satisfaction

Product target satisfaction is established according to the Contract and applicable engineering method. The common proposal does not prescribe how that target is technically demonstrated.

Illustrative project-defined mechanisms can include direct state observation, integration result, test Evidence, manufacturing result, deployed state, delivered physical item, accepted configuration, or another domain-specific mechanism.

The common semantic requirement is only that:

$$ProductTargetSatisfied(C)$$

must not be inferred solely from:

$$Accepted(w,C)$$

unless the applicable Acceptance rule explicitly establishes Product target satisfaction.

### 6.9 Product / Work Product cardinality independence

The relationship between Product structure and Work Product structure is many-to-many in the common model. One Work Product can concern several Product elements. Several Work Products can concern one Product or Product element.

Therefore no one-to-one structural mapping is assumed. Let the Project Profile define the applicable relation:

$$RelatesWPToProduct(w,P,\kappa).$$

Then:

$$|\{p:RelatesWPToProduct(w,P,\kappa)\}|$$

and:

$$|\{w:RelatesWPToProduct(w,P,\kappa)\}|$$

are not universally constrained to one.

### 6.10 Work Product integration and Product integration

Work Product integration and Product integration are distinct operations.

The Integrator Contract constructs a coherent Work Product from qualified Work Product inputs. Therefore:

$$IntegrateWorkProducts(w_1,\ldots,w_n,w_I)\not\Rightarrow IntegrateProductElements(P_1,\ldots,P_n,P_I).$$

Likewise:

$$ProductIntegrated(P)\not\Rightarrow WorkProductsIntegrated.$$

When a project requires both, its engineering method and Contract topology establish the relation between them.

### 6.11 Product observation and historical Work Product state

Product state can evolve after a Work Product has been Accepted. Later operation can reveal degradation, failure, unexpected behaviour, changed environment, or another new condition.

Such later Product state does not retroactively rewrite historical Acceptance:

$$LaterProductState(P,t_2)\not\Rightarrow RewriteAcceptance(w^r,C^k,t_1).$$

The historical statement remains that $w^r$ was Accepted against $C^k$ under the information and rules applicable at $t_1$.

New Product information can instead create new Evidence, Feedback Exchange Items, Decision reassessment, Work Product revision, new Contract, successor Contract, Change Management activity, or another applicable governed response.

## 7. Operational algebra

### 7.1 Purpose of the algebra

The operational algebra defines what the Hive can compute mechanically before semantic reasoning. It also makes relation semantics explicit enough to prevent path-based hallucinated traceability.

The algebra is many-sorted. Source and target roles restrict each relation family. A relation valid for Decisions is not automatically valid for source code, evidence, Contracts, or Work Products.

### 7.2 Common structural operations

The common engine supports:

- set membership, union, intersection, and difference;
- relation domain and range;
- converse;
- image and inverse image;
- relation restriction;
- structural relational composition;
- bounded graph traversal;
- strongly connected component detection;
- revision and scope filtering;
- provenance and materialization lookup.

Semantic composition is a separate Project Profile rule.

#### 7.2.1 Bounded traversal

There is no default engineering operation that traverses the complete graph.

A traversal query explicitly supplies its control parameters:

$$Q=(Start,Roles,Direction,ScalePolicy,Stop,Budget)$$

and:

$$Traverse(G,Q)\subseteq G$$

where:

- `Start` identifies the initial elements;
- `Roles` identifies permitted relation families;
- `Direction` selects forward, converse, or explicitly permitted bidirectional traversal;
- `ScalePolicy` limits traversal according to Scale and Magnification rules;
- `Stop` defines termination conditions;
- `Budget` bounds Resource Cost.

Mathematical converse allows traversal in either direction without creating a second semantic fact.

A structural traversal result establishes reachability only:

$$Reachable_Q(a,b)\not\Rightarrow Justifies(a,b).$$

Semantic use of a discovered path still requires the applicable relation validators.

Traversal therefore cannot be used as an implicit whole-project closure operation.

### 7.3 Relation vocabulary

The common proposal defines the algebra, not a universal engineering dictionary of relation names. A project introduces relation kinds, source/target signatures, validators, converse display labels, semantic composition rules, and change-impact semantics through the Project Profile.

A semantic relation has one canonical direction and one canonical stored fact.

For a typed relation:

$$r\subseteq S_r\times T_r$$

its mathematical converse is:

$$r^{\smile}=\{(y,x)\mid(x,y)\in r\}.$$

The converse is a derived view of the same relation. It is not a second independently asserted graph fact.

A Project Profile can define human-readable labels for both directions. For example:

$$Supports_{\kappa}\Longleftrightarrow IsSupportedBy_{\kappa}$$

where:

$$IsSupportedBy_{\kappa}=Supports_{\kappa}^{\smile}.$$

Therefore:

$$Supports_{\kappa}(e,p)\iff IsSupportedBy_{\kappa}(p,e).$$

Similarly, where those relation families are defined:

$$Implements\Longleftrightarrow ImplementedBy$$

$$Supersedes\Longleftrightarrow IsSupersededBy$$

$$References\Longleftrightarrow IsReferencedBy.$$

The display labels do not create additional semantic relations.

For a relation $r$, forward trace traversal from a source set $X$ is:

$$Forward_r(X)=r[X]$$

and reverse trace traversal from a target set $Y$ is:

$$Reverse_r(Y)=r^{\smile}[Y].$$

The same canonical relation therefore supports both questions: what does this element relate to, and what relates to this element?

A traversal can use the forward direction, converse direction, or explicitly permitted bidirectional traversal according to the existing bounded-traversal rules.

Reverse traversal does not reverse engineering causality, authority, or semantic implication. It provides reverse traceability over the same canonical relation.

### 7.4 Cycles

A mathematical converse loop is neutral. A temporal iteration across revisions is valid. A proof cycle without an admissible external anchor is invalid. A prerequisite deadlock is invalid unless the Project Profile defines explicit synchronization or joint-commitment semantics.

Cycle validity therefore depends on relation semantics and revision/time, not graph topology alone.

## 8. State consistency, data reliability, and model quality

### 8.1 Scope, revision, and time

Every semantic use is qualified by the context required by its relation family. Typical qualifiers are Scope, revision, branch, time, Contract, Engineering Layer, Project Profile revision, and authority domain.

For Engineering State $X^\beta_t$, a Scope is an anchored subset:

$$\sigma=(a,S_\sigma),\qquad S_\sigma\subseteq X^\beta_t$$

where $a$ identifies the Scope anchor or governing context.

Scopes in the same Engineering State support ordinary set operations:

$$S_{\sigma_1}\cap S_{\sigma_2},\quad S_{\sigma_1}\cup S_{\sigma_2},\quad S_{\sigma_1}\setminus S_{\sigma_2},\quad S_{\sigma_1}\subseteq S_{\sigma_2}.$$

A Scope does not need to be graph-connected.

State evolution preserves predecessor States:

$$X^\beta_t\rightarrow X^{\beta'}_{t'}.$$

Comparison across different Engineering States uses an explicit revision mapping:

$$\rho_{(\beta,t)\rightarrow(\beta',t')}:X^\beta_t\rightharpoonup X^{\beta'}_{t'}.$$

The mapping is partial because an engineering element can be introduced, removed from active continuation, split, merged, or otherwise lack a one-to-one successor.

Name equality, repository path equality, or apparent structural similarity does not substitute for revision mapping.

Later discovery can add previously unknown structure while preserving prior State:

$$Trace_{t_0}\subseteq Trace_{t_1}.$$

#### 8.1.1 Revision-aware relation instances

A relation instance is qualified by the revisions of its endpoints and by the context in which it applies.

A conceptual relation record is:

$$e=(x^i,r,y^j,\sigma,I,\kappa)$$

where:

- $x^i$ is the source Proposition revision;
- $r$ is the relation family;
- $y^j$ is the target Proposition revision;
- $\sigma$ is the affected Scope;
- $I$ is the applicability interval;
- $\kappa$ contains relation-specific context such as authority, Contract, Engineering Layer, or Project Profile.

Historical relation instances are preserved. A later relation does not destructively rewrite the earlier fact.

#### 8.1.2 Scoped supersession

Supersession is revision-, Scope-, and time-qualified.

A conceptual form is:

$$Supersedes(p_2^k,p_1^j,\sigma,t).$$

This means that revision $p_2^k$ supersedes revision $p_1^j$ for the stated Scope from the applicable time onward.

Supersession does not:

- erase the superseded revision;
- rewrite historical states;
- automatically supersede unrelated dependent elements;
- imply global replacement outside the declared Scope.

Propagation beyond the stated Scope follows the applicable relation, Magnification traversal, Decision, and Contract rules.

### 8.2 Identity and provenance

Semantic identity and material identity are separate. A Proposition can have several materializations and an Engineering Object can carry several Proposition revisions. Provenance records reconnect State Projections with their governed engineering information and preserve the source of exploratory results, Evidence, Human inputs, materialized engineering results, and external effects.

### 8.3 Data reliability

The model distinguishes:

- structural validity;
- semantic validity;
- evidence sufficiency;
- authority validity;
- scale validity;
- Contract admissibility;
- information-boundary compliance;
- Project Profile conformance.

A successful structural check does not imply successful semantic or evidence checks.


The applicable reliability dimensions depend on the engineering concept and governed operation.

A relation used for traceability follows relation typing and semantic validation.

Evidence used in justification follows Evidence relevance, provenance, sufficiency, independence, and other applicable Evidence rules.

Decision commitment follows the applicable Evidence, authority, Scope, Scale, UNKNOWN, and Decision rules.

Contract transitions follow Contract guards and authority.

Work Product Acceptance follows the Acceptance rules of the applicable Contract.

Product materialization follows the applicable Product, Contract, integration, physical-realization, or supporting-process semantics.

Success in one validity dimension does not establish another validity dimension.

Likewise, successful validation for one governed operation does not establish permission for a different operation.

Confidence remains outside these validity dimensions. It can summarize process health but cannot substitute for any applicable engineering validator or authority rule.

### 8.3.1 Confidence boundary

The proposal does not abbreviate Confidence as `Conf`, because `Conf` is commonly overloaded with Configuration and related engineering terminology.

For an active problem or task $q$, the Hive can maintain:

$$Confidence_H(q,t)$$

where $H$ identifies the Hive execution context, $q$ identifies the active task or exploration problem, and $t$ identifies observation time.

Confidence is a time-varying operational indication of how the ongoing autonomous exploration/development process appears to be trending toward a useful outcome under the current information and Resource Envelope.

Confidence is not another semantic or validation property. In particular:

$$Confidence\neq StructuralValidity$$

$$Confidence\neq SemanticValidity$$

$$Confidence\neq EvidenceSufficiency$$

$$Confidence\neq AuthorityValidity$$

$$Confidence\neq ContractAdmissibility$$

Confidence does not authorize an Engineering State transition.

### 8.3.2 Confidence is not a correctness quantity

Confidence does not substitute for computational properties that already have their own formal semantics:

$$Confidence\neq Probability$$

$$Confidence\neq Precision$$

$$Confidence\neq Accuracy$$

$$Confidence\neq Uncertainty$$

$$Confidence\neq StatisticalSignificance$$

and, more generally:

$$Confidence\neq ComputationalAssuranceMetric.$$

A probability estimate, confidence interval, precision value, uncertainty bound, reliability estimate, statistical test result, simulation distribution, or similar quantity retains its own mathematical semantics. Confidence can use such quantities as inputs; it cannot silently reinterpret itself as one of them.

Therefore a value such as:

$$Confidence_H(q,t)=0.82$$

does not mean:

$$P(Success(q))=0.82$$

unless a Project Profile separately defines such a probabilistic model. In that case the probability remains a distinct computational quantity and is not the definition of Confidence.

### 8.3.3 Confidence is not materialized engineering content

Confidence is not a Work Product property:

$$Confidence\not\subseteq WorkProductProperties.$$

It is not a Proposition role:

$$Confidence\not\subseteq PropositionRoles.$$

It is not Evidence, Decision, Exchange Item, Work Product, or Product state:

$$Confidence\neq Evidence$$

$$Confidence\neq Decision.$$

Confidence is operational state maintained by the Hive. Exposing the current Confidence indication to a Human operator or another authorized monitoring function does not turn Confidence into Product or Work Product content.

### 8.3.4 Confidence is time-varying

Confidence is not a static qualification assigned to an object. It evolves with exploration:

$$Confidence_H(q,t_0),Confidence_H(q,t_1),\ldots,Confidence_H(q,t_n).$$

Where the representation is numeric, a trend can be expressed as:

$$\Delta Confidence_H(q,t)=Confidence_H(q,t)-Confidence_H(q,t-\Delta t).$$

A Project Profile can use an ordinal or categorical equivalent instead. Confidence can therefore be improving, stable, degrading, volatile, or insufficiently established. No universal numeric representation is required.

Historical Confidence observations remain associated with the Solution Exploration state in which they were produced. Later observations do not rewrite earlier ones.

### 8.3.5 Confidence and solution continuity

Confidence follows the temporal continuity of Solution Exploration. Material changes in the task definition, Solution Universe, Resource Envelope, Project Profile, or exploration conditions can change how the Confidence series is interpreted.

The Hive therefore does not assume that Confidence values are directly comparable across incompatible execution contexts.

### 8.4 Work Product information boundary

Existence in the Solution Space does not grant permission to expose information in a Work Product:

$$Exists(x,SolutionSpace)\not\Rightarrow PermittedIn(x,WP,C).$$

This protects formal structure, semantic role, intellectual property, security, safety information, supplier data, and other project-defined boundaries.

### 8.5 Check cascade and assessment economy

Engineering checking follows a cost-ordered cascade.

The classes do not represent increasing quality. They represent increasingly expensive ways to establish different engineering properties.

A subject can require one, two, or all three classes. The classes are not bound to a particular Engineering Layer, Work Product type, lifecycle phase, or Actor.

The applicable sequence is:

$$Instrumental \rightarrow LowProfile \rightarrow HighProfile$$

A later stage is entered only when that stage is required for the property being assessed and every applicable cheaper stage has passed.

A failed cheaper check stops the cascade. The subject is corrected or otherwise dispositioned before a more expensive assessment proceeds.

#### 8.5.1 Instrumental Checks

Instrumental Checks operate on explicit data structures and deterministic rules.

Typical subjects include:

- schema and syntax;
- required fields;
- type and relation signatures;
- graph invariants;
- deterministic consistency rules;
- calculable constraints;
- trace structure;
- revision and identity consistency;
- information-boundary rules;
- executable validators.

Instrumental Checks can be executed repeatedly at low marginal cost and close to the point where engineering information is created or changed.

A failed Instrumental Check prevents unnecessary semantic assessment when the same defect is already established mechanically.

Passing an Instrumental Check establishes only the property checked by that instrument. It does not establish semantic correctness.

#### 8.5.2 Low-profile Assessment

Low-profile Assessment operates only after the applicable Instrumental Checks have passed.

It evaluates bounded semantic properties using semi-instrumented structures such as:

- controlled checklists;
- defined review questions;
- semantic-role rules;
- expected information patterns;
- domain-specific review templates;
- bounded consistency criteria.

Its purpose is to align semantics on top of formally valid engineering information without reopening unrestricted engineering reasoning.

Low-profile Assessment can identify defects that Instrumental Checks cannot establish because those defects require interpretation.

A failed Low-profile Assessment stops the cascade before High-profile Assessment.

The subject is corrected or dispositioned and the applicable cheaper checks are repeated before further escalation.

#### 8.5.3 High-profile Assessment

High-profile Assessment is used only for residual properties that cannot be established adequately through Instrumental Checks or Low-profile Assessment.

It can require:

- broad Product context;
- trade-space exploration;
- specialist judgement;
- conflicting-evidence reconciliation;
- multi-domain reasoning;
- independent reasoning;
- substantial computational or human resources.

High-profile Assessment is not a duplicate validation round over defects that cheaper mechanisms are expected to detect.

Therefore:

> A High-profile Assessment should normally operate on a subject that is already instrumentally valid and semantically aligned under the applicable Low-profile Assessment.

Its purpose is to address remaining open engineering questions, not to compensate for inadequate lower-cost validation.

#### 8.5.4 Gating rule

For an engineering subject $x$, the check classes are ordered by Resource Cost:

$$I \prec L \prec H$$

where:

- $I$ = Instrumental Check;
- $L$ = Low-profile Assessment;
- $H$ = High-profile Assessment.

The cascade is strictly gated:

$$Run(L,x) \Rightarrow Pass(I,x)$$

$$Run(H,x) \Rightarrow Pass(I,x)\land Pass(L,x)$$

and therefore:

$$Fail(I,x) \Rightarrow \neg Run(L,x)\land\neg Run(H,x)$$

$$Fail(L,x) \Rightarrow \neg Run(H,x)$$

A subject does not have to proceed to every check class. Checking can stop after the cheapest stage that establishes all properties required at that point.

However, a more expensive stage cannot bypass a cheaper stage.

Every engineering context therefore provides enough explicit structure to support Instrumental Checks before semantic assessment. Where this is not possible with the current engineering method, data representation, or tooling, the deficiency is itself an engineering-economy problem and drives improvement of that method, representation, or tooling.

#### 8.5.5 Coverage discipline

The Check Cascade accumulates validation capability from expensive reasoning into cheaper and more repeatable mechanisms.

A finding made at one check class is examined to determine whether the same condition can be established reliably at a cheaper class.

If a Low-profile Assessment discovers a condition that can be established deterministically, the Hive creates a Decision to improve Instrumental Checks.

$$LowProfileFinding \rightarrow Decision \rightarrow InstrumentalCheck$$

If a High-profile Assessment discovers a condition that can be established through a bounded semantic rule, the Hive creates a Decision to improve Low-profile Assessment.

$$HighProfileFinding \rightarrow Decision \rightarrow LowProfileRule$$

If the High-profile finding can be established deterministically, the Decision can improve Instrumental Checks directly:

$$HighProfileFinding \rightarrow Decision \rightarrow InstrumentalCheck$$

The same defect class should therefore move downward through the Check Cascade whenever a cheaper representation preserves the required meaning and reliability.

A High-profile Assessment should not repeatedly discover conditions that the established Low-profile or Instrumental mechanisms are expected to identify.

Likewise, a Low-profile Assessment should not repeatedly discover conditions that established Instrumental Checks can identify.

The intended evolution is:

$$HighProfile \rightarrow LowProfile \rightarrow Instrumental$$

as engineering knowledge becomes sufficiently structured.

This evolution improves the engineering method itself rather than merely reducing the cost of one execution.

#### 8.5.6 Instrumentation improvement

When a finding can be checked at lower Resource Cost without losing the required semantic meaning, the Hive records a Decision to improve the checking infrastructure.

The improvement can introduce or revise:

- schemas;
- relation constraints;
- data structures;
- deterministic validators;
- calculations;
- checklists;
- review questions;
- semantic-role constraints;
- other bounded validation mechanisms.

The Decision remains subject to ordinary engineering authority, Resource Envelope, and implementation economics.

The existence of a possible automation does not require immediate implementation when the expected saving does not justify its cost.

> Repeated expensive reasoning should be converted into cheaper validation when the conversion is semantically adequate and economically justified.

#### 8.5.7 Re-entry after a finding

A finding that changes the assessed subject invalidates every affected result downstream of that change.

After correction, Decision rework, or another disposition, checking resumes from the cheapest check class whose result can have been affected.

For example, a Low-profile finding that causes a structural change returns through Instrumental Checks before Low-profile Assessment is repeated:

$$LowProfile \xrightarrow{finding} DecisionRework \rightarrow Instrumental \rightarrow LowProfile$$

A High-profile finding that causes broader rework similarly returns through the complete affected cascade:

$$HighProfile \xrightarrow{finding} DecisionRework \rightarrow Instrumental \rightarrow LowProfile \rightarrow HighProfile$$

A finding also triggers the coverage-discipline rule in Section 8.5.5.

Therefore, when a Low-profile or High-profile finding can be detected reliably at lower Resource Cost, the Hive creates a Decision to improve the cheaper checking mechanism rather than relying on the expensive stage to rediscover the same condition.

Re-entry is determined by the effect of the change, not by the stage at which the problem happened to be discovered.

#### 8.5.8 Engineering-layer independence and minimum structure

Check classes are not assigned to particular Engineering Layers.

Every Engineering Layer supports the Check Cascade:

$$Instrumental \rightarrow LowProfile \rightarrow HighProfile$$

The exact data structures, validators, checklists, semantic rules, and reasoning methods differ by engineering context, but a more expensive check does not substitute for a missing cheaper checking capability.

A Product-level Work Product therefore requires Instrumental Checks before Low-profile or High-profile Assessment when those later assessments are required.

The same rule applies to software, physical engineering, manufacturing, simulation, human studies, and other project domains.

If an Engineering Layer is insufficiently structured to support useful Instrumental Checks, the proposal treats this as a deficiency in engineering method, data representation, or tooling rather than as justification to begin directly with expensive reasoning.

The Hive creates or proposes Decisions to improve the applicable:

- engineering structure;
- data representation;
- schemas and relations;
- instrumentation;
- validators;
- checklists;
- methods;
- tools.

The objective is to move validation toward explicit and inexpensive mechanisms while preserving the semantics required by the engineering context.

Acceptance stage and check class remain separate dimensions:

- Executor conformity assessment uses the Check Cascade;
- independent Acceptance uses the Check Cascade;
- Acceptance responsibility determines **who performs or owns the assessment**;
- the Check Cascade determines **in what cost order the assessment proceeds**.

Independent Acceptance therefore does not justify bypassing Instrumental or Low-profile checks.

## 9. Scale, Magnification, Decision Blast Radius, and Decision Extent

Scale provides a common engineering-order reference for Engineering Layers.

Magnification uses that Scale to locate engineering information and to control bounded traversal of the underlying graph data model.

Decision Blast Radius and Decision Extent use the same propagation geometry at different stages of a Decision lifecycle.

### 9.1 Scale

The proposal uses one project-wide **interval Scale**.

Scale provides the common reference for engineering order of magnitude among Engineering Layers.

Engineering Layers do not require fixed or pre-assigned numerical coordinates. Their Scale placement is relative and is established from Magnification.

Scale establishes:

- coarser/finer order;
- adjacency;
- interval distance;
- Scale delta;
- alignment required for direct cross-Domain engineering relations.

The occupied Scale can evolve as engineering work establishes additional Engineering Layers.

Such evolution does not require a predefined hierarchy of Layer names.

### 9.2 Scale interval and distance

Let:

$$\delta_s>0$$

denote one adjacent Magnification interval on Scale.

For Engineering Layers $L_i$ and $L_j$, let:

$$\Delta s(L_i,L_j)$$

denote their signed Scale delta. The sign identifies the project-defined coarser/finer direction.

For adjacent Layers in one Domain:

$$Adjacent_d(L_i,L_j)\Rightarrow |\Delta s(L_i,L_j)|=\delta_s.$$

If the current Domain-local path from $L_i$ to $L_j$ contains $n$ adjacent Scale intervals, then:

$$|\Delta s(L_i,L_j)|=n\delta_s.$$

Scale delta is therefore additive over adjacent Magnification intervals.

Absolute numerical Scale coordinates are optional representations and are not part of Engineering Layer identity or Scale semantics.

### 9.3 Engineering Layer establishment and refinement

Each scale-sensitive semantic element belongs to one Engineering Layer for the applicable semantic role.

Therefore:

$$Layer(x)=L_i\Rightarrow Scale(x)=Scale(L_i).$$

A semantic element does not directly belong to several Engineering Layers for the same semantic role.

A new Engineering Layer is established when governed engineering information requires a Magnification distinct from the currently adjacent Layers.

Suppose $L_i$ and $L_j$ are adjacent and engineering work establishes intermediate Layer $L_k$. The refined order is:

$$Scale(L_i)<Scale(L_k)<Scale(L_j).$$

Adjacency becomes:

$$Adjacent_d(L_i,L_k)$$

and:

$$Adjacent_d(L_k,L_j).$$

The new adjacent relations retain the same Scale-interval semantics:

$$|\Delta s(L_i,L_k)|=|\Delta s(L_k,L_j)|=\delta_s.$$

The current endpoint distance therefore becomes:

$$|\Delta s(L_i,L_j)|=2\delta_s.$$

The pre-existing Layers retain their identity and relative order. Historical Engineering States retain the Scale relations and deltas applicable at their observation time.

A materialized Engineering Object can contain engineering information belonging to several Engineering Layers without becoming one multi-Layer semantic element. The graph represents the applicable Layer-local semantic elements separately and relates them through valid graph relations and traversal.

### 9.4 Direct relation locality

A direct engineering relation is valid only between elements aligned at the same Scale position under the current Magnification relations.

For direct semantic relation $r$:

$$r(x,y)\Rightarrow Scale(x)=Scale(y).$$

Therefore:

$$Scale(x)\neq Scale(y)\Rightarrow\neg DirectEngineeringRelation(x,y).$$

Equal Scale is necessary but not sufficient. Scale alignment is an engineering relation, not equality of immutable numerical coordinates.

The underlying graph can structurally contain an edge between arbitrary addressable nodes. Such an edge acquires engineering relation semantics only when the applicable validators succeed.

Scale, Domain topology, Scope, revision, Evidence, authority, Contract, information boundary, and relation-specific semantics constrain engineering use of graph connectivity.

These restrictions constrain long-range semantic coupling and resulting potential change impact without requiring the underlying graph representation to prohibit arbitrary structural edges.

### 9.5 Parallel engineering domains

Engineering Domains use the same project-wide interval Scale.

Each Domain establishes only the Engineering Layers required by its engineering information. Domains therefore do not need identical Layer structures.

Direct cross-Domain relations are valid only where the participating Layers are aligned at the same Scale position:

$$CrossDomainRelation(x_a,x_b)\Rightarrow Scale(x_a)=Scale(x_b).$$

Cross-Domain alignment does not create missing intermediate Layers in either Domain.

An intermediate Layer is established only where that Domain's engineering information requires another Magnification.

**Illustration.**

Two Domains can contain different numbers of Engineering Layers while still having particular Layers aligned for direct cross-Domain information exchange. This Illustration defines no mandatory Layer hierarchy, Layer count, or naming scheme.

### 9.6 Magnification

Magnification is an operator on Scale.

Applied to engineering information, Magnification determines its relative engineering order with respect to other applicable engineering information.

Scale uses that Magnification to establish Layer ordering, alignment, adjacency, interval distance, and Scale delta.

Operational Magnification performs bounded traversal through those established Scale relations toward applicable coarser or finer engineering information.

Conceptually:

$$Magnify(x,m_t)=Project_{m_t}(Traverse(x,m_t,B))$$

where $m_t$ is the target Magnification and $B$ is the applicable traversal budget.

Magnification uses existing engineering information and established Engineering Layers. It does not create missing engineering content.

Where engineering activity determines that another distinct Magnification is required, governed engineering work establishes an additional Engineering Layer. Scale then incorporates the new Layer using the ordinary interval semantics of adjacent Layers.

### 9.7 Magnification change and permitted Scale traversal

Operational Magnification follows the established Scale relations toward applicable coarser or finer engineering information.

Magnification operates on engineering information that exists or is explicitly created through governed engineering activity.

It does not manufacture missing detail.

#### 9.7.1 Adjacent Engineering Layer rule

Adjacency is evaluated against the Engineering Layers established in the applicable Engineering State.

Two Engineering Layers in Domain $d$ are adjacent when no established Layer of that Domain lies between them in Scale order:

$$Adjacent_d(L_i,L_j)\Leftrightarrow\neg\exists L_k:\ L_k\in d\land Scale(L_i)<Scale(L_k)<Scale(L_j).$$

A Scale transition occurs only between adjacent Layers:

$$CrossScaleTransfer(L_i,L_j)\Rightarrow Adjacent_d(L_i,L_j).$$

A Domain can contain any number of Engineering Layers required by its information structure.

When an intermediate Layer is established, adjacency is refined accordingly. Each new adjacent relation retains the same Scale-interval semantics, while the delta between the pre-existing endpoint Layers increases by the inserted interval.

The underlying graph can contain a shorter structural edge, but that edge does not override the current Scale and adjacency relations.

Magnification therefore prevents vertical semantic compaction.

#### 9.7.2 No diagonal propagation between parallel engineering Domains

A single relation or transfer must not simultaneously change Domain and Scale position.

For different Domains $d_a\neq d_b$:

$$Domain(x)=d_a\land Domain(y)=d_b\land Scale(x)\neq Scale(y)\Rightarrow\neg DirectRelation(x,y).$$

The same restriction applies to Exchange Items.

One Exchange Item performs at most one engineering-topology transition: a Scale transition between adjacent Engineering Layers inside one Domain, or a cross-Domain transition at the same Scale position.

Where an engineering effect requires both changes, separate validated exchanges and an intermediate local interpretation establish the path.

No single Exchange Item represents a diagonal shortcut.

### 9.8 Exchange Item and Feedback Exchange Item propagation

A consequence crossing an Engineering Layer boundary is transferred through an Exchange Item or Feedback Exchange Item and interpreted at the receiving Layer.

One governed transfer uses one Exchange Item identity.

For Decision propagation:

$$Decision_i\rightarrow ExchangeItem_{i\rightarrow j}\rightarrow LocalInterpretation_j.$$

The Exchange Item delivers the boundary-relative Decision projection.

Where a new local Decision is required:

$$LocalInterpretation_j\rightarrow Decision_j.$$

An Objective Exchange Item transfers a Work Product while the Work Product retains its Engineering Object identity and source-Contract role.

For feedback:

$$Evidence_j\rightarrow FeedbackExchangeItem_{j\rightarrow i}\rightarrow LocalInterpretation_i.$$

A Feedback Exchange Item is a specialized Informational Exchange Item. It delivers a boundary-relative projection of the originating Evidence.

An Exchange Item originates in one engineering context and is consumed by the context on the other side of its governed boundary. Consumption does not create another Exchange Item identity.

Forward and reverse graph traversal use the same Exchange Item.

The transfer preserves applicable source identity and provenance. It does not make the source Decision, Evidence, Work Product, or authority directly operative at the receiving Engineering Layer.

Every receiving Layer performs its own local interpretation.

### 9.9 Human locality across Engineering Layers

The Scale rules apply equally to Human-originated Decisions.

A Human participating in multiple Engineering Layers does not create a direct semantic or authority path among them.

$$Participates(h,L_i)\land Participates(h,L_j)\not\Rightarrow AuthorityPropagation(h,L_i,L_j).$$

A Human Decision at $L_j$ must be supported by the applicable local engineering information and authority at $L_j$.

Information known to the Human from another Engineering Layer can affect the receiving Layer only through the ordinary governed engineering mechanisms applicable to that Layer.

Human identity cannot substitute for missing Layer artifacts, traceability, Exchange Items, Feedback Exchange Items, or local Decisions.

### 9.10 Missing representations and terminal traversal

If Magnification traversal cannot find applicable engineering information at the required coarser or finer order, it returns no applicable representation.

Magnification does not establish missing engineering information merely because a consumer requests another Magnification.

Where the required information is absent, truthful incompleteness applies.

If the engineering need requires an additional Magnification, the absence is recorded as a Gap and governed engineering activity can establish the required Engineering Layer and content.

The current element remains terminal for that traversal direction until the engineering topology is extended.

### 9.11 Exploration can extend the engineering state

A Contract can explicitly authorize engineering work that creates previously absent coarser or finer engineering information.

If exploration legitimately produces new element $y$:

$$Explore(C,x)\rightarrow Create(y).$$

The resulting element becomes governed Engineering State when it is intentionally recorded with the applicable semantic identity, provenance, status, Scope, and validation.

Therefore:

$$MagnificationTraversal\neq SolutionSpaceExploration.$$

Magnification traverses established Scale relations.

Engineering exploration can create engineering information. Where that information requires a distinct Magnification, engineering exploration can also establish a new Engineering Layer.

Establishing the Layer inserts another Scale interval into the current Domain topology. Existing Layer identities and order remain unchanged, while Scale deltas are evaluated against the refined current topology.

### 9.12 Magnification band

A normal scale-sensitive semantic element belongs to one Engineering Layer for one semantic role.

Audit can nevertheless detect content whose semantic construction spans incompatible Engineering Layers.

A Magnification band represents the ordered Scale span over which that incompatible content occurs. It does not imply a predefined numerical Layer system.

Represent the observed range as:

$$Band(x)=[m_{min},m_{max}].$$

For a clean element:

$$m_{min}=m_{max}.$$

A non-zero band:

$$m_{min}\neq m_{max}$$

is an abnormal condition.

It can indicate malformed import, faulty extraction, inappropriate aggregation, incorrect graph-node construction, legacy data problems, or another defect.

A Magnification band is not a normal compatibility mechanism.

Confirmed mixed-level content requires rework assessment.

### 9.13 Magnification band, Brittleness, and Confidence

A Magnification-band anomaly directly affects Brittleness assessment because mixed-level content makes local change more likely to create disproportionate propagation, rework, or invalid dependencies.

Therefore:

$$MagnificationBand(x,t)\Rightarrow ReassessBrittleness(x,t).$$

Brittleness can in turn affect the applicable operational Confidence:

$$Brittleness(x,t)\rightarrow ConfidenceUpdate(q,t).$$

There is no universal direct rule:

$$MagnificationBand(x,t)\Rightarrow PermanentConfidencePenalty.$$

The condition is transient for Confidence.

When the malformed element is corrected and the mixed-level condition no longer exists, it is no longer an active Confidence input.

Its history remains available for post-mortem analysis and future Brittleness assessment.

Thus the intended dependency is:

$$MagnificationBand\rightarrow Brittleness\rightarrow Confidence$$

where applicable, rather than a permanent direct Confidence penalty.

### 9.14 Execution sub-scale

An Engineering Layer can contain a local execution sub-scale.

Execution sub-scale positions do not introduce additional engineering Magnification and therefore do not add Scale intervals.

For Engineering Layer $L_i$, let:

$$\epsilon\in E_i$$

represent a local execution sub-scale position.

An execution position can therefore be represented as:

$$(L_i,\epsilon).$$

The execution sub-scale can arrange parallel work, sequential implementation, local integration order, verification gates, implementation gates, and rework loops without changing the Layer's position in the engineering Scale.

Therefore:

$$ExecutionDepth\not\Rightarrow EngineeringScaleChange.$$

But:

$$ExecutionDepth\Rightarrow PossibleExecutionSubScaleDifference.$$

### 9.15 Contract topology does not define engineering Scale

Contract hierarchy alone does not establish Scale.

Therefore:

$$ChildContract(C_c,C_p)\not\Rightarrow FinerScale(C_c,C_p).$$

Parent, child, integration, and verification Contracts can operate at different execution sub-scale positions while remaining inside the same Engineering Layer.

A Contract can also genuinely operate at another Scale position when its engineering content establishes that relationship.

Contract topology itself does not determine which case applies.

### 9.16 Decision Blast Radius

Decision Blast Radius is calculated for a **Decision Candidate before commitment**.

For Decision Candidate $d^{candidate}$ evaluated against current Engineering State $X_t$:

$$BR(d^{candidate},X_t)$$

is the calculated reach of the change through the engineering state available to the Decision exploration.

Decision Blast Radius answers:

> **If this Decision Candidate were applied to the current engineering state, how far would the change propagate?**

The calculation can discover affected Decisions, Engineering Layers, Exchange Items, Work Products, Contracts, verification, integration, Product state, physical realization, or other material engineering consequences.

It is computation over a candidate state.

It is not commitment.

Therefore:

$$Calculated(BR(d^{candidate},X_t))\not\Rightarrow Committed(d).$$

### 9.17 Decision Blast Radius, feasibility, and economy

Calculating Decision Blast Radius is part of deciding whether the Decision Candidate is viable.

The calculated propagation can expose an empty feasible Solution Space, inability of an affected Engineering Layer to accommodate the change, excessive Work Product rework, reverification or reintegration, unavailable capability, Resource Envelope violation, physical or supplier consequences, unacceptable engineering or economic impact, or another reason not to commit the candidate.

Conceptually:

$$CalculateBlastRadius(d^{candidate},X_t)\rightarrow AssessFeasibilityAndEconomy(d^{candidate}).$$

The resulting assessment can lead to commitment, revision, further exploration, deferral, or rejection of the candidate.

A large Decision Blast Radius does not automatically invalidate a candidate.

A small Decision Blast Radius does not automatically justify it.

Blast Radius exposes propagation structure so that the Hive can assess whether the change is technically and economically rational before commitment.

### 9.18 Decision Extent

Decision Extent applies to a **committed Decision**.

For committed Decision $d$:

$$DecisionExtent(d,t)$$

records how far the Decision has actually propagated through materialized engineering state at time $t$.

Decision Extent answers:

> **How far has this committed Decision already propagated?**

Decision Extent makes actual consequences visible before they become hidden rework, refactoring, reverification, reintegration, coordination, physical change, or other engineering cost.

Decision Extent is temporal:

$$DecisionExtent(d,t_1)\neq DecisionExtent(d,t_2)$$

in general.

As engineering proceeds, previously unknown effects can appear and the observed Decision Extent can grow.

### 9.19 Decision Blast Radius and Decision Extent

Decision Blast Radius and Decision Extent measure the same kind of propagation reach at different stages.

Decision Blast Radius is calculated from the pre-commit candidate state:

$$BR(d^{candidate},X_{precommit}).$$

Decision Extent is observed from committed engineering state:

$$DecisionExtent(d,t).$$

They need not be equal.

It is possible that:

$$DecisionExtent(d,t)<BR(d^{candidate},X_{precommit})$$

because downstream Engineering Layers absorb the change earlier than the initial calculation indicated.

It is also possible that:

$$DecisionExtent(d,t)>BR(d^{candidate},X_{precommit})$$

because subsequent engineering exposes consequences not represented in the state used for the original Blast Radius calculation.

Therefore:

$$DecisionExtent(d,t)\lessgtr BR(d^{candidate},X_{precommit})$$

is legitimate.

A material deviation between calculated Blast Radius and observed Decision Extent is itself useful engineering information and can trigger reassessment.

### 9.20 Decision Extent and Brittleness

Decision Extent and Brittleness answer different questions.

**Decision Extent asks:**

> **How far has this Decision propagated?**

**Brittleness asks:**

> **How severe is the engineering and economic consequence of a relatively small, subtle, local, or wrong-Magnification trigger?**

A Decision can have large Decision Extent without being brittle when a broad change is expected to affect a broad region.

It can have small Decision Extent but high Brittleness when a localized effect is disproportionately expensive.

It can have both large Decision Extent and high Brittleness, which is a strong reason for Decision reassessment.

Neither property is inferred from the other.

### 9.21 Nearest affected Engineering Layer

Propagation stops at the nearest Engineering Layer in the affected domain that can accommodate the Decision Candidate within its local Solution Space and applicable domain-local propagation boundary.

For Decision Candidate $d^{candidate}$ and affected Engineering Layer $L$, let $X'$ be the prospective Engineering State produced by local accommodation of that Decision.

Local accommodation requires:

$$CanAccommodate(d^{candidate},L,X')\Rightarrow\mathcal F(X')\neq\varnothing.$$

The calculated local propagation must also remain inside the applicable single-domain extent established by the Project Profile.

The nearest affected Layer is therefore established from feasible change accommodation, not merely numerical Scale distance.

If the Layer absorbs the change locally, propagation stops.

If it cannot, the applicable information is materialized for the next adjacent Engineering Layer.

### 9.22 Multi-domain change

A Decision can affect several engineering domains.

Each affected domain evaluates the change in its own Solution Space and determines its own accommodation locality.

For:

$$AffectedDomains(d^{candidate})$$

the applicable domain contexts are consulted individually.

One domain can absorb the change locally while another requires propagation to another Engineering Layer.

There is no requirement that all affected Domains reach the same Magnification.

Cross-domain coordination remains limited to same-Scale relations.

A change requiring both domain transition and Scale transition is decomposed into valid same-Scale cross-domain relations and adjacent-layer domain-local propagation.

### 9.23 Scale and Decision-propagation invariants

> **One project-wide interval Scale:** all Engineering Domains use the same engineering Scale.

> **No fixed absolute coordinates:** Scale semantics depend on order, intervals, deltas, and alignment rather than permanent numerical positions.

> **Magnification establishes relative placement:** relative engineering Magnification determines Layer placement; Scale establishes ordering, alignment, adjacency, interval distance, and delta among those Layers.

> **Adjacent interval preservation:** adjacent Engineering Layers use the same Scale-interval semantics.

> **Dynamic Layer insertion:** an intermediate Engineering Layer can be established when engineering information requires another Magnification.

> **Refinement changes current delta:** inserting an intermediate Layer replaces one adjacent interval by two adjacent intervals; the former endpoint distance increases while Layer identity and order remain preserved.

> **Historical Scale state:** previous Engineering States retain their previous adjacency and Scale deltas.

> **Scale-local semantic elements:** a scale-sensitive graph element belongs to one Engineering Layer for the applicable role.

> **Material object versus graph representation:** one materialized artifact can contain representations from several Engineering Layers or Magnifications, while the underlying graph data model represents the corresponding semantic elements separately.

> **Direct relation locality:** $r(x,y)\Rightarrow Scale(x)=Scale(y)$.

> **Same-Scale cross-Domain relations only:** direct relations between parallel Domain or Product topologies cannot be diagonal.

> **Adjacent-Layer propagation only:** a Scale transition must not bypass an established intermediate Engineering Layer.

> **Magnification is an operator:** Magnification locates engineering information by relative order and performs bounded traversal; it does not define another engineering axis.

> **Magnification traversal does not generate detail:** governed engineering activity creates missing information and any required intermediate Layer.

> **No Human shortcut:** a Human participating at multiple Engineering Layers does not create cross-layer authority, support, Evidence, or Decision semantics.

> **Magnification band is abnormal:** incompatible Magnifications inside one semantic element require rework assessment.

> **Magnification-band effect is mediated through Brittleness:** $MagnificationBand\rightarrow Brittleness\rightarrow Confidence$ where applicable.

> **Decision Blast Radius is calculated before commitment.**

> **Decision Blast Radius calculation is non-mutating.**

> **Decision Blast Radius participates in feasibility and change-economy assessment.**

> **Decision Extent belongs to a committed Decision.**

> **Decision Extent is temporal.**

> **Decision Extent can be smaller or larger than the original Decision Blast Radius.**

> **Nearest affected Engineering Layer is determined by feasible local accommodation and domain extent, not Scale distance alone.**

> **Multi-domain change requires domain-local accommodation assessment.**

> **Execution depth can use a local sub-scale without changing engineering Scale.**

**Illustration — Figure 9-1.**

Figure 9-1 visualizes the interval Scale, dynamic Engineering Layer refinement, Magnification traversal, parallel Engineering Domains, same-Scale cross-Domain exchange, adjacent-Layer propagation, execution sub-scale, Decision Blast Radius, and Decision Extent. It shows prohibited diagonal and Layer-skipping transfers only as rejected cases. The figure derives from §9 and introduces no additional semantics. The rendering specification is maintained in `../assets/prompts/figure_9_1_prompt.md`.


## 10. Decisions, trade space, exploration, and human intervention

### 10.1 Trade space

For bounded engineering problem:

$$q,$$

the Trade Space:

$$T(q,t)$$

is the project-visible subset of the applicable Solution Space represented for comparison or exploration at observation point $t$.

The Trade Space can contain candidates with:

- established feasibility;
- established infeasibility;
- unresolved feasibility;
- pending evaluation.

The currently feasible part represented inside the Trade Space is:

$$\mathcal F(X_t)\cap T(q,t).$$

Engineering exploration can enlarge or restructure:

$$T(q,t)$$

inside:

$$\mathcal S_\kappa.$$

A changed Space-defining context provides the corresponding Solution Space for subsequent Trade Spaces.

A Trade Space can contain discrete alternatives and references to continuous optimization delegated to simulations, field tests, calibration systems, or external optimizers. Continuous parameter optimization is not automatically Hive global search.

### 10.2 Local and global extrema

For candidate $x$ and declared neighborhood $N(x)$:

$$LocalOpt(x,N)\Leftrightarrow \nexists y\in N(x):Better(y,x).$$

For theoretical Solution Universe $\Omega$:

$$GlobalOpt(x,\Omega)\Leftrightarrow \nexists y\in\Omega:Better(y,x).$$

The Hive normally knows only a project-visible subset of $\Omega$. A local optimum can therefore be established relative to a declared neighborhood while global optimality remains unknown.

**Extremum Exploration** deliberately expands the active neighborhood or opens a materially different trajectory to search for another local extremum or to challenge whether the current region is adequate. It does not imply exhaustive global search.

### 10.3 Trajectories, clusters, and outliers

A trajectory is a temporally ordered path of candidate outcomes and Decisions for one problem. A cluster is sufficiently independent support for one trajectory. Cluster power controls resource survival, not truth.

An outlier is preserved even if it has low current support:

$$Outlier(o)\land Discovered(o)\Rightarrow Preserve(o).$$

If an outlier later gains evidence, novelty value, or post-mortem relevance, it can become active without reconstructing lost reasoning.

### 10.4 Reshuffling

Reshuffling is primarily a **vertical change and Decision-rework process** that occurs when an Engineering Layer committed to a Product direction without exploring its Solution Space deeply enough to support delivery through the affected downstream layers.

The originating layer effectively treated its current solution as if it were sufficient for complete Product delivery in one step. Downstream engineering then discovers constraints, incompatibilities, missing Decisions, excessive Decision Extent, or other facts that the original exploration did not expose.

These findings propagate upward through the applicable adjacent-layer propagation and Exchange Item mechanisms and can require the originating or intermediate layers to revise Decisions that were previously treated as stable.

Reshuffling can therefore include:

- reopening an upstream Decision;
- revising a Product or interface constraint;
- changing downstream Exchange Items;
- invalidating or revising dependent Decisions;
- Work Product rework;
- reverification and reintegration;
- Contract revision;
- renewed exploration at one or more Engineering Layers.

Reshuffling is primarily vertical because its cause is a mismatch between the depth of exploration performed at one Engineering Layer and the engineering reality discovered at adjacent downstream layers.

Ordinary local correction inside one Engineering Layer is **not** Reshuffling when the layer can absorb the change without reopening commitments at another Scale.

The preferred engineering behaviour is:

> An Engineering Layer explores sufficiently before committing downstream constraints, while downstream findings propagate upward only to the nearest Engineering Layer whose Decision must change.

This does not require exhaustive exploration before every commitment. The required depth is bounded by the current Product context, available evidence, Resource Envelope, and expected Decision Extent.

#### 10.4.1 Rollback

Rollback is an Evidence-supported engineering activity that completely cancels one previously committed Decision.

Rollback is governed by $C_R$ and belongs to one Engineering Layer $L_R$.

The Rollback target is $d_0$. The corresponding Contract context and materialized Work Product are $C_0$ and $w_0$. Thus:

$$\{d_0,C_0,w_0\}\subseteq\Gamma_R(C_R).$$

Applicable Evidence establishes the engineering basis for cancellation of $d_0$.

Rollback operates against the current Engineering State rather than restoring a historical Product snapshot. Its purpose is complete cancellation of the selected Decision and its applicable materialized continuation.

#### 10.4.2 Deprecation and Rollback

Deprecation and Rollback describe different Product evolution.

**Deprecation** is forward evolution. Later engineering supersedes or replaces earlier engineering and continues Product development through the newer realization.

**Rollback** cancels a previously committed Decision and removes its applicable materialized continuation from the current Product state.

Rollback therefore acts on current Product realization rather than returning the Product to the historical state that existed before the cancelled Decision. Product Evolution History remains in $K_t$ while active Materialized Product State changes.

::: {custom-style="Illustration"}
**Illustration - Deprecation versus Rollback.** An earlier Product realization uses incandescent lighting. Ordinary engineering later replaces it with LED lighting; this is Deprecation because the Product continues through the newer lighting realization. In parallel, the wiring-harness topology evolves for unrelated engineering reasons. A later Rollback cancels the original lighting Decision completely. Because the LED realization belongs to the continuation of that Decision, the lighting succession is included in the Rollback Closure. The current wiring-harness topology remains because it is outside that closure. The resulting Product retains the parallel harness evolution and contains no materialized realization of the cancelled lighting Decision. The Product is not restored to the earlier historical snapshot.
:::

#### 10.4.3 Rollback Closure

The Rollback Closure $\Gamma_R(C_R)$ is the least same-Layer set of Decisions, Contracts, and Work Products whose active effects have to be cancelled or rematerialized together to completely cancel $d_0$.

The initial Rollback subject belongs to the closure:

$$\{d_0,C_0,w_0\}\subseteq\Gamma_R(C_R).$$

The closure is confined to the Rollback Layer:

$$\Gamma_R(C_R)\subseteq D_{L_R}\cup C_{L_R}\cup W_{L_R}.$$

Later same-Layer engineering enters the Rollback Closure when it forms part of the deprecating, superseding, replacing, or materially dependent continuation of an element already in the closure and cannot remain valid after cancellation of that element.

The Decision-Contract-Work Product succession is therefore included whenever the materialized engineering history requires it. A Rollback cannot select an isolated historical Work Product while retaining a later same-Layer realization whose validity depends on the cancelled Decision.

#### 10.4.4 Rollback of current materialization

Let $R_t(C_R)$ be the subset of the active Materialized Product State attributable to the Rollback Closure and incompatible with cancellation of $d_0$. For a successful Rollback:

$$R_t(C_R)\subseteq P^{mat}_t$$

and the resulting active materialization is:

$$P^{mat}_{t+1}=P^{mat}_t\setminus R_t(C_R).$$

Rollback therefore removes the complete materialized continuation being cancelled from current Product realization. Materialized engineering outside $R_t(C_R)$ remains in the Product and preserves compatible parallel engineering.

If the set difference does not produce a valid same-Layer engineering state, the Rollback Closure expands to include additional required same-Layer engineering or the Rollback remains blocked. Rollback therefore removes a complete engineering continuation rather than an arbitrary subset selected for convenience.

#### 10.4.5 Single-Layer boundary

Rollback is local to one Engineering Layer.

If cancellation of $d_0$ exposes an effect requiring a Decision on another Engineering Layer, that effect enters the ordinary adjacent-Layer engineering process. The Rollback Contract does not cancel Decisions or materialized Work Products owned by another Engineering Layer.

This separates responsibility for local cancellation from Product-wide engineering response.

#### 10.4.6 Previously rolled-back history

Rollback does not traverse backward through an element already cancelled by a successful Rollback.

If such an element is required to construct the proposed Rollback Closure, the new engineering problem is formulated from the applicable current Materialized Product State.

This prevents repeated cancellation of the same historical engineering continuation and bounds Rollback-induced Brittleness.

#### 10.4.7 Rollback classification

Rollback has one engineering purpose: complete cancellation of one committed Decision and the same-Layer materialized continuation that cannot remain valid without it.

The resulting Work Product can change any technical aspect required to materialize that cancellation and retain a valid same-Layer remainder.

A request that introduces a replacement realization or materially new Product intent in addition to cancellation is not a Rollback. Such a request is rejected under the Rollback classification. Continuation as ordinary engineering work is a separate Decision and Contract activity.

#### 10.4.8 Rollback outcome

Rollback Solution Exploration establishes the Rollback Closure and evaluates the resulting same-Layer state.

Possible outcomes include:

- successful Rollback;
- expansion of the Rollback Closure;
- additional Evidence requirement;
- a Known Gap;
- a blocker in current materialized state;
- rejection of Rollback classification;
- absence of a viable Rollback.

Successful Rollback produces the Work Product required by $C_R$ and updates the Materialized Product State according to §10.4.4.

The cancelled Decision, affected Contracts, Work Products, Evidence, and historical relations remain in Product Evolution History $K_t$. Failed, cancelled, rejected, and non-selected Rollback exploration also remains historically addressable under the ordinary exploration, Evidence, Contract-history, and provenance model.

#### 10.4.9 Rollback and traceability

Rollback uses the existing multidimensional Product graph and ordinary relation algebra.

The Rollback Closure provides a bounded same-Layer filter for Rollback reasoning and traceability traversal. Rollback Contract properties can also be used as query filters.

Historical and current engineering relations retain the same traversal, Scope, revision, Scale, and semantic-validation rules used by ordinary Product evolution.

An implementation can represent a Rollback Contract with a specialized node kind and additional properties.

### 10.5 Human intervention geometry

Let current Hive candidate set be $B$ and human input normalized to set $A$. Human interaction can create exact match, narrowing, broadening, equality, partial intersection, or disjoint geometry relative to $B$. The human-interaction class is orthogonal to this set geometry.

Human input is assessed before execution. Human authority does not create mathematical or engineering feasibility.

## 11. Contracts and Product delivery

### 11.1 Contract structure

A Contract records **who** is responsible, **what** result is expected, and **when or under which dependencies** execution can proceed.

**Who** identifies the Issuer, Assignment and resulting Executor, supplementary parties where applicable, and any explicitly delegated Acceptance responsibility.

**What** identifies the Product target, required Work Product, Executor Obligation, Resource Envelope, Acceptance rules, and applicable enforcement.

**When and dependencies** identify prerequisites, expected dependencies, execution topology, and revision/time context required to determine when execution can start, continue, block, submit a result, or require reassessment.

The Contract is durable and revision-qualified. Previous Contract states remain addressable so that later fulfilment, failure, discontinuation, reassignment, or post-mortem analysis does not rewrite execution history.

A Contract becomes executable only when its Assignment is unambiguous for the applicable scope. Conflicting directives that would establish incompatible Assignments for the same scope require resolution under the applicable authority rules before execution proceeds. Human-originated input does not bypass this rule. The Human role and authority model is a prerequisite of safe execution and is defined separately from this Contract section.

A Contract identifies its Product relationship and required Work Product independently. A Contract can create or modify Product state, verify Product state, analyze Product state, produce Evidence about Product state, construct a Work Product without directly changing Product state, or perform another Project Profile-defined engineering responsibility. The Contract must not infer Product effect merely from the type or existence of its Work Product.

The Product provides the top-level scope and intent context; Contracts are bounded execution mechanisms inside that Product context. Product identity and Product-level intent can continue while Contracts are created, revised, split, fulfilled, discontinued, or replaced.


#### 11.1.1 Formal Contract data structure

A Contract is not one lifecycle-state object and is not one mutable tuple whose fields are destructively updated.

A Contract has:

1. a stable Contract identity;
2. one or more immutable Contract definition revisions;
3. a temporal lifecycle state associated with an applicable definition revision;
4. an append-only execution and governance history.

Conceptually:

$$Contract(C)=(Identity(C),Definitions(C),Lifecycle(C),History(C)).$$

These components have different semantics.

Changing lifecycle state does not by itself create a new Contract definition revision.

Changing governed Contract content can create a new definition revision.

Historical events do not mutate earlier definitions or lifecycle observations.

##### 11.1.1.1 Contract identity

Every Contract has a stable identity:

$$cid(C).$$

Contract identity persists across ordinary Contract revisions:

$$C^0,C^1,\ldots,C^k.$$

Therefore:

$$cid(C^i)=cid(C^j)$$

for revisions of the same Contract.

A successor Contract has a different identity:

$$Succeeds(C_2,C_1)\Rightarrow cid(C_2)\neq cid(C_1).$$

The successor relation preserves continuity without pretending that materially different governed work remains the same Contract.

##### 11.1.1.2 Contract definition revision

A Contract definition revision is an immutable governed record.

For revision $k$:

$$C^k=\langle cid,k,type,issuer,authorityRef,productContext,productTarget,workProductRequirement,assignment,executionPolicy,resourceBudget,prerequisiteSpec,dependencySpec,acceptanceSpec,informationPolicy,enforcementSpec,topologyRef,profileRef,revisionMeta\rangle.$$

This is a conceptual typed record.

It does not require a positional tuple in implementation.

A conformant implementation can use structured objects, graph nodes/relations, database records, SysML elements, documents, or another representation while preserving the same semantics.

##### 11.1.1.3 Contract type

$$type(C^k)$$

identifies the Project Profile-defined Contract class relevant to execution policy and other Contract-specific rules.

Contract type can distinguish, for example:

- development;
- production;
- verification;
- test;
- integration;
- analysis;
- external supply;
- another project-defined Contract class.

The common model does not define a universal Contract taxonomy.

The existing execution-policy relation remains:

$$ExecutionPolicy(type(C),PP).$$

Contract type therefore selects applicable policy.

It does not by itself establish execution validity.

##### 11.1.1.4 Issuer and authority reference

$$issuer(C^k)=a$$

identifies the Actor that created or issued the applicable Contract revision.

The Contract can preserve a reference to the authority basis used to validate that operation:

$$authorityRef(C^k).$$

The authority reference does not make authority an internal Contract-owned property.

It provides provenance to the explicit external authority model.

Validity requires:

$$AuthorizedFor(Issuer(C^k),IssueOrRevise,C^k,\sigma,t,\kappa).$$

Therefore:

$$Issuer(C)=a\not\Rightarrow UniversalAuthority(a).$$

The authority remains operation-, Scope-, time-, and context-qualified.

##### 11.1.1.5 Product context and Product target

The Contract definition contains both:

$$productContext(C^k)$$

and:

$$productTarget(C^k).$$

These are not identical.

`productContext` identifies the Product whose top-level scope and intent establish the engineering context.

`productTarget` identifies the Contract-specific engineering objective inside that Product context.

Conceptually:

$$ProductTarget(C^k)=(P,\tau_P)$$

where $P$ is the Product and $\tau_P$ is the Contract-specific target condition or target semantics.

Therefore:

$$ProductTarget(C)\subseteq ProductContext(P)$$

conceptually.

The target can concern creation, modification, analysis, verification, Evidence generation, integration, delivery, or another governed Product-related effect.

##### 11.1.1.6 Required Work Product specification

The Contract definition does not contain the future submitted Work Product revision itself.

It contains a **Work Product Requirement**:

$$WPReq(C^k).$$

Conceptually:

$$WPReq(C^k)=(role,schema,semanticScope,validationRules,traceabilityRules,supplementaryInformation,informationBoundary).$$

The exact schema belongs to the Project Profile.

The actual submitted Work Product is linked later through lifecycle execution:

$$Submit(w^r,C^k).$$

Thus:

$$WPReq(C^k)\neq w^r.$$

This prevents the Contract requirement and its eventual fulfilment artifact from collapsing into one object.

##### 11.1.1.7 Assignment

Assignment remains part of the Contract definition:

$$Assignment(C^k,a).$$

For an executable Contract:

$$\exists!a:\ Assignment(C^k,a).$$

The definition records one accountable Executor, not the set of all participants.

Therefore:

$$Executor(C^k)\neq Participants(C^k)$$

in general.

A Contract can involve many Human, Hive, Agent, supplier, tool, facility, or organizational participants while retaining one accountable Executor.

A reassignment creates a revised Contract definition when the accountable Executor changes:

$$Executor(C^k)=a$$

$$Executor(C^{k+1})=b.$$

Earlier Assignment remains historical.

##### 11.1.1.8 Obligation is derived Contract semantics

Obligation is not restored as a separately required object.

Instead it is derived from the Contract semantics.

Conceptually:

$$Obligation(C^k)=Fulfil(Executor(C^k),ProductTarget(C^k),WPReq(C^k),AcceptanceSpec(C^k)).$$

This means that the Executor is accountable for either:

- delivering the required Contract result under the applicable Acceptance conditions; or
- explicitly reporting inability to fulfil.

Therefore a separate stored `Obligation` object is optional implementation detail.

The common model requires the semantics, not a second object.

##### 11.1.1.9 Execution policy

Each definition references its applicable execution policy:

$$ExecutionPolicyRef(C^k).$$

Resolved policy determines constraints such as:

- Executor eligibility;
- independence;
- prohibited role combinations;
- development/verification separation;
- permitted Hive topology;
- external-party constraints;
- required physical or organizational separation.

Validity requires:

$$Assignment(C^k,a)\Rightarrow SatisfiesExecutionPolicy(a,C^k,PP).$$

Policy is definition-level governance.

Whether execution can start at time $t$ remains a runtime readiness question.

##### 11.1.1.10 Resource Budget and Resource Envelope

The Contract definition can establish a Contract-specific Resource Budget:

$$R_C^k.$$

The project/Hive has the broader Resource Envelope:

$$R_H.$$

Conceptually:

$$R_C^k\preceq R_H$$

where the Project Profile defines the relevant multidimensional comparison.

The Contract budget can constrain:

- context;
- model calls;
- compute;
- wall time;
- money;
- Human effort;
- energy;
- equipment;
- external capacity;
- another project-defined resource.

Resource allocation is distinct from runtime resource availability.

Therefore:

$$Budgeted(r,C)\not\Rightarrow Available(r,C,t).$$

The latter participates in readiness.

##### 11.1.1.11 Prerequisite specification

The Contract definition contains a set of readiness predicates:

$$PrerequisiteSpec(C^k)=\{p_1,p_2,\ldots,p_n\}.$$

A prerequisite is not limited to another Contract.

It can refer to:

- completion of external work;
- another Contract state;
- availability of a Work Product;
- Product state;
- Evidence;
- computational capacity;
- physical resources;
- facilities;
- manufacturing capability;
- supplier availability;
- legal/commercial condition;
- Human participation;
- environmental condition;
- another Project Profile-defined predicate.

At runtime:

$$Ready(C^k,t)\Rightarrow\forall p\in PrerequisiteSpec(C^k):Evaluate(p,X_t)=TRUE.$$

`UNKNOWN` prerequisite evaluation does not silently become `TRUE`.

The Project Profile determines whether an unresolved predicate blocks readiness or receives another explicit disposition.

##### 11.1.1.12 Dependency specification

A dependency is a typed relation between Contract execution and another stateful subject.

Conceptually:

$$Dependency=(source,target,condition,requiredState,scope,revisionPolicy).$$

For Contracts:

$$DependsOn(C_i,C_j,\delta).$$

A dependency does **not** automatically mean that the target Contract must be `FULFILLED`.

For example the required condition can be:

$$State(C_j)=READY$$

or:

$$State(C_j)=FULFILLED$$

or:

$$Accepted(w_j,C_j)$$

or another defined predicate.

Thus:

$$Dependency\neq CompletionDependency$$

universally.

This is important for parallel engineering.

##### 11.1.1.13 Internal and external dependencies

A Contract dependency target can be inside or outside the Hive-governed Contract model.

For internal Contract $C_i$:

$$DependsOn(C_i,C_j,\delta)$$

can reference another governed Contract.

For external condition $x$:

$$DependsOnExternal(C_i,x,\delta)$$

can represent:

- supplier contract fulfilment;
- legal agreement;
- customer approval;
- external laboratory result;
- regulatory permission;
- physical delivery;
- third-party service;
- another externally governed event.

The Hive need not falsely represent every external process as an internal Hive Contract.

It needs an explicit observable condition and provenance sufficient to evaluate the dependency.

##### 11.1.1.14 Dependency is not authority

Dependency topology transports execution conditions.

It does not create authority.

Therefore:

$$DependsOn(C_i,C_j)\not\Rightarrow AuthorityInheritance(C_i,C_j).$$

Likewise, a parent/child Contract relation does not itself make one Executor authoritative over another Contract.

##### 11.1.1.15 Prerequisite and dependency distinction

A **dependency** describes a relationship.

A **prerequisite** describes a condition that must currently evaluate as satisfied for a defined lifecycle transition.

A dependency can therefore exist without currently gating readiness.

Conceptually:

$$Dependency(C_i,x)\not\Rightarrow x\in ReadyPrerequisites(C_i).$$

The Contract definition or Project Profile establishes when that dependency becomes a readiness predicate.

This prevents every known relationship from unnecessarily serializing execution.

##### 11.1.1.16 Acceptance specification

The Contract definition contains:

$$AcceptanceSpec(C^k).$$

Conceptually:

$$AcceptanceSpec=(ExecutorConformityRules,IndependentAcceptanceRules,EvidenceRequirements,AllowedGapPolicy,DelegationPolicy,DispositionRules,FulfilmentPredicate).$$

This structure defines the applicable assessment semantics.

It does not contain the result of an Acceptance attempt.

Acceptance results belong to lifecycle/history.

##### 11.1.1.17 Fulfilment predicate

The Contract definition explicitly states what constitutes fulfilment.

For ordinary Contract $C$, it includes Acceptance of the required Work Product:

$$AcceptedRequiredWorkProduct(C).$$

For Product Delivery Contract:

$$Fulfilled(C)\Rightarrow AcceptedRequiredWorkProduct(C)\land ProductTargetSatisfied(C).$$

Additional Project Profile-defined fulfilment conditions can apply.

This prevents lifecycle logic from inferring fulfilment merely because a file was submitted or a Product changed.

##### 11.1.1.18 Information policy

The Contract definition contains or references an applicable information policy:

$$InformationPolicy(C^k).$$

It governs:

- information that may enter execution;
- information that may appear in the Work Product;
- protected or proprietary information;
- supplier information;
- personal information;
- internal rationale exposure;
- required provenance;
- cross-boundary materialization;
- other Project Profile-defined information restrictions.

Availability in Solution Space does not mean permission to expose information through a Contract Work Product.

##### 11.1.1.19 Enforcement specification

The Contract can reference project-defined enforcement semantics:

$$EnforcementSpec(C^k).$$

Possible consequences include:

- refusal of Acceptance;
- failed gate;
- rework;
- reassessment;
- escalation;
- prevention of subsequent execution;
- commercial/legal remedy;
- discontinuation;
- another applicable project mechanism.

These are not universal consequences.

The common model requires enforceability to be explicit where the Contract depends on it.

##### 11.1.1.20 Execution topology reference

The Contract definition can reference its execution-topology context:

$$TopologyRef(C^k).$$

This can include relations to:

- parent Contract;
- child Contracts;
- Integrator Contract;
- verification Contract;
- supplier Contract;
- successor Contract;
- Team API context;
- another applicable execution relation.

These topology relations remain distinct from Product topology and authority topology.

##### 11.1.1.21 Project Profile reference

Every Contract definition is interpreted against an applicable Project Profile revision:

$$profileRef(C^k)=PP^m.$$

A Contract cannot silently change meaning because the Project Profile changed later.

Therefore:

$$Interpret(C^k)$$

uses its applicable Project Profile revision unless a governed Contract/Profile migration explicitly establishes another basis.

##### 11.1.1.22 Definition revision metadata

Each Contract definition revision preserves at minimum:

$$RevisionMeta(C^k)=(predecessor,createdAt,effectiveFrom,changeReason,provenance).$$

A Contract definition revision can identify the governed source that caused the revision, including its initiating Decision, Human input, dependency change, Product-state change, authority change, failure or reassessment event, exploration result, or another addressable causal source.

Revision metadata supports historical explanation.

It does not replace canonical relations to the source engineering information.

##### 11.1.1.23 Runtime lifecycle view

The immutable Contract definition and the current lifecycle state remain separate.

For definition revision $C^k$:

$$Runtime(C^k,t)=(State,ReadinessEvaluation,Blockers,ExecutionContext,SubmissionRef,AcceptanceAttemptRef)_t.$$

This is a conceptual runtime projection.

Not every field exists in every state.

For example, before submission:

$$SubmissionRef=\varnothing.$$

Before Acceptance:

$$AcceptanceAttemptRef=\varnothing.$$

The lifecycle state is therefore not embedded permanently into the definition revision.

##### 11.1.1.24 Lifecycle state is temporal

For one unchanged Contract definition:

$$State(C^k,t_1)=READY$$

can later become:

$$State(C^k,t_2)=EXECUTING.$$

No Contract-definition revision is required merely because normal FSM execution occurred.

By contrast, a material Contract semantic change creates:

$$C^k\rightarrow C^{k+1}.$$

The successor definition is then re-evaluated through the accepted FSM entry predicates.

This separates:

$$DefinitionRevision$$

from:

$$LifecycleTransition.$$

##### 11.1.1.25 Contract event history

Contract history is append-only.

Let:

$$History(C)=\langle e_0,e_1,\ldots,e_n\rangle.$$

A Contract event can record, as applicable:

- definition created;
- definition revised;
- Assignment established;
- Assignment changed;
- readiness evaluation;
- lifecycle transition;
- blocker detected;
- blocker cleared;
- execution started;
- inability reported;
- Work Product submitted;
- Acceptance started;
- Acceptance disposition;
- rework requested;
- reassessment entered;
- Product target satisfied;
- Contract fulfilled;
- Contract discontinued;
- successor created;
- another Project Profile-defined event.

Events preserve:

$$(type,time,actor/context,relatedState,provenance).$$

The event log does not need to duplicate all engineering data.

It references Engineering State where possible.

##### 11.1.1.26 Event history is not canonical-state duplication

Contract history must not become an ever-growing copy of Product state or internal reasoning.

It records Contract-relevant state transitions and references the relevant canonical objects.

Therefore:

$$History(C)\neq ReplayOfEntireEngineeringState.$$

This preserves the proposal's state-centric, low-context-overhead architecture.

##### 11.1.1.27 Derived Contract views

Common Contract properties can be computed from definition plus history.

For example:

$$CurrentDefinition(C,t)$$

$$CurrentExecutor(C,t)$$

$$CurrentState(C,t)$$

$$CurrentBlockers(C,t)$$

$$LatestSubmission(C,t)$$

$$LatestAcceptanceDisposition(C,t).$$

These are derived views.

They do not need independent mutable truth stores if the implementation can compute them reliably from canonical Contract state.

##### 11.1.1.28 Definition validity

A Contract definition revision is valid only when its applicable structural rules hold.

At minimum:

$$ValidContractDefinition(C^k)\Rightarrow$$

- stable Contract identity exists;
- exactly one Issuer is identifiable for the revision operation;
- Issuer authority is valid;
- Product context is identified;
- Product target is defined sufficiently for the Contract;
- required Work Product specification exists;
- exactly one Assignment exists where the revision is expected to be executable;
- Assignment satisfies execution policy;
- resource-budget semantics are defined;
- prerequisite/dependency predicates are type-valid;
- Acceptance semantics are defined;
- information-policy references are resolvable;
- applicable Project Profile revision is identified.

A `DEFINED` Contract can still lack executable Assignment or satisfied readiness predicates.

Definition validity therefore does not imply readiness.

##### 11.1.1.29 Partial Contract definition

Creation of Contract identity can precede full executable definition.

This is necessary because the accepted FSM includes:

$$DEFINED.$$

Therefore:

$$ContractExists(C)\not\Rightarrow Executable(C).$$

A partially specified Contract can remain `DEFINED` while missing, for example:

- valid Assignment;
- required prerequisite information;
- Resource Budget;
- dependency resolution;
- another required executable-field value.

Missing required Contract information remains explicit under truthful incompleteness.

##### 11.1.1.30 Material Contract revision

A change requires a Contract-definition revision when it alters governed Contract semantics such as:

- Product target;
- required Work Product;
- Executor Assignment;
- execution policy;
- Resource Budget;
- readiness prerequisites;
- dependency conditions;
- Acceptance rules;
- information boundary;
- enforcement;
- applicable Project Profile basis;
- another material Contract field.

Thus:

$$MaterialContractChange\Rightarrow C^k\rightarrow C^{k+1}.$$

The earlier definition remains addressable.

##### 11.1.1.31 Runtime observation is not automatically Contract revision

Not every environmental change revises the Contract.

For example:

- required compute becomes temporarily unavailable;
- an external dependency changes state;
- a blocker is cleared;
- a test facility becomes available.

These events can change runtime lifecycle state while the Contract definition remains unchanged.

Therefore:

$$RuntimeConditionChange\not\Rightarrow ContractDefinitionRevision.$$

A revision is required only when the governed Contract semantics themselves change.

##### 11.1.1.32 Revision versus successor Contract

A revision preserves Contract identity when the governed obligation remains meaningfully continuous.

A successor Contract is appropriate when the change creates a materially new governed obligation.

Conceptually:

$$SameGovernedObligation\Rightarrow RevisionCandidate$$

whereas:

$$MateriallyNewObligation\Rightarrow SuccessorContractCandidate.$$

The common model does not define one universal numerical threshold between these cases.

The Project Profile determines the applicable identity-continuity rule.

Examples that can justify successor identity include material change of:

- Product purpose;
- accountability model;
- external/legal obligation;
- Work Product semantics;
- delivery model;
- Contract class;
- another project-defined identity criterion.

##### 11.1.1.33 Contract decomposition relation

Contract decomposition is represented as relation, not nested mutable containment.

For parent $C_p$ and child $C_i$:

$$ChildContract(C_i,C_p).$$

The relation is revision-qualified.

A child Contract has its own complete definition:

$$ValidContractDefinition(C_i).$$

Parent fields are not implicitly inherited unless the relevant Project Profile rule explicitly derives them.

In particular:

$$Executor(C_p)=a\not\Rightarrow Executor(C_i)=a.$$

This preserves the already accepted decomposition semantics.

##### 11.1.1.34 Supplementary participants

A Contract can identify or reference supplementary execution participants without turning them into Executors.

Let:

$$Participates(a,C,role).$$

Then:

$$Participates(a,C,role)\not\Rightarrow Executor(C)=a.$$

Supplementary participation can emerge during execution.

Adding a participant requires a Contract revision only when the applicable Contract semantics make that participant definition-governed.

Transient internal Hive Agents need not become Contract-definition fields.

##### 11.1.1.35 Contract data structure and Team API

The Contract definition can reference the applicable Team API boundary.

It does not embed every communication.

Therefore:

$$TeamAPIRef(C)$$

identifies the governed communication context while individual Questions, Requests, Clarifications, Exchange Items, Feedback Exchange Items, and Work Products remain their own addressable elements.

The Contract is governance structure.

It is not a message container.

##### 11.1.1.36 Contract data structure and Confidence

Confidence is **not a Contract-definition field**.

The Hive can maintain:

$$Confidence_H(C,t)$$

as an operational observation associated with execution.

Contract and Acceptance failures affect that indicator as already defined.

But:

$$Confidence_H(C,t)\notin Definition(C^k).$$

This preserves the distinction between durable Contract semantics and drifting operational health indication.


#### 11.1.2 Contract execution as Solution Exploration

A Contract remains a durable governance record defining responsibility, target result, resources, execution conditions, Acceptance, and history.

The execution governed by a Contract is part of Solution Exploration. Let $\mathcal{X}$ be the Solution Exploration activity of the Hive. For Contract $C$:

$$Execution(C)\subseteq\mathcal{X}.$$

This does not redefine the Contract itself as an exploration artifact. It means that execution under the Contract explores, constructs, validates, reworks, and converges toward a state that satisfies the Contract.

A Contract therefore bounds exploration through its Product target, required Work Product, Assignment, Resource Envelope, execution policy, dependencies, Acceptance rules, authority, and information boundaries.

Contract execution does not escape the general exploration rules merely because it is obligatory work. Resource use, trajectory survival, convergence, divergence, back-off, deactivation, preservation, and post-mortem rules apply to Contract-governed execution.

#### 11.1.3 Contract lifecycle

A Contract is a durable, revision-qualified governance record.

Its lifecycle is represented as a finite-state machine:

$$ContractState(C)\in\{DEFINED,ASSIGNED,READY,EXECUTING,BLOCKED,SUBMITTED,UNDER\_ACCEPTANCE,REWORK\_REQUIRED,REASSESSMENT\_REQUIRED,FULFILLED,DISCONTINUED\}.$$

The lifecycle is not strictly monotonic. Forward progress is normal, but material changes can invalidate already satisfied lifecycle predicates and move a successor Contract revision to an earlier state.

#### 11.1.4 State-entry predicates

Each state has explicit entry conditions.

**DEFINED.** A Contract is `DEFINED` when a valid Contract identity and sufficient governed semantics exist to preserve it, but a valid executable Assignment is not yet established.

**ASSIGNED.** A Contract is `ASSIGNED` when exactly one valid Executor has been established:

$$\exists!a:\ Assignment(C,a)$$

and:

$$SatisfiesExecutionPolicy(Executor(C),C,PP).$$

Assignment does not establish readiness.

**READY.** A Contract is `READY` only when all currently applicable execution prerequisites are satisfied.

Let:

$$ReadyPrerequisites(C)$$

be the Project Profile- and Contract-defined prerequisite set.

It can include, without limitation:

- completion of external work;
- completion of an external Contract;
- completion or required state of dependent internal Contracts;
- availability of required Work Products;
- availability of required Evidence;
- availability of computational resources;
- availability of physical resources;
- availability of test facilities;
- availability of manufacturing capability;
- availability of external services;
- required personnel or Human participation;
- authority prerequisites;
- legal or commercial prerequisites;
- environmental or physical conditions;
- required Product state;
- dependency synchronization conditions.

Then:

$$READY(C)\iff ASSIGNED(C)\land\forall p\in ReadyPrerequisites(C):Satisfied(p).$$

This makes readiness explicitly dependent on the broader execution environment rather than only on internal Contract state.

**EXECUTING.** A `READY` Contract can enter `EXECUTING` when execution begins:

$$READY\rightarrow EXECUTING.$$

Execution remains bounded Solution Exploration and remains subject to Resource Envelope, Contract policy, Evidence, authority, convergence/divergence, and validation rules.

**BLOCKED.** A Contract is `BLOCKED` when continued execution is temporarily impossible while the current Contract basis remains potentially valid.

$$BLOCKED(C)\Rightarrow RecordedBlocker(C).$$

Examples include temporary resource unavailability, an unfinished dependency, unavailable external input, temporary physical access failure, or a temporarily unresolved required condition.

**SUBMITTED.** A Contract enters `SUBMITTED` only after explicit submission of a prepared Work Product revision.

**UNDER_ACCEPTANCE.** The submitted result enters independent Acceptance assessment.

**REWORK_REQUIRED.** The submitted result is not acceptable, but the current Contract basis remains valid and correction can continue through normal execution.

**REASSESSMENT_REQUIRED.** The current Contract basis itself requires reconsideration before ordinary execution can continue.

**FULFILLED.** The required Work Product has satisfied the applicable independent Acceptance rules.

**DISCONTINUED.** The Contract has ended without successful fulfilment under that Contract identity.

#### 11.1.5 Formal Contract lifecycle FSM

For Contract definition revision $C^k$, let the common lifecycle state set be:

$$Q_C=\{DEFINED,ASSIGNED,READY,EXECUTING,BLOCKED,SUBMITTED,UNDER\_ACCEPTANCE,REWORK\_REQUIRED,REASSESSMENT\_REQUIRED,FULFILLED,DISCONTINUED\}.$$

The lifecycle machine is:

$$FSM_C=(Q_C,E_C,G_C,\delta_C)$$

where:

- $Q_C$ is the state set;
- $E_C$ is the set of recognized lifecycle events;
- $G_C$ is the applicable guard set;
- $\delta_C$ is a partial guarded transition function.

For ordered lifecycle event $e_n$:

$$z_{n+1}=\delta_C(z_n,e_n,C^k,X_t)$$

when the applicable transition exists and its guard succeeds.

If no applicable transition exists:

$$\delta_C(z_n,e_n,C^k,X_t)\uparrow.$$

An undefined transition does not permit the Hive to invent a successor lifecycle state.

##### 11.1.5.1 Lifecycle events are ordered

Contract lifecycle events form a temporal sequence:

$$\Sigma_C=\langle e_0,e_1,\ldots,e_n\rangle.$$

The FSM evaluates them in their canonical event order.

Lifecycle processing is not assumed commutative:

$$\delta_C(\delta_C(q,e_a),e_b)\neq\delta_C(\delta_C(q,e_b),e_a)$$

in general.

For example, loss of a readiness prerequisite before execution starts can produce a different lifecycle path from loss of the same resource after execution has started.

Event order is therefore part of Contract history.

#### 11.1.6 Common lifecycle guards

##### 11.1.6.1 Assignment-valid guard

Define:

$$G_A(C^k,t)$$

as:

$$ValidAssignment(C^k,t)\land(\exists!a:\ Assignment(C^k,a))\land SatisfiesExecutionPolicy(Executor(C^k),C^k,PP).$$

Then:

$$ASSIGNED(C^k,t)\Rightarrow G_A(C^k,t).$$

##### 11.1.6.2 Readiness guard

Define:

$$G_R(C^k,t)=G_A(C^k,t)\land\bigwedge_{p\in PrerequisiteSpec(C^k)}Evaluate(p,X_t)=TRUE.$$

Then:

$$READY(C^k,t)\Rightarrow G_R(C^k,t).$$

`UNKNOWN` does not evaluate as `TRUE`.

##### 11.1.6.3 Execution-entry guard

Execution requires:

$$G_E(C^k,t)=G_R(C^k,t)\land StartExecution(C^k,t).$$

Therefore:

$$READY\rightarrow EXECUTING$$

only when $G_E$ holds.

##### 11.1.6.4 Temporary-block guard

Define:

$$G_B(C^k,t)=TemporaryContinuationBlock(C^k,t)\land CurrentContractBasisPotentiallyValid(C^k,t).$$

Then:

$$EXECUTING\rightarrow BLOCKED$$

when $G_B$ holds.

A condition that invalidates the Contract basis is not merely a blocker.

##### 11.1.6.5 Reassessment guard

Define $G_X(C^k,t)$ to include applicable conditions such as:

$$ReportInability(C)$$

$$CriticalUnhealthyExecution(C)$$

$$MaterialContractBasisInvalid(C)$$

$$MaterialAcceptanceBasisInvalid(C)$$

$$UnrecoverableResourceCondition(C)$$

$$InvalidExecutionTopology(C)$$

or another Project Profile-defined critical condition.

Then:

$$G_X(C^k,t)\Rightarrow REASSESSMENT\_REQUIRED$$

from applicable active states.

##### 11.1.6.6 Submission guard

Submission requires:

$$G_S(C^k,w^r,t)=EXECUTING(C^k,t)\land ExecutorConformityPassed(w^r,C^k)\land ExplicitSubmit(w^r,C^k,t).$$

Therefore:

$$EXECUTING\rightarrow SUBMITTED.$$

Repository presence, visibility, or acknowledgement does not satisfy $G_S$.

##### 11.1.6.7 Acceptance-entry guard

$$G_U(C^k,w^r,t)=Submitted(w^r,C^k)\land BeginIndependentAcceptance(w^r,C^k,t).$$

Therefore:

$$SUBMITTED\rightarrow UNDER\_ACCEPTANCE.$$

##### 11.1.6.8 Fulfilment guard

`FULFILLED` is governed by the Contract's explicit fulfilment predicate:

$$G_F(C^k,t)=FulfilmentPredicateSatisfied(C^k,t).$$

For an ordinary Contract this includes the required Work Product Acceptance.

For a Product Delivery Contract it additionally includes Product target satisfaction as defined in Section 6.8.

Therefore:

$$Accepted(w,C)\not\Rightarrow FULFILLED(C)$$

universally.

Instead:

$$G_F(C,t)\Rightarrow FULFILLED(C).$$

#### 11.1.7 Runtime transition relation

The common same-definition-revision runtime transitions are:

| From | To | Required event / guard |
|---|---|---|
| `DEFINED` | `ASSIGNED` | $G_A$ becomes true |
| `ASSIGNED` | `READY` | $G_R$ becomes true |
| `ASSIGNED` | `DEFINED` | $G_A$ becomes false |
| `READY` | `EXECUTING` | $G_E$ |
| `READY` | `ASSIGNED` | $G_A\land\neg G_R$ - readiness lost while Assignment remains valid |
| `READY` | `DEFINED` | $\neg G_A$ |
| `EXECUTING` | `BLOCKED` | $G_B$ |
| `EXECUTING` | `SUBMITTED` | $G_S$ |
| `EXECUTING` | `REASSESSMENT_REQUIRED` | $G_X$ |
| `BLOCKED` | `EXECUTING` | blocker cleared, $G_R$, and execution resumes |
| `BLOCKED` | `ASSIGNED` | temporary block resolved but readiness remains false and $G_A$ remains true |
| `BLOCKED` | `DEFINED` | Assignment becomes invalid |
| `BLOCKED` | `REASSESSMENT_REQUIRED` | blocker is reclassified as a material Contract-basis problem |
| `SUBMITTED` | `UNDER_ACCEPTANCE` | $G_U$ |
| `SUBMITTED` | `REASSESSMENT_REQUIRED` | submitted basis becomes materially invalid before Acceptance begins |
| `UNDER_ACCEPTANCE` | `FULFILLED` | Acceptance disposition permits fulfilment and $G_F$ holds |
| `UNDER_ACCEPTANCE` | `REWORK_REQUIRED` | Acceptance disposition = `REWORK_REQUIRED` |
| `UNDER_ACCEPTANCE` | `REASSESSMENT_REQUIRED` | Acceptance disposition = `REASSESSMENT_REQUIRED` |
| `REWORK_REQUIRED` | `EXECUTING` | execution basis remains valid, $G_R$, and governed rework starts |
| `REWORK_REQUIRED` | `ASSIGNED` | rework remains required, Assignment valid, but readiness is not satisfied |
| `REWORK_REQUIRED` | `DEFINED` | Assignment becomes invalid |
| `REWORK_REQUIRED` | `REASSESSMENT_REQUIRED` | ordinary rework is no longer sufficient |
| `REASSESSMENT_REQUIRED` | `DEFINED` | reassessment/revision leaves no valid executable Assignment |
| `REASSESSMENT_REQUIRED` | `ASSIGNED` | valid Assignment exists but readiness is not satisfied |
| `REASSESSMENT_REQUIRED` | `READY` | Contract basis valid and all readiness predicates hold |
| `REASSESSMENT_REQUIRED` | `EXECUTING` | Contract basis valid, $G_R$, and governed continuation explicitly resumes |
| `REASSESSMENT_REQUIRED` | `REWORK_REQUIRED` | reassessment concludes that ordinary rework under the valid Contract basis is sufficient |
| any non-terminal state | `DISCONTINUED` | valid discontinuation condition |
| `FULFILLED` | - | terminal for this Contract identity |
| `DISCONTINUED` | - | terminal for this Contract identity |

This table is the normative common transition relation.


##### 11.1.7.1 Readiness loss is not necessarily Contract revision

A runtime readiness condition can change without changing the Contract definition.

For example:

$$READY(C^k,t_1)$$

and later:

$$\neg ResourceAvailable(r,C^k,t_2)$$

can produce:

$$READY(C^k)\rightarrow ASSIGNED(C^k)$$

while remaining on the same definition revision.

Therefore:

$$ReadinessLoss\not\Rightarrow ContractDefinitionRevision.$$

##### 11.1.7.2 Blocking and readiness loss differ

`BLOCKED` means that execution had already begun and cannot temporarily continue.

Therefore:

$$READY\land\neg G_R\Rightarrow ASSIGNED$$

rather than:

$$READY\rightarrow BLOCKED.$$

By contrast:

$$EXECUTING\land TemporaryContinuationBlock\Rightarrow BLOCKED.$$

This keeps `BLOCKED` as an execution-state condition rather than a generic synonym for not ready.

##### 11.1.7.3 BLOCKED is recoverable only while the Contract basis remains viable

If the blocker exposes a fundamental Contract problem:

$$BLOCKED\land G_X\Rightarrow REASSESSMENT\_REQUIRED.$$

The model must not repeatedly classify a fundamental infeasibility as a temporary blocker merely to keep execution alive.

##### 11.1.7.4 Rework re-entry is guarded

Acceptance disposition `REWORK_REQUIRED` does not imply immediate execution.

Before rework restarts, Assignment and readiness are re-evaluated.

Thus:

$$REWORK\_REQUIRED\land G_R\land StartRework\Rightarrow EXECUTING.$$

But:

$$REWORK\_REQUIRED\land G_A\land\neg G_R\Rightarrow ASSIGNED$$

once re-entry is initiated.

And:

$$REWORK\_REQUIRED\land\neg G_A\Rightarrow DEFINED.$$

This prevents rework from bypassing readiness.

#### 11.1.8 Definition-revision transition relation

Runtime transition and Contract-definition revision are different operations.

Define:

$$\delta_{run}$$

for lifecycle evolution under one $C^k$, and:

$$\delta_{rev}$$

for the effect of:

$$C^k\rightarrow C^{k+1}.$$

Therefore:

$$\delta_{run}\neq\delta_{rev}.$$

##### 11.1.8.1 Revision re-entry basis

For successor definition revision $C^{k+1}$, define:

$$BaseReentry(C^{k+1},t)=\begin{cases}
DEFINED,&\neg G_A\\
ASSIGNED,&G_A\land\neg G_R\\
READY,&G_R.
\end{cases}$$

A definition revision by itself does not silently start execution.

Thus:

$$BaseReentry\notin\{EXECUTING,SUBMITTED,UNDER\_ACCEPTANCE,FULFILLED\}.$$

An explicit continuation or resume event can subsequently move `READY` to `EXECUTING`.

This makes definition revision and execution restart separately observable.

##### 11.1.8.2 Revision from DEFINED, ASSIGNED or READY

For:

$$q\in\{DEFINED,ASSIGNED,READY\}$$

a material revision produces:

$$(C^k,q)\rightarrow(C^{k+1},BaseReentry(C^{k+1})).$$

Hence:

$$READY(C^k)\rightarrow ASSIGNED(C^{k+1})$$

when Assignment remains valid but the revised Contract introduces an unsatisfied readiness prerequisite.

Likewise:

$$READY(C^k)\rightarrow DEFINED(C^{k+1})$$

when Assignment validity is lost.

A revision can also move an earlier state forward:

$$DEFINED(C^k)\rightarrow READY(C^{k+1})$$

when the revised Contract establishes a valid Assignment and all readiness predicates already hold.

The FSM is therefore not directionally monotonic across revisions.

##### 11.1.8.3 Revision during active execution

A material definition revision while the Contract is `EXECUTING` terminates execution under the old definition revision as an active continuation basis.

The old execution history remains attached to $C^k$.

The new definition revision is re-entered through:

$$BaseReentry(C^{k+1},t).$$

Execution under $C^{k+1}$ requires a subsequent governed continuation:

$$READY(C^{k+1})\rightarrow EXECUTING(C^{k+1}).$$

Therefore:

$$Revision\neq AutomaticExecutionContinuation.$$

Where the Project Profile requires explicit reassessment before re-entry, the transition can instead be:

$$EXECUTING(C^k)\rightarrow REASSESSMENT\_REQUIRED(C^{k+1})$$

followed by the ordinary reassessment exit rules.

##### 11.1.8.4 Revision during submission or Acceptance

Submission and Acceptance are revision-specific.

Suppose:

$$Submitted(w^r,C^k).$$

If:

$$C^k\rightarrow C^{k+1}$$

and the revision is material to that submission or Acceptance basis:

$$MaterialToAcceptance(C^k,C^{k+1},w^r),$$

then:

$$Submitted(w^r,C^k)\not\Rightarrow Submitted(w^r,C^{k+1})$$

and:

$$AcceptedAgainst(w^r,C^k)\not\Rightarrow AcceptedAgainst(w^r,C^{k+1}).$$

The new definition revision re-enters through its applicable Contract lifecycle basis.

A non-material revision can preserve unaffected Acceptance work only when the Project Profile explicitly establishes that non-materiality.

No Acceptance status transfers merely through revision ancestry.

##### 11.1.8.5 Revision from REWORK_REQUIRED

If Contract semantics change while rework is required:

$$REWORK\_REQUIRED(C^k)\land Revision(C^k,C^{k+1}),$$

the old rework disposition remains historical.

The new revision is not assumed to inherit it.

Instead:

$$State(C^{k+1})=BaseReentry(C^{k+1},t)$$

unless explicit reassessment remains required.

This prevents obsolete rework instructions from becoming obligations under a materially changed Contract.

##### 11.1.8.6 Terminal states do not revise in place

`FULFILLED` and `DISCONTINUED` remain terminal for the Contract identity.

Therefore:

$$FULFILLED(C)\not\rightarrow Revision(C)$$

as ordinary continuation, and:

$$DISCONTINUED(C)\not\rightarrow Revision(C).$$

New materially governed work after either terminal state is represented through:

$$Succeeds(C_2,C_1)$$

or another applicable external process.

This preserves the terminal-state semantics already established.

#### 11.1.9 Unsupported transition invariant

A lifecycle transition is valid only when it belongs to the common transition relation or an explicitly permitted Project Profile extension that does not contradict the common model.

Therefore:

$$Transition(C,z_i,z_j)\Rightarrow(z_i,z_j)\in E_C$$

for common transitions.

Examples of invalid shortcuts include:

$$DEFINED\not\rightarrow EXECUTING$$

without Assignment and readiness;

$$ASSIGNED\not\rightarrow SUBMITTED;$$

$$SUBMITTED\not\rightarrow FULFILLED$$

without independent Acceptance and the Contract fulfilment predicate; and:

$$REWORK\_REQUIRED\not\rightarrow FULFILLED$$

without a successor Work Product submission and Acceptance.

#### 11.1.10 No hidden same-state iteration

An event that does not change lifecycle state can still be recorded in Contract history.

It is not represented as an artificial FSM self-transition merely to show activity.

Thus:

$$ObservedEvent(C,t)\land State(C,t^-)=State(C,t^+)$$

does not require:

$$Transition(q,q).$$

Examples include additional Evidence received while `EXECUTING`, progress inside `EXECUTING`, waiting during `UNDER_ACCEPTANCE`, or new diagnostic information while `BLOCKED`.

This retains the existing principle that activity does not equal lifecycle progress.

#### 11.1.11 Discontinuation

Discontinuation remains a governed terminal event.

Let:

$$G_D(C,t)$$

be the applicable discontinuation guard.

Possible Project Profile-defined bases include explicit authorized cancellation, demonstrated infeasibility, permanent resource withdrawal, unrecoverable external dependency, replacement by successor Contract, or another governed reason.

Then:

$$q\rightarrow DISCONTINUED$$

for non-terminal $q$ only when $G_D$ holds.

Discontinuation preserves the Contract definition revisions, lifecycle observations, Work Products, Evidence, Acceptance attempts, and event history.

#### 11.1.12 Event and transition audit

Every lifecycle transition record preserves at minimum:

$$LifecycleEvent=(cid,definitionRevision,fromState,toState,eventType,guardResult,time,provenance).$$

Where a definition revision participates, the event additionally references:

$$C^k\rightarrow C^{k+1}.$$

This allows the Hive to distinguish:

$$READY(C^k)\rightarrow ASSIGNED(C^k)$$

caused by runtime prerequisite loss from:

$$READY(C^k)\rightarrow ASSIGNED(C^{k+1})$$

caused by Contract revision.

The visible state names are the same. The causal semantics are not.

#### 11.1.13 Human intervention and lifecycle effect

Human Arbitrary Input, Human Voluntary Choice, or Human Prescriptive Choice does not bypass the Contract authority and revision rules.

Human input itself does not directly mutate the Contract FSM. However, when Human input is legitimately incorporated and materially revises the Contract:

$$HumanInput\rightarrow GovernedContractRevision\rightarrow ReevaluateLifecyclePredicates.$$

The re-entry rules in Section 11.1.8 then apply.

#### 11.1.14 Dependency-driven readiness

Dependencies are explicit readiness conditions where applicable.

For dependent Contracts $C_a$ and $C_b$:

$$DependsForReadiness(C_a,C_b,s_b)$$

means that $C_a$ can become `READY` only when $C_b$ reaches required state $s_b$.

For example, a project can require:

$$State(C_b)=FULFILLED$$

before:

$$State(C_a)=READY.$$

The common model does not require every dependency to wait for full fulfilment. A Project Profile can require another state or a particular accepted Work Product.

External activities can be represented in the same readiness logic without being forced into internal Contract semantics.

#### 11.1.15 Resource-driven readiness

Resource Envelope declaration and resource availability are distinct.

A Contract can have an authorized budget but still lack the actual resource needed to begin execution. Therefore:

$$ResourceBudgeted(r,C)\not\Rightarrow ResourceAvailable(r,C,t).$$

Where resource $r$ is a readiness prerequisite:

$$RequiredResource(r,C)\land\neg ResourceAvailable(r,C,t)\Rightarrow\neg READY(C).$$

This applies to computational and physical resources.

#### 11.1.16 Revision is not lifecycle state

Revision remains orthogonal to state:

$$Revision(C)\neq ContractState(C).$$

A revision can cause lifecycle re-entry or reassessment, but the revision itself is not a lifecycle state.

Earlier Contract revisions remain historically addressable.

### 11.2 Contract decomposition

A Contract can be decomposed when fulfilment requires separable execution responsibilities.

Each resulting Contract remains a complete Contract for its own scope. Every Contract has exactly one accountable Executor:

$$\exists!a:\ Assignment(C,a).$$

This invariant applies to every Contract, including Contracts involving teams, multiple contributors, several supporting Actors, or several internal Hive execution participants. A Contract can involve many participants while still having one accountable Executor. The accountable Executor is therefore not equivalent to the set of people, Agents, organizations, or systems participating in execution.

#### 11.2.1 Decomposition creates new Assignments

For:

$$Split(C_p)=\{C_1,C_2,\ldots,C_n\}$$

each resulting Contract has its own Assignment:

$$\forall C_i\in Split(C_p):\exists!a:\ Assignment(C_i,a).$$

The decomposition does not imply:

$$Executor(C_i)=Executor(C_j)$$

for distinct Contracts $C_i$ and $C_j$. Nor does the parent Assignment automatically propagate into child Contracts:

$$Executor(C_p)=a\not\Rightarrow Executor(C_i)=a.$$

A decomposition that simply assigns every resulting responsibility to the same Executor is not the default semantics of Contract splitting. Whether reuse is permissible depends on the applicable execution policies.

#### 11.2.2 Contract-type execution policies

Different Contract types can impose different execution policies. Let:

$$ExecutionPolicy(type(C),PP)$$

define the applicable restrictions.

An Assignment is valid only when:

$$Assignment(C,a)\Rightarrow SatisfiesExecutionPolicy(a,C,PP).$$

For an executable Contract revision, Assignment is unique:

$$\exists!a:\ Assignment(C^k,a).$$

Define the derived Executor function:

$$Executor(C^k)=a\iff Assignment(C^k,a)$$

when the applicable Assignment is valid and unique.

Execution policy can constrain eligible Executor classes, required independence, prohibited combinations of responsibilities, required separation between development, production, testing, verification, integration, Acceptance, or other activities, permitted Hive topology, and external-party requirements.

For Contracts whose execution roles require independence:

$$IndependentExecutionRequired(C_i,C_j)\Rightarrow Executor(C_i)\neq Executor(C_j).$$

Thus development and independent testing or verification cannot use the same Executor when the applicable engineering method requires independent execution. The exact required separation is Project Profile controlled.

#### 11.2.3 Contract decomposition distributes responsibility

A child Contract produces a complete Work Product relative to its own obligation. That Work Product can remain only one input relative to a broader parent objective.

Therefore:

$$CompleteFor(w_i,C_i)\not\Rightarrow CompleteFor(w_i,C_p).$$

Contract decomposition distributes execution responsibility. It does not fragment the Product automatically and does not transfer the parent Executor's authority to child Executors or vice versa. Parent and child Contracts retain their own Issuer, Assignment, Executor, Product target, Work Product, Obligation, Resource Envelope, execution policy, Acceptance rules, revision, and history.

#### 11.2.4 Contract decomposition does not imply Hive decomposition

Contract splitting does not require Hive splitting:

$$ContractSplit\not\Rightarrow HiveSplit.$$

A Hive can coordinate multiple Contracts while preserving their distinct Assignments, Executors, Resource Envelopes, execution policies, Work Products, validation, and Acceptance.

The Hive can use lightweight specialized Agents internally. If Hive $H$ is the Contract Executor:

$$Executor(C)=H$$

and Agent $a_k$ performs a bounded operation:

$$Performs(a_k,x,C)$$

this does not imply:

$$Executor(C)=a_k.$$

A lightweight Agent is an internal computational participant unless explicitly given another role by the model. The Contract-facing responsibility remains stable even when the Hive creates, replaces, deactivates, or reallocates its internal Agents.

#### 11.2.5 Upper-layer Actor and Hive execution boundary

An Actor operating at an upper Engineering Layer interacts with the Hive through the applicable governed engineering boundary. Conceptually:

$$Actor_{upper}\leftrightarrow Hive\leftrightarrow\{Agent_1,\ldots,Agent_n\}.$$

The upper-layer Actor does not depend on the identity or continued existence of the Hive's lightweight specialized Agents. Therefore:

$$Interacts(Actor_{upper},Hive)\not\Rightarrow Directs(Actor_{upper},Agent_k)$$

unless an explicit execution mechanism establishes such interaction.

The Hive can change its internal execution topology without forcing that topology into the upper-layer engineering model.

#### 11.2.6 Human participation at several layers

The same Human can participate at several Engineering Layers. Human identity does not merge those engineering contexts.

For Human $h$:

$$Participates(h,L_i)\land Participates(h,L_j)$$

does not imply:

$$AuthorityPropagation(L_i,L_j)$$

and does not imply:

$$ImplicitDecision(h,L_i,L_j).$$

A Human's awareness of both contexts can inform reasoning, but it does not make an undocumented choice a valid cross-layer Decision. Where Decision semantics are required, the Decision remains explicit, scoped, and authority-qualified. Personal continuity, informal discussion, presumed intent, organizational habit, or the fact that the same person already knows the information cannot replace explicit Decision materialization.

#### 11.2.7 Execution topology does not imply authority topology

An execution relation is not an authority relation by default:

$$ExecutionRelation(x,y)\not\Rightarrow AuthorityRelation(x,y).$$

This includes relations created by Contract decomposition, Work Product dependency, verification, integration, shared Hive execution, and Team API communication.

Similarly:

$$ChildContract(C_c,C_p)\not\Rightarrow AuthorityInheritance(C_p,C_c)$$

and:

$$ChildContract(C_c,C_p)\not\Rightarrow AuthorityInheritance(C_c,C_p).$$

Authority remains explicit and context-qualified.

### 11.3 Integration

Integration constructs a coherent Work Product from qualified inputs according to the applicable Contract and project engineering method. The proposal does not prescribe how technical integration is implemented. Technical construction details belong to the engineering domain and Project Profile where applicable.

The governance invariants are:

$$Integration\neq AuthorityAggregation$$

and:

$$Integration\neq DecisionAggregation.$$

Combining Work Products does not merge their Decision authority domains.

#### 11.3.1 Parallel exploration before integration

Potential interaction between engineering activities does not require a permanent classification of those activities as independent or dependent. Separate Contract trajectories can explore prospective Work Products concurrently while those results remain in Solution Space or intermediate engineering state. Their interaction can become visible later as engineering information develops.

The common convergence point for materialized Work Products is Integration.

#### 11.3.2 Integration convergence

For Integration Contract $C_I$, let $W_I$ be the materialized Work Products required for that integration. Define the ready subset:

$$W^{ready}_{C_I}=\{w\in W_I\mid IntegrationReady(w,C_I)\}.$$

Therefore:

$$W^{ready}_{C_I}\subseteq W_I.$$

Construction of the intended integrated Work Product is available when:

$$W^{ready}_{C_I}=W_I.$$

While:

$$W_I\setminus W^{ready}_{C_I}\neq\varnothing,$$

the intended integration remains incomplete.

The unfinished source Contracts can continue their own exploration and preparation. Other unrelated Contracts can also continue. Integration therefore serializes the participating materialized inputs at their convergence point without imposing a global sequential Product-development process.

The common progression is:

$$\text{parallel Solution Exploration}\rightarrow W_I\rightarrow w_I\rightarrow\text{integrated verification}\rightarrow\text{final applicable Acceptance}.$$

Contract-specific prerequisites and dependencies can gate individual Contracts before this point. They do not create a universal Product-wide Decision sequence.

### 11.4 Integrator Contract

An Integrator Contract is used when several Work Products must be constructed into a coherent result. It has exactly one accountable Executor:

$$\exists!a:\ Assignment(C_I,a).$$

The Integrator is responsible for determining that every candidate input is fit for the intended integration operation.

#### 11.4.1 Mandatory Work Product verification before integration

For every candidate input Work Product $w$:

$$CandidateInput(w,C_I)\Rightarrow VerifyForIntegration(w,C_I).$$

Actual integration is permitted only after the required input checks succeed:

$$Integrate(w,C_I)\Rightarrow IntegrationReady(w,C_I).$$

Source-Contract Acceptance alone does not establish integration readiness:

$$Accepted(w,C_s)\not\Rightarrow IntegrationReady(w,C_I).$$

The Integrator must assess the Work Product against the specific context in which it will be integrated. The proposal does not prescribe the technical content of this verification. The Integrator Contract, Project Profile, applicable engineering method, and Work Product semantics define the necessary checks.

#### 11.4.2 Rework request

When a Work Product is not integration-ready, the Integrator can request rework. Where correction is necessary for fulfilment of the Integrator Contract, issuing that rework request is part of the Integrator's Obligation.

$$\neg IntegrationReady(w,C_I)\Rightarrow RequestRework(I,w).$$

The Integrator does not thereby gain unrestricted authority to change the originating engineering Decision:

$$RequestRework(I,w)\not\Rightarrow DesignAuthority(I,w).$$

The responsible source Contract receives the issue through the applicable feedback or Contract mechanism and performs the required reassessment.

#### 11.4.3 Verification after integration

Verification of the integrated Work Product can expose incompatibilities that could not be observed on isolated inputs. The execution loop can therefore be:

$$VerifyInputs\rightarrow Integrate\rightarrow VerifyIntegratedResult.$$

When integrated-result verification fails:

$$VerifyIntegratedResult\rightarrow Diagnose\rightarrow RequestRework$$

followed by:

$$Rework\rightarrow ReverifyInput\rightarrow Reintegrate.$$

A revised Work Product must be reverified before it is used again:

$$Revised(w)\Rightarrow ReverifyForIntegration(w,C_I).$$

Previous verification is not silently inherited by a changed revision.

#### 11.4.4 Integrator construction responsibility

Within its own Contract, the Integrator controls coherent-product construction. This includes input qualification, integration sequencing, applicable compatibility checks, construction, ancestry preservation, integration-specific validation, Gap exposure, and initiation of necessary rework.

Therefore:

$$ConstructionResponsibility(I,C_I)\not\Rightarrow DesignAuthority(I,C_k)$$

for a contributing source Contract $C_k$. The Integrator's power to reject an input for integration or request rework is not the same as authority to change the source design.

#### 11.4.5 Integration ancestry

The integrated Work Product preserves ancestry to contributing Work Products and applicable boundary information. For contributing Work Product $w_k$ and integrated Work Product $w_I$:

$$Contributes(w_k,w_I).$$

The converse is derived:

$$IsContributedToBy=Contributes^{\smile}.$$

Both forward and reverse traceability are available without authority inheritance.

$$Contributes(w_k,w_I)\not\Rightarrow Authority(w_I,w_k)$$

and:

$$Contributes(w_k,w_I)\not\Rightarrow Authority(w_k,w_I).$$

### 11.5 Verification execution topology

Development, production, verification, testing, and integration can have different Contract execution policies. The common proposal does not require one universal physical separation. It does require the actual topology to satisfy the applicable independence rule:

$$SatisfiesIndependence(actual,required,PP).$$

Where independent verification or testing is required:

$$Executor(C_{development})\neq Executor(C_{verification}).$$

The required separation can be implemented through different Actors, Hive instances, organizations, models, providers, infrastructure, or another Project Profile mechanism. A single Hive can coordinate related Contracts only when doing so remains compatible with the required independence.

### 11.6 Acceptance

Acceptance remains the Contract-governed independent assessment of fulfilment and Work Product conformance.

It has two sequential stages:

$$ExecutorConformity\rightarrow Submission\rightarrow IndependentAcceptance.$$

Executor self-check is not independent Acceptance. Independent Acceptance is performed by the Issuer or explicitly permitted delegate.

#### 11.6.1 Executor conformity

Before submission, the Executor performs the applicable checks and records:

- conformance results;
- relevant Evidence;
- Known Gaps;
- permitted deferred conditions;
- non-conformities;
- revision information.

If conformity cannot legitimately be established:

$$\neg ExecutorConformityPassed(w,C)\Rightarrow\neg NormalSubmit(w,C).$$

The Contract continues execution, becomes blocked, or enters reassessment according to the cause.

#### 11.6.2 Submission

Submission is explicit:

$$Submit(w^r,C^k,t).$$

Neither visibility nor repository presence implies submission:

$$RepositoryPresence(w)\not\Rightarrow Submitted(w,C)$$

$$VisibleToIssuer(w)\not\Rightarrow Submitted(w,C).$$

A normal submission transitions the Contract from `EXECUTING` to `SUBMITTED`.

The submitted Work Product revision remains historically addressable as the subject of that Acceptance attempt. Later correction creates a successor Work Product revision rather than rewriting the submitted revision.

#### 11.6.3 Acknowledgement

Acknowledgement is neither submission nor Acceptance:

$$Acknowledged(w,C)\not\Rightarrow Accepted(w,C)$$

$$Acknowledged(w,C)\not\Rightarrow Fulfilled(C).$$

#### 11.6.4 Independent Acceptance

The normal transition is:

$$SUBMITTED\rightarrow UNDER\_ACCEPTANCE.$$

Acceptance assesses the exact submitted Work Product revision against the applicable Contract revision.

The Executor conformity record is Evidence or input to the assessment. It is not proof.

The independent assessment considers the submitted Work Product, applicable Evidence, Known Gaps and their dispositions, Acceptance rules, required verification independence, applicable Check Cascade results, and Contract fulfilment.

#### 11.6.5 Acceptance dispositions

The common Acceptance dispositions are:

$$AcceptanceDisposition\in\{ACCEPTED,REWORK\_REQUIRED,REASSESSMENT\_REQUIRED\}.$$

`ACCEPTED` means Contract fulfilment has been established.

`REWORK_REQUIRED` means ordinary correction remains appropriate under the current Contract basis.

`REASSESSMENT_REQUIRED` means the underlying Contract basis must be reconsidered.

#### 11.6.6 Successful Acceptance

Successful Acceptance produces:

$$UNDER\_ACCEPTANCE\rightarrow FULFILLED.$$

For the required coherent Work Product:

$$Accepted(w^r,C^k)$$

establishes Work Product Acceptance against that Contract revision. Contract fulfilment occurs only when the applicable fulfilment predicate also holds:

$$G_F(C^k,t)\Rightarrow Fulfilled(C^k).$$

For an ordinary Contract, Work Product Acceptance can satisfy the required fulfilment predicate. For a Product Delivery Contract, Product target satisfaction is an additional condition. Therefore:

$$Accepted(w,C)\not\Rightarrow Fulfilled(C)$$

universally.

Successful Acceptance establishes that the submitted result satisfies the applicable Contract Acceptance rules. It does not by itself imply release, deployment, production, baselining, or another project-specific lifecycle transition.

#### 11.6.7 Rework

Failed Acceptance of $w^r$ does not mutate that revision.

Instead:

$$w^r\rightarrow w^{r+1}.$$

The lifecycle proceeds:

$$UNDER\_ACCEPTANCE\rightarrow REWORK\_REQUIRED\rightarrow EXECUTING\rightarrow SUBMITTED.$$

Applicable checks are repeated or explicitly reused where unaffected.

#### 11.6.8 Acceptance failure and Contract failure

A failed Acceptance attempt does not by itself mean permanent Contract failure:

$$\neg Accepted(w^r,C)\not\Rightarrow Discontinued(C).$$

However, Acceptance failure is a Contract-execution observation. Repeated or material Acceptance failure contributes to the health analysis in Section 17.

#### 11.6.9 Contract and Acceptance failures affect Confidence

Contract and Acceptance failures are mandatory inputs to the next relevant Confidence update.

Let:

$$FailureObservation(C,t)$$

include events such as:

- Executor conformity failure;
- Work Product rejection;
- Acceptance failure;
- repeated rework;
- Contract blocking;
- missed dependency;
- unavailable critical resources;
- integration failure;
- verification failure;
- reported inability to fulfil;
- transition to `REASSESSMENT_REQUIRED`.

Then:

$$FailureObservation(C,t)\Rightarrow IncludeInConfidenceUpdate(C,t+\Delta t).$$

Acceptance failure specifically contributes to the validation/rework history used by the Confidence model:

$$AcceptanceFailure\rightarrow ConfidenceObservation.$$

It is not necessary that every failure mechanically lowers Confidence by a fixed amount. A failed test can remove substantial uncertainty and expose a clear correction path.

Therefore:

$$Failure\not\Rightarrow FixedConfidenceDecrease.$$

But a material Contract or Acceptance failure must not be ignored when updating Confidence:

$$MaterialFailure\Rightarrow ConfidenceAffected.$$

This preserves the distinction:

$$Confidence\neq ContractState$$

and:

$$Confidence\neq AcceptanceDisposition.$$

#### 11.6.10 Repeated failure

Repeated Acceptance failure contributes to execution divergence:

$$RepeatedAcceptanceFailure\rightarrow ExecutionHealthInput.$$

This can subsequently contribute to lower Confidence, back-off, Executor or Agent deactivation, reassessment, Contract revision, successor Contract, or discontinuation.

These are independent mechanisms. No single implication is automatic.

#### 11.6.11 Discontinuation

A Contract can terminate unsuccessfully as:

$$DISCONTINUED.$$

Its full history remains addressable:

$$Discontinued(C)\not\Rightarrow DeleteHistory(C).$$

Discontinuation can follow from infeasibility, authority decision, exhausted or withdrawn resources, replacement by a successor Contract, unrecoverable external dependency, cancellation, or another Project Profile-defined reason.

#### 11.6.12 Successor Contract

When the execution model changes so materially that the existing Contract no longer represents the same governed obligation, a successor Contract can be established:

$$Succeeds(C_2,C_1).$$

The original Contract remains historical. Successor creation is not a restart or rewrite.

#### 11.6.13 Illustration - in-house Product replaced by third-party Product

::: {custom-style="Illustration"}
Consider an initial Contract $C_{internal}$ whose Product target is an internally developed component. Its execution model assumes internal design, internal implementation or manufacturing, internal verification capability, internally controlled change authority, and internal access to engineering Evidence.

During exploration the Hive determines that purchasing a third-party component is economically or technically preferable.

This is not merely a different implementation trajectory inside the same Contract if the change materially alters responsibility, authority, dependencies, Evidence availability, or fulfilment obligations.

A successor engineering Contract can therefore be established:

$$Succeeds(C_{thirdparty},C_{internal}).$$

The successor Product target now depends on an external supplier. That change can create additional prerequisite obligations outside the original engineering Contract, for example an external legal/commercial Contract $C_{legal}$ covering project-specific matters such as procurement obligation, delivery terms, price/payment terms, warranties, licensing, intellectual-property rights, permitted use, data rights, confidentiality, liability, compliance representations, change-notification duties, support/service obligations, product discontinuation or obsolescence, required supplier Evidence, acceptance and rejection rights, or applicable regulatory or export conditions.

These matters are illustrative. The common proposal does not prescribe commercial law or supplier-contract content.

What is normative to the governance model is that the external dependency must not be hidden.

If legal/commercial fulfilment is required before engineering execution can legitimately continue:

$$DependsForReadiness(C_{thirdparty},C_{legal},s)$$

for the applicable required state $s$.

For example:

$$Fulfilled(C_{legal})\Rightarrow LegalPrerequisiteSatisfied(C_{thirdparty}).$$

Until that condition holds:

$$\neg READY(C_{thirdparty}).$$

A Decision to replace internal realization with a third-party Product therefore changes the Solution Space and can create new external Contract dependencies that did not exist in the in-house trajectory:

$$ChangeToThirdPartySolution\not\Rightarrow PreserveOriginalObligationSet.$$

The Hive must reassess Contract topology, Evidence availability, authority, Resource Envelope, readiness prerequisites, and Acceptance rules.
:::

#### 11.6.14 Contract revision during Acceptance

If:

$$C^k\rightarrow C^{k+1}$$

during submission or Acceptance, materiality to the Acceptance basis is assessed.

Where material:

$$MaterialToAcceptance(C^k,C^{k+1},w^r)\Rightarrow ReassessSubmissionOrAcceptance.$$

Acceptance under the old basis does not automatically transfer.

#### 11.6.15 Work Product FSM

The Work Product submission FSM is:

$$PREPARED\rightarrow SUBMITTED\rightarrow UNDER\_ACCEPTANCE\rightarrow ACCEPTED$$

or:

$$UNDER\_ACCEPTANCE\rightarrow NOT\_ACCEPTED.$$

A failed revision remains historical:

$$NOT\_ACCEPTED(w^r)\rightarrow Prepare(w^{r+1})$$

rather than mutation of $w^r$.

#### 11.6.16 Contract FSM summary

The principal success path is:

$$DEFINED\rightarrow ASSIGNED\rightarrow READY\rightarrow EXECUTING\rightarrow SUBMITTED\rightarrow UNDER\_ACCEPTANCE\rightarrow FULFILLED.$$

But the actual model is a guarded graph, not a one-way pipeline.

The normative guarded transition relation is defined in Section 11.1.7. It distinguishes same-revision runtime regression from definition-revision re-entry. For example:

$$READY(C^k)\rightarrow ASSIGNED(C^k)$$

can occur when a runtime readiness prerequisite is lost while Assignment remains valid, whereas:

$$READY(C^k)\rightarrow ASSIGNED(C^{k+1})$$

can occur when a material Contract revision preserves Assignment but introduces an unsatisfied readiness prerequisite.

The model also includes recoverable execution blocking, guarded rework re-entry, reassessment, explicit discontinuation, and revision-specific submission/Acceptance. Every transition preserves history. There is no same-state transition used to hide iteration.

#### 11.6.17 Product boundary

Acceptance assesses Work Product conformance and Contract fulfilment.

Where the Contract is a Product Delivery Contract, Contract fulfilment also requires:

$$ProductTargetSatisfied(C).$$

Thus:

$$Accepted(w,C)$$

and:

$$ProductTargetSatisfied(C)$$

are separate predicates even where both are required for:

$$Fulfilled(C).$$

For a Product Delivery Contract:

$$Fulfilled(C)\iff AcceptedRequiredWorkProduct(C)\land ProductTargetSatisfied(C)$$

subject to any additional applicable Contract conditions.

For a non-delivery Contract, Product target satisfaction can represent verification, analysis, characterization, or another target semantics rather than Product mutation.

#### 11.6.18 Product / Work Product rework boundary

Work Product rework and Product rework are not equivalent:

$$WorkProductRework\not\Rightarrow ProductRework$$

and:

$$ProductRework\not\Rightarrow WorkProductRework$$

universally.

Work Product rework can occur because traceability is incomplete, Evidence is inadequate, required supplementary information is missing, Work Product content violates its schema, or Acceptance rationale is insufficient while Product state remains unchanged.

Product rework can change the engineered subject. The affected Work Products are then identified through impact analysis. If the Product rework affects a Work Product's validity:

$$MaterialToWP(\Delta p,w,C)\Rightarrow Reassess(w,C).$$

`MaterialToWP` is Project Profile-defined.

### 11.7 Team API

A Team API is the governed cross-Actor or cross-Hive communication boundary used to coordinate Product evolution and Contract execution.

Conceptually:

$$TeamAPI: Actor/Hive\leftrightarrow Actor/Hive.$$

A Team API can carry or reference Questions, Requests, Clarifications, Exchange Items, Feedback Exchange Items, Work Products, Contract-relevant execution information, and other Project Profile-defined communications.

Team API does not prescribe Product architecture or technical Product interfaces. It governs engineering communication between execution parties.

Shared Team API access does not imply shared authority:

$$SharedTeamAPI(a,b)\not\Rightarrow SharedAuthority(a,b).$$

### 11.8 Blast containment

A Decision has direct effect only inside its local Contract and bounded Hive/Team context. Other parties are affected only when an Exchange Item that they consume changes.

$$Affected(Team,d)\Leftrightarrow\exists e\in UpdatedExchangeItems(d):Consumes(Team,e).$$

If a team does not consume a changed Exchange Item, that team is outside the native blast area for that Decision.

## 12. Evidence and validation locality

### 12.1 Evidence as a Proposition role

Evidence is a Proposition used by a defined validator or engineering argument to support another Proposition in a defined engineering context.

For context $\kappa$:

$$E_{\kappa}=\{p\in\mathbb P\mid EvidenceRole(p,\kappa)\}.$$

Evidence therefore shares the common Proposition algebra.

Evidence-specific semantics extend that algebra rather than replacing it.

A principal Evidence relation is:

$$Supports_{\kappa}\subseteq E_{\kappa}\times\mathbb P$$

with derived converse:

$$IsSupportedBy_{\kappa}=Supports_{\kappa}^{\smile}.$$

Therefore:

$$Supports_{\kappa}(e,p)\iff IsSupportedBy_{\kappa}(p,e).$$

A Decision is a Proposition, so Evidence can directly support an informed local Decision:

$$Supports_{\kappa}\subseteq E_{\kappa}\times D_{\kappa}$$

where applicable.

This does not imply that every Evidence Proposition supports every Decision or that Evidence support alone establishes Decision correctness.

The applicable relation validators determine whether a particular support relation is legitimate.

### 12.2 Evidence existence, relevance, support, and sufficiency

Evidence existence, relevance, support, and sufficiency are separate properties.

For:

$$e\in E_{\kappa}$$

and:

$$p\in\mathbb P$$

the following implications do not generally hold:

$$Exists(e)\not\Rightarrow Relevant(e,p,\kappa)$$

$$Relevant(e,p,\kappa)\not\Rightarrow Supports_{\kappa}(e,p)$$

$$Supports_{\kappa}(e,p)\not\Rightarrow Sufficient(e,p,\kappa).$$

A test result, analysis, simulation, inspection, field observation, end-user claim, regulatory statement, human study, review result, or another recorded Proposition can therefore exist without being valid Evidence for every Proposition to which it can be structurally connected.

The Project Profile defines the applicable Evidence validators and sufficiency rules.

Evidence evaluation uses the Check Cascade where applicable.

Deterministic Evidence properties are established instrumentally before more expensive semantic assessment proceeds.

### 12.3 Direct local Evidence use

Evidence directly affects Decision making only where its support relation is valid in the local engineering context.

For local Evidence $e_i$ and Decision $d_i$:

$$Supports_{\kappa_i}(e_i,d_i)$$

can be used directly when the applicable Scale, Magnification, Scope, revision, state, and Evidence validators permit that relation.

Reverse traceability is available through the converse:

$$IsSupportedBy_{\kappa_i}(d_i,e_i).$$

The two expressions identify the same semantic edge.

This permits efficient bidirectional engineering questions such as which Decisions this Evidence supports and which Evidence supports this Decision, without storing two independent relations.

Evidence does not acquire authority because it supports a Decision.

Likewise, a Decision does not make every Evidence item that supports it relevant to every context affected by the Decision.

### 12.4 Evidence feedback across Engineering Layers

Evidence does not directly cross an incompatible Engineering Layer boundary as an evidential relation.

For Evidence $e_j$ at Engineering Layer $L_j$ and a broader Engineering Layer $L_i$:

$$Reachable(e_j,L_i)\not\Rightarrow DirectlyApplicable(e_j,L_i)$$

and:

$$Reachable(e_j,p_i)\not\Rightarrow Supports_{\kappa_i}(e_j,p_i).$$

When locally assessed Evidence identifies a condition relevant to the adjacent broader Scale, the originating context produces a Feedback Exchange Item.

The feedback loop is:

$$Evidence_j\rightarrow FeedbackExchangeItem_{j\rightarrow i}\rightarrow LocalInterpretation_i$$

and, when a Decision is required:

$$LocalInterpretation_i\rightarrow Decision_i.$$

This preserves the compact established propagation form:

$$Evidence_j\rightarrow FeedbackExchangeItem_{j\rightarrow i}\rightarrow Decision_i$$

with local interpretation understood as part of the receiving operation.

The originating Evidence remains associated with its local engineering context.

The Feedback Exchange Item carries only the information appropriate for the receiving boundary.

### 12.5 Feedback Exchange Item information discipline

A Feedback Exchange Item is a specialized Informational Exchange Item used to deliver a boundary-relative projection of Evidence from an affected Engineering Layer toward an adjacent broader Engineering Layer.

Its purpose is to communicate the Evidence information required for reassessment at the receiving boundary.

The originating Evidence remains associated with its local engineering context and remains canonically addressable.

The Feedback Exchange Item preserves source identity and provenance sufficient for reverse traversal and explicit retrieval of the originating Evidence.

The applicable Project Profile and Contract determine required Evidence projection content, permissible supplementary provenance, information-exposure restrictions, and required Work Product interaction.

The receiving Layer can explicitly retrieve the originating Evidence where the projection is insufficient for its governed engineering activity.

### 12.6 Evidence and Work Products

A Work Product is not interchangeable with a Feedback Exchange Item.

A Work Product is the complete result required by a Contract.

A Feedback Exchange Item is boundary-relative communication used for feedback propagation.

Evidence Propositions can nevertheless participate in Work Products according to the applicable Contract and Project Profile.

A Work Product can contain Evidence, reference Evidence, contain Evidence relations, carry an applicable Feedback Exchange Item, use Evidence to support its conformity claim, or become input to another Contract.

The existence of Evidence in a Work Product does not make that Evidence directly applicable to every Engineering Layer that can access the Work Product.

Therefore:

$$ContainedIn(e,WP)\not\Rightarrow DirectlyApplicable(e,L)$$

for an arbitrary receiving Engineering Layer $L$.

Evidence use remains governed by local Evidence and Scale rules.

Work Product information-boundary rules remain applicable independently of Evidence traceability.

### 12.7 Explicit Evidence retrieval

The originating Evidence remains canonically addressable and traceable.

A Feedback Exchange Item or Work Product can preserve a reference to its source Evidence without copying the Evidence into the receiving context.

Therefore:

$$Addressable(e)\not\Rightarrow Distributed(e)$$

and:

$$ReferencedBy(f,e)\not\Rightarrow ImportedIntoDecisionContext(e).$$

A receiving Engineering Layer can explicitly retrieve source Evidence when the Feedback Exchange Item does not contain sufficient information for local assessment, independent verification requires the source Evidence, a local Evidence argument requires detailed provenance, or the applicable Contract or Project Profile requires it.

Retrieval makes the Evidence available for an explicit receiving activity.

It does not automatically establish that the retrieved Evidence supports a receiving-layer Proposition.

The local support relation must still be established under the applicable Evidence validators.

### 12.8 No automatic Evidence composition

Evidence participates in the Proposition graph and can therefore be reached through structural traversal.

Structural reachability does not establish Evidence support.

For:

$$e\in E_{\kappa}$$

and:

$$p\in\mathbb P$$

$$Reachable_G(e,p)\not\Rightarrow Supports_{\kappa}(e,p).$$

Likewise:

$$Supports_{\kappa}(e,p_1)\land r(p_1,p_2)\not\Rightarrow Supports_{\kappa}(e,p_2)$$

unless the applicable relation calculus explicitly defines a sound semantic composition rule for that combination.

The same restriction applies when the path contains Decisions, Exchange Items, Feedback Exchange Items, Work Products, Engineering Objects, or other Propositions.

A sequence of valid graph edges does not automatically create evidential closure.

This prevents Evidence laundering, accidental Evidence inheritance, implicit Evidence composition, uncontrolled cross-Scale Evidence reach, foreign-context pollution, and authority being inferred from Evidence volume or verbosity.

### 12.9 Broad-relevance Evidence and field feedback

A single Evidence Proposition can have potentially broad Product relevance without having broad direct evidential applicability.

For Evidence $e$:

$$WidePotentialRelevance(e)\not\Rightarrow WideDirectApplicability(e).$$

Consider a field bug report describing unexpected behavior in one vehicle or one component.

The report can potentially indicate a condition relevant to a physical element, component, subsystem, vehicle behavior, fleet population, Product requirements, or customer experience.

This potential Scale range does not create direct Evidence relations to every one of those contexts.

The owning Engineering Layer first assesses the Evidence locally.

If the condition can be resolved locally, propagation stops.

If the condition is relevant to the adjacent broader Engineering Layer, the local context creates:

$$FeedbackExchangeItem_{component\rightarrow subsystem}.$$

The subsystem context interprets that feedback and reassesses its local Solution Space and Decisions.

If the subsystem resolves the condition, propagation stops.

If it cannot, that layer creates a new Feedback Exchange Item for the next affected Scale.

The original field report does not need to enter every Product, architecture, software, manufacturing, regulatory, UX, or service Decision context merely because the observed condition can eventually have consequences there.

The same principle applies to an end-user claim.

An end-user claim can be important Evidence at the context in which it is assessed and can initiate a substantial feedback loop.

It does not thereby become direct Evidence for every Engineering Layer reached by that feedback loop.

### 12.10 Confidence and Evidence processing

Confidence can use Evidence-processing history and trend information as inputs to an operational assessment of likely task outcome.

For example, the Hive can observe that Evidence of a certain form has historically tended to confirm a trajectory, expose a recurring deficiency, require additional testing, create a Gap, trigger rework, or remain inconclusive.

These observations can contribute to:

$$Confidence_H(q,t)$$

or to an internal Evidence-processing indication such as:

$$Confidence_H(EvidenceProcess,q,t).$$

This means that, based on current Evidence, historical resolution patterns, and the current trend, the process appears more or less likely to resolve successfully.

It does not mean:

$$P(Claim\mid Evidence)=Confidence.$$

Confidence is not itself Evidence and does not replace the Evidence algebra.

A Confidence threshold cannot by itself dismiss or accept Evidence:

$$Confidence_H(q,t)<\theta\not\Rightarrow Dismiss(e)$$

$$Confidence_H(q,t)>\theta\not\Rightarrow AcceptEvidence(e).$$

Evidence remains subject to its own relevance, provenance, independence, representativeness, applicability, sufficiency, and validity rules.

Confidence can also contribute to deciding where additional Evidence processing is economically useful. It must not be the sole threshold for discarding Evidence or for substantive Human escalation.

Thus, as a universal rule:

$$Confidence_H(q,t)<\theta\not\Rightarrow HumanAlert(q).$$

A Project Profile can combine Confidence with actual operational observations such as repeated validation failure, Resource Envelope pressure, unhealthy divergence, inability to obtain required Evidence, persistent rework, deadline risk, or explicit Human-reserved authority.

## 13. Maturity, prescriptiveness, and brittleness

Maturity in this proposal is not an Acceptance state, completeness score, quality grade, or lifecycle state.

It represents **deliberate prescriptiveness** at a defined engineering context: how much of the currently feasible solution freedom a Proposition removes.

Maturity changes alter the Solution Space. They therefore also require reassessment of the affected Decision Blast Radius and Decision Extent.

### 13.1 Prescriptiveness order

For context $\kappa$, let:

$$F_\kappa$$

be the feasible solution region before applying Proposition $p$.

Let:

$$F_\kappa[p]=\{x\in F_\kappa\mid x\text{ satisfies }p\}$$

be the feasible region remaining after $p$ is applied.

Two Propositions are equivalent with respect to prescriptiveness when they leave the same feasible region:

$$p_1\equiv_\kappa p_2\iff F_\kappa[p_1]=F_\kappa[p_2].$$

Define the prescriptiveness order by:

$$[p_1]_\kappa\preceq_M[p_2]_\kappa\iff F_\kappa[p_2]\subseteq F_\kappa[p_1].$$

Therefore $p_2$ is at least as prescriptive as $p_1$ when it leaves no more solution freedom than $p_1$.

The order is partial. Propositions constraining different dimensions can be incomparable.

Prescriptiveness is context-qualified. The same Proposition can remove substantial freedom in one engineering context and little freedom in another.

### 13.2 Maturity interpretation

Maturity describes whether the degree of prescriptiveness is intentional and appropriate for the current engineering horizon.

A mature Proposition does not have to contain more detail.

A high-level Proposition can be mature while deliberately preserving substantial implementation freedom.

A detailed Proposition can be mature when the applicable engineering context has sufficient reason and authority to constrain that detail.

The model therefore does not infer:

$$MoreDetail\Rightarrow MoreMature$$

or:

$$MorePrescriptive\Rightarrow Better.$$

Maturity, correctness, evidence sufficiency, Acceptance, and lifecycle state remain separate properties.

### 13.3 Maturity change and Decision Extent

A change in Maturity changes the feasible Solution Space and can alter the effects of existing Decisions.

Therefore:

$$MaturityChanged(p,\kappa)\Rightarrow ReassessBlastAndExtent(p,\kappa).$$

This rule does not mean that every Maturity change necessarily produces a large Decision Extent.

It means that the existing Decision Blast Radius cannot be assumed to remain valid after the feasible Solution Space changes.

An increase in prescriptiveness can:

- invalidate downstream alternatives;
- narrow existing implementation choices;
- require Decision rework;
- change Exchange Items;
- trigger Work Product rework or reverification;
- propagate through subsequent Engineering Layers under the adjacent-layer propagation rules. The economic impact can therefore be much larger than the apparent size of the changed Proposition.

#### 13.3.1 Freezing a de-facto downstream solution

A special case occurs when an upstream Maturity change formalizes a solution that is already established de facto at the adjacent downstream Scale.

In this case the material implementation can already conform to the new upstream restriction, so the immediate Decision Blast Radius can be smaller than for a genuinely new constraint.

This does **not** make the pattern economically or architecturally desirable by itself.

The upstream change still evolves the Solution Space and requires the affected downstream state, traceability, evidence, Decisions, and Work Products to be reassessed for consistency.

The pattern can be legitimate when downstream engineering has, for a valid reason, performed engineering normally owned by an upstream context and the result is subsequently propagated upward through the applicable adjacent-layer propagation and authority rules.

Examples can include a lower-level feasibility discovery, supplier engineering result, manufacturing constraint, or implementation finding that causes the upstream context to adopt an already-developed solution.

The exception therefore permits **reverse engineering influence**, not silent inversion of Scale authority.

### 13.4 Revision Envelope

Brittleness is evaluated against a declared set of plausible perturbations or revisions.

For Proposition or solution state $p$, let:

$$\Delta(p,\kappa)$$

be the Revision Envelope applicable in context $\kappa$.

The Revision Envelope can include:

- plausible requirement changes;
- parameter changes;
- interface changes;
- implementation substitutions;
- environmental changes;
- local physical changes;
- changes to assumptions;
- other project-relevant perturbations.

A brittleness claim without a declared Revision Envelope is incomplete.

### 13.5 Impact of revision

For a perturbation:

$$\delta\in\Delta(p,\kappa)$$

let:

$$Impact(p,\delta,\kappa)$$

represent the resources and engineering effects required to restore a valid state.

Impact is multidimensional and can include:

$$Impact=(time,money,compute,humanEffort,rework,reverification,coordination,physicalChange,schedule,\ldots).$$

Re-exploration is one possible component. It is not the definition of Brittleness.

Likewise, the applicable Contract Resource Envelope does not define whether the solution is brittle. A solution can be brittle even when a particular project has enough resources to absorb the impact.

### 13.6 Brittleness

Brittleness is sensitivity of an engineering solution to a **small, subtle, local, or wrong-Scale detail whose change produces disproportionate engineering and economic impact**.

The Project Profile defines how the applicable context distinguishes a minor trigger from severe impact.

Conceptually:

$$Brittle(p,\Delta,\Theta,\kappa)$$

holds when:

$$\exists\delta\in\Delta(p,\kappa):MinorOrWrongScale(\delta,p,\kappa)\land Severe_\Theta(Impact(p,\delta,\kappa)).$$

`MinorOrWrongScale` can represent a change that is, for the applicable context:

- small in scope;
- subtle in meaning;
- local in Product structure;
- low in apparent implementation effort;
- introduced at an inappropriate Scale or Magnification.

`Severe` represents disproportionate effect on engineering economy, including time, money, computation, human effort, physical work, coordination, or other applicable resources.

The common proposal does not prescribe one universal numeric threshold.

The essential property is **disproportion** between the apparent significance of the triggering detail and the resulting impact.

### 13.7 Maturity and Brittleness

Maturity and Brittleness remain formally distinct properties.

The proposal does not assert:

$$MoreMature\Rightarrow MoreBrittle$$

because that implication is not established.

However, increasing prescriptiveness can create conditions that make Brittleness more likely: fewer remaining alternatives can make later changes harder to absorb and can increase Decision Extent or downstream rework.

Therefore a material increase in Maturity should prompt Brittleness assessment, but Brittleness is established only from actual sensitivity to plausible perturbations.

A highly prescriptive solution can remain robust.

A less prescriptive solution can still be brittle when a subtle or wrong-Scale detail produces severe consequences.

### 13.8 Relationship to Decision Extent

Decision Extent and Brittleness answer different questions.

**Decision Extent** asks:

> How far does the effect of this Decision reach?

**Brittleness** asks:

> How severe is the engineering and economic consequence of a relatively small or inappropriate trigger?

A Decision can have:

- large Decision Extent without being brittle, when a broad change is expected to affect a broad region;
- small Decision Extent but high Brittleness, when a small local change causes severe cost inside that region;
- both large Decision Extent and high Brittleness, which is a strong signal that the Decision requires reassessment.

Maturity changes can affect both dimensions and therefore require reassessment of each rather than assuming one from the other.

## 14. UNKNOWNs, Gaps, and Future Actions

UNKNOWNs and Gaps preserve incomplete engineering knowledge explicitly.

Missing or invalid engineering information does not become complete through a plausible but unjustified relation.

### 14.1 Orphan and false-parent Gap

For required relation family $r$:

$$RequiredRelation(p,r,\kappa)\land\nexists q:Valid_r(p,q,\kappa)\Rightarrow Orphan(p,r,\kappa).$$

A false-parent Gap occurs when an asserted relation fails semantic validation:

$$Asserted_r(p,q,\kappa)\land\neg Valid_r(p,q,\kappa)\Rightarrow FalseParentGap(p,q,r,\kappa).$$

An invalid relation does not resolve an Orphan.

The governance model rewards explicit incompleteness and penalizes false closure:

$$Reward(ExplicitOrphan)>Reward(UnsupportedTrace),$$

$$Penalty(DelusiveTraceability)>Penalty(ExplicitOrphan).$$

The purpose is to make truthful incompleteness economically preferable to fabricated traceability.

### 14.2 UNKNOWN

An UNKNOWN is required information whose value, validity, applicability, or result is not yet established.

#### 14.2.1 Owned UNKNOWN

An owned UNKNOWN belongs to the current engineering context.

If a Decision depends on it:

$$OwnedUnknown(u,\kappa)\land DependsOn(d,u)\Rightarrow BlocksCommitment(d)$$

until the UNKNOWN is resolved or explicitly dispositioned.

#### 14.2.2 Foreign UNKNOWN

A foreign UNKNOWN originates outside the current engineering context.

It becomes blocking only when material to the current commitment:

$$ForeignUnknown(u,\kappa)\land MaterialTo(u,d,\kappa)\Rightarrow BlocksCommitment(d).$$

Materiality is Project Profile dependent.

Non-material foreign UNKNOWNs do not trigger unbounded investigation.

### 14.3 Known Gap

A Known Gap is an explicit known deficiency.

The deficiency and affected engineering context are known. Its final resolution is not yet available.

A Known Gap is therefore different from an UNKNOWN.

### 14.4 Future Action

A Future Action provides controlled deferred closure for a Known Gap when the required engineering result cannot yet be produced because necessary Product state, evidence, or physical realization does not yet exist.

A Future Action is represented as:

$$FA=(Party,Trigger,Outcome,Artifacts,Method,DoR,DoD).$$

where:

- `Party` identifies the responsible party;
- `Trigger` identifies the condition that makes execution possible;
- `Outcome` identifies the required result;
- `Artifacts` identifies the required Engineering Objects or information;
- `Method` identifies the applicable activity or reference;
- `DoR` identifies readiness conditions;
- `DoD` identifies completion conditions.

A Future Action is not an UNKNOWN. The Gap, responsibility, expected result, and closure mechanism are known. Execution is deferred because its prerequisites are not yet available.

#### 14.4.1 Deferred closure and Baseline

A project can establish a Baseline that contains a Known Gap when the applicable Project Profile permits deferred closure and a valid Future Action controls that Gap.

Conceptually:

$$KnownGap(g)\land FutureAction(f,g)\land AuthorizedDeferredClosure(g,f,B)\Rightarrow BaselinePermitted(B).$$

The Future Action does not claim that the Gap is resolved. It allows Product progression without fabricating information that cannot yet legitimately exist.

#### 14.4.2 Completion

When the Future Action becomes executable, the responsible party performs the defined activity and produces the required artifacts.

Successful completion requires:

$$FutureActionCompleted(f)\land RequiredArtifactsValid(f)\Rightarrow GapResolved(g).$$

The resulting artifacts enter the applicable controlled engineering state according to project Configuration Management rules. They do not rewrite the historical state in which the Gap remained unresolved.

A failed Future Action preserves the Gap and triggers applicable reassessment or another authorized disposition.

### 14.5 Commitment and Acceptance boundary

A Decision does not become binding while a required owned UNKNOWN or material foreign UNKNOWN remains unresolved. For the applicable Scope $\sigma$, time $t$, and engineering context $\kappa$:

$$Binding(d,\sigma,t)\Rightarrow\neg OwnedUnknownRequired(d,\kappa)\land\neg MaterialForeignUnknownRequired(d,\kappa).$$

A Known Gap can cross a Baseline, commitment, or Acceptance boundary only when the applicable Contract or Project Profile explicitly permits that disposition.

Where deferred closure depends on a later Product state, the applicable Future Action identifies the responsible party, trigger, required outcome, artifacts, and completion conditions.

### 14.6 Temporal evolution

Typical semantic transitions include:

$$UNKNOWN\rightarrow Resolved$$

$$UNKNOWN\rightarrow KnownGap$$

$$KnownGap\rightarrow FutureAction\rightarrow Resolved.$$

Transitions preserve history. Later discovery does not rewrite earlier engineering state.

### Illustrative Material - Future Actions

*The following material is illustrative. It does not establish additional rules.*

Engineering Design can establish that a component requires calibration while valid calibration values cannot yet be produced because the Product is not sufficiently materialized. The Baseline can preserve the Known Gap together with a Future Action that identifies the responsible party, the required in-field or pre-production activity, and the artifacts that must later be produced and added to the controlled Product state as project-defined Supplementary Documents.

A typical progression is:

$$DesignNeed\rightarrow KnownGap\rightarrow FutureAction\rightarrow MaterializedProduct\rightarrow Calibration\rightarrow CalibrationArtifacts\rightarrow GapClosure.$$

The same pattern can apply to A/B testing, feature-flagged activation, parameter tuning, field measurement, commissioning adjustment, controlled deployment observation, supplier measurements available only from produced hardware, and other activities whose valid result depends on a later Product state.

The common temporal condition is:

$$CannotKnowNow\land CanKnowAfter(ProductState).$$

## 15. Recursive Y-model

The Y-model defines operational reconciliation rules from the point of view of a particular Product engineering need.

Engineering Domains evolve their Decisions, Contracts, Work Products, Evidence, and other engineering information independently and concurrently.

Product engineering establishes the information it requires and requests that information from the applicable Engineering Domains.

Each resulting information flow forms a Y Branch for that reconciliation.

### 15.1 Consumer-established information flow

A Y Branch is established by a Product engineering consumer need.

The information flow is pull-driven. Product engineering establishes the need and requests the required information. The source Domain interprets that request, resolves the applicable information, and returns it through an Exchange Item for Product engineering interpretation.

An Engineering Domain does not independently establish or push an information flow into Product engineering.

The consumer request determines the required engineering information.

The source Domain resolves the request against its applicable Engineering State and Magnification.

The Y Branch remains applicable while the consumer need and governed information relationship remain applicable.

A change inside the source Domain does not independently create a downstream information flow.

Where changed source information affects an established consumer need, that established relationship is reassessed through the applicable exchange and feedback mechanisms.

### 15.2 Fixed and Negotiable branches

The Y-model places each Y Branch on the Fixed or Negotiable side of the current Product engineering reconciliation.

Information requested from a Prescriptive Domain is placed on the Fixed branch.

Information requested from an Engineered Domain is normally placed on the Negotiable branch.

Information from an Engineered Domain can instead be placed on the Fixed branch when applicable engineering conditions make changing that source economically ineffective for the current reconciliation.

Both branches support feedback.

The receiving Product engineering activity does not directly modify information governed by another Engineering Domain.

For a Negotiable Y Branch, a receiving finding can request reconsideration by the governing Domain. The governing Domain interprets the feedback, determines whether a Decision or rework is required, and returns revised information through a subsequent Exchange Item where applicable.

A Fixed Y Branch can use the same feedback path.

Its difference is the Product engineering disposition.

Product engineering cannot resolve incompatibility with Fixed information by choosing an economically acceptable deviation from that information.

From the current Product engineering point of view, changing the Fixed-side source lies outside the economically effective Solution Exploration of that reconciliation.

The incompatibility remains explicit until Product engineering finds an admissible solution, establishes infeasibility, or a separately governed change alters the information that caused the Y Branch to be Fixed.

### 15.3 Domain and Scale locality

Cross-Domain information exchange occurs at the same Scale position.

Cross-Scale propagation occurs through adjacent Engineering Layers inside one Engineering Domain.

The two operations are distinct.

One Exchange Item cannot simultaneously change both Engineering Domain and Scale.

The underlying graph can contain arbitrary structural edges, but engineering use of those edges remains subject to Scale, Domain, semantic, Scope, authority, Contract, information-boundary, and relation validation.

Magnification preserves applicable intermediate Engineering Layers and prevents a valid vertical engineering flow from being compacted into a distant direct relation merely because the underlying graph contains such an edge.

### 15.4 Magnification and information relevance

Magnification controls traversal through the Engineering Layers of an Engineering Domain.

The common model does not prescribe a fixed number of Engineering Layers.

Different Domains can contain different engineering detail.

Product engineering requests the information required by its current engineering need.

The source Domain resolves that request at the applicable Magnification.

Fine engineering information remains local while the consumer need does not require it.

When fine engineering creates a material consequence relevant to a coarser Product engineering need, the requested information is resolved through the applicable Domain-local adjacent Layers before the cross-Domain exchange occurs.

The complete fine-detail Work Product does not need to become part of the coarser Product engineering context.

**Illustration — homologation.**

Product engineering pulls required information from a Prescriptive homologation Domain at the applicable Magnification, so the resulting Y Branch is Fixed. Finer homologation engineering remains local until the Product engineering consumer requires information representing its material consequence. This Illustration defines no required homologation process, Layer structure, or implementation binding.

**Illustration — accessibility and UX.**

Accessibility information pulled from a Prescriptive Domain is Fixed, while information pulled from an Engineered UX Domain is normally Negotiable even when the UX Decisions were developed using Fixed accessibility information. This Illustration defines no required accessibility, UX, or implementation process and creates no implementation binding.

## 16. Supporting processes over Solution Space

Configuration Management, Change Management, Problem Resolution, Quality Assurance, Risk Management, Measurement, release management, production control, and similar disciplines operate over Solution Space entries and Engineering Objects.

They are supporting processes, not universal semantic primitives. A Baseline, for example, exists only where Configuration Management establishes it. A production batch can be accepted without becoming a Baseline. Software can pass acceptance testing before deployment, while production deployment performs only project-defined sanity checks.

Supporting-process predicates remain Project Profile parameters unless a Contract or applicable external norm makes them obligatory.

Supporting-process states apply independently to Product and Work Product where the project defines them. For example:

$$Baselined(w)\not\Rightarrow Baselined(P)$$

and:

$$Released(P)\not\Rightarrow Released(w).$$

The project can deliberately align such states. The common model does not. Likewise:

$$Accepted(w,C)\not\Rightarrow Released(P)$$

$$Accepted(w,C)\not\Rightarrow Deployed(P)$$

$$Accepted(w,C)\not\Rightarrow Produced(P).$$

## 17. Swarm exploration, divergence, waste, and resource control

### 17.1 Resource Envelope

The proposal does not use the phrase `bounded resources` as an undefined scalar. A Resource Envelope is a vector of declared availability or limits:

$$R=(context,modelCalls,compute,wallTime,money,humanEffort,energy,equipment,externalCapacity,\ldots).$$

A Contract can define a narrower Resource Budget inside the project/Hive envelope.

### 17.2 Cluster support and resource survival

Clusters exist only relative to one Swarm task or problem statement.

For problem $q$, let:

$$C_{d,q,t}$$

be the Cluster of contributions that support Decision $d$ at time $t$.

Cluster support measures **independent convergence**, not truth.

The Project Profile defines:

$$Support_{PP}(C_{d,q,t})$$

using contribution independence, evidence, provenance, and other applicable factors.

Repeated or strongly correlated contributions do not automatically increase effective support. Therefore:

$$MoreContributions(C)\not\Rightarrow MoreEvidence(C)$$

and:

$$GreaterSupport(C)\not\Rightarrow True(d).$$

Cluster support is used for **resource allocation and trajectory survival**.

For trajectory $\tau$:

$$Allocation(\tau,t)=Rate_{PP}(Support,Evidence,Progress,Novelty,DeliveryValue,Divergence,ResourceCost,ResourceEnvelope).$$

The Project Profile defines the rating function and thresholds.

An active trajectory can receive increased, maintained, reduced, or zero allocation.

Zero allocation deactivates exploration but does not delete its results:

$$Allocation(\tau,t)=0\not\Rightarrow Delete(\tau).$$

Discovered Decisions, evidence, alternatives, and outliers remain addressable.

### 17.3 Waste and overthinking

Waste is not synonymous with overhead. Required verification, governance, communication, or setup can consume resources without being waste.

Waste occurs when an operation produces neither required process effect nor reusable progress, evidence, knowledge, or Product value. Polling loops, repeated context replay, unnecessary status messages, redundant branch reasoning, and reasoning about deterministic facts are candidate waste categories when the project can establish that they add no required effect.

Overthinking is a reasoning-specific waste mode. Before assigning further reasoning work to a Swarm, the Hive should determine whether deterministic algebra, an existing Decision, recorded evidence, or a previously preserved outcome already resolves the question.

### 17.4 Contention and divergence

Different trajectories are not divergent merely because they differ.

Two trajectories contend only when they address the same scoped problem and cannot coexist in one valid solution:

$$Contend(\tau_1,\tau_2,q)\Rightarrow SameProblem(\tau_1,\tau_2,q)\land\neg CoexistFeasibly(\tau_1,\tau_2,q).$$

Difference without incompatibility does not require reconciliation.

#### 17.4.1 Divergence as reconciliation difficulty

Divergence is the engineering difficulty of reconciling contending trajectories.

It is not defined by:

- textual distance;
- semantic embedding distance;
- number of disagreeing agents;
- majority size.

Reconciliation is a direct exploration problem, consistent with Section 10.4.

Let:

$$\mathcal{R}_{rec}(\tau_1,\tau_2,t)$$

be the valid reconciliation candidates discovered so far.

Each candidate $r$ has a Resource Cost vector:

$$RC(r)=(money,time,compute,humanEffort,WPRework,physicalRework,coordination,scheduleExposure,\ldots).$$

The observed divergence is therefore determined from the explored reconciliation space rather than from an assumed inverse operation.

The proposal does not assume a universal scalar distance.

#### 17.4.2 Divergence health

The Project Profile defines a health function:

$$Health_{PP}(\tau_1,\tau_2,t)$$

using factors such as:

- explored reconciliation cost;
- persistence of incompatibility;
- progress;
- independent support;
- evidence;
- expected Product value;
- consumed Resource Cost;
- available Resource Envelope.

Persistent strong support on both sides does not justify unlimited continued expenditure.

When divergence becomes unhealthy, active allocation is reduced according to the Project Profile.

#### 17.4.3 Back-off

Back-off controls **future resource expenditure**, not preservation of engineering knowledge.

Conceptually:

$$UnhealthyDivergence(\tau,t)\Rightarrow Allocation(\tau,t+\Delta t)<Allocation(\tau,t).$$

A Project Profile can define exponential or another project-appropriate back-off function.

Repeated failure to produce useful progress can eventually result in:

$$Allocation(\tau,t)=0.$$

The trajectory is then inactive but remains addressable.

#### 17.4.4 Post-mortem and exploratory restart

When a trajectory is deactivated because of unhealthy divergence, the Hive preserves:

- relevant Decisions;
- rejected and surviving alternatives;
- evidence;
- outliers;
- reconciliation attempts;
- causes of failure;
- Resource Cost.

A post-mortem can update the known Solution Space and create a new exploration trajectory.

This is an **exploration restart**. It does not erase the earlier trajectory.

It is also distinct from Contract identity: a Contract is not restarted merely because its execution encounters divergence.

### 17.5 Contract execution convergence and divergence

Contract execution is bounded Solution Exploration and therefore uses the same convergence/divergence governance as other exploration.

For Contract $C$, let $\tau_C$ denote its active execution trajectory. The trajectory can include construction attempts, verification results, integration attempts, rework, repeated submissions, feedback resolution, alternative execution approaches, and repair exploration.

Contract execution is healthy while the trajectory demonstrates sufficient progress toward a valid fulfilment state under the applicable Resource Envelope.

#### 17.5.1 Rework is exploration

A rework request does not imply that one predetermined correction exists. It reopens the affected part of Solution Exploration:

$$ReworkRequest\rightarrow AffectedSolutionExploration$$

not:

$$ReworkRequest\rightarrow PredeterminedFix.$$

The responsible context explores a valid correction under the applicable Contract, Decision, Evidence, Scale, and authority rules. This is consistent with the existing rule that, in general:

$$Repair(\Delta)\neq\Delta^{-1}.$$

#### 17.5.2 Repeated rework and integration failure

One failed integration attempt does not by itself establish unhealthy divergence. Failure provides Evidence about the current trajectory. Repeated failure without adequate progress is a convergence signal.

Relevant signals can include repeated rejection of the same Work Product, recurrence of the same defect class, repeated incompatibility, repeated integration or verification failure, repeated rework without reducing the affected problem, increasing Resource Cost with insufficient progress, persistent disagreement between responsible Actors, and inability to reconcile contending engineering trajectories.

The Project Profile can include these factors in the existing divergence-health calculation:

$$Health_{PP}(\tau_C,t).$$

Continuous activity is not equivalent to convergence. Therefore:

$$MoreReworkCycles\not\Rightarrow MoreProgress$$

and:

$$MoreIntegrationAttempts\not\Rightarrow Convergence.$$

#### 17.5.3 Contract back-off

When Contract execution becomes unhealthy:

$$UnhealthyDivergence(\tau_C,t)\Rightarrow Allocation(\tau_C,t+\Delta t)<Allocation(\tau_C,t)$$

under the applicable Project Profile.

Back-off reduces future expenditure on the failing execution trajectory. It does not erase the Contract, Work Products, Decisions, Evidence, failed integration results, rework requests, verification results, provenance, or execution history.

Repeated failure can eventually produce:

$$Allocation(\tau_C,t)=0.$$

The current execution trajectory then becomes inactive. Contract history remains addressable.

#### 17.5.4 Agent and Actor deactivation

Back-off can operate on execution resources contributing to an unhealthy trajectory.

For an internal Agent $a$:

$$PersistentLowValue(a,\tau_C)\Rightarrow Deactivate(a,\tau_C)$$

can remove that Agent from active execution while preserving useful outputs and provenance.

For an Actor $A$, deactivation is Contract/context qualified. The model does not infer global deletion or invalidity of the Actor. Instead, $Deactivate(A,C)$ means that the Actor is no longer used in the applicable active Contract role or execution trajectory.

If the deactivated Actor is the Contract Executor:

$$Executor(C)=A\land Deactivate(A,C)$$

then execution cannot continue under an implicit replacement. A new valid Assignment is required:

$$Deactivate(Executor(C),C)\Rightarrow RequireReassignment(C)$$

before governed execution resumes. This preserves:

$$\exists!a:\ Assignment(C,a)$$

for every executable Contract state.

#### 17.5.5 Post-mortem and recovery

Unhealthy Contract divergence triggers the existing exploration post-mortem logic.

Recovery can require a different Agent population, another Swarm composition, Executor reassignment, Contract revision, Contract decomposition, a different integration strategy, reopening an engineering Decision, additional Evidence, modification of Resource Envelope, escalation to another Actor, Human intervention where applicable, a successor Contract, or termination where no viable continuation exists.

The recovery mechanism addresses the cause of unhealthy execution rather than merely repeating the failed trajectory. Therefore:

$$Unhealthy(\tau_C)\not\Rightarrow Repeat(\tau_C)$$

without a justified change to the execution conditions.

#### 17.5.6 Contract continuity and exploration restart

An exploratory restart is not a rewrite of Contract history. The original Contract state and failed trajectory remain addressable.

Recovery can continue under the same Contract where its semantics permit recovery, or through revision, reassignment, decomposition, successor Contract, or another governed transition.

Therefore:

$$ExplorationRestart\neq HistoricalContractReset.$$

The Hive preserves failure information because it is part of the Solution Space and is required to prevent repetition of the same unhealthy trajectory.

### 17.6 Confidence as operational exploration-health indication

Confidence is a time-varying operational indication of Solution Exploration health under the information currently available to the Hive and the applicable Resource Envelope.

For bounded task or problem $q$:

$$Confidence_H(q,t).$$

Confidence can also be evaluated for a trajectory or a scoped Decision context where that distinction is operationally useful.

Confidence is related to convergence and divergence without being equivalent to either:

$$Convergence\not\Rightarrow HighConfidence$$

$$Divergence\not\Rightarrow LowConfidence.$$

Confidence remains distinct from the Resource Envelope itself.

#### 17.6.1 Inputs and update

The Project Profile defines the Confidence representation, observation window, update frequency, and applicable inputs. Inputs can include progress, convergence, divergence, Evidence, Decision progression, validation results, rework history, Resource Cost, remaining Resource Envelope, and historical resolution patterns.

Confidence need not be monotonic. New Evidence, failed validation, a newly viable trajectory, or a material resource change can alter the indicator in either direction.

#### 17.6.2 Semantic boundaries

Confidence is not truth, probability, precision, Evidence, authority, Decision, Acceptance, Back-off, or Work Product content.

A high or low Confidence indication therefore establishes none of those properties.

Confidence is not Back-off:

$$Confidence\neq BackOff.$$

Low Confidence does not itself require Back-off:

$$LowConfidence_H(\tau,t)\not\Rightarrow BackOff(\tau).$$

Back-off remains governed by the divergence and resource rules of §§17.4–17.5.

#### 17.6.3 Exploration diversity

Confidence can inform resource allocation and reassessment without forcing deterministic selection of the currently highest-rated trajectory.

A Project Profile can permit bounded stochastic or Monte-Carlo mechanisms for exploration diversity. Such mechanisms operate on exploration policy; they do not randomize the Confidence indication itself.

Exploration remains constrained by Engineering State, Contracts, authority, validation, Resource Envelope, and commitment rules.

#### 17.6.4 Operator-facing representation

A Human operator can observe Confidence and its trend without reconstructing the full exploration history.

**Illustration.** A Project Profile can map Confidence to a traffic-light presentation for operator attention. The labels and thresholds are presentation choices only; they establish no Decision, validator result, Evidence disposition, authority, Contract transition, or Back-off.

#### 17.6.5 Automated use

A Project Profile can use Confidence as one input to automated operational policy where the policy has an Evidence basis appropriate to the applicable environment.

Confidence alone establishes no Decision, authority, Acceptance, Evidence disposition, Contract transition, Product materialization, Rollback, or Back-off.

#### 17.6.6 Post-mortem learning

Post-mortem analysis can compare historical Confidence with later observed outcomes to identify systematic drift, delayed failure recognition, poor interpretation of Evidence trends, or ineffective response to resource pressure.

The Project Profile or computational components can then be tuned prospectively. Historical Confidence values remain unchanged.

## 18. Derived no-sphere theorem

### Theorem NS-1 - No authority or Evidence sphere

Assume:

1. Decision and Evidence are Proposition roles.
2. Proposition relations are typed and context-qualified.
3. Every canonical relation has a derived converse available for reverse traceability.
4. Converse traversal does not create a second semantic fact.
5. Structural reachability does not establish semantic justification.
6. Decisions have direct effect only inside their valid local engineering context.
7. Evidence directly supports Propositions only where its Evidence relation is valid locally.
8. Cross-Scale effects require applicable adjacent-layer materialization and local interpretation.
9. Downward Decision effects are materialized through Exchange Items.
10. Upward Evidence effects are materialized through Feedback Exchange Items.
11. Receiving Engineering Layers perform local interpretation.
12. Evidence support, evidential closure, and Decision authority do not automatically compose through relation paths.

Then neither forward nor reverse graph traversal can make a local Decision or local Evidence Proposition directly authoritative or evidentially sufficient at an incompatible foreign Engineering Layer.

A local Decision can influence another Scale through:

$$Decision_i\rightarrow ExchangeItem_{i\rightarrow j}\rightarrow Decision_j$$

when a receiving Decision is required.

Local Evidence can influence a broader Scale through:

$$Evidence_j\rightarrow FeedbackExchangeItem_{j\rightarrow i}\rightarrow Decision_i$$

when a receiving Decision is required.

The corresponding graph can be traversed in reverse for traceability.

For example, from a Decision the Hive can trace toward the Feedback Exchange Item and ultimately toward the Evidence that caused the feedback.

Such reverse traversal answers what source information contributed to this local Decision.

It does not make the receiving Decision authoritative over the source Evidence and does not make the originating Evidence directly sufficient for the receiving Decision.

Therefore, let $\sigma_j$ be the applicable receiving Scope at Engineering Layer $L_j$. Then:

$$Reachable(d_i,L_j)\not\Rightarrow Binding(d_i,\sigma_j,t)$$

and:

$$Reachable(e_j,L_i)\not\Rightarrow EvidenceClosure_i(e_j).$$

Likewise:

$$ReverseReachable(d_i,e_j)\not\Rightarrow Supports_{\kappa_i}(e_j,d_i)$$

unless that local support relation is independently valid.

The model therefore supports full bidirectional traceability without creating bidirectional semantic authority.

Information can propagate through many Engineering Layers while Decisions, Evidence support, evidential closure, and authority remain local.

**Derived property:** Decisions and Evidence remain local semantic Propositions. Their engineering effects cross Scale boundaries only through explicit materialized exchanges and renewed local interpretation. Forward and reverse graph traversal preserve traceability but do not create semantic inheritance.

### Execution-topology extension

Execution topology does not create authority topology. Therefore:

$$Reachable_{ContractTopology}(C_i,C_j)\not\Rightarrow Authority(C_i,C_j)$$

$$SameHuman(h,L_i,L_j)\not\Rightarrow AuthorityPropagation(L_i,L_j)$$

$$SameHive(C_i,C_j)\not\Rightarrow AuthorityCollapse(C_i,C_j)$$

and:

$$Integrates(I,w)\not\Rightarrow DesignAuthority(I,w).$$

Contract execution can propagate results, feedback, rework requests, verification failures, and integration consequences without propagating implicit Decision authority.

**Derived property:** execution topology transports responsibility, results, dependencies, feedback, and exploration state. It does not transport authority unless an explicit authority mechanism establishes that effect.

# Part V - Conformance and Project Profile

## 19. Conformance

Conformance is evaluated against the common proposal plus the applicable Project Profile revision.

A conformant implementation MUST:

- preserve Proposition and Engineering Object distinction;
- validate relation use before semantic justification;
- preserve unresolved required information explicitly;
- enforce Scale locality, adjacent-layer propagation, and same-Scale cross-domain relation rules;
- enforce Human ingress and Decision authority rules;
- preserve all discovered outcomes while controlling active resource allocation;
- separate Decision authority from Exchange Item communication;
- enforce Contract accountability, Assignment and Obligation semantics, Work Product schemas, information boundaries, and Acceptance rules;
- apply the Check Cascade so that a higher-cost check does not bypass a failing or missing cheaper checking capability;
- satisfy required verification independence topology;
- preserve revision/time history;
- keep project-specific lifecycle/support-process predicates in the Project Profile unless the common model explicitly defines them.

A conformance claim MUST identify the model version, Project Profile revision, checker/review method, and evidence set.

### 19.1 Concurrent evolution and Rollback checks

The formal audit includes the following additional checks.

- **Concurrent divergence:** valid trajectories can originate from the same $X_0$ and remain intersecting while differing in their engineering progression.
- **Decision-order sensitivity:** for different admissible commitment orders over the same $D^*$, the most probable outcome is distinct trajectories and distinct ordered Work Product sequences.
- **Product-result divergence:** for repeated valid Hive executions from the same initial engineering basis, the most probable outcome is $P^{mat}_a\neq P^{mat}_b$; equality is a special convergence case established for the participating trajectories.
- **Monotonic Product Evolution History:** $t_1<t_2\Rightarrow K_{t_1}\subseteq K_{t_2}$.
- **Non-monotonic materialization:** Materialized Product State can grow or contract.
- **Non-monotonic Solution Space:** Solution Space can expand or contract as engineering progresses.
- **Decision/Contract dependency separation:** Contract dependency topology is distinct from Decision ordering.
- **Integration convergence:** the intended integration is available only when $W^{ready}_{C_I}=W_I$.
- **Rollback Evidence basis:** cancellation of a committed Decision has applicable Evidence.
- **One Rollback target:** one Rollback Contract cancels one committed Decision.
- **Single-Layer Rollback Closure:** $\Gamma_R(C_R)\subseteq D_{L_R}\cup C_{L_R}\cup W_{L_R}$.
- **Rollback Closure completeness:** same-Layer engineering that cannot remain valid after cancellation belongs to the Rollback Closure.
- **Current-state subtraction:** successful Rollback produces $P^{mat}_{t+1}=P^{mat}_t\setminus R_t(C_R)$.
- **Parallel-work preservation:** compatible materialization outside $R_t(C_R)$ remains active.
- **No snapshot restoration:** Rollback operates on current materialization rather than restoring an earlier historical Product snapshot.
- **Previously rolled-back history:** a new Rollback does not traverse backward through an element already cancelled by successful Rollback.
- **Cross-Layer locality:** one Rollback Contract does not cancel another Engineering Layer's Decisions or Work Products.
- **Rollback classification:** replacement realization or materially new Product intent is handled as ordinary engineering rather than Rollback.
- **Common traceability:** Rollback uses the common Product graph and relation algebra.

## 20. Project Profile

The Project Profile supplies project-specific values for parameters that the common model intentionally leaves open.

It specializes the common model for a Product, engineering domain, organization, lifecycle, or implementation context. It does not redefine the common foundation.

| Parameter group | Project-defined content |
|---|---|
| **Product and capability** | Product boundaries; admissible Product kinds and Product-intent representation; Product scope and state vocabularies; Product-to-Contract scoping; Product target satisfaction and Product Delivery Contract classes; Product/Work Product relations, composition and materiality; Hive capability representation and acquisition; enabling-technology representation and availability; Product Development Envelope assessment; capability and enablement change detection; external capability, supplier, and tooling involvement; Product-level acceptance, qualification, certification, release, production, deployment, delivery, and their relation to Contract Acceptance. |
| **Semantic model and relations** | Proposition roles; Engineering Object families; relation vocabulary; source/target signatures; converse labels; validators; semantic-composition rules. |
| **Scale and engineering topology** | Scale orientation; Magnification interpretation; adjacent Scale interval semantics; Engineering Layer establishment and refinement; Engineering Domain topology and Domain Nature; cross-Domain Scale alignment; Magnification traversal; state-relative adjacency; adjacent-Layer transfer; same-Scale cross-Domain relation rules; execution sub-scale rules; Product engineering consumer-need representation; Y Branch establishment and applicability; Y Branch placement rules; Informational and Objective Exchange Item boundary rules; Feedback Exchange Item rules. |
| **Work Products, Evidence, and validation** | Work Product schemas; semantic-role constraints; required validators; information-exposure policies; Acceptance rules; Instrumental Checks; Low-profile and High-profile Assessments; escalation and instrumentation-improvement rules; Evidence rules; UNKNOWN materiality; Gap and Future Action policy. |
| **Contract definition and lifecycle** | Contract-type vocabulary and required fields; identity, revision-materiality, and successor criteria; Product-target representation; Work Product Requirement schema; prerequisite and dependency types, states, and internal/external representation; Contract Resource Budget; Acceptance Specification; information policy; enforcement; supplementary participants; event types and retention; derived runtime views; Contract/Profile migration; readiness prerequisite kinds; lifecycle transition guards; runtime-regression and definition-revision materiality; same-time event ordering; temporary blocking and reassessment; readiness evaluation and resumption; Work Product preparation, submission, and revision handling; Acceptance materiality, dispositions, delegation, and reuse of unaffected validation or Evidence; discontinuation guards; blocker categories; successor and external Contract dependencies. |
| **Authority and Human input** | Contract parties; explicit authority sources and records; authority kinds and operation-level requirements; Human and non-Human authority Scope and applicability; Contract-Issuer, Contract-revision, Assignment, Decision-commitment, and Acceptance-delegation authority; delegability, delegation limits, revocation, expiry, and role combinations; Human identity/authentication where applicable; Human-input normalization, transformation, Scope, ordering, atomic/joint groups, composability, Decision Space derivation, infeasibility handling, retraction, supersession, and recovery. |
| **Execution, communication, verification, and integration** | Team API rules; external-party communication constraints and formats; Contract-type execution policies and Executor eligibility; required Contract-type independence and Hive/Actor separation; validation/verification independence topology; integration/composition strategies and validation requirements; integration-input verification and rework rules. |
| **Exploration, resources, Rollback, and recovery** | Trade Space representation; trajectory rating; Cluster independence; outlier policy; Rollback Cost model; Resource Envelope dimensions and measurement; invention allocation; Waste classification; Contract-execution health, divergence, and back-off; Agent and Contract-role Actor deactivation; reassignment; recovery; termination; post-mortem criteria. |
| **Confidence** | Response to material Contract and Acceptance failures; representation; observation window; trend calculation; update frequency; inputs from convergence/divergence, Evidence, Decision progression, validation, Resource Cost, remaining Resource Envelope, and historical resolution; permitted exploration-diversity mechanisms; operator-facing representation; permitted automated uses and their Evidence basis; post-mortem tuning and drift assessment. |
| **Supporting processes and lifecycle vocabulary** | Configuration Management, Change Management, Baseline, release, deployment, production, risk, quality, and other supporting-process predicates; lifecycle labels for Decisions, Engineering Objects, Work Products, Contracts, and other project elements. |

The Project Profile cannot create authority from Confidence, title, expertise, apparent seniority, conversational style, organizational visibility, or other social cues.

It cannot collapse Contract definition revision, lifecycle state, and historical event history into one destructively mutable state.

It cannot redefine Product and Work Product as universally identical concepts.

It cannot redefine Confidence as truth, probability, precision, Evidence, authority, Decision, Acceptance, Back-off, or Work Product content.

Technical Product interfaces remain engineering content. The Project Profile can configure their applicable engineering rules, but it does not make them part of the common governance model merely by naming them.

## 21. Formal model audit

### 21.1 Audit role

The Formal Model Audit tests the proposal against its defining sections.

It does not create a parallel source of engineering semantics.

Definitions, axioms, derived properties, Contract rules, relation semantics, and other engineering rules remain authoritative in the sections where they are defined.

An audit check therefore identifies:

1. the property being tested;
2. its defining section;
3. the countermodel or invalid condition being sought;
4. the observed result.

Where audit wording conflicts with a defining rule, the defining rule governs and the audit check is corrected.

### 21.2 Foundation countermodels

Each Foundation Axiom includes its own Intent, Statement, Boundary, and Validation argument.

A release audit tests at least the following countermodels:

| Axiom | Countermodel |
|---|---|
| **AX-1 – Semantic legitimacy** | A structural graph path is accepted as engineering justification without the applicable semantic validators. |
| **AX-2 – Truthful incompleteness** | Missing engineering information is replaced by fabricated completion or false traceability. |
| **AX-3 – Scale locality** | Decision, Evidence, authority, or semantic effect bypasses an applicable Engineering Layer or uses a diagonal cross-domain/Scale shortcut. |
| **AX-4 – Delegated autonomy** | Human approval becomes universally required, or the Hive commits an operation outside its applicable authority. |
| **AX-5 – Resource-rated exploration** | Low-support discoveries are deleted, or active exploration consumes resources without Resource Envelope control. |
| **AX-6 – Concurrent non-deterministic Product evolution** | Product engineering is treated as one deterministic sequential trajectory, or Product materialization is assumed to grow monotonically. |

### 21.3 Cross-cutting audit index

Cross-cutting audit areas reference their defining sections instead of restating those rules.

| Audit area | Primary audit focus | Defining model |
|---|---|---|
| **Engineering State and computation** | State Projection boundedness, temporary computation boundary, state-relative reassessment, historical preservation | §§5.4, 6.1 |
| **Human authority and input** | Explicit authority, operation/Scope/time qualification, ordered transformations, partial composition, history preservation | §5.5 |
| **Semantic algebra and revision** | Proposition/Object separation, relation typing, converse consistency, revision mapping, scoped supersession | §§5.3, 7, 8.1 |
| **Data reliability and checking** | Independent validity dimensions, Check Cascade order, cheaper-check improvement, re-entry after findings | §§8.3–8.5 |
| **Scale and Magnification** | same-Scale direct relations, adjacent-Layer transfer, no diagonal propagation, Magnification traversal | §9 |
| **Decision propagation** | Blast Radius before commitment, Decision Extent after materialization, locality and Brittleness distinction | §§9.16–9.22 |
| **Product and Work Product** | role/state separation, many-to-many relation, Acceptance locality, Product Delivery specialization, integration independence | §§6.7–6.11 |
| **Contracts and execution topology** | one accountable Assignment, readiness guards, lifecycle transitions, revision/runtime separation, authority locality | §11 |
| **Integration** | input qualification, readiness convergence, integration verification, contribution traceability | §§11.3–11.4 |
| **Evidence and feedback** | Evidence typing, local support, converse traceability, Feedback Exchange Item propagation, Evidence retrieval | §12 |
| **UNKNOWN, Gap, Future Action** | explicit incompleteness, commitment boundary, deferred closure, temporal preservation | §14 |
| **Rollback and Reshuffling** | Rollback Closure, current-materialization subtraction, single-Layer locality, preservation of parallel engineering | §10.4 and applicable propagation rules |
| **Execution resources and Confidence** | allocation, divergence/back-off, participant deactivation, Confidence boundaries and drift | §17 |
| **Formal identifiers** | symbol uniqueness, signature consistency, Project Profile suffixes, source integrity | §4.4 and §21.4 |

A release audit can add project-specific checks through the Project Profile.

Those checks can specialize open project parameters but retain the common-model semantics of their defining sections.

### 21.4 Formal Vocabulary Registry

The registry contains reusable common-model identifiers. Project Profile extension identifiers and explicitly local helper variables remain defined in their owning section.

| Identifier | Type / signature | Meaning | Defining section | Formal role |
|---|---|---|---|---|
| $Materializes$ | $\mathbb P\times\mathbb O$ relation | Connects a Proposition with an Engineering Object carrying or realizing it | §6.2 | relation |
| $DecisionKind(p,\kappa)$ | predicate | Proposition node $p$ has Decision kind in context $\kappa$ | §6.2 | predicate |
| $EvidenceRole(p,\kappa)$ | predicate | Proposition $p$ has Evidence role in context $\kappa$ | §6.2 / §12 | predicate |
| $ProductRole(x,\kappa)$ | predicate | $x$ plays Product role | §6.7 | predicate |
| $WorkProductRole(x,C)$ | predicate | $x$ plays Work Product role for $C$ | §6.7 | predicate |
| $AuthorizedFor(a,o,x,\sigma,t,\kappa)$ | predicate | Actor authority for operation $o$ on subject $x$ | §5.5 | predicate |
| $Binding(d,\sigma,t)$ | predicate/relation | Decision $d$ is binding in Scope/time | §5.5 | governed relation |
| $Assignment(C,a)$ | relation | Actor $a$ is the accountable Assignment of Contract $C$ | §11.1 | relation |
| $Issuer(C)$ | function | Issuer of Contract $C$ | §11.1 | function |
| $Executor(C)$ | partial derived function | Unique Actor established by valid Assignment | §11.1 | derived function |
| $DecisionSupport(x,d)$ | relation | Actor/Cluster $x$ supports Decision $d$ | §6.4 | relation |
| $AgreesWith(x,d)$ | relation | Actor/Cluster $x$ agrees with Decision $d$ | §6.4 | relation |
| $Supports_\kappa$ | $E_\kappa\times\mathbb P$ relation | Evidence support in context $\kappa$ | §12 | relation |
| $IsSupportedBy_\kappa$ | converse of $Supports_\kappa$ | Reverse Evidence-support traversal | §12 | derived relation |
| $RelatesWPToProduct(w,P,\kappa)$ | relation | Project-defined Work Product/Product relation | §6.9 | extension relation |
| $Accepted(w,C)$ | predicate | Work Product Accepted under Contract | §6.7 / §11.6 | predicate |
| $Fulfilled(C)$ | predicate | Contract fulfilment established | §6.8 / §11 | predicate |
| $ProductTargetSatisfied(C)$ | predicate | Contract Product target satisfied | §6.8 | predicate |
| $ProductStateTransition(P)$ | predicate | Applicable Product-state transition established | §6.7 | predicate |
| $BR(d^{candidate},X)$ | function | Decision Blast Radius for Decision Candidate $d^{candidate}$ evaluated against Engineering State $X$ | §9.16 | function |
| $DecisionExtent(d,t)$ | function | Actual materialized propagation of committed Decision | §9.18 | function |
| $CanAccommodate(d^{candidate},L,X')$ | predicate | Layer $L$ can accommodate Decision Candidate $d^{candidate}$ in prospective State $X'$ | §9.21 | predicate |
| $AffectedDomains(d^{candidate})$ | function/set-valued mapping | Domains affected by Decision Candidate $d^{candidate}$ | §9.22 | function |
| $\Phi_A(X)$ | partial transformation | Human input $A$ applied to Engineering State $X$ | §5.5 | function |
| $Composable(A,B,X)$ | predicate | Ordered Human inputs compose over State $X$ | §5.5 | predicate |
| $PrerequisiteSpec(C)$ | function/set-valued mapping | Contract readiness prerequisites | §11.1 | function |
| $Evaluate(p,X)$ | function | Evaluates prerequisite $p$ against Engineering State $X$ | §11.1 | function |
| $\delta_C$ | partial function | Guarded Contract lifecycle transition | §11.1 | function |
| $G_A,G_R,G_E,G_B,G_X,G_S,G_U,G_F,G_D$ | predicates | Contract lifecycle guards | §11.1 | predicates |
| $IntegrationReady(w,C_I)$ | predicate | Work Product ready for stated integration | §11.4 | predicate |
| $Contributes(w_k,w_I)$ | relation | Work Product ancestry/contribution | §11.4 | relation |
| $Confidence_H(q,t)$ | function/indicator | Hive operational Confidence for scoped problem | §17.6 | indicator |
| $Allocation(o,t)$ | function | Active Resource allocation | AX-5 / §17 | function |
| $Rate_{PP}$ | Project Profile-defined function | Resource/trajectory rating | §17 | extension function |
| $Health_{PP}$ | Project Profile-defined function | Execution/divergence health | §17 | extension function |
| $Indicator_{PP}$ | Project Profile-defined function | Confidence indicator | §17.6 | extension function |
| $Explore_{PP}$ | Project Profile-defined function | Stochastic/trajectory exploration policy | §17.6 | extension function |
| $TrafficLight_{PP}$ | Project Profile-defined function | Operator-facing Confidence projection | §17.6 | extension function |
| $Update_{PP}$ | Project Profile-defined function | Confidence temporal update | §17.6 | extension function |

The registry is the common reference for reusable named predicates, relations, and functions. New reusable formal identifiers are added here when introduced.

### 21.5 Formal-source checks

The release audit applies the following model-integrity checks.

| Check | Required condition |
|---|---|
| **Symbol uniqueness** | Each reusable mathematical symbol has one §4.4 dictionary meaning. |
| **Predicate/function signature** | Reusable predicates and functions use the signature in §21.4. |
| **Product/Proposition notation** | $P$ denotes Product, $p$ denotes Proposition, and $\mathbb P$ denotes the Proposition set. |
| **Engineering State notation** | Engineering State uses $X_t$. |
| **Projection/revision notation** | $\Pi_q(X_t)$ denotes State Projection and $\rho$ denotes revision mapping. |
| **Project Profile notation** | $PP$ identifies Project Profile semantics; $P$ remains reserved for Product. |
| **Integration readiness** | $W^{ready}_{C_I}\subseteq W_I$, with full readiness exactly when $W^{ready}_{C_I}=W_I$. |
| **Formal-source integrity** | Mathematical source renders the intended operators and contains no control-character corruption of TeX expressions. |

These checks validate representation consistency. Their engineering semantics remain defined in the referenced proposal sections.

# Part VI - References and supporting material

## 22. Language and meaning references

The applicable ADS language and meaning basis for this proposal is:

1. **ADS-00 - Governance and Bootstrap**, version 5.0.0-rc.1, for the governance provisions applicable to the Language & Meaning Core.
2. **LMC-01 - External Language Standards Profile**, version 5.0.0-rc.1.
3. **LMC-02 - Project Terminology and Meaning Control**, version 5.0.0-rc.1.
4. **LMC-03 - Information Construction and Applicability**, version 5.0.0-rc.1.
5. **LMC-04 - Language and Meaning Conformance**, version 5.0.0-rc.1.

External language, terminology, drafting, information-development, and conformity standards apply through LMC-01 and remain authoritative for their own content.

The proposal-specific profile in §4 extends this common basis with the language and meaning rules required by the formal Hive engineering model.

## 23. Formal-knowledge representation references

The proposal uses the following specifications as design references, not normative dependencies:

1. OpenMath Standard 2.0r2 and Content Dictionaries - semantic representation of mathematical objects, symbols, Commented Mathematical Properties, and Formal Mathematical Properties. https://openmath.org/standard/om20-2019-07-01/
2. TPTP Language - annotated formula roles including axiom, hypothesis, definition, assumption, lemma, theorem, corollary, conjecture, and type. https://tptp.org/UserDocs/TPTPLanguage/TPTPLanguage.shtml
3. OMDoc - document/theory-level distinction among axioms, definitions, assertions/theorems, proofs, and related mathematical statements. https://www.omdoc.org/
4. SMT-LIB 2.7 - rigorous common languages and background theories for solver interaction. https://smt-lib.org/language.shtml

The proposal adopts the distinction between expression syntax and statement role. It does not require serialization in OpenMath, TPTP, OMDoc, or SMT-LIB.

## 24. Supporting AI architecture references

The following sources are illustrative/supportive only:

- OpenAI Agents SDK, agent orchestration, manager/agents-as-tools and handoff patterns. https://openai.github.io/openai-agents-python/multi_agent/
- CrewAI Crews, role-bearing agents, tasks, processes, manager and memory concepts. https://docs.crewai.com/en/concepts/crews
- AutoGen/ConversableAgent message-based agent communication. https://microsoft.github.io/FLAML/docs/reference/autogen/agentchat/conversable_agent/
- Tree of Thoughts: Deliberate Problem Solving with Large Language Models, NeurIPS 2023. https://papers.nips.cc/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html
- Graph of Thoughts: Solving Elaborate Problems with Large Language Models, AAAI 2024. https://ojs.aaai.org/index.php/AAAI/article/view/29720

## 25. Project supporting material

The following project material informed this revision:

- `harness-hive-dialogue-recap.md` - non-normative recap used to restore the state-centric Hive architecture, bounded traversal, trade-space, trajectory, cluster, Rollback-cost, and non-actor design direction. Later accepted decisions in this proposal take precedence where the recap is older.
- `resource_consumption_recap.md` - decision recap for context/input, orchestration, polling waste, and root/sub-agent resource use.
- `session_resource_analysis.xlsx` - supporting workbook containing summary, category, phase, waste, support, agent, sub-agent, timing, session, and daily pivots.
