---
title: "Hive/Swarm Engineering Governance"
subtitle: "Formal Proposal - Draft 0.24"
date: "17 September 2026"
---

**Status.** Accepted Abstract, Part I Section 3, Language Foundation, Contract terminology/Acceptance revisions, Scale/Scaling/Magnification/Extent revisions, Check Cascade, Scope/revision/traversal restoration, Maturity/Brittleness restoration, Reshuffling/repair exploration, Cluster/divergence resource-survival revisions, Evidence Proposition algebra/feedback-locality/reversible-traceability revisions, and Candidate Delta/canonical-state computation-boundary revisions are integrated. Other unresolved formalization items remain unchanged. ASD-STE100 conformance is not claimed without designated checker or review evidence.

**Normative basis.** Approved project discussion and accepted changes through Draft 0.8, aligned with the project dialogue recap and resource-consumption analysis where those sources do not conflict with later decisions.

**Mathematics.** Mathematical expressions are represented as native editable equations in the Word build.

[[STATIC_TOC]]

# Part I - Proposal in plain terms

## 1. Abstract and intent

This proposal originates from a practical problem observed in AI-assisted engineering: a substantial part of computation can be spent coordinating agents, replaying context, polling execution, and maintaining an artificial organization around the engineering work. These problems largely originate from applying human-like organizational, reasoning, and consensus models directly to AI execution.

Orchestration frameworks and role models shaped like real organizations inherit many of the same deficiencies: locked waits, polling, administrative and coordination work, and context pollution by intermediate thinking. AI makes these losses directly visible because they immediately appear as computational and execution cost.

This proposal does not aim to build a better virtual organization or incrementally improve orchestration processes. It proposes a different coordination and synchronization model whose purpose is to reduce overall engineering cost while preserving engineering rigor.

**Hive** is a form of distributed intelligence in which orchestration is performed through coordinated multi-agent operations rather than through a persistent human-like organization. To an observer, it acts as one coherent engineering intelligence while retaining distributed specialization internally.

Engineering meaning is held in explicit shared state rather than in conversations or private agent memory. At its foundation, this state is represented as a multidimensional temporal graph that preserves project entities, evidence, relationships, and evolution without requiring the whole history to participate in every task.

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
| Communication cost risk | Repeated delegation, messaging, status polling, history replay | Repeated long reasoning and branch evaluation | Small semantic projections and small candidate deltas by default |
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
- The preferred repair path is therefore the smallest one that resolves the problem correctly. Wider reshuffling is justified only when the affected level cannot absorb the change.
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

# Part II - Language Foundation

## 4. Language Foundation

### 4.1 Intent

The Language Foundation keeps proposal terminology and technical communication consistent, concise, and reviewable without defining a new controlled language.

#### 4.1.1 Controlled English

ASD-STE100 is the primary controlled-English basis for project-authored textual content. Applicable ISO plain-language, terminology, and technical-drafting guidance supplements it.

#### 4.1.2 Normative Language

BCP 14 provides the semantics of normative keywords when the proposal intentionally states technical requirements.

Normative wording remains distinct from ordinary descriptive or explanatory text.

#### 4.1.3 Terminology

The proposal uses controlled terminology. A concept has one preferred term unless the proposal explicitly defines distinct terms for distinct meanings.

Definitions remain concise, distinct, and cross-consistent.

#### 4.1.4 Goals

The Language Foundation has four goals:

- maintain one preferred term for one concept;
- keep definitions concise and cross-consistent;
- separate Illustrations visibly from proposal content;
- use normative keywords only when technical requirement semantics are intended.

### 4.2 Norms

| Norm | Role in this proposal | Applicability |
|---|---|---|
| **ASD-STE100 Issue 9** | Core controlled-English basis | Applies to project-authored textual content. A conformance claim requires evidence from the project-designated checker or review process. |
| **ISO 24495-1** | Plain-language guidance | Supplements ASD-STE100 where reader-oriented clarity and comprehension are relevant. |
| **ISO 704** | Terminology guidance | Supports concept definition, preferred terms, terminology consistency, and definition quality. |
| **ISO/IEC Directives, Part 2** | Technical-drafting guidance | Supports organization and drafting of technical and normative content. |
| **BCP 14 – RFC 2119 and RFC 8174** | Normative keyword semantics | Applies to technical normative statements as defined in §4.3.4. |

### 4.3 Applicability

#### 4.3.1 Project-authored Text

Project-authored textual content uses the controlled-English principles defined by ASD-STE100 and the supplementary language guidance identified in §4.2.

This applies to definitions, descriptions, rationale, constraints, explanations, and other textual statements written specifically for this proposal.

Normative textual statements follow §4.3.4.

Mathematical content follows §4.3.5.

#### 4.3.2 Illustrations

Illustrations explain, demonstrate, or contextualize proposal concepts without becoming part of the formal model.

An Illustration can contain representative engineering situations, examples, example values, possible implementations, or explanatory scenarios.

Illustrations do not establish definitions, axioms, relation semantics, Project Profile defaults, Contract obligations, conformance criteria, or other normative properties.

Illustrations are visually separated from proposal content and explicitly identified as **Illustration**.

#### 4.3.3 Protected Source Text

Citations, quotations, imported requirements, legal text, contractual text, identifiers, URLs, externally defined terminology, and other protected source material remain unchanged unless transformation is explicitly required.

The presence of imported text does not automatically make its terminology, wording, or normative force part of this proposal.

Where imported material conflicts with proposal terminology, the original material remains intact and its relation to the proposal is stated separately.

#### 4.3.4 BCP 14 Scope

BCP 14 defines the normative meaning of the uppercase keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and other applicable BCP 14 terms.

BCP 14 semantics apply only where the proposal intentionally defines a technical requirement.

In the current proposal structure, normative technical statements are contained in Parts III–V unless a section explicitly states otherwise.

Outside normative use, equivalent lowercase words retain their ordinary English meaning.

Quoted or imported material retains the normative semantics of its source.

#### 4.3.5 Mathematical Content

Mathematical content expresses the formal structure of the proposal through definitions, relations, predicates, sets, functions, equations, invariants, and derived properties.

Mathematical statements use consistent notation and preserve the distinction between:

- **Definition** – introduces the meaning of a mathematical object or term;
- **Axiom** – establishes a foundational proposition accepted by the model;
- **Assumption** – states a condition under which a result applies;
- **Lemma** – establishes an intermediate result used by another formal statement;
- **Theorem or Derived Property** – follows from definitions, axioms, assumptions, or previously established results;
- **Conjecture** – states a proposition that has not yet been established.

Structural mathematical operations do not acquire engineering semantics unless those semantics are explicitly defined.

Mathematical notation in the Markdown master uses a representation that preserves clean source evolution and can be converted accurately into native mathematical notation in derived Word and PDF representations.

#### 4.3.6 Project Profile

The Project Profile supplies formal project-specific values where the common proposal deliberately leaves parameters open.

A Project Profile can define project-specific terminology, relation vocabularies, validation rules, authority structures, engineering topology, resource models, lifecycle predicates, independence requirements, construction strategies, and other parameters identified by the proposal.

Project Profile content specializes the common model. It does not modify the common foundation.

#### 4.3.7 Conformance Evaluation

Conformance Evaluation determines whether an implementation, engineering state, process configuration, or other evaluated subject satisfies:

- the common requirements of this proposal; and
- the applicable Project Profile.

Conformance Evaluation does not introduce new engineering rules. It evaluates the subject against rules already established by the proposal and the applicable Project Profile.

### 4.4 Dictionary

The dictionary is intentionally compact. A term definition may reference another defined term rather than repeating its semantics. Project-specific specializations belong in the Project Profile.

| Term | Definition |
|---|---|
| **Acceptance** | Contract-governed process that assesses Contract fulfilment and the resulting Work Product against the applicable Acceptance rules and records the resulting disposition. |
| **Check Cascade** | Cost-ordered sequence of applicable checks in which a more expensive check is entered only after all applicable cheaper checks have passed. |
| **Assignment** | Contract relation that identifies the Actor responsible for execution of that Contract. A valid Assignment establishes that Actor as the Executor in the Contract context. Assignment is part of the Contract state, not a separate Engineering Object. |
| **Actor** | Human, Hive, external organization, or other authority-capable participant. Computational micro-agents are not Actors unless a Project Profile grants that role. |
| **Agent** | Computational participant that performs a bounded operation. Agent identity does not create semantic authority. |
| **Baseline** | Configuration Management reference state created only when the applicable Configuration Management process defines it. |
| **Binding** | Scoped and time-qualified prescriptive force of an obligatory Decision. Binding applies to Decisions, not Work Products or Exchange Items. |
| **Cluster** | Set of sufficiently independent contributions within a Swarm that support one Decision for one task/problem statement. A Decision can then preserve or direct a trajectory. |
| **Conformance Evaluation** | Formal check of implementation/state against this model plus the applicable Project Profile. |
| **Contract** | Durable governed record that defines a Product target, required Work Product, Issuer, Assignment, Resource Envelope, execution topology, Acceptance rules, enforcement, and the information required to preserve execution and fulfilment history. |
| **Decision** | Rationale-bearing Proposition that preserves or directs a possible course of exploration or behavior. A Decision is not an Engineering Object. |
| **Delusive Traceability** | Apparently complete traceability created through semantically invalid, fabricated, or unjustified relations. |
| **Engineering Layer** | Project-defined bounded Scale and Magnification context within which engineering elements can be reasoned about as one coherent Product view. |
| **Engineering Object** | Materialized project entity with tool, repository, physical, or document identity. It can carry or materialize one or more Propositions. |
| **Evidence** | Recorded information used by a defined validator or argument to support a Proposition. Evidence is scope- and role-specific. |
| **Exchange Item** | Boundary-relative information object used to communicate Propositions, Product interfaces, results, feedback, or other materialized information. |
| **Executor** | Actor responsible for fulfilment of an assigned Contract, including delivery of the required Work Product or explicit reporting that fulfilment cannot be completed. A Human can be an Executor when assigned responsibility for a Contract result. |
| **Exploration** | Bounded computational attempt to extend, test, compare, or refine the current Solution Space. |
| **Extent** | Measurable reach of a Decision effect within its current Scale and Magnification. Significant Extent usually has severe economic effect and can question the rationality of the originating Decision. |
| **Extremum Exploration** | Exploration intended to discover a different local extremum or challenge whether a materially better region exists outside the current search neighborhood. |
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
| **Magnification** | Resolution at which an engineering subject is examined or represented. Magnification defines the admissible detail for reasoning at an Engineering Layer; it is a view of a Scale, not the Scale itself. |
| **Micro-agent** | Short-lived, specialized, low-Resource-Cost Agent used for one narrow exploration or validation operation. |
| **Obligation** | Responsibility of an Executor for the complete result of an assigned Contract. The Executor delivers the required result or explicitly reports inability to fulfil the Contract to the authoritative party or parties. Obligation is Contract semantics, not necessarily a separate stored object. |
| **Outlier** | Discovered outcome or trajectory with low current cluster support. It remains recorded even when active allocation is zero. |
| **Overthinking** | Reasoning expenditure whose expected information or decision value is lower than its Resource Cost, or reasoning applied to a result that deterministic state/algebra can establish directly. |
| **Product** | Coherent engineered subject whose state is created, evolved, verified, accepted, produced, or delivered. |
| **Product API** | Exchange Item that materializes a Product-interface Decision in a project-appropriate representation. |
| **Product Delivery** | Contract fulfilment in which accepted Work Products advance the Product to the Contract target state. |
| **Project Profile** | Formal project input that defines open parameters such as relation vocabulary, scale topology, Work Product schemas, validators, authority, resource models, lifecycle predicates, and validation independence. |
| **Proposition** | Core addressable semantic element of the solution model. It is not an Engineering Object by default. It can later be materialized, carried, or realized by Engineering Objects. |
| **Relation** | Typed semantic or structural association between addressable elements, qualified by scope, revision, time, and Project Profile semantics. |
| **Reshuffling** | Primarily vertical Decision rework caused when an Engineering Layer committed downstream constraints without sufficient exploration to support delivery through affected downstream layers. A downstream finding becomes Reshuffling when it cannot be absorbed locally and requires Decision change at an adjacent or higher Engineering Layer. |
| **Resource Cost** | Multi-dimensional consumption caused by an operation, exploration, Contract, trajectory, or change. |
| **Resource Envelope** | Declared availability/limits for relevant resource dimensions such as context, model calls, compute, wall time, money, human effort, energy, equipment, and external capacity. It is not a universal scalar. |
| **Scale** | Project-relative position of an engineering subject or representation in an ordered topology of size, decomposition, or abstraction. Scale supports comparison of elements by relative level and approximate order of magnitude; it does not require one universal numeric scale. |
| **Scaling** | Project-defined transition between different Scales. Scaling prevents direct semantic or operational linkage between elements that belong to incompatible engineering orders and requires information to be reconciled and materialized at the receiving Scale. |
| **Solution Space** | Addressable set of currently known candidate states, constraints, outcomes, and their relations for a scoped problem. |
| **Swarm** | Population of specialized computational participants assigned by the Hive to one bounded task. Swarm contributions can form Clusters supporting Decisions. |
| **Team API** | Project-defined set of Work Products and communications used to coordinate Product evolution among parties. |
| **Trade Space** | Project-visible candidate region used to compare alternatives for one problem under current constraints, evidence, and authority. |
| **Trajectory** | Temporally ordered path of exploration outcomes and Decisions through a Trade Space. |
| **UNKNOWN** | Required information whose value, validity, applicability, or result has not been established. |
| **Waste** | Resource consumption that creates neither required governance/validation effect nor reusable progress, evidence, knowledge, or Product value for the active objective. |
| **Work Product** | Complete required Contract result prepared under a defined schema and Acceptance rule. A Work Product can be an input to another Contract. |

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

This proposal separates the role of a mathematical expression from its expression syntax.

OpenMath is useful for representing mathematical objects, symbols, Content Dictionaries, and Formal Mathematical Properties. It does not by itself provide the document-level distinction needed here between an axiom, theorem, assumption, and conjecture. OMDoc and TPTP explicitly represent those statement roles. The proposal adopts that role separation without requiring any one serialization format.

**Definition.** Introduces a term, symbol, relation, function, or predicate meaning Can be used after introduction.

**Axiom.** Foundation statement accepted by this proposal and not derived from another proposal statement Basis for derived properties and conformance.

**Assumption.** Explicit scoped condition supplied by a problem or Project Profile Valid only in its declared scope; must not become a universal rule.

**Lemma.** Derived intermediate result Used to simplify a later proof.

**Theorem / Derived Property.** Result derived from Definitions, Axioms, and declared Assumptions Can be used where its proof conditions hold.

**Conjecture.** Proposed relation or property not yet established Cannot support conformance or commitment.

An **Invariant** is a property that must hold in every valid state of a specified scope. Its logical source can be an Axiom, Theorem, Contract rule, or Project Profile rule; `Invariant` is therefore a state-property class, not a separate proof role.

A formal statement record has the conceptual form:

$$S=(id,role,intent,statement,scope,dependencies,evidence,validation).$$

### 5.3 Core set, relation, and graph algebra

Let $U$ be the addressable semantic universe for a project revision. Let $P\subseteq U$ be Propositions and $O\subseteq U$ be Engineering Objects. The two sets are not interchangeable.

A materialization relation can connect them:

$$Materializes\subseteq P\times O.$$

A Proposition can have several materializations and one Engineering Object can carry several Propositions.

A typed binary relation $r$ has source and target sets:

$$r\subseteq S_r\times T_r.$$

Its converse is:

$$r^{\smile}=\{(y,x)\mid(x,y)\in r\}.$$

The converse is a mathematical view of the same relation. It does not create a second independent semantic fact.

The common structural algebra includes domain, range, image, inverse image, restriction, converse, set union/intersection/difference, and relational composition. Structural composition is:

$$r\circ s=\{(x,z)\mid\exists y:(x,y)\in s\land(y,z)\in r\}.$$

Structural composition creates a path relation. It does not create semantic entailment unless the Project Profile defines a sound semantic composition rule for the relation family.

A graph $G=(V,E)$ is a projection of addressable elements and relation instances for navigation and analysis. Graph reachability is therefore weaker than semantic justification:

$$Reachable_G(a,b)\not\Rightarrow Justifies(a,b).$$

A relation validator has the generic form:

$$V_r(e,\kappa)\in\{\top,\bot,?\},$$

where $\kappa$ contains the applicable scope, revision, time, Project Profile, authority, and other relation-specific context.

### 5.4 Computational algebra

The Hive separates **canonical engineering state** from the temporary computation used to propose changes to that state.

Let:

$$S_t$$

be the canonical engineering state at revision/time $t$.

For a bounded engineering problem $q$, computation starts from a projection of that state:

$$\Pi_q(S_t)\subseteq S_t.$$

The projection contains the semantic state required for the problem under the applicable Scope, Scale, Magnification, Contract, authority, revision, and Project Profile rules.

A projection is a computational view. It is not an independent canonical engineering state.

Therefore:

$$x\in\Pi_q(S_t)\Rightarrow x\in S_t$$

for canonical elements selected into the projection, while temporary structures introduced during computation do not thereby become members of $S_t$.

The computational sequence is:

$$S_t\rightarrow\Pi_q(S_t)\rightarrow DeterministicOps\rightarrow BoundedSemanticComputation\rightarrow\Delta_q\rightarrow Admission\rightarrow S_{t+1}.$$

where $\Delta_q$ is a Candidate Delta.

The sequence establishes a strict boundary:

$$Computation\neq CanonicalMutation.$$

A participant can compute, infer, explore, simulate, compare, or propose a change without being able to apply that change directly to canonical engineering state.

#### 5.4.1 Deterministic operations before semantic computation

The Hive applies deterministic operations before assigning unresolved work to semantic reasoning.

For projection:

$$\Pi_q(S_t)$$

the deterministic stage can establish properties such as:

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
- declared Scale and Magnification compatibility;
- other mechanically decidable Project Profile rules.

Let:

$$K_q=DeterministicOps(\Pi_q(S_t))$$

be the mechanically established state available to the computation.

Only properties that remain unresolved after applicable deterministic operations enter semantic computation.

Therefore:

$$DeterministicallyResolvable(x)\Rightarrow\neg RequireSemanticReasoning(x)$$

unless the Project Profile explicitly requires an additional semantic assessment for that property.

The purpose is not to prohibit semantic reasoning. The purpose is to prevent expensive or probabilistic reasoning from being used to rediscover facts that the explicit engineering state and algebra already establish.

#### 5.4.2 Bounded semantic computation

Semantic computation operates on the bounded problem projection and the deterministic results established from it.

Conceptually:

$$C_q=SemanticCompute(\Pi_q(S_t),K_q,R_q)$$

where $R_q$ is the applicable Resource Envelope for the computation.

$C_q$ is temporary computational state.

It can contain:

- intermediate hypotheses;
- reasoning branches;
- model outputs;
- simulation results not yet admitted;
- candidate relations;
- candidate Decisions;
- candidate Evidence;
- candidate UNKNOWNs or Gaps;
- rejected alternatives;
- other temporary structures required by the computation.

Temporary computational state is not canonical merely because it exists.

Therefore:

$$x\in C_q\not\Rightarrow x\in S_t$$

and:

$$Generated(x)\not\Rightarrow Canonical(x).$$

Only the engineering information selected for preservation or proposed canonical change crosses the computation boundary.

This prevents intermediate reasoning from becoming engineering state by accident.

#### 5.4.3 Computational participants

Agents, micro-agents, humans, simulations, solvers, tools, and other computational participants can contribute to bounded semantic computation.

Persistent participant identity is not required for computation.

The engineering state therefore does not depend on the continued existence of the participant that produced a candidate.

What must survive where applicable is provenance sufficient to identify the origin and applicable context of the proposed result.

A computational participant does not obtain canonical-state authority merely by producing an output.

Therefore:

$$Produces(a,\Delta_q)\not\Rightarrow CanApply(a,\Delta_q)$$

and:

$$Produces(a,p)\not\Rightarrow Canonical(p).$$

The ability to generate a Candidate Delta and the authority to admit its effects are separate properties.

This rule applies equally to highly capable models, deterministic tools, humans, and other contributors.

#### 5.4.4 Candidate Delta

A Candidate Delta is a proposed change to canonical engineering state.

It is not a successor state and it is not engineering truth.

For problem $q$:

$$\Delta_q=(P_{cand},R_{cand},D_{cand},E_{cand},U_{cand},G_{cand},F_{cand},Req_{cand})$$

where the components can contain proposed:

- Propositions;
- Relations;
- Decisions;
- Evidence;
- UNKNOWNs;
- Gaps;
- Future Actions;
- Requests or Work Product needs.

The components are typed views within the common ontology.

For example:

$$D_{cand}\subseteq P_{cand}$$

and:

$$E_{cand}\subseteq P_{cand}$$

where those candidate Propositions carry Decision and Evidence roles respectively.

The tuple does not define Decisions and Evidence as ontologically separate from Propositions.

A Candidate Delta can also propose revision, deactivation, supersession, relation change, materialization, or another state operation permitted by the common model and Project Profile.

The Candidate Delta expresses:

> **This is the change proposed by the computation.**

It does not express:

> **This change is already part of the Product state.**

Therefore:

$$Candidate(\Delta_q)\not\Rightarrow Admitted(\Delta_q)$$

and:

$$Candidate(p)\not\Rightarrow ActiveProposition(p).$$

#### 5.4.5 Candidate Delta base state

A Candidate Delta is evaluated relative to the canonical state from which its problem projection was derived.

Let:

$$Base(\Delta_q)=S_t$$

identify that base state or its revision-qualified identity.

The meaning of the Candidate Delta is therefore not independent from its base state.

If canonical engineering state changes materially before the Candidate Delta is applied, prior validation cannot automatically be reused.

For:

$$S_t\neq S_{t'}$$

the model does not infer:

$$Admissible(\Delta_q,S_t)\Rightarrow Admissible(\Delta_q,S_{t'}).$$

Instead, the Hive determines whether the changed state affects the Candidate Delta.

When the applicable state has changed:

$$AffectedBy(\Delta_q,S_t\rightarrow S_{t'})\Rightarrow Revalidate(\Delta_q,S_{t'}).$$

A Candidate Delta can therefore become stale without becoming historically invalid.

Its original computation and provenance remain addressable, while its applicability to the new canonical state must be reassessed.

#### 5.4.6 Candidate Delta admission

A Candidate Delta reaches canonical engineering state only through explicit admission.

Let:

$$ApplicableValidators(\Delta_q,S_t,\kappa)$$

be the validators required for the proposed change in engineering context $\kappa$.

Admission requires every applicable blocking validator to permit the change.

Conceptually:

$$Admissible(\Delta_q,S_t,\kappa)$$

holds only when the Candidate Delta satisfies the applicable validation rules.

These can include:

- structural validity;
- relation typing;
- semantic validity;
- Scope and revision validity;
- Scale and Magnification validity;
- Evidence rules;
- authority validity;
- Contract admissibility;
- Work Product information-boundary rules;
- applicable Check Cascade results;
- Project Profile conformance;
- other domain-specific validators required by the affected state.

This does not require every Candidate Delta to satisfy every validator defined by the project. Only applicable validators participate.

Formally:

$$Admissible(\Delta_q,S_t,\kappa)\Rightarrow\forall v\in ApplicableValidators(\Delta_q,S_t,\kappa):Pass(v).$$

where the Project Profile determines whether an unresolved validator blocks admission, creates an explicit UNKNOWN or Gap, requires escalation, or permits another defined disposition.

Truthful incompleteness remains applicable during admission.

The Hive does not fabricate a passing result merely to make a Candidate Delta admissible.

#### 5.4.7 Controlled application

Only an admitted Candidate Delta can apply its proposed engineering changes to canonical state.

For an admitted delta:

$$Admissible(\Delta_q,S_t,\kappa)\Rightarrow S_{t+1}=Apply(S_t,\Delta_q,\kappa).$$

The application operation itself is controlled.

It preserves the applicable:

- identity rules;
- revision history;
- temporal history;
- Scope;
- provenance;
- relation semantics;
- Contract state;
- authority boundaries;
- Scale and Magnification rules;
- information boundaries.

Application creates a successor state.

It does not rewrite the previous canonical state.

Therefore:

$$Apply(S_t,\Delta_q)=S_{t+1}$$

does not imply destructive historical replacement of $S_t$.

Instead:

$$S_t\rightarrow S_{t+1}$$

is a revision-qualified state transition and $S_t$ remains addressable according to the historical-state rules.

#### 5.4.8 Rejected, deferred, and partially admissible candidates

Failure to admit the proposed engineering change does not require deletion of the Candidate Delta.

A Candidate Delta can be:

- admitted;
- rejected;
- deferred;
- returned for correction;
- decomposed into independently admissible parts where the applicable semantics permit;
- retained as an exploratory alternative;
- converted into a Gap, UNKNOWN, Future Action, or another applicable state element.

The exact disposition is Project Profile and context dependent.

The critical invariant is:

$$\neg Admissible(\Delta_q)\not\Rightarrow ApplyProposedChange(\Delta_q)$$

while preservation of useful discovery remains possible:

$$Discovered(\Delta_q)\Rightarrow PreserveApplicableKnowledge(\Delta_q).$$

A rejected Candidate Delta can therefore remain valuable for post-mortem analysis, alternate trajectories, later revisions, or repeated engineering exploration without contaminating active Product state.

#### 5.4.9 Candidate Delta is not a Work Product

A Candidate Delta and a Work Product have different roles.

A Candidate Delta is a proposal to evolve canonical engineering state.

A Work Product is a complete Contract-required result governed by its schema and Acceptance rules.

A computation can propose a Work Product, propose changes to a Work Product, or identify the need for one through a Candidate Delta.

This does not make the Candidate Delta itself the required Work Product.

Therefore:

$$CandidateDelta\neq WorkProduct$$

in general.

Likewise, admission of a Candidate Delta does not by itself mean that a Contract Work Product has been Accepted.

Canonical-state admission and Contract Acceptance remain separate operations.

### 5.5 Human ingress and choice set

Human interaction is a known set before delegated-autonomy rules are applied:

$$H=\{HAI,HVC,HPC,HWP\}.$$

- `HAI` = HUMAN_ARBITRARY_INPUT.
- `HVC` = HUMAN_VOLUNTARY_CHOICE.
- `HPC` = HUMAN_PRESCRIPTIVE_CHOICE.
- `HWP` = HUMAN_WORK_PRODUCT.

`HAI` can arrive asynchronously and can project a successor engineering universe. It can be controversial or outside the current Hive recommendation. It does not erase prior state.

`HVC` is optional while autonomous continuation remains possible.

`HPC` is required only for an obligatory Decision when no Hive-committable choice remains or when that Decision authority is explicitly human.

`HWP` is a Work Product supplied by a Human or human organization. It is assessed using the same applicable Work Product, information-boundary, traceability, and validation rules as other Work Products.

Binding is restricted to obligatory Decisions:

$$Binding\subseteq Decision\times Scope\times Time.$$

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

**Intent.** Prevent information visibility from becoming cross-scale prescriptive authority or inherited evidence closure.

**Statement.** Direct semantic relations and Decisions operate within the applicable scale rule. Cross-scale effects require an explicit permitted bridge, materialized Exchange Item, or other Project Profile mechanism followed by local interpretation.

$$DirectSemanticUse(x,y,\kappa)\Rightarrow ScaleValid(x,y,\kappa).$$

$$CrossScaleEffect\Rightarrow ExplicitBridge\land LocalInterpretation.$$

**Boundary.** AX-3 does not fix universal engineering levels. Magnification frames and allowed bridges are Project Profile parameters.

**Validation.** Remove AX-3 and a local Decision or evidence item can silently become authoritative over arbitrary remote layers, producing the authority/evidence sphere that the model is designed to prevent.

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

$$Allocation(o,t)=Rate(o,Progress,Novelty,Evidence,Independence,RepairCost,DeliveryValue,ResourceEnvelope).$$

$$Allocation(o,t)=0\not\Rightarrow Delete(o).$$

The Hive seeks a satisfactory Contract/Product path under the declared Resource Envelope. It does not promise a global optimum unless a Contract explicitly requires and defines such an objective. Outliers can remain in the semi-latent Solution Space even when their active allocation is zero.

The Hive MUST NOT spend production effort on invention until known means are exhausted and the applicable invention allocation is approved.

**Boundary.** AX-5 does not limit the number of discovered outcomes and does not treat majority support as truth. It limits only active expenditure.

**Validation.** Remove AX-5 and the model can either discard low-support discoveries or consume unlimited resources on persistent trajectories. Both conflict with the intended resource and post-mortem behavior.

# Part IV - Formal Proposal

## 6. Operational state, data structure, and roles

### 6.1 Canonical semantic state

The formal runtime is state-centric. Canonical engineering state contains semantic identities, relations, accepted state transitions, applicable Contracts and obligations, evidence records, Gaps, UNKNOWNs, and Project Profile context. Repositories, authoring tools, databases, model stores, and physical records are projections of that state, not the state itself.

For an addressable universe $U_{b,t}$ identified by branch/universe $b$ and time $t$, a repository or tool projection is:

$$\pi_k:U_{b,t}\rightarrow R_k.$$

Different projections can represent the same Proposition or Engineering Object. File-system containment does not imply semantic containment.

Canonical engineering state is the authoritative engineering state used as the basis for subsequent projections, Decisions, Contracts, validation, and Product evolution.

Temporary computation is external to that authority boundary until its proposed effects are admitted.

Conceptually:

$$CanonicalState\;|\;Computation$$

with only controlled operations crossing the boundary:

$$CanonicalState\rightarrow Projection\rightarrow Computation$$

and:

$$Computation\rightarrow CandidateDelta\rightarrow Admission\rightarrow CanonicalState.$$

There is no direct operation:

$$SemanticComputation\rightarrow CanonicalMutation$$

without Candidate Delta admission.

This separation makes the model state-centric rather than agent-centric.

A Swarm can disappear after producing its result without losing the engineering state required for later work. A different participant can continue from the canonical state without replaying the original private reasoning process.

### 6.2 Proposition and Engineering Object

A Proposition is the core semantic element. It can represent a claim, need, candidate structure, Decision, interface intent, expected behavior, constraint, question, request, gap statement, or another addressable semantic unit.

An Engineering Object is a materialized project entity such as a requirement record, document, model element, source file, binary, simulation result, test artifact, physical part, assembly, configuration record, or other tool/physical item.

Materialization is many-to-many:

$$Materializes\subseteq P\times O.$$

A Decision is a Proposition role and is not an Engineering Object. A Decision can later materialize into an ADR, plan, change request, Product definition, Exchange Item, or another Engineering Object.

Decision, Evidence, Question, Request, constraint, expected behavior, interface intent, Gap statement, and other semantic roles specialize Proposition semantics without creating separate semantic universes.

For an engineering context $\kappa$, let:

$$D_{\kappa}=\{p\in P\mid DecisionRole(p,\kappa)\}$$

and:

$$E_{\kappa}=\{p\in P\mid EvidenceRole(p,\kappa)\}.$$

Therefore:

$$D_{\kappa}\subseteq P$$

and:

$$E_{\kappa}\subseteq P.$$

A Decision and an Evidence item are therefore Propositions playing different semantic roles.

Evidence inherits the common Proposition algebra, including semantic identity, Scope, revision and temporal qualification, provenance, materialization, typed relations, converse relations, image and inverse-image operations, bounded forward and reverse traversal, and historical addressability.

Evidence extends the common Proposition algebra with Evidence-specific relations and validators required to establish relevance, support, sufficiency, independence, representativeness, provenance, and local evidential closure.

Membership in the common Proposition algebra does not imply predicate substitutability. An operation defined for Evidence is valid only when the participating Proposition has the required Evidence role and the applicable relation validators succeed.

### 6.3 Communication Proposition roles

The common minimum communication roles are:

$$CommRole\supseteq\{Question,Request,Clarification\}.$$

Projects can add roles through the Project Profile. Exchange Item is not another conversational role; it is a boundary-relative materialized information role that carries applicable Propositions.

### 6.4 Decision

A Decision is a rationale-bearing Proposition that preserves or directs a possible course of Hive exploration or behavior. Agreement is a relation to a Decision, not the definition of a Decision.

$$Supports(actorOrCluster,d)$$

$$Agreement(S,d).$$

A Decision can be contested, supported by an outlier, committed, deactivated, deprecated, or superseded. Suggested lifecycle labels are project-configurable; the common requirement is that deactivation does not delete historical knowledge.

### 6.5 Exchange Item

An Exchange Item is a boundary-relative materialized information object. Its representation is project-specific. It can be a textual document, model file, protocol schema, CAN matrix, Revit artifact, drawing, source code, binary, simulation result, physical sample record, or another information form appropriate to the Product.

A Product API is a design Decision materialized as one or more Exchange Items:

$$DesignDecision(d_{api})\land Materializes(d_{api},e_{api})\land IsExchangeItem(e_{api},b).$$

Exchange Item atomicity is boundary-relative. Feedback can target an internal locator of the Exchange Item when the representation supports it.

### 6.6 Work Product

A Work Product is a complete obligatory Contract result. It has its own schema, permitted information boundary, applicable checks under Section 8.5, required validation, supplementary information, and Acceptance rule. A lower-level Work Product does not automatically become content of an upper Work Product merely because it exists.

$$IsWorkProduct(w,C)\Rightarrow ConformsToSchema(w,C).$$

A Work Product can become an input to another Contract while remaining the complete result of its source Contract.

### 6.7 Product

A Product is the coherent engineered subject at a defined boundary. Product structure and Work Product structure are different. Contract decomposition can split execution without fragmenting the final Product view delivered by the layer.

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

$$Supports\Longleftrightarrow IsSupportedBy$$

where:

$$IsSupportedBy=Supports^{\smile}.$$

Therefore:

$$Supports(e,p)\iff IsSupportedBy(p,e).$$

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

Every semantic use is qualified by the context required by its relation family. Typical qualifiers are scope, revision, branch/universe, time, Contract, Engineering Layer, Project Profile revision, and authority domain.

For an addressable engineering universe $U_{b,t}$, a Scope is an anchored subset:

$$\sigma=(a,S_\sigma),\qquad S_\sigma\subseteq U_{b,t}$$

where $a$ identifies the Scope anchor or governing context.

Scopes in the same engineering universe support ordinary set operations:

$$S_{\sigma_1}\cap S_{\sigma_2},\quad S_{\sigma_1}\cup S_{\sigma_2},\quad S_{\sigma_1}\setminus S_{\sigma_2},\quad S_{\sigma_1}\subseteq S_{\sigma_2}.$$

A Scope does not need to be graph-connected.

Atomic changes create successor addressable universes while preserving predecessors:

$$U_{b,t}\rightarrow U_{b',t'}.$$

Comparison across different engineering universes uses an explicit revision mapping:

$$\Pi_{(b,t)\rightarrow(b',t')}:U_{b,t}\rightharpoonup U_{b',t'}.$$

The mapping is partial because an element can be introduced, removed from active continuation, split, merged, or otherwise lack a one-to-one successor.

Name equality, repository path equality, or apparent structural similarity does not substitute for revision mapping.

Later discovery can add previously unknown structure without rewriting prior state:

$$Trace_{t_0}\subseteq Trace_{t_1}.$$

where the later trace can contain additional structure while the historical universe remains addressable.

#### 8.1.1 Revision-aware relation instances

A relation instance is qualified by the revisions of its endpoints and by the context in which it applies.

A conceptual relation record is:

$$e=(p^i,r,q^j,\sigma,I,\kappa)$$

where:

- $p^i$ is the source Proposition revision;
- $r$ is the relation family;
- $q^j$ is the target Proposition revision;
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

Propagation beyond the stated Scope follows the applicable relation, Scaling, Decision, and Contract rules.

### 8.2 Identity and provenance

Semantic identity and material identity are separate. A Proposition can have several materializations and an Engineering Object can carry several Proposition revisions. Provenance records reconnect tool/repository projections and preserve the source of candidate deltas, evidence, human inputs, and external effects.

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

The same reliability dimensions apply to Candidate Delta admission.

A Candidate Delta does not become admissible merely because one validation dimension succeeds.

For example:

$$StructuralValid(\Delta)\not\Rightarrow SemanticValid(\Delta)$$

$$SemanticValid(\Delta)\not\Rightarrow AuthorityValid(\Delta)$$

$$EvidenceSufficient(\Delta)\not\Rightarrow ContractAdmissible(\Delta)$$

and:

$$GeneratedByTrustedParticipant(\Delta)\not\Rightarrow Admissible(\Delta).$$

Admission is therefore conjunctive over the validators applicable to the proposed effect, rather than based on producer identity or one global confidence value.

This section does not define model-confidence or calibration semantics. Those remain separate from the computation-boundary rules.

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
- domain-specific review templates;- bounded consistency criteria.

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

## 9. Scale, Scaling, Magnification, and Extent

Engineering elements differ both in their position within Product decomposition or abstraction and in the resolution used to reason about them.

The proposal separates **Scale**, **Magnification**, and **Extent**, and uses **Scaling** to govern movement of information between different engineering orders.

### 9.1 Scale

Scale identifies the relative engineering order of a subject or representation within the Project Profile.

A project can distinguish, for example, a Product, subsystem, component, subcomponent, implementation element, or another project-specific progression. The proposal does not prescribe one universal hierarchy.

Scale is comparative. Elements can occupy the same approximate engineering order, or one can belong to a broader or finer order than another.

A relation that is meaningful at one Scale does not automatically remain meaningful at another Scale.

The existence of a graph path does not authorize an engineering operation that bypasses intermediate engineering orders.

Direct linkage across incompatible Scales is not permitted merely because both elements are available in the same Solution Space.

### 9.2 Magnification and comparison

Magnification identifies the resolution at which an engineering subject is examined.

The Project Profile defines a set of admissible Magnification bands:

$$\mathcal{M}_P$$

and assigns an applicable Magnification to an engineering element:

$$\mu(x)\in\mathcal{M}_P$$

The Project Profile defines the comparison relation between Magnification bands.

For two engineering elements $x$ and $y$:

$$SameMagnification(x,y)\iff\mu(x)=\mu(y)$$

$$FinerThan(x,y)\iff\mu(x)>_M\mu(y)$$

$$CoarserThan(x,y)\iff\mu(x)<_M\mu(y)$$

where $>_M$ and $<_M$ are project-defined Magnification relations.

These relations express engineering resolution. They do not necessarily represent physical size, numerical magnitude, organizational hierarchy, or Contract depth.

Magnification comparison therefore provides at least:

- same engineering resolution;
- finer engineering resolution;
- coarser engineering resolution.

A Project Profile can define a partial order when engineering domains do not admit one universal linear ordering.

Scale answers:

> **At what engineering order does this element belong?**

Magnification answers:

> **At what resolution is this element being examined?**

An element can remain at the same Scale while its Magnification changes for investigation.

Increased Magnification does not transfer authority from the element's local engineering context to another Scale.

### 9.3 Direct-link restriction

A Hive operation does not directly operate, bind, constrain, integrate, or establish a semantic relation between elements whose Scale or Magnification is incompatible for that operation.

For a direct engineering relation $r$:

$$Direct_r(x,y)\Rightarrow ScaleCompatible_r(x,y)\land MagnificationCompatible_r(x,y)$$

Compatibility is relation-specific and is defined by the Project Profile.

When two elements belong to incompatible engineering orders, the proposal does not create a direct semantic edge between them. Their interaction uses Scaling.

This prevents a higher-level Product context from directly operating implementation details several engineering orders below it.

It also prevents detailed implementation information from acquiring direct authority over broader Product contexts.

Examples of prohibited shortcuts include:

- Product-level reasoning directly operating a Hall-effect sensor implementation inside an ABS component;
- UX research directly constraining application source code;
- customer-level intent directly binding implementation artifacts without the intermediate engineering interpretation required by the project.

The restriction applies even when all involved elements are visible to the same Hive.

Visibility does not imply direct bindability.

### 9.4 Scaling

Scaling transfers relevant information between different engineering orders without creating a direct semantic relation between the original source and destination elements.

A Scaling transition contains three conceptual activities:

1. identify information that is relevant beyond the originating Scale;
2. materialize that information for the applicable boundary;
3. interpret it locally at the receiving Scale.

The receiving Scale establishes its own local engineering meaning from the received information.

Scaling therefore does not mean automatic inheritance of:

- Decisions;
- authority;
- evidence closure;
- implementation detail;
- semantic relations.

#### 9.4.1 Downward Decision propagation

A Decision at one Scale does not directly become a Decision at another Scale.

The propagation pattern is:

$$Decision_i\rightarrow ExchangeItem_{i\rightarrow j}\rightarrow Decision_j$$

The Exchange Item materializes the information required by the receiving Scale.

The receiving context interprets that information and establishes its own Decision where a Decision is required.

The original Decision remains associated with its originating engineering context. It does not become invisible authority over lower Scales.

#### 9.4.2 Upward evidence and feedback propagation

Evidence follows the same Scale-locality principle as Decisions.

Evidence can directly participate in reasoning within the Engineering Layer in which its evidential relation is valid.

For Evidence $e_j$ and Decision $d_j$ in Engineering Layer $L_j$:

$$e_j\in E_j$$

$$d_j\in D_j$$

a valid local support relation can be:

$$Supports_j(e_j,d_j).$$

Its converse is:

$$IsSupportedBy_j(d_j,e_j)$$

and therefore:

$$Supports_j(e_j,d_j)\iff IsSupportedBy_j(d_j,e_j).$$

These are two traversal views of one canonical relation.

No Exchange Item is required merely to relate Evidence and a Decision that belong to the same compatible local engineering context.

Evidence locality changes at an Engineering Layer boundary.

Evidence found at a finer Scale does not directly establish a Decision or evidential closure at a broader Scale.

The established upward feedback pattern is:

$$Evidence_j\rightarrow FeedbackExchangeItem_{j\rightarrow i}\rightarrow Decision_i.$$

The first transition means that the originating Engineering Layer uses its local Evidence to determine what information must be materialized as feedback for the receiving boundary.

It does not mean that the complete Evidence Proposition, its complete materialization, or the complete local reasoning context is redistributed to the receiving Engineering Layer.

The Feedback Exchange Item carries the information required for the receiving Scale to assess the condition.

The receiving Scale interprets the Feedback Exchange Item in its own engineering context and determines whether its local Decision or Solution Space must change.

Where evidential closure is required at the receiving Scale, that Scale establishes or records Evidence appropriate to its own context.

Therefore:

$$Evidence_j\not\Rightarrow EvidenceClosure_i$$

and:

$$PotentiallyRelevant(Evidence_j,L_i)\not\Rightarrow DirectDecisionInput_i(Evidence_j).$$

Foreign Evidence can inform local reasoning. It does not automatically become local Evidence or inherit evidential closure into another Scale.

##### Feedback traceability

The relation between source Evidence and the Feedback Exchange Item remains traceable.

Let:

$$ProducesFeedback\subseteq E_j\times FEI_{j\rightarrow i}.$$

Then its converse is:

$$IsFeedbackFrom=ProducesFeedback^{\smile}.$$

Therefore:

$$ProducesFeedback(e_j,f_{j\rightarrow i})\iff IsFeedbackFrom(f_{j\rightarrow i},e_j).$$

This relation records provenance between the local Evidence and the resulting boundary feedback.

It does not imply that the Feedback Exchange Item reproduces the Evidence contents.

In particular:

$$IsFeedbackFrom(f,e)\not\Rightarrow Contents(e)\subseteq Contents(f).$$

The Feedback Exchange Item can preserve a reference to the originating Evidence when required for provenance or later retrieval without importing that Evidence into every receiving Decision context.

#### 9.4.3 Nearest affected Scale

Bottom-up Evidence feedback stops at the nearest affected Engineering Layer that can resolve the condition correctly.

If the receiving Engineering Layer can absorb the feedback within its local Solution Space and authority, propagation stops.

If the receiving Engineering Layer cannot resolve the condition locally, it determines the information relevant to the next boundary and produces a new Feedback Exchange Item.

A feedback chain can therefore have the form:

$$Evidence_k\rightarrow FeedbackExchangeItem_{k\rightarrow j}\rightarrow Decision_j$$

followed, only when further propagation is necessary, by:

$$Decision_j\rightarrow FeedbackExchangeItem_{j\rightarrow i}\rightarrow Decision_i.$$

The original Evidence does not acquire direct semantic reach over every Engineering Layer traversed by the resulting feedback loop.

Each boundary produces a locally relevant materialization, and each receiving Engineering Layer performs its own interpretation.

This limits unnecessary Decision rework, Work Product rework, reverification, and coordination.

### 9.5 Scaling and Decision blast

Decision blast remains local to the engineering context in which the Decision exists.

Scaling allows the **effects** of a Decision to cross a Scale boundary, but the Decision itself does not become a cross-layer authority edge.

A cross-Scale effect therefore requires:

- materialized boundary information;
- interpretation at the receiving Scale;
- local reasoning;
- a local Decision when the received information changes the local solution.

This prevents Decision Blast Radius from becoming an uncontrolled sphere in which one Decision directly affects unrelated engineering orders.

A broader Decision constrains the next relevant Scale instead of directly manipulating arbitrary implementation details several orders below it.

A finer-scale finding propagates upward only through explicit feedback and local reassessment.

When a Decision effect cannot be absorbed locally, or its Extent becomes economically significant, the affected context materializes the condition as Feedback or another applicable Exchange Item.

The receiving authoritative context reassesses the Decision before further propagation.

### 9.6 Decision Extent

Extent measures how far the effect of a Decision propagates within its local engineering context.

Extent is derived from **Decision Blast Radius** and makes the consequences of a Decision visible before they become hidden rework, refactoring, reverification, reintegration, or coordination cost.

Extent is evaluated within the current Scale and Magnification.

A significant Extent usually has a severe economic effect. Growth of Extent therefore questions whether the originating Decision remains rational under the current Product state, Resource Envelope, and available alternatives.

When Extent becomes material, the Hive does not silently continue propagation.

The affected region is exposed and the Decision is reassessed by the Actor that has authority for the affected context.

Depending on the applicable authority model, that Actor can be:

- an authorized Hive participant;
- a Human;
- another Contract-authorized Actor.

The reassessment can result in:

- confirmation of the Decision;
- clarification or narrowing of the Decision;
- revision of the Decision;
- supersession of the Decision;
- additional exploration;
- additional evidence collection;
- feedback to the adjacent Scale when the effect cannot be resolved locally.

Extent remains local to its Scale.

Increasing Extent does not give the originating Decision authority over another Scale.

### 9.7 Engineering Layer and execution sub-layer

An Engineering Layer defines a bounded Scale and Magnification context in which the project maintains one coherent Product view.

An execution sub-layer defines Contract execution topology inside that Engineering Layer.

Contract decomposition, parallel execution, verification Contracts, or an Integrator Contract do not create a new Scale merely because they introduce additional execution depth.

Execution depth and engineering Scale are independent properties.

Several Contracts can therefore operate at different execution sub-layers while remaining at the same Scale and Magnification.

### 9.8 Scale-compatible engineering operations

Engineering operations that directly combine, integrate, trace, constrain, or establish semantic closure between elements operate only on compatible Scale and Magnification unless the Project Profile explicitly defines an applicable Scaling boundary.

For example:

$$Integrate(x,y)\Rightarrow ScaleCompatible(x,y)\land MagnificationCompatible(x,y)$$

Different-Scale inputs require an explicit Scaling or other project-defined transformation before they become valid inputs to the same local engineering operation.

The transformation preserves the applicable:

- semantic rules;
- traceability;
- validation;
- evidence;
- information boundaries.

Scaling is an explicit reconciliation mechanism. It is not permission to recursively copy information across Product decomposition.

Scale compatibility and Extent answer different questions.

Scale and Magnification determine whether engineering elements can participate directly in the same engineering operation.

Extent determines how far the consequences of a Decision spread within that compatible local context.

A Decision can remain fully Scale-compatible while its Extent becomes economically unacceptable.

### 9.9 Scale and Extent rules

> **Scale locality:** an engineering element can directly operate on, constrain, integrate with, or establish semantic closure for another element only when the applicable relation permits their Scale and Magnification combination. Cross-order effects use Scaling and local interpretation.

> **Extent control:** Decision Extent is evaluated during exploration and propagation. Significant Extent triggers economic assessment and authoritative reassessment before further commitment or propagation.

These rules preserve the **no-sphere** property: Decisions create local reasoning and local effects; cross-Scale consequences pass through explicit materialization, interpretation, and renewed authority.

## 10. Decisions, trade space, exploration, and human intervention

### 10.1 Trade space

For problem $q$, the Trade Space $T(q,t)$ is the project-visible region of candidate outcomes that can currently be compared under applicable constraints, evidence, authority, and Product/Contract objectives.

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

The originating layer effectively treated its current solution as if it were sufficient for complete Product delivery in one step. Downstream engineering then discovers constraints, incompatibilities, missing Decisions, excessive Extent, or other facts that the original exploration did not expose.

These findings propagate upward through the applicable Scaling and Exchange Item mechanisms and can require the originating or intermediate layers to revise Decisions that were previously treated as stable.

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

#### 10.4.1 Repair is a search problem

A valid repair is not obtained by algebraically reversing the change that caused the problem.

For a change $\Delta$:

$$Repair(\Delta)\neq \Delta^{-1}$$

in general.

The reason is that the successor Solution Space can contain alternatives that did not exist, were not visible, or were not selected before the change.

A repair can therefore:

- restore an earlier solution;
- revise an existing Decision;
- choose another previously known alternative;
- discover a new local alternative;
- redistribute constraints;
- change an interface;
- alter another affected Decision;
- propagate feedback to an adjacent engineering context.

Repair is established by **direct exploration of the successor Solution Space**.

#### 10.4.2 Distributed repair exploration

Let:

$$A(\Delta)$$

be the engineering contexts directly affected by change $\Delta$.

Each affected context explores repair alternatives inside its own Scale, authority, evidence, and Contract boundaries.

When a candidate repair changes an Exchange Item, constraint, evidence condition, or another boundary-relevant element, the applicable adjacent context joins the exploration.

Conceptually:

$$A_0(\Delta)\rightarrow A_1(\Delta)\rightarrow \cdots$$

where additional affected contexts are discovered through materialized propagation rather than assumed from unrestricted graph reachability.

Several adjacent teams or Contract contexts can therefore explore the change in parallel.

This exploration determines:

- whether the change can be absorbed locally;
- which Decisions require rework;
- which Work Products are affected;
- whether additional Scaling is required;
- the actual Resource Cost of viable alternatives.

#### 10.4.3 Repair candidate set

At time $t$, let:

$$\mathcal{R}(\Delta,t)$$

be the set of valid repair candidates discovered so far through direct exploration.

A candidate $r$ belongs to this set only when it restores a valid engineering state under the applicable semantic, Scale, evidence, Contract, and authority rules.

Its cost is a vector:

$$RC(r)=(review,rework,reverification,coordination,schedule,money,compute,humanEffort,physicalChange,\ldots)$$

The common model does not reduce this vector to one universal scalar.

#### 10.4.4 Minimum known repair

Because repair alternatives are discovered incrementally, the Hive generally cannot claim a theoretical global minimum repair cost.

Instead, at time $t$, it can identify the non-dominated repair candidates in the explored set:

$$ParetoRepair(\Delta,t)=\{r\in\mathcal{R}(\Delta,t)\mid \nexists r'\in\mathcal{R}(\Delta,t):RC(r')\prec RC(r)\}$$

A Project Profile or Contract can select among these candidates using its applicable priorities and authority.

A claim of **minimum repair** is therefore qualified by the explored Solution Space.

The proposal does not infer:

$$ObservedRepairMinimum=GlobalRepairMinimum$$

unless the applicable search domain is demonstrably complete.

#### 10.4.5 Local absorption

If the affected Engineering Layer can repair the issue within its local Solution Space, authority, and materialized boundary commitments, the change is absorbed locally and does not become Reshuffling.

Reshuffling begins when the finding requires a Decision change at an adjacent or higher Engineering Layer.

Conceptually:

$$LocalRepair(\Delta,\kappa)\land NoMaterialBoundaryChange(\Delta,\kappa)\Rightarrow StopUpwardPropagation$$

This preserves parallel work and minimizes Decision rework at higher Scales.

If no adequate local repair is found, or every viable repair changes material boundary information, the affected context propagates the relevant feedback to the nearest adjacent context.

This is the repair counterpart of the Scale/Extent rules in Section 9.

#### 10.4.6 Repair exploration and Extent

Reshuffling is often discovered through downstream repair exploration. An apparently valid upstream Decision can reveal increasing Extent as adjacent Engineering Layers attempt to realize it.

Decision Extent helps determine where repair exploration must occur.

As exploration discovers additional affected engineering elements, the observed Extent can increase.

Therefore Extent is not necessarily known completely when the change is first proposed.

A repair investigation can reveal that an apparently local change has:

- larger Decision Blast Radius;
- additional affected Work Products;
- new reverification requirements;
- broader Product consequences;
- severe economic impact.

Such findings can invalidate the original Decision rationale and trigger its reassessment.

#### 10.4.7 Repair stopping condition

Repair exploration stops when the applicable authority has enough information to select a valid repair under the available Resource Envelope and decision criteria.

It does not require exhaustive enumeration of every theoretically possible repair.

The Hive preserves rejected and non-selected repair candidates when their rationale or evidence remains useful for later Decisions, post-mortem analysis, or future change.

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

### 11.2 Contract decomposition

A Contract can be decomposed into child Contracts when the Product target requires separable execution domains. Child Contracts provide complete results of their own scope. Those Work Products become inputs to the parent execution.

Contract decomposition does not imply Hive decomposition. The same Hive can coordinate all child Contracts while maintaining horizontal Product and Team APIs.

### 11.3 Integration and composition

Integration is project-specific. Direct integration requires compatible magnification:

$$Integrate(x,y)\Rightarrow M(x)\sim M(y).$$

The common algebra does not prescribe copying, aggregation, model merge, compilation, physical assembly, packaging, or another integration strategy. Each Work Product keeps its own schema and validation rules. Cross-scale incorporation is only allowed through a project-defined strategy that preserves information boundaries and validation.

Integration is not aggregation.

### 11.4 Integrator Contract

When partial Work Products need to become one coherent same-scale Work Product, the parent can create a separate Integrator Contract. The Integrator can receive multiple Work Products as a side effect of the parent topology while remaining vertically scoped to its own Contract obligation.

The Integrator does not gain horizontal authority over child Decisions. It builds the coherent result required by its Contract.

### 11.5 V-model verification topology

The Hive cannot both fulfill and validate the same Contract role. Production, test planning/test-suite production, integration verification, and other required verification activities are separate Contracts where the applicable engineering method requires that separation.

The Project Profile defines the required independence topology. It can require separate roles inside one Hive, separate Hive instances using the same model, separate departments, separate enterprises, different model providers, different infrastructure, or another topology.

Conformance uses a predicate rather than a universal scalar independence order:

$$SatisfiesIndependence(actual,required,profile).$$

### 11.6 Acceptance

Acceptance is the Contract-governed assessment of fulfilment and Work Product conformance. It is distinct from Assignment, Obligation, execution, release, deployment, production, and baselining.

Both Acceptance stages use the Check Cascade defined in Section 8.5. A more expensive applicable assessment does not proceed while a cheaper applicable check is failing. Independent Acceptance repeats or independently establishes the required evidence according to the Contract; independence does not convert every check into a High-profile Assessment.

Acceptance has two sequential stages with different responsibility and evidential meaning. Stage 1 establishes the Executor's own conformity claim and submission state. Stage 2 independently evaluates that claim and produces the Contract Acceptance disposition. Passing Stage 1 is therefore a prerequisite for normal Stage 2 assessment, but it is not independent Acceptance.

#### 11.6.1 Executor conformity assessment

Before submission, the Executor performs the applicable checks against the Contract and prepares the Work Product for assessment. The Executor records the conformity result, Known Gaps, identified non-conformities, relevant evidence, and any condition that prevents a complete fulfilment claim.

This stage is a self-assessment by the Executor. It establishes what the Executor claims to have fulfilled and with what evidence. It does not bind the Issuer to accept the result. When conformity cannot be established, the Executor reports that condition explicitly instead of presenting a partial or known-invalid result as conformant.

#### 11.6.2 Independent Acceptance assessment

After submission, the Issuer performs an independent assessment of Contract fulfilment and Work Product conformance, or delegates that assessment when the Contract permits delegation. The independent assessment considers the submitted Work Product, the Executor conformity record, applicable evidence, Known Gaps, and the Contract Acceptance rules. It does not treat the Executor's conformity claim as proof by itself.

This stage produces the Contract Acceptance disposition. The disposition and its rationale are recorded in Contract history. Failed Acceptance does not erase the submitted Work Product, conformity record, evidence, Contract state, or earlier Decisions; these records remain available for correction, governance, and post-mortem analysis.

Successful Acceptance establishes that the submitted result satisfies the applicable Contract Acceptance rules. It does not by itself imply release, deployment, production, baselining, or another project-specific lifecycle transition.

### 11.7 Product API and Team API

A Product API is an Exchange Item of a project-appropriate kind that materializes an interface Decision. Its representation depends on the Product nature.

A Team API is the set of Work Products and communications used by parties to evolve the Product. Hive-Human communication is native to the model. External-party communication can require a Project Profile communication Contract and can be limited to formats such as PDF, spreadsheet, email, supplier portal, or another external boundary representation.

### 11.8 Blast containment

A Decision has direct effect only inside its local Contract and bounded Hive/Team context. Other parties are affected only when an Exchange Item that they consume changes.

$$Affected(Team,d)\Leftrightarrow\exists e\in UpdatedExchangeItems(d):Consumes(Team,e).$$

If a team does not consume a changed Exchange Item, that team is outside the native blast area for that Decision.

## 12. Evidence and validation locality

### 12.1 Evidence as a Proposition role

Evidence is a Proposition used by a defined validator or engineering argument to support another Proposition in a defined engineering context.

For context $\kappa$:

$$E_{\kappa}=\{p\in P\mid EvidenceRole(p,\kappa)\}.$$

Evidence therefore shares the common Proposition algebra.

Evidence-specific semantics extend that algebra rather than replacing it.

A principal Evidence relation is:

$$Supports_{\kappa}\subseteq E_{\kappa}\times P_{\kappa}$$

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

$$p\in P_{\kappa}$$

the following implications do not generally hold:

$$Exists(e)\not\Rightarrow Relevant(e,p,\kappa)$$

$$Relevant(e,p,\kappa)\not\Rightarrow Supports(e,p,\kappa)$$

$$Supports(e,p,\kappa)\not\Rightarrow Sufficient(e,p,\kappa).$$

A test result, analysis, simulation, inspection, field observation, end-user claim, regulatory statement, human study, review result, or another recorded Proposition can therefore exist without being valid Evidence for every Proposition to which it can be structurally connected.

The Project Profile defines the applicable Evidence validators and sufficiency rules.

Evidence evaluation uses the Check Cascade where applicable.

Deterministic Evidence properties are established instrumentally before more expensive semantic assessment proceeds.

### 12.3 Direct local Evidence use

Evidence directly affects Decision making only where its support relation is valid in the local engineering context.

For local Evidence $e_i$ and Decision $d_i$:

$$Supports_i(e_i,d_i)$$

can be used directly when the applicable Scale, Magnification, Scope, revision, state, and Evidence validators permit that relation.

Reverse traceability is available through the converse:

$$IsSupportedBy_i(d_i,e_i).$$

The two expressions identify the same semantic edge.

This permits efficient bidirectional engineering questions such as which Decisions this Evidence supports and which Evidence supports this Decision, without storing two independent relations.

Evidence does not acquire authority because it supports a Decision.

Likewise, a Decision does not make every Evidence item that supports it relevant to every context affected by the Decision.

### 12.4 Evidence feedback across Engineering Layers

Evidence does not directly cross an incompatible Engineering Layer boundary as an evidential relation.

For Evidence $e_j$ at Engineering Layer $L_j$ and a broader Engineering Layer $L_i$:

$$Reachable(e_j,L_i)\not\Rightarrow DirectlyApplicable(e_j,L_i)$$

and:

$$Reachable(e_j,p_i)\not\Rightarrow Supports_i(e_j,p_i).$$

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

A Feedback Exchange Item is a specialized Exchange Item used to materialize feedback from an affected Engineering Layer toward an adjacent broader Engineering Layer.

Its purpose is to communicate the engineering condition that requires reassessment.

It is not a container for unrestricted replication of the originating context.

For Feedback Exchange Item $f_{j\rightarrow i}$:

$$Contents(f_{j\rightarrow i})\subseteq BoundaryRelevant(State_j,B_{j\rightarrow i})$$

where $B_{j\rightarrow i}$ is the applicable boundary.

The applicable Project Profile and Contract determine required feedback information, permissible supplementary information, provenance requirements, Evidence references, information-exposure restrictions, and required Work Product interaction.

The objective is sufficient engineering feedback without unnecessary propagation of local state.

The Feedback Exchange Item therefore does not automatically contain the complete originating Evidence set, all supporting observations, unrelated Evidence, local Decision rationale, complete reasoning history, irrelevant implementation detail, or all materializations of the source Evidence.

This protects foreign Decision contexts from irrelevant information accumulation while preserving traceability to the source.

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

$$e\in E$$

and:

$$p\in P$$

$$Reachable_G(e,p)\not\Rightarrow Supports(e,p).$$

Likewise:

$$Supports(e,p_1)\land r(p_1,p_2)\not\Rightarrow Supports(e,p_2)$$

unless the applicable relation calculus explicitly defines a sound semantic composition rule for that combination.

The same restriction applies when the path contains Decisions, Exchange Items, Feedback Exchange Items, Work Products, Engineering Objects, or other Propositions.

A sequence of valid graph edges does not automatically create evidential closure.

This prevents Evidence laundering, accidental Evidence inheritance, implicit Evidence composition, uncontrolled cross-Scale Evidence reach, foreign-context pollution, and authority being inferred from Evidence volume or verbosity.

### 12.9 Large-Extent Evidence and field feedback

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

## 13. Maturity, prescriptiveness, and brittleness

Maturity in this proposal is not an Acceptance state, completeness score, quality grade, or lifecycle state.

It represents **deliberate prescriptiveness** at a defined engineering context: how much of the currently feasible solution freedom a Proposition removes.

Maturity changes alter the Solution Space. They therefore also require reassessment of the affected Decision Blast Radius and Extent.

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

This rule does not mean that every Maturity change necessarily produces a large Extent.

It means that the existing Decision Blast Radius cannot be assumed to remain valid after the feasible Solution Space changes.

An increase in prescriptiveness can:

- invalidate downstream alternatives;
- narrow existing implementation choices;
- require Decision rework;
- change Exchange Items;
- trigger Work Product rework or reverification;
- propagate through subsequent Engineering Layers under the Scaling rules.The economic impact can therefore be much larger than the apparent size of the changed Proposition.

#### 13.3.1 Freezing a de-facto downstream solution

A special case occurs when an upstream Maturity change formalizes a solution that is already established de facto at the adjacent downstream Scale.

In this case the material implementation can already conform to the new upstream restriction, so the immediate Decision Blast Radius can be smaller than for a genuinely new constraint.

This does **not** make the pattern economically or architecturally desirable by itself.

The upstream change still evolves the Solution Space and requires the affected downstream state, traceability, evidence, Decisions, and Work Products to be reassessed for consistency.

The pattern can be legitimate when downstream engineering has, for a valid reason, performed engineering normally owned by an upstream context and the result is subsequently propagated upward through the applicable Scaling and authority rules.

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

### 13.8 Relationship to Extent

Extent and Brittleness answer different questions.

**Extent** asks:

> How far does the effect of this Decision reach?

**Brittleness** asks:

> How severe is the engineering and economic consequence of a relatively small or inappropriate trigger?

A Decision can have:

- large Extent without being brittle, when a broad change is expected to affect a broad region;
- small Extent but high Brittleness, when a small local change causes severe cost inside that region;
- both large Extent and high Brittleness, which is a strong signal that the Decision requires reassessment.

Maturity changes can affect both dimensions and therefore require reassessment of each rather than assuming one from the other.

## 14. UNKNOWNs, Gaps, and Future Actions

UNKNOWNs and Gaps preserve incomplete engineering knowledge explicitly.

Missing or invalid engineering information does not become complete through a plausible but unjustified relation.

### 14.1 Orphan and false-parent Gap

For required relation family $r$:

$$RequiredRelation(p,r,\kappa)\land\nexists q:Valid_r(p,q,\kappa)\Rightarrow Orphan(p,r,\kappa).$$

A false-parent Gap occurs when an asserted relation fails semantic validation:

$$Asserted_r(p,q,\kappa)\land\neg Valid_r(p,q,\kappa)\Rightarrow FalseParentGap(p,q,r,\kappa).$$

An invalid relation does not repair an Orphan.

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

A Decision does not become binding while a required owned UNKNOWN or material foreign UNKNOWN remains unresolved:

$$Bind(d,\kappa)\Rightarrow\neg OwnedUnknownRequired(d,\kappa)\land\neg MaterialForeignUnknownRequired(d,\kappa).$$

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

## 15. Recursive Y/V architectural model

The recursive Y/V model reconciles negotiable and fixed-horizon sources at every engineering magnification.

The left branch contains sources that can be negotiated within the current horizon, such as Product requests, UX findings, business choices, or lower-cost design alternatives. The right branch contains sources treated as fixed at that horizon, such as applicable law, established natural constraints, already committed high-cost manufacturing, or other non-negotiable obligations.

The center reconciles contradictions and produces a feasible region. Engineering realization then generates evidence, deficiencies, and Product feedback that can reopen the appropriate negotiable side.

The same pattern can recur at Product, system, subsystem, component, implementation, manufacturing, deployment, or another Project Profile layer.

## 16. Supporting processes over Solution Space

Configuration Management, Change Management, Problem Resolution, Quality Assurance, Risk Management, Measurement, release management, production control, and similar disciplines operate over Solution Space entries and Engineering Objects.

They are supporting processes, not universal semantic primitives. A Baseline, for example, exists only where Configuration Management establishes it. A production batch can be accepted without becoming a Baseline. Software can pass acceptance testing before deployment, while production deployment performs only project-defined sanity checks.

Supporting-process predicates remain Project Profile parameters unless a Contract or applicable external norm makes them obligatory.

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

$$Support_P(C_{d,q,t})$$

using contribution independence, evidence, provenance, and other applicable factors.

Repeated or strongly correlated contributions do not automatically increase effective support. Therefore:

$$MoreContributions(C)
ot\Rightarrow MoreEvidence(C)$$

and:

$$GreaterSupport(C)
ot\Rightarrow True(d).$$

Cluster support is used for **resource allocation and trajectory survival**.

For trajectory $\tau$:

$$Allocation(\tau,t)=Rate_P(Support,Evidence,Progress,Novelty,DeliveryValue,Divergence,ResourceCost,ResourceEnvelope).$$

The Project Profile defines the rating function and thresholds.

An active trajectory can receive increased, maintained, reduced, or zero allocation.

Zero allocation deactivates exploration but does not delete its results:

$$Allocation(\tau,t)=0
ot\Rightarrow Delete(\tau).$$

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

$$Health_P(\tau_1,\tau_2,t)$$

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
8. Cross-Scale effects require an applicable Scaling or boundary mechanism.
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

Therefore:

$$Reachable(d_i,L_j)\not\Rightarrow Binding(d_i,L_j)$$

and:

$$Reachable(e_j,L_i)\not\Rightarrow EvidenceClosure_i(e_j).$$

Likewise:

$$ReverseReachable(d_i,e_j)\not\Rightarrow Supports_i(e_j,d_i)$$

unless that local support relation is independently valid.

The model therefore supports full bidirectional traceability without creating bidirectional semantic authority.

Information can propagate through many Engineering Layers while Decisions, Evidence support, evidential closure, and authority remain local.

**Derived property:** Decisions and Evidence remain local semantic Propositions. Their engineering effects cross Scale boundaries only through explicit materialized exchanges and renewed local interpretation. Forward and reverse graph traversal preserve traceability but do not create semantic inheritance.

# Part V - Conformance and Project Profile

## 19. Conformance

Conformance is evaluated against the common proposal plus the applicable Project Profile revision.

A conformant implementation MUST:

- preserve Proposition and Engineering Object distinction;
- validate relation use before semantic justification;
- preserve unresolved required information explicitly;
- enforce scale/bridge rules;
- enforce Human ingress and Decision authority rules;
- preserve all discovered outcomes while controlling active resource allocation;
- separate Decision authority from Exchange Item communication;
- enforce Contract accountability, Assignment and Obligation semantics, Work Product schemas, information boundaries, and Acceptance rules;
- apply the Check Cascade so that a higher-cost check does not bypass a failing or missing cheaper checking capability;
- satisfy required verification independence topology;
- preserve revision/time history;
- keep project-specific lifecycle/support-process predicates in the Project Profile unless the common model explicitly defines them.

A conformance claim MUST identify the model version, Project Profile revision, checker/review method, and evidence set.

## 20. Project Profile

The Project Profile defines at least the parameters that are required by the project:

- Product boundaries and engineering magnification layers;
- Proposition roles and Engineering Object families;
- relation vocabulary, signatures, converse labels, validators, and semantic composition rules;
- scale compatibility and permitted bridges;
- Contract parties, authority, human Decision scopes, enforcement, and Contract resource models;
- Work Product schemas, semantic-role constraints, required validators, information-exposure policies, and acceptance rules;
- required Instrumental Checks, Low-profile Assessments, High-profile Assessments, escalation conditions, and instrumentation-improvement rules;
- Product API representations and Team API communication rules;
- Trade Space representation, trajectory rating, cluster independence, outlier policy, repair-cost model, deactivation and post-mortem criteria;
- Resource Envelope dimensions, measurement rules, invention allocations, and waste classification;
- validation/verification independence topology;
- Evidence rules, UNKNOWN materiality, Gap and Future Action policy;
- supporting-process predicates such as Configuration Management, Change Management, baseline, release, deployment, production, risk, and quality rules;
- lifecycle labels for Decisions, Engineering Objects, Work Products, Contracts, and other project elements;
- external-party communication constraints and permitted formats;
- integration/composition strategies and their validation requirements.

## 21. Formal model audit

Each Foundation Axiom has a defined Intent, Statement, Boundary, and Validation argument. A release audit SHOULD test at least the following countermodels:

- **AX-1:** Arbitrary graph path used as valid engineering trace
- **AX-2:** Hidden or fabricated completion replaces unresolved information
- **AX-3:** Local Decision/evidence becomes remote authority without a bridge
- **AX-4:** Universal human approval or unauthorized Hive commitment
- **AX-5:** Low-support discoveries are deleted or active search consumes unlimited resources

The audit also checks term uniqueness, Proposition/Engineering Object separation, Work Product information boundaries, Project Profile scoping, relation-role typing, revision/time qualification, and conformance-test evidence. It also checks Check Cascade gating: no higher-cost check proceeds while a cheaper required check is failing or absent, and lower-cost checking capability is improved when a more expensive assessment discovers a condition that can be established reliably at lower Resource Cost.

Additional incompleteness and deferred-closure invariants are:

- **Truthful incompleteness incentive** - Explicit Orphans are preferred over fabricated or semantically invalid traceability. Delusive Traceability receives a stronger governance penalty than exposed incompleteness.
- **Commit UNKNOWN boundary** - No required owned UNKNOWN or material foreign UNKNOWN remains unresolved when a Decision becomes binding.
- **Future Action completeness** - A Future Action identifies responsible party, trigger, expected outcome, required artifacts, method/reference, DoR, and DoD.
- **Deferred Baseline truthfulness** - A Baseline with an authorized Known Gap records the Gap and its Future Action explicitly. Unavailable engineering values are not fabricated.
- **Temporal closure** - Artifacts produced through a Future Action enter a later controlled engineering state and do not rewrite the earlier state in which the Gap was unresolved.

Additional exploration invariants are:

- **Cluster independence** - Cluster support accounts for contribution independence; correlated repetition does not become independent evidence.
- **Support is not truth** - Cluster support affects resource survival but does not establish semantic correctness.
- **Contention locality** - Divergence is evaluated only between trajectories addressing the same scoped problem and requiring incompatible resolutions.
- **Explored divergence** - Reconciliation difficulty is derived from directly explored valid reconciliation alternatives, not textual distance or an inverse operation.
- **Knowledge survival** - Zero active allocation never deletes discovered Decisions, evidence, outliers, or trajectory history.

Additional Evidence-locality and traceability invariants are:

- **Evidence Proposition typing** - Every Evidence item used semantically is a Proposition playing an Evidence role in the applicable context: $E_{\kappa}\subseteq P$.
- **Evidence relation typing** - Every Evidence support relation satisfies its Evidence-source and Proposition-target signature.
- **Converse consistency** - Every converse relation is derived from the canonical relation and is not stored as an independent semantic fact: $r^{\smile}(y,x)\iff r(x,y)$.
- **Bidirectional traceability** - Applicable relations support bounded forward and converse traversal. Forward and reverse navigation do not imply semantic composition.
- **Local Evidence support** - Evidence can directly support a Decision or other Proposition only in a context where the applicable Evidence relation is valid.
- **Feedback materialization** - Upward Evidence effects cross an Engineering Layer boundary through a Feedback Exchange Item.
- **Feedback provenance** - A Feedback Exchange Item can be traced back to the Evidence that produced it without requiring the complete Evidence contents to be redistributed.
- **Nearest affected Scale** - Upward feedback stops at the nearest Engineering Layer capable of resolving the condition correctly.
- **Local evidential closure** - Foreign Evidence does not automatically establish evidential closure in the receiving Engineering Layer.
- **Evidence retrieval without inheritance** - Source Evidence can be referenced or explicitly retrieved without automatically acquiring a local support relation.
- **Work Product separation** - A Work Product can carry or reference Evidence and Feedback Exchange Items but does not become interchangeable with a Feedback Exchange Item.
- **No automatic Evidence composition** - A structural path does not become an Evidence support relation without an explicit valid semantic composition rule.
- **No Evidence-volume authority** - Quantity, repetition, detail, or verbosity of Evidence does not establish authority, relevance, support, or sufficiency.
- **No Evidence sphere** - Broad potential relevance of Evidence does not create direct Evidence applicability across Engineering Layers.
- **Traceability is not reversibility of engineering semantics** - Converse graph traversal is a structural operation. It does not imply that causality, authority, change propagation, repair, or another engineering operation is semantically invertible.

Additional computation-boundary invariants are:

- **Canonical-state boundary** - Temporary computation cannot mutate canonical engineering state directly.
- **Projection boundedness** - Semantic computation operates on an explicitly bounded projection of canonical state rather than assuming unrestricted whole-project context.
- **Deterministic-first computation** - Applicable mechanically decidable properties are established before unresolved semantic reasoning is assigned.
- **Temporary-state separation** - Intermediate reasoning, hypotheses, and computational structures do not become canonical elements merely because they were generated.
- **Candidate status** - A Candidate Delta is a proposal, not a successor state, accepted Proposition, Decision, Evidence closure, Work Product, or truth claim.
- **Producer/admission separation** - Producing a Candidate Delta does not grant authority to apply it.
- **Base-state qualification** - Every Candidate Delta is qualified by the canonical state or revision from which its problem projection was derived.
- **Stale-delta reassessment** - A Candidate Delta affected by subsequent canonical-state change must be revalidated before application.
- **Applicable-validator admission** - Canonical application requires successful disposition of every validator applicable to the proposed effect.
- **Truthful admission failure** - Missing or failed validation remains explicit and is not replaced by fabricated closure.
- **Controlled application** - An admitted Candidate Delta produces a revision-qualified successor state without destructively rewriting the previous state.
- **Rejected-candidate preservation** - Failure of admission blocks the proposed canonical change but does not require deletion of useful exploratory knowledge.
- **Candidate Delta / Work Product separation** - Candidate Delta admission and Contract Work Product Acceptance are distinct operations.
- **Participant transience** - Persistence of the participant that produced a candidate is not required for persistence of admitted engineering state; required provenance survives independently.

# Part VI - References and supporting material

## 22. Language and terminology references

The following references define the proposal's language and terminology foundation:

1. ASD-STE100, Simplified Technical English, Issue 9, January 2025. https://www.asd-ste100.org/
2. BCP 14: RFC 2119 and RFC 8174. https://www.rfc-editor.org/info/bcp14/
3. ISO 24495-1:2023, Plain language - Part 1: Governing principles and guidelines. https://www.iso.org/standard/78907.html
4. ISO 704:2022, Terminology work - Principles and methods. https://www.iso.org/standard/79077.html
5. ISO/IEC Directives, Part 2, Principles and rules for the structure and drafting of ISO and IEC documents. https://www.iso.org/directives-and-policies.html

ASD-STE100 applies to project-authored prose throughout the proposal. BCP 14 applies only to technical normative keywords as defined in Section 4.2.

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

## 25. Supporting engineering references

Engineering standards and frameworks remain supportive/non-normative in this common proposal unless a Project Profile makes them applicable. Examples include Automotive SPICE, APQP, ISO 26262-family standards, INCOSE requirements guidance, NASA systems/software engineering guidance, and project-specific V-model processes.

## 26. Project supporting material

The following project material informed this revision:

- `harness-hive-dialogue-recap.md` - non-normative recap used to restore the state-centric Hive architecture, bounded traversal, trade-space, trajectory, cluster, repair-cost, and non-actor design direction. Later accepted decisions in this proposal take precedence where the recap is older.
- `resource_consumption_recap.md` - decision recap for context/input, orchestration, polling waste, and root/sub-agent resource use.
- `session_resource_analysis.xlsx` - supporting workbook containing summary, category, phase, waste, support, agent, sub-agent, timing, session, and daily pivots.

# Compilation status

Draft 0.24 retains the structural rewrite introduced in Draft 0.9 and corrects the Hive/Swarm/Hive Mind model. Hive is the complete execution model; Swarms are task-assigned populations commanded by the Hive; Clusters form from sufficiently independent Swarm contributions supporting Decisions; and Hive Mind is the distributed/federated intelligence paradigm, not a centralized reasoning-core component. The draft retains the formal definitions for Product, Reshuffling, Waste, Resource Envelope, Extremum Exploration, Proposition, Engineering Object, and formal statement roles.

**Terminology decision.** Hive, Swarm, and Hive Mind are related but distinct. Hive denotes the complete execution model. Swarm denotes task-assigned execution populations commanded by the Hive. Hive Mind denotes the distributed/federated intelligence paradigm under which the system behaves coherently as a whole while preserving individual actor traits, properties, and behaviours.

**Formal-restoration status.** Draft 0.24 restores explicit Scope algebra, revision mapping, revision-aware relation records, scoped supersession, bounded traversal, the revised Maturity/Brittleness model, the Reshuffling/repair-exploration model, Cluster/divergence resource-survival rules, the UNKNOWN/Gap/Future Action model with truthful-incompleteness incentives and deferred Baseline closure, Evidence Proposition algebra with Feedback Exchange Item locality, converse/reverse traceability, the derived no-sphere theorem, and Candidate Delta/canonical-state computation-boundary semantics. Older formal structures that conflict with later accepted semantics remain retired and are reviewed separately before restoration.

**Repair discovery invariant.** Repair cost is established from valid alternatives discovered through direct exploration of the affected and adjacent Solution Spaces. It is not derived by applying an inverse operation to the originating change.

**Reshuffling locality invariant.** A downstream finding becomes Reshuffling only when it cannot be absorbed within the affected local Engineering Layer and requires vertical Decision rework. Propagation stops at the nearest Engineering Layer capable of resolving the finding correctly.

## Open backlog

- **3D concept illustration:** add a dedicated 3D model showing Engineering Layers, Scale, Magnification, Decision Blast Radius, Extent, and cross-layer information propagation. The figure must explain the concept itself rather than merely provide an example hierarchy.
- **Scale formalization:** recover and rework the mathematical model for Scale comparison, Magnification comparison/compatibility, Scale-compatible relations and operations, cross-Scale propagation, Decision Blast Radius, and Extent assessment. The recovered algebra must preserve the locality and no-sphere semantics established in Section 9.
- **Minimal-repair formalization:** model minimal repair cost as an outcome of direct Solution Space exploration by the affected and adjacent engineering contexts. It cannot be computed as an inverse operation of the proposed change because feasible repairs, local absorption, alternative Decisions, and cross-Scale consequences must be discovered rather than algebraically reversed.