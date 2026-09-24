---
title: "Hive/Swarm Engineering Governance"
subtitle: "Formal Proposal - Draft 0.21"
date: "16 September 2026"
---

**Status.** Accepted Abstract, Part I Section 3, Language Foundation, Contract terminology/Acceptance revisions, Scale/Scaling/Magnification/Extent revisions, Check Cascade, Scope/revision/traversal restoration, Maturity/Brittleness restoration, Reshuffling/repair exploration, and Cluster/divergence resource-survival revisions are integrated. Other unresolved formalization items remain unchanged. ASD-STE100 conformance is not claimed without designated checker or review evidence.

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
| **Engineering Layer** | Project-defined bounded Scale and Magnification context within which engineering elements can be reasoned about as one coherent Product view. |
| **Engineering Object** | Materialized project entity with tool, repository, physical, or document identity. It can carry or materialize one or more Propositions. |
| **Evidence** | Recorded information used by a defined validator or argument to support a Proposition. Evidence is scope- and role-specific. |
| **Exchange Item** | Boundary-relative information object used to communicate Propositions, Product interfaces, results, feedback, or other materialized information. |
| **Executor** | Actor responsible for fulfilment of an assigned Contract, including delivery of the required Work Product or explicit reporting that fulfilment cannot be completed. A Human can be an Executor when assigned responsibility for a Contract result. |
| **Exploration** | Bounded computational attempt to extend, test, compare, or refine the current Solution Space. |
| **Extent** | Measurable reach of a Decision effect within its current Scale and Magnification. Significant Extent usually has severe economic effect and can question the rationality of the originating Decision. |
| **Extremum Exploration** | Exploration intended to discover a different local extremum or challenge whether a materially better region exists outside the current search neighborhood. |
| **Future Action** | Contracted resolution of a Known Gap with an identified Party, Outcome, Method, Definition of Ready, and Definition of Done. |
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

The Hive uses deterministic algebra before assigning semantic reasoning work to a Swarm.

The computational sequence is:

$$ProjectState\rightarrow Projection(q)\rightarrow StructuralOps\rightarrow SemanticQuestions\rightarrow CandidateDelta\rightarrow Validation\rightarrow SuccessorState.$$

`Projection(q)` selects the semantic state needed for problem $q$. Structural operations compute deterministic facts such as reachability, relation type checks, revision lookup, set membership, known dependency closure, and declared scope intersection. Only unresolved semantic questions are sent to micro-agents, humans, simulations, or other reasoning resources.

A Candidate Delta can contain:

$$\Delta_q=(P_{cand},R_{cand},D_{cand},E_{cand},U_{cand},G_{cand},F_{cand},Req_{cand}).$$

where the terms represent proposed Propositions, Relations, Decisions, Evidence, UNKNOWNs, Gaps, Future Actions, and Requests/Work Product needs.

The Hive MUST NOT make a canonical state transition merely because a model generated a candidate. Applicable relation, authority, evidence, Contract, and Project Profile validators determine whether the candidate can affect active state.

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

### 6.2 Proposition and Engineering Object

A Proposition is the core semantic element. It can represent a claim, need, candidate structure, Decision, interface intent, expected behavior, constraint, question, request, gap statement, or another addressable semantic unit.

An Engineering Object is a materialized project entity such as a requirement record, document, model element, source file, binary, simulation result, test artifact, physical part, assembly, configuration record, or other tool/physical item.

Materialization is many-to-many:

$$Materializes\subseteq P\times O.$$

A Decision is a Proposition role and is not an Engineering Object. A Decision can later materialize into an ADR, plan, change request, Product definition, Exchange Item, or another Engineering Object.

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
