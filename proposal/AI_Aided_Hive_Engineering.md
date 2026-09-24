Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
Hive/Swarm Engineering Governance
Formal Proposal - Draft 0.9
15 September 2026
Status. Structural rewrite after Draft 0.8. The document separates a non-specialist proposal overview,
the language foundation, the mathematical Foundation, the formal operational proposal, and
conformance/profile material. ASD-STE100 conformance is not claimed without designated checker or
review evidence.
Normative basis. Approved project discussion and accepted changes through Draft 0.8, aligned with
the project dialogue recap and resource-consumption analysis where those sources do not conflict with
later decisions.
Mathematics. Mathematical expressions are represented as native editable equations in the Word
build.
# Contents
Part I - Proposal in plain terms: Abstract and intent; Why a Hive/Swarm architecture; Non-specialist
operating model.
Part II - Language Foundation: Intent; Norms; Applicability; Dictionary.
Part III - Foundation: Reasoning preface; formal statement roles; relation/graph/set algebra;
computational algebra; human ingress; Foundation Axioms.
Part IV - Formal Proposal: Operational state and roles; operational algebra; consistency and reliability;
scale; trade-space exploration; Contracts and Product delivery; evidence; maturity; UNKNOWNs/Gaps;
recursive Y/V; supporting processes; Swarm resource control; no-sphere theorem.
Part V - Conformance and Project Profile: Conformance requirements; Project Profile; formal model
audit.
Part VI - References and supporting material.
Part I - Proposal in plain terms
# 1. Abstract and intent
The proposal defines a state-centric Hive/Swarm architecture for engineering work. It does not model
an engineering organization as a hierarchy of persistent AI workers. It also does not treat long internal
reasoning chains as the primary product of intelligence. The primary state is a semantic engineering
model. Computational participants are temporary resources that read a small relevant projection of
that state and return small candidate changes.
A Hive is the problem-local semantic and governance computation that owns this engineering process.
A Swarm is the transient set of specialized computational participants that the Hive allocates to current
explorations. The Hive Mind is the reasoning core that selects a bounded semantic projection, creates
narrow questions or requests, invokes low-cost specialized micro-agents or other engines, reconciles
their candidate outputs, and updates the current solution model only after validation.
Hive reasoning is therefore intentionally different from a long conversation among agents. A micro-agent should receive only the propositions, relations, constraints, evidence, and resource limits
required for its narrow problem. It should return a compact candidate semantic delta. Large histories,
full-project context, repeated polling, and persistent private agent memory are not the default
coordination mechanism. This design targets low communication cost, low energy and compute
consumption, low context replay, and reduced overthinking.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
The proposal is engineering-oriented. It treats requirements, models, source code, physical parts, tests,
contracts, evidence, human decisions, and external information as different materializations or roles
around a common semantic state. It preserves the V-model and applicable engineering standards. It
does not replace domain methods such as Automotive SPICE, APQP, ISO 26262-family processes,
Configuration Management, Change Management, or project-specific verification methods.
A Product is the coherent engineered subject whose state is being created, evolved, verified, or
delivered. A Product can be a complete system, a component, software, infrastructure, a physical asset,
a service, or another project-defined product boundary. A Work Product is not the Product itself. It is a
contractual result used to create, change, evidence, integrate, accept, or transfer Product state.
Contractual Product Delivery therefore means fulfillment of a Contract through accepted Work
Products that advance the Product to the Contract target state.
The economic target is not a global mathematical optimum. The Hive seeks a satisfactory Contract and
Product outcome while controlling declared resource use, unnecessary reshuffling, rework, and waste.
It can preserve many alternatives and outliers without continuously spending resources on all of them.
# 2. Why a Hive/Swarm architecture
## 2.1 Three orchestration paradigms
Dimension Organization-mimetic harness Reasoning-mimetic harness Hive/Swarm proposal
Primary unit Roles, agents, teams, tasks Reasoning steps and branches Semantic state, problem-local Hive,
trajectories
Coordination Delegation, handoffs, messages Chained or branched reasoning Typed relations and small candidate deltas
State carrier Agent/session memory and task
state
Reasoning trace/search structure Canonical semantic state and provenance
Specialization Specialist agents/tools Specialist reasoning stages Transient micro-agents, solvers, tools,
humans
Authority and
truth
Often coupled to role/workflow Often coupled to evaluator/search
score
Explicit validators, Contracts, scope,
evidence, Project Profile
Search Task/workflow execution Thought-space search Trade-space trajectories; all discoveries
retained
Communication
risk
Handoffs, polling, history replay Long branch/reasoning replay Small state projections and compact
semantic deltas
Failure handling Retry, handoff, escalation Backtrack, reflect, branch Preserve outcome, re-rate trajectory, post-mortem, reallocate
Engineering
traceability
Added by application Usually external to method Native relation/state property
Cross-layer
authority
Workflow-dependent Usually unmodeled Materialize Exchange Item; reconcile locally
Illustration - established patterns. Current agent frameworks commonly expose
manager/worker, agents-as-tools, handoff, crew, task, process, memory, and conversation
concepts. OpenAI Agents SDK and CrewAI are examples of this family. Tree of Thoughts and
Graph of Thoughts are examples of deliberate reasoning-space search. These examples
illustrate the comparison categories; they do not define proposal conformance.
## 2.2 Project evidence for communication cost
The project resource analysis is supporting evidence for the architecture choice, not proof of a
universal law. Across 333 retained session files, the analysis measured 1.432 billion input tokens and
## 4.7 million output tokens. Direct polling/status activity accounted for 19.9% of input. Supporting
orchestration accounted for another 10.5%. Root/orchestrator sessions carried 97.9% of input while
sub-agents carried 2.1%.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
Direct polling/status waste - 19.9% of archive input. Do not make repeated wait/list/status
interactions a core coordination mechanism.
wait_agent alone - 15.7%. Prefer state-change and semantic-completion conditions.
Supporting orchestration - 10.5%. Reduce repeated messages, follow-up restatement, spawn
overhead, and interruption.
Root/orchestrator sessions - 97.9% of archive input. Reduce central context replay and long
orchestration sessions.
Sub-agents - 2.1%. In this archive, cheap specialists were not the dominant measured cost;
coordination/context was.
The measured archive does not contain exact model identifiers for all sub-agents and its phase timing
includes explicit proxy values. The proposal therefore uses these data as a decision input, not as a
universal performance benchmark.
# 3. Non-specialist operating model
The following sequence summarizes the formal proposal without requiring relation algebra.
The project defines a Product, its engineering layers, Project Profile, applicable norms, Contracts,
authority boundaries, Work Product schemas, and declared Resource Envelopes.
The Hive represents the current engineering meaning as Propositions and typed Relations. Files,
models, code, assemblies, reports, and other Engineering Objects materialize or carry that meaning.
For each active problem, the Hive selects only the relevant semantic projection. It does not load the
entire project by default.
The Hive Mind creates narrow explorations. A Swarm of specialized micro-agents, solvers, simulations,
tools, humans, or external services can execute them.
Each exploration returns candidate Propositions, Relations, Decisions, evidence, UNKNOWNs, Gaps,
Work Product requests, or other small semantic deltas.
The Hive validates those candidates before they affect active state. Structural reachability never
becomes semantic truth by itself.
A Decision reduces or redirects the active design space for a local problem. Decision authority remains
local. Cross-team or cross-layer effects appear through updated Exchange Items that the other party
actually consumes.
Contracts turn engineering intent into obligatory Work Products. Contract decomposition can create
child production, planning, verification, and integration Contracts without splitting the Hive itself.
A layer can contain many Contract sub-layers but still produces a coherent Product definition and
implementation state at that engineering magnification.
Verification is independent according to the applicable Project Profile. The mathematics permits same-group, separate-Hive, separate-department, separate-enterprise, or other required validation
topologies.
The Executor controls immediate traceability quality, Known Gaps, and the fulfilment proposal.
Acceptance is a separate obligation assigned to applicable actors.
Trade-space exploration preserves every discovered outcome. Active resource allocation can be
reduced to zero for weak trajectories without deleting their knowledge.
The Hive stops expanding a trajectory when the expected value of more exploration does not justify its
Resource Cost, or when the Contract objective is satisfied. Global optimality is not assumed.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
Supporting processes such as Configuration Management, Change Management, Problem Resolution,
Quality Assurance, Risk Management, and Measurement operate over the Solution Space. They are not
core semantic primitives.
Historical state remains addressable. Later revisions supersede or extend prior state; they do not
rewrite it.
Part II - Language Foundation
# 4. Language Foundation
## 4.1 Intent
The Language Foundation makes formal prose short, stable, and machine-reviewable without
inventing a new controlled language. Project-authored prose uses ASD-STE100 as the core controlled-English principle. ISO plain-language and terminology guidance supplements it. BCP 14 is reserved for
normative keywords in the technical parts of this proposal.
The Language Foundation has four goals:
one concept has one preferred term in the proposal;
definitions are short and cross-consistent;
examples are visually isolated from formal text;
normative keywords are used only where they carry technical requirement semantics.
## 4.2 Norms
ASD-STE100 Issue 9 governs project-authored English throughout the proposal, including the Abstract,
dictionary, formal model, and illustrations. A conformance claim requires the project-designated
checker or review evidence.
ISO 24495-1 applies as supporting plain-language guidance. ISO 704 applies to terminology construction
and definition quality. ISO/IEC Directives Part 2 applies as supporting technical drafting guidance.
BCP 14 (RFC 2119 and RFC 8174) applies only to technical normative clauses in Part III - Foundation,
Part IV - Formal Proposal, and Part V - Conformance and Project Profile. Outside those parts, the
words must, should, may, and related forms are ordinary English unless they occur in a quotation or
source title. Technical BCP 14 keywords are written in uppercase when normative semantics are
intended.
Citations, quotations, imported requirements, legal text, contractual text, identifiers, URLs, and
protected source text remain unchanged.
## 4.3 Applicability
All ordinary proposal text is formal. Concrete examples are the only non-formal explanatory content
and appear in unnumbered Illustration blocks. An Illustration does not create an axiom, requirement,
Project Profile default, Contract obligation, relation semantic, or conformance rule.
A Project Profile supplies project-specific values where the common model deliberately leaves a
parameter open. A Conformance Evaluation tests an implementation or engineering state against the
common model and the applicable Project Profile.
## 4.4 Dictionary
The dictionary is intentionally compact. A term definition may reference another defined term rather
than repeating its semantics. Project-specific specializations belong in the Project Profile.
Acceptance Obligation. Contract obligation assigned to an actor to evaluate a fulfilment proposal or
applicable Work Product.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
Acceptor. Actor that carries an Acceptance Obligation for a Contract.
Actor. Human, Hive, external organization, or other authority-capable participant. Computational
micro-agents are not Actors unless a Project Profile grants that role.
Agent. Computational participant that performs a bounded operation. Agent identity does not create
semantic authority.
Baseline. Configuration Management reference state created only when the applicable Configuration
Management process defines it.
Binding. Scoped and time-qualified prescriptive force of an obligatory Decision. Binding applies to
Decisions, not Work Products or Exchange Items.
Cluster. Set of sufficiently independent exploration contributions supporting one trajectory for one
problem statement.
Conformance Evaluation. Formal check of implementation/state against this model plus the
applicable Project Profile.
Contract. Governed execution agreement with one accountable Executor, one or more issuing parties,
optional supplementary parties, obligations, a Product target, Work Product obligations, resource
constraints, acceptance rules, and enforcement.
Decision. Rationale-bearing Proposition that preserves or directs a possible course of exploration or
behavior. A Decision is not an Engineering Object.
Engineering Layer. Project-defined magnification range that yields a coherent Product view at that
scale.
Engineering Object. Materialized project entity with tool, repository, physical, or document identity. It
can carry or materialize one or more Propositions.
Evidence. Recorded information used by a defined validator or argument to support a Proposition.
Evidence is scope- and role-specific.
Exchange Item. Boundary-relative information object used to communicate Propositions, Product
interfaces, results, feedback, or other materialized information.
Executor. Single accountable Actor that controls current-level Contract fulfilment and immediate
traceability quality.
Exploration. Bounded computational attempt to extend, test, compare, or refine the current Solution
Space.
Extremum Exploration. Exploration intended to discover a different local extremum or challenge
whether a materially better region exists outside the current search neighborhood.
Future Action. Contracted resolution of a Known Gap with an identified Party, Outcome, Method,
Definition of Ready, and Definition of Done.
Gap. Explicitly known missing relation, evidence, content, capability, or result required for a stated
purpose.
Hive. Persistent problem-local semantic and governance computation operating over canonical
engineering state.
Hive Mind. Hive reasoning core that selects bounded state projections, allocates narrow computations,
reconciles candidates, and controls active exploration.
Human Arbitrary Input (HAI). Exogenous human input that can arrive at any time and can preempt
the current continuation without erasing history.
Human Prescriptive Choice (HPC). Human choice required when an obligatory Decision cannot be
committed by the Hive.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
Human Voluntary Choice (HVC). Optional human choice made while autonomous Hive continuation
remains possible.
Human Work Product (HWP). Work Product supplied by a Human or human organization. Human
origin does not bypass validation.
Integrator. Executor of an integration Contract that constructs a coherent same-scale Work Product
from applicable partial Work Products and evidence.
Justification. Valid relation/evidence structure that satisfies the applicable validators for using a
Proposition as a decision, trace, or commitment basis.
Known Gap. Gap whose existence and scope are known and recorded.
Local Optimum / Local Extremum. Best/extreme candidate relative to a declared neighborhood or
currently explored region, not the entire theoretical Solution Space.
Global Optimum / Global Extremum. Best/extreme candidate over a declared complete Solution
Space and objective. The Hive does not claim this property unless completeness and the objective are
explicitly established.
Magnification. Engineering scale of a Proposition, Engineering Object, Decision, Exchange Item, Work
Product, or Product view.
Micro-agent. Short-lived, specialized, low-Resource-Cost Agent used for one narrow exploration or
validation operation.
Outlier. Discovered outcome or trajectory with low current cluster support. It remains recorded even
when active allocation is zero.
Overthinking. Reasoning expenditure whose expected information or decision value is lower than its
Resource Cost, or reasoning applied to a result that deterministic state/algebra can establish directly.
Product. Coherent engineered subject whose state is created, evolved, verified, accepted, produced, or
delivered.
Product API. Exchange Item that materializes a Product-interface Decision in a project-appropriate
representation.
Product Delivery. Contract fulfilment in which accepted Work Products advance the Product to the
Contract target state.
Project Profile. Formal project input that defines open parameters such as relation vocabulary, scale
topology, Work Product schemas, validators, authority, resource models, lifecycle predicates, and
validation independence.
Proposition. Core addressable semantic element of the solution model. It is not an Engineering Object
by default. It can later be materialized, carried, or realized by Engineering Objects.
Relation. Typed semantic or structural association between addressable elements, qualified by scope,
revision, time, and Project Profile semantics.
Reshuffling. Reopening or reallocating previously active solution commitments because a change
propagates beyond its original local problem. Reshuffling cost measures resulting review, rework,
reverification, and coordination.
Resource Cost. Multi-dimensional consumption caused by an operation, exploration, Contract,
trajectory, or change.
Resource Envelope. Declared availability/limits for relevant resource dimensions such as context,
model calls, compute, wall time, money, human effort, energy, equipment, and external capacity. It is
not a universal scalar.
Resource Budget. Contract- or operation-scoped allocation drawn from a Resource Envelope.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
Solution Space. Addressable set of currently known candidate states, constraints, outcomes, and their
relations for a scoped problem.
Swarm. Transient population of micro-agents and other computational engines allocated by a Hive.
Team API. Project-defined set of Work Products and communications used to coordinate Product
evolution among parties.
Trade Space. Project-visible candidate region used to compare alternatives for one problem under
current constraints, evidence, and authority.
Trajectory. Temporally ordered path of exploration outcomes and Decisions through a Trade Space.
UNKNOWN. Required information whose value, validity, applicability, or result has not been
established.
Waste / Wasteful. Waste is Resource consumption that creates neither required governance/validation
effect nor reusable progress, evidence, knowledge, or Product value for the active objective. An
operation is wasteful when the Project Profile classifies its consumption as Waste.
Work Product. Complete obligatory Contract result prepared under a defined schema and acceptance
rule. A Work Product can be an input to another Contract. # Part III - Foundation
# 5. Foundation
## 5.1 Preface - reasoning before mathematics
The model starts from five non-technical observations.
First, a graph edge is not truth. Engineering traceability fails if the model treats any path as semantic
justification.
Second, missing information must remain visible. A false trace is more dangerous than an explicit
unresolved item because it hides the need for work.
Third, engineering has scale. A component-level decision and a Product-level decision can both be valid
without one inheriting the other’s authority.
Fourth, autonomy has an authority boundary. A Hive should decide when a feasible choice is inside its
authority and should ask for human prescription only when the missing commitment requires it.
Fifth, exploration has a cost. The Hive should preserve discoveries but should not keep spending
resources on every trajectory or promise a global optimum when Contract fulfilment does not require
one.
The mathematics below exists to make those observations testable. Sets represent candidate spaces.
Relations represent typed associations. Graphs provide projections for navigation. Validators decide
whether a relation can be used semantically. Time and revision preserve history. Resource vectors
control active computation without deleting knowledge.
## 5.2 Formal statement roles
This proposal separates the role of a mathematical expression from its expression syntax.
OpenMath is useful for representing mathematical objects, symbols, Content Dictionaries, and Formal
Mathematical Properties. It does not by itself provide the document-level distinction needed here
between an axiom, theorem, assumption, and conjecture. OMDoc and TPTP explicitly represent those
statement roles. The proposal adopts that role separation without requiring any one serialization
format.
Definition. Introduces a term, symbol, relation, function, or predicate meaning Can be used after
introduction.
Axiom. Foundation statement accepted by this proposal and not derived from another proposal
statement Basis for derived properties and conformance.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
Assumption. Explicit scoped condition supplied by a problem or Project Profile Valid only in its
declared scope; must not become a universal rule.
Lemma. Derived intermediate result Used to simplify a later proof.
Theorem / Derived Property. Result derived from Definitions, Axioms, and declared Assumptions Can
be used where its proof conditions hold.
Conjecture. Proposed relation or property not yet established Cannot support conformance or
commitment.
An Invariant is a property that must hold in every valid state of a specified scope. Its logical source can
be an Axiom, Theorem, Contract rule, or Project Profile rule; Invariant is therefore a state-property
class, not a separate proof role.
A formal statement record has the conceptual form:
S=(i d ,r ol e ,i nt e nt ,st at e me nt ,s c o p e ,d e p e n d e n c i e s, e v i d e n c e , v ali d a t i o n) .
## 5.3 Core set, relation, and graph algebra
Let U be the addressable semantic universe for a project revision. Let P⊆U be Propositions and
O⊆U be Engineering Objects. The two sets are not interchangeable.
A materialization relation can connect them:
M a t e ri aliz e s⊆P×O .
A Proposition can have several materializations and one Engineering Object can carry several
Propositions.
A typed binary relation r has source and target sets:
r⊆Sr×Tr
.
Its converse is:
r
⌣={( y , x ) ∣( x , y )∈r}.
The converse is a mathematical view of the same relation. It does not create a second independent
semantic fact.
The common structural algebra includes domain, range, image, inverse image, restriction, converse, set
union/intersection/difference, and relational composition. Structural composition is:
r ∘ s={( x ,z) ∣∃ y :( x , y )∈s∧( y ,z)∈r}.
Structural composition creates a path relation. It does not create semantic entailment unless the Project
Profile defines a sound semantic composition rule for the relation family.
A graph G=(V , E) is a projection of addressable elements and relation instances for navigation and
analysis. Graph reachability is therefore weaker than semantic justification:
R e a c h a bl eG
( a ,b) ⇒ ̸J u st i f i e s( a ,b) .
A relation validator has the generic form:
V r
( e ,κ )∈{⊤,⊥,? },
where κ contains the applicable scope, revision, time, Project Profile, authority, and other relation-specific context.
## 5.4 Computational algebra
The Hive Mind uses deterministic algebra before allocating semantic reasoning.
The computational sequence is:
Pr o j e c t S t at e→Pr o j e c t i o n ( q)→S tr u c t u r alO p s→S e ma nt i c Qu e st i o n s.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
S e ma n t i c Qu e st i o n s→C a n d i d a t e D e l t a→V ali d a t i o n→S u c c e ss o r S t a t e .
Projection(q) selects the semantic state needed for problem q. Structural operations compute
deterministic facts such as reachability, relation type checks, revision lookup, set membership, known
dependency closure, and declared scope intersection. Only unresolved semantic questions are sent to
micro-agents, humans, simulations, or other reasoning resources.
A Candidate Delta can contain:
Δq=¿
where the terms represent proposed Propositions, Relations, Decisions, Evidence, UNKNOWNs, Gaps,
Future Actions, and Requests/Work Product needs.
The Hive MUST NOT make a canonical state transition merely because a model generated a candidate.
Applicable relation, authority, evidence, Contract, and Project Profile validators determine whether the
candidate can affect active state.
## 5.5 Human ingress and choice set
Human interaction is a known set before delegated-autonomy rules are applied:
H={H A I , H V C , H PC , H W P}.
HAI = HUMAN_ARBITRARY_INPUT.
HVC = HUMAN_VOLUNTARY_CHOICE.
HPC = HUMAN_PRESCRIPTIVE_CHOICE.
HWP = HUMAN_WORK_PRODUCT.
HAI can arrive asynchronously and can project a successor engineering universe. It can be
controversial or outside the current Hive recommendation. It does not erase prior state.
HVC is optional while autonomous continuation remains possible.
HPC is required only for an obligatory Decision when no Hive-committable choice remains or when
that Decision authority is explicitly human.
HWP is a Work Product supplied by a Human or human organization. It is assessed using the same
applicable Work Product, information-boundary, traceability, and validation rules as other Work
Products.
Binding is restricted to obligatory Decisions:
Bi n d i n g⊆D e c isi o n×S c o p e×T ime .
## 5.6 AX-1 - Semantic legitimacy
Intent. Prevent a graph, document link, or path from becoming engineering truth only because it
exists.
Statement. A relation can support a justification or commitment only when every applicable validator
for that relation is established in the current context.
Define:
V ali dr
( κ )=T y p eV ali d∧S e ma nt i cV ali d∧S c al eV ali d∧S t at eV ali d .
Then:
U s e F o r J u st i f i c at i o n (r,κ ) ⇒ V ali dr
( κ ) .
R e a c h a bl eG
( a ,b) ⇒ ̸J u st i f i e s( a ,b) .
Boundary. AX-1 does not state that a Proposition is true merely because all relation validators pass. It
states that invalid relations cannot be used as a justification path.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
Validation. Remove AX-1 and an arbitrary edge can satisfy a trace requirement without semantic
evidence. The resulting model admits false trace closure. The axiom is therefore necessary for the
proposal’s trace semantics.
## 5.7 AX-2 - Truthful incompleteness
Intent. Preserve missing information instead of hiding it behind a plausible but unsupported relation.
Statement. When a required justification, evidence item, relation, or result cannot be established, the
model records the unresolved state explicitly and does not fabricate completion.
M issi n g R e q uir e d ( x ,κ )=R e q uir e d ( x ,κ )∧¬E st a blis h e d ( x ,κ ) .
M issi n g R e q uir e d ( x ,κ ) ⇒ E x pli c it U n r e s ol v e d ( x ,κ ) .
A project can classify the unresolved state as ORPHAN, UNKNOWN, KNOWN_GAP, CONFLICT, or
another Project Profile category. The category must preserve the fact that the required item is
unresolved.
Boundary. AX-2 does not require every unknown to block every activity. Materiality and commitment
rules remain project- and Contract-specific.
Validation. Remove AX-2 and the model can improve apparent completeness by inventing links or
suppressing gaps. That directly conflicts with truthful traceability.
## 5.8 AX-3 - Scale locality
Intent. Prevent information visibility from becoming cross-scale prescriptive authority or inherited
evidence closure.
Statement. Direct semantic relations and Decisions operate within the applicable scale rule. Cross-scale
effects require an explicit permitted bridge, materialized Exchange Item, or other Project Profile
mechanism followed by local interpretation.
Dir e c t S e ma nt i c U s e ( x , y ,κ ) ⇒ S c al eV ali d ( x , y ,κ ) .
C r o ss S c al e E f f e c t ⇒ E x pli c it Bri d g e∧Lo c al I nt e r p r e t at i o n .
Boundary. AX-3 does not fix universal engineering levels. Magnification frames and allowed bridges
are Project Profile parameters.
Validation. Remove AX-3 and a local Decision or evidence item can silently become authoritative over
arbitrary remote layers, producing the authority/evidence sphere that the model is designed to prevent.
## 5.9 AX-4 - Delegated autonomy
Intent. Let the Hive act without routine human approval while preserving explicit human authority
boundaries.
For problem q define:
H i v e S p a c e ( q)=F e a si bl e ( q) ∩ H i v e A u t h o riz e d ( q) .
Statement. If H i v e S p a c e ( q) is non-empty, the Hive can continue autonomously. If an obligatory
Decision is required, feasible choices exist, and none can be committed by the Hive,
HUMAN_PRESCRIPTIVE_CHOICE is required. If no feasible choice exists, human authority cannot make
the solution feasible; the conflict remains explicit until the problem changes.
H i v e S p a c e ( q) ≠⌀ ⇒ A u t o n omo u sC o nt i nu e ( q) .
Define:
N e e d s H PC ( q)=F e a si bl e ( q) ≠⌀∧H i v e S p a c e ( q)=⌀∧N e e d sO bli g at o r y D e c isi o n ( q) .
Then:
N e e d s H PC ( q) ⇒ H PC ( q)=R EQU I R E D .
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
F e a si bl e ( q)=⌀ ⇒ Pr e s e r v eC o n f li c t ( q) .
Boundary. AX-4 does not block HAI, HVC, or HWP while autonomous continuation is possible.
Validation. Remove AX-4 and either all commitments require human approval or the Hive can make
commitments outside its authority. Both outcomes violate the delegated-autonomy objective.
## 5.10 AX-5 - Resource-rated exploration
Intent. Preserve all discoveries while concentrating active resources on trajectories that justify
continued expenditure.
Statement. Every discovered outcome is retained with provenance and status:
Dis c o v e r e d ( o ,q ,t ) ⇒ Pr e s e r v e ( o ,q ,t ) .
Active resource allocation is separate from preservation:
A ll o c a t i o n ( o ,t )=R a t e ( F e a t u r e s( o ,t ) ) .
Features(o,t) can include progress, novelty, evidence, independence, repair cost, Product/Contract
value, and Resource Cost/Envelope terms defined by the Project Profile.
A ll o c at i o n ( o ,t )=0 ⇒ ̸D e l e t e ( o) .
The Hive seeks a satisfactory Contract/Product path under the declared Resource Envelope. It does not
promise a global optimum unless a Contract explicitly requires and defines such an objective. Outliers
can remain in the semi-latent Solution Space even when their active allocation is zero.
The Hive MUST NOT spend production effort on invention until known means are exhausted and the
applicable invention allocation is approved.
Boundary. AX-5 does not limit the number of discovered outcomes and does not treat majority support
as truth. It limits only active expenditure.
Validation. Remove AX-5 and the model can either discard low-support discoveries or consume
unlimited resources on persistent trajectories. Both conflict with the intended resource and post-mortem behavior.
Part IV - Formal Proposal
# 6. Operational state, data structure, and roles
## 6.1 Canonical semantic state
The formal runtime is state-centric. Canonical engineering state contains semantic identities, relations,
accepted state transitions, applicable Contracts and obligations, evidence records, Gaps, UNKNOWNs,
and Project Profile context. Repositories, authoring tools, databases, model stores, and physical records
are projections of that state, not the state itself.
For an addressable universe Ub ,t
 identified by branch/universe b and time t, a repository or tool
projection is:
πk
:Ub ,t→Rk
.
Different projections can represent the same Proposition or Engineering Object. File-system
containment does not imply semantic containment.
## 6.2 Proposition and Engineering Object
A Proposition is the core semantic element. It can represent a claim, need, candidate structure,
Decision, interface intent, expected behavior, constraint, question, request, gap statement, or another
addressable semantic unit.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
An Engineering Object is a materialized project entity such as a requirement record, document, model
element, source file, binary, simulation result, test artifact, physical part, assembly, configuration
record, or other tool/physical item.
Materialization is many-to-many:
M a t e ri aliz e s⊆P×O .
A Decision is a Proposition role and is not an Engineering Object. A Decision can later materialize into
an ADR, plan, change request, Product definition, Exchange Item, or another Engineering Object.
## 6.3 Communication Proposition roles
The common minimum communication roles are:
C omm R ol e⊇{Qu e st i o n , R e q u e st ,C l a ri f i c at i o n}.
Projects can add roles through the Project Profile. Exchange Item is not another conversational role; it
is a boundary-relative materialized information role that carries applicable Propositions.
## 6.4 Decision
A Decision is a rationale-bearing Proposition that preserves or directs a possible course of Hive
exploration or behavior. Agreement is a relation to a Decision, not the definition of a Decision.
S u p p o rt s( a c t o r O rC l u st e r,d )
A g r e e me nt ( S ,d ) .
A Decision can be contested, supported by an outlier, committed, deactivated, deprecated, or
superseded. Suggested lifecycle labels are project-configurable; the common requirement is that
deactivation does not delete historical knowledge.
## 6.5 Exchange Item
An Exchange Item is a boundary-relative materialized information object. Its representation is project-specific. It can be a textual document, model file, protocol schema, CAN matrix, Revit artifact, drawing,
source code, binary, simulation result, physical sample record, or another information form
appropriate to the Product.
A Product API is a design Decision materialized as one or more Exchange Items:
D e si g n D e c isi o n( da pi)∧M at e ri aliz e s( da pi
, ea pi) .
I s E x c h a n g e I t e m( ea pi
,b) .
Exchange Item atomicity is boundary-relative. Feedback can target an internal locator of the Exchange
Item when the representation supports it.
## 6.6 Work Product
A Work Product is a complete obligatory Contract result. It has its own schema, permitted information
boundary, formal and semantic checks, required validation, supplementary information, and
acceptance rule. A lower-level Work Product does not automatically become content of an upper Work
Product merely because it exists.
I sW o r k Pr o d u c t (w ,C) ⇒ C o n f o r m sT o S c h e ma (w ,C) .
A Work Product can become an input to another Contract while remaining the complete result of its
source Contract.
## 6.7 Product
A Product is the coherent engineered subject at a defined boundary. Product structure and Work
Product structure are different. Contract decomposition can split execution without fragmenting the
final Product view delivered by the layer.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
# 7. Operational algebra
## 7.1 Purpose of the algebra
The operational algebra defines what the Hive can compute mechanically before semantic reasoning. It
also makes relation semantics explicit enough to prevent path-based hallucinated traceability.
The algebra is many-sorted. Source and target roles restrict each relation family. A relation valid for
Decisions is not automatically valid for source code, evidence, Contracts, or Work Products.
## 7.2 Common structural operations
The common engine supports:
set membership, union, intersection, and difference;
relation domain and range;
converse;
image and inverse image;
relation restriction;
structural relational composition;
bounded graph traversal;
strongly connected component detection;
revision and scope filtering;
provenance and materialization lookup.
Semantic composition is a separate Project Profile rule.
## 7.3 Relation vocabulary
The common proposal defines the algebra, not a universal engineering dictionary of relation names. A
project introduces relation kinds, source/target signatures, validators, converse display labels, semantic
composition rules, and change-impact semantics through the Project Profile.
## 7.4 Cycles
A mathematical converse loop is neutral. A temporal iteration across revisions is valid. A proof cycle
without an admissible external anchor is invalid. A prerequisite deadlock is invalid unless the Project
Profile defines explicit synchronization or joint-commitment semantics.
Cycle validity therefore depends on relation semantics and revision/time, not graph topology alone.
# 8. State consistency, data reliability, and model quality
## 8.1 Scope, revision, and time
Every semantic use is qualified by the context required by its relation family. Typical qualifiers are
scope, revision, branch/universe, time, Contract, engineering layer, Project Profile revision, and
authority domain.
Atomic changes create successor addressable universes while preserving predecessors:
Ub ,t→Ub′ ,t ′
.
Later field discovery can add previously unknown structure without rewriting the prior state.
Historical trace can therefore expand:
T r a c et
0⊆T r a c et
1
.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
## 8.2 Identity and provenance
Semantic identity and material identity are separate. A Proposition can have several materializations
and an Engineering Object can carry several Proposition revisions. Provenance records reconnect
tool/repository projections and preserve the source of candidate deltas, evidence, human inputs, and
external effects.
## 8.3 Data reliability
The model distinguishes:
structural validity;
semantic validity;
evidence sufficiency;
authority validity;
scale validity;
Contract admissibility;
information-boundary compliance;
Project Profile conformance.
A successful structural check does not imply successful semantic or evidence checks.
## 8.4 Work Product information boundary
Existence in the Solution Space does not grant permission to expose information in a Work Product:
E x ist s( x , S ol u t i o n S p a c e) ⇒ ̸Pe r mit t e d I n ( x ,W P,C) .
This protects formal structure, semantic role, intellectual property, security, safety information,
supplier data, and other project-defined boundaries.
# 9. Scale and magnification topology
Magnification and extent are separate.
M ( x ) ≈ M ( ℓ )
for objects operating at engineering layer ℓ, while the extent of a Decision, Exchange Item, or Work
Product can differ substantially.
A Decision whose blast approaches the extent of an entire layer is not automatically invalid. It is
economically suspicious because it can cause large reshuffling and rework. Such a point is a natural
place for additional economic assessment or human intervention.
Engineering layer and Contract execution sub-layer are different coordinates. A single engineering
layer can contain arbitrary Contract staging while still producing one coherent Product view at its
magnification.
Illustration - one possible scale profile. A project can define a progression such as Product
need -> use case -> system specification -> architecture -> component specification ->
implementation. In that profile, a Use Case can contain interaction steps and desired
outcomes but not detailed algorithms. Another project can define different scale frames and
permitted bridges. The illustration does not define universal engineering levels.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
# 10. Decisions, trade space, exploration, and human intervention
## 10.1 Trade space
For problem q, the Trade Space T ( q ,t ) is the project-visible region of candidate outcomes that can
currently be compared under applicable constraints, evidence, authority, and Product/Contract
objectives.
A Trade Space can contain discrete alternatives and references to continuous optimization delegated to
simulations, field tests, calibration systems, or external optimizers. Continuous parameter optimization
is not automatically Hive global search.
## 10.2 Local and global extrema
For candidate x and declared neighborhood N ( x ):
Lo c alO p t ( x ,N )⇔∄ y∈N ( x ) :B e t t e r( y , x ) .
For theoretical Solution Universe Ω:
Gl o b alO p t ( x ,Ω)⇔∄ y∈Ω:B e t t e r( y , x ) .
The Hive normally knows only a project-visible subset of Ω. A local optimum can therefore be
established relative to a declared neighborhood while global optimality remains unknown.
Extremum Exploration deliberately expands the active neighborhood or opens a materially different
trajectory to search for another local extremum or to challenge whether the current region is adequate.
It does not imply exhaustive global search.
## 10.3 Trajectories, clusters, and outliers
A trajectory is a temporally ordered path of candidate outcomes and Decisions for one problem. A
cluster is sufficiently independent support for one trajectory. Cluster power controls resource survival,
not truth.
An outlier is preserved even if it has low current support:
Ou t li e r( o)∧Dis c o v e r e d ( o) ⇒ Pr e s e r v e ( o) .
If an outlier later gains evidence, novelty value, or post-mortem relevance, it can become active
without reconstructing lost reasoning.
## 10.4 Reshuffling
Reshuffling is the reopening or reallocation of previously active solution commitments due to
propagated change. A project can represent reshuffling cost as a vector:
RC ( Δ)=( c1
,…, cn ) .
The Project Profile can map the components to review, rework, reverification, coordination, schedule
exposure, money, physical change, or other relevant costs.
The common model does not force these dimensions into one scalar.
## 10.5 Human intervention geometry
Let current Hive candidate set be B and human input normalized to set A. Human interaction can
create exact match, narrowing, broadening, equality, partial intersection, or disjoint geometry relative
to B. The human-interaction class is orthogonal to this set geometry.
Human input is assessed before execution. Human authority does not create mathematical or
engineering feasibility.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
# 11. Contracts and Product delivery
## 11.1 Contract structure
A Contract has one accountable Executor and one or more issuing parties. Supplementary parties can
be added when execution reveals new needs. Contract participation can therefore evolve by revision
without erasing prior states.
A conceptual Contract tuple is:
C=( IC
, XC
, SC
,OC
,T a r g e tC
,W PC
, RC
, AC
, EC
,T C ) ,
where IC is the issuing-party set, XC the single Executor, SC supplementary parties, OC obligations,
T a r g e tC the Product target, W PC Work Product obligations, RC Contract resource constraints, AC
acceptance rules, EC enforcement, and T C execution topology.
## 11.2 Contract decomposition
A Contract can be decomposed into child Contracts when the Product target requires separable
execution domains. Child Contracts provide complete results of their own scope. Those Work Products
become inputs to the parent execution.
Contract decomposition does not imply Hive decomposition. The same Hive can coordinate all child
Contracts while maintaining horizontal Product and Team APIs.
## 11.3 Integration and composition
Integration is project-specific. Direct integration requires compatible magnification:
I nt e g r at e ( x , y ) ⇒ M ( x ) ∼ M ( y ) .
The common algebra does not prescribe copying, aggregation, model merge, compilation, physical
assembly, packaging, or another integration strategy. Each Work Product keeps its own schema and
validation rules. Cross-scale incorporation is only allowed through a project-defined strategy that
preserves information boundaries and validation.
Integration is not aggregation.
## 11.4 Integrator Contract
When partial Work Products need to become one coherent same-scale Work Product, the parent can
create a separate Integrator Contract. The Integrator can receive multiple Work Products as a side
effect of the parent topology while remaining vertically scoped to its own Contract obligation.
The Integrator does not gain horizontal authority over child Decisions. It builds the coherent result
required by its Contract.
## 11.5 V-model verification topology
The Hive cannot both fulfill and validate the same Contract role. Production, test planning/test-suite
production, integration verification, and other required verification activities are separate Contracts
where the applicable engineering method requires that separation.
The Project Profile defines the required independence topology. It can require separate roles inside one
Hive, separate Hive instances using the same model, separate departments, separate enterprises,
different model providers, different infrastructure, or another topology.
Conformance uses a predicate rather than a universal scalar independence order:
S at isf i e sI n d e p e n d e n c e ( a c t u al ,r e q uir e d , p r o f il e) .
## 11.6 Acceptance obligations
Acceptance is a Contract obligation, not a generic lifecycle state of every Proposition. Actors whose
direct Work Products participate as inputs can receive Acceptance Obligations. Delegated/contracted
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
third parties do not automatically participate in parent Contract acceptance; the parent Executor is
responsible for accepting their Work Products into the parent execution.
The Executor controls immediate traceability quality and Known Gaps, and informs Acceptors through
a fulfilment proposal.
A conceptual fulfilment proposal is:
F PC=(W PC
,T r a c e S umma r yC
,K n ow nG a p sC
,V e ri f i c at i o n E v i d e n c eC
, S u p pl e me nt a r yC ) .
Successful Contract completion occurs when the Contract acceptance rule is satisfied. Baseline, release,
deployment, production, and other lifecycle predicates remain project-specific and are not implied by
acceptance.
## 11.7 Product API and Team API
A Product API is an Exchange Item of a project-appropriate kind that materializes an interface Decision.
Its representation depends on the Product nature.
A Team API is the set of Work Products and communications used by parties to evolve the Product.
Hive-Human communication is native to the model. External-party communication can require a
Project Profile communication Contract and can be limited to formats such as PDF, spreadsheet, email,
supplier portal, or another external boundary representation.
## 11.8 Blast containment
A Decision has direct effect only inside its local Contract and bounded Hive/Team context. Other parties
are affected only when an Exchange Item that they consume changes.
Let ChangedEI(d) be the Exchange Items updated by Decision d. Then:
A f f e c t e d (T e am,d )⇔∃ e∈C h a n g e d E I ( d ) :C o n s ume s(T e am, e) .
If a team does not consume a changed Exchange Item, that team is outside the native blast area for that
Decision.
# 12. Evidence and validation locality
Evidence is developed locally for the claim and engineering layer that requires it. Foreign evidence can
inform local evidence generation but does not automatically close a higher- or lower-scale claim.
F o r e i g n E v i d e n c e→Lo c al E v i d e n c e A c t i v it y→Lo c al E v i d e n c eO b j e c t .
Lo c al E v i d e n c eO b j e c t →Lo c al J u st i f i c a t i o n .
This prevents evidence laundering across scale or authority boundaries.
Verification and validation methods remain Project Profile and domain-method concerns. Test
existence alone does not prove the tested claim. Applicable observability, reachability,
representativeness, independence, and acceptance rules determine evidence value.
# 13. Maturity, prescriptiveness, and brittleness
Maturity in this proposal is not a separate Acceptance state. It describes deliberate prescriptiveness and
design-space reduction at a specific authority boundary.
A mature high-level Proposition can remain coarse when lower-level freedom is intentional. A detailed
prescription can also be mature when the authority has evidence and reason to constrain that
dimension.
Brittleness is separate from prescriptiveness. Let ΔP
( p) be the declared Revision Envelope for
Proposition p. A project can define:
Brit t l e ( p , Δ,Θ)
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
when a change inside the expected revision environment creates repair cost above threshold Θ or
violates another Project Profile brittleness rule.
# 14. UNKNOWNs, Gaps, and Future Actions
UNKNOWN and Gap are explicit semantic states, not missing text placeholders.
A known gap with a valid contracted Future Action can remain in an accepted Work Product when the
Contract acceptance rule allows it. A Future Action contains at least:
F A=( Pa rt y ,Ou t c ome , M e t h o d , D o R , D o D) .
A foreign unknown does not automatically trigger unlimited recursive investigation. Materiality to
current commitment determines whether it blocks progression.
# 15. Recursive Y/V architectural model
The recursive Y/V model reconciles negotiable and fixed-horizon sources at every engineering
magnification.
The left branch contains sources that can be negotiated within the current horizon, such as Product
requests, UX findings, business choices, or lower-cost design alternatives. The right branch contains
sources treated as fixed at that horizon, such as applicable law, established natural constraints, already
committed high-cost manufacturing, or other non-negotiable obligations.
The center reconciles contradictions and produces a feasible region. Engineering realization then
generates evidence, deficiencies, and Product feedback that can reopen the appropriate negotiable side.
The same pattern can recur at Product, system, subsystem, component, implementation,
manufacturing, deployment, or another Project Profile layer.
# 16. Supporting processes over Solution Space
Configuration Management, Change Management, Problem Resolution, Quality Assurance, Risk
Management, Measurement, release management, production control, and similar disciplines operate
over Solution Space entries and Engineering Objects.
They are supporting processes, not universal semantic primitives. A Baseline, for example, exists only
where Configuration Management establishes it. A production batch can be accepted without becoming
a Baseline. Software can pass acceptance testing before deployment, while production deployment
performs only project-defined sanity checks.
Supporting-process predicates remain Project Profile parameters unless a Contract or applicable
external norm makes them obligatory.
# 17. Swarm exploration, divergence, waste, and resource control
## 17.1 Resource Envelope
The proposal does not use the phrase bounded resources as an undefined scalar. A Resource Envelope
is a vector of declared availability or limits:
R=(r1
,…,rn ) .
The Project Profile names the dimensions. Typical dimensions include context, model calls, compute,
wall time, money, human effort, energy, equipment, and external capacity.
A Contract can define a narrower Resource Budget inside the project/Hive envelope.
## 17.2 Resource survival
Candidate trajectories are rated using project-defined functions. Relevant inputs can include
independent support, evidence strength, novelty, progress, Product/Contract value, repair cost,
divergence persistence, and Resource Cost.
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
A trajectory can be strengthened, maintained, reduced, or deactivated. Deactivation stops active
expenditure; it does not delete discovered outcomes.
## 17.3 Waste and overthinking
Waste is not synonymous with overhead. Required verification, governance, communication, or setup
can consume resources without being waste.
Waste occurs when an operation produces neither required process effect nor reusable progress,
evidence, knowledge, or Product value. Polling loops, repeated context replay, unnecessary status
messages, redundant branch reasoning, and reasoning about deterministic facts are candidate waste
categories when the project can establish that they add no required effect.
Overthinking is a reasoning-specific waste mode. The Hive Mind should first ask whether deterministic
algebra, an existing Decision, recorded evidence, or a previously preserved outcome already resolves
the question before allocating another reasoning trajectory.
## 17.4 Divergence and post-mortem
Divergence is measured as reconciliation/repair difficulty, not semantic-text distance alone. The project
can use a vector such as:
R e p air=( c1
,…, cn ) .
The Project Profile can map the components to money, time, Hive utilization, Work Product rework,
physical rework, schedule exposure, or other relevant repair costs.
Persistent incompatible trajectories can lose active resource allocation. A post-mortem preserves useful
findings and can reactivate an outlier or create a new trajectory.
Contract divergence is different. A Contract is not restarted. At critical divergence, Human intervention
can occur. If the Contract remains inside its Resource Budget and authority envelope, the Hive can
revise or re-create the execution topology after post-mortem analysis while preserving the historical
Contract state.
# 18. Derived no-sphere theorem
Theorem NS-1 - No authority/evidence sphere. Assume AX-1 through AX-4, local Decision blast,
Exchange Item boundary materialization, and local evidence generation. Then a Decision at one
engineering layer cannot directly establish a binding or evidenced Proposition at a non-local layer
merely through graph reachability.
Every traversed boundary requires the Project Profile’s allowed bridge, materialized information, local
interpretation, and applicable evidence/authority checks.
The theorem allows information to cross boundaries while preventing authority and evidential closure
from propagating automatically.
Part V - Conformance and Project Profile
# 19. Conformance
Conformance is evaluated against the common proposal plus the applicable Project Profile revision.
A conformant implementation MUST:
preserve Proposition and Engineering Object distinction;
validate relation use before semantic justification;
preserve unresolved required information explicitly;
enforce scale/bridge rules;
enforce Human ingress and Decision authority rules;
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
preserve all discovered outcomes while controlling active resource allocation;
separate Decision authority from Exchange Item communication;
enforce Contract accountability, Work Product schemas, information boundaries, and acceptance
obligations;
satisfy required verification independence topology;
preserve revision/time history;
keep project-specific lifecycle/support-process predicates in the Project Profile unless the common
model explicitly defines them.
A conformance claim MUST identify the model version, Project Profile revision, checker/review
method, and evidence set.
# 20. Project Profile
The Project Profile defines at least the parameters that are required by the project:
Product boundaries and engineering magnification layers;
Proposition roles and Engineering Object families;
relation vocabulary, signatures, converse labels, validators, and semantic composition rules;
scale compatibility and permitted bridges;
Contract parties, authority, human Decision scopes, enforcement, and Contract resource models;
Work Product schemas, semantic-role constraints, required validators, information-exposure policies,
and acceptance rules;
Product API representations and Team API communication rules;
Trade Space representation, trajectory rating, cluster independence, outlier policy, repair-cost model,
deactivation and post-mortem criteria;
Resource Envelope dimensions, measurement rules, invention allocations, and waste classification;
validation/verification independence topology;
Evidence rules, UNKNOWN materiality, Gap and Future Action policy;
supporting-process predicates such as Configuration Management, Change Management, baseline,
release, deployment, production, risk, and quality rules;
lifecycle labels for Decisions, Engineering Objects, Work Products, Contracts, and other project
elements;
external-party communication constraints and permitted formats;
integration/composition strategies and their validation requirements.
# 21. Formal model audit
Each Foundation Axiom has a defined Intent, Statement, Boundary, and Validation argument. A release
audit SHOULD test at least the following countermodels:
AX-1: Arbitrary graph path used as valid engineering trace
AX-2: Hidden or fabricated completion replaces unresolved information
AX-3: Local Decision/evidence becomes remote authority without a bridge
AX-4: Universal human approval or unauthorized Hive commitment
AX-5: Low-support discoveries are deleted or active search consumes unlimited resources
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
The audit also checks term uniqueness, Proposition/Engineering Object separation, Work Product
information boundaries, Project Profile scoping, relation-role typing, revision/time qualification, and
conformance-test evidence.
Part VI - References and supporting material
# 22. Language and terminology references
The following references define the proposal’s language and terminology foundation:
ASD-STE100, Simplified Technical English, Issue 9, January 2025. https://www.asd-ste100.org/
BCP 14: RFC 2119 and RFC 8174. https://www.rfc-editor.org/info/bcp14/
ISO 24495-1:2023, Plain language - Part 1: Governing principles and guidelines.
https://www.iso.org/standard/78907.html
ISO 704:2022, Terminology work - Principles and methods. https://www.iso.org/standard/79077.html
ISO/IEC Directives, Part 2, Principles and rules for the structure and drafting of ISO and IEC documents.
https://www.iso.org/directives-and-policies.html
ASD-STE100 applies to project-authored prose throughout the proposal. BCP 14 applies only to technical
normative keywords as defined in Section 4.2.
# 23. Formal-knowledge representation references
The proposal uses the following specifications as design references, not normative dependencies:
OpenMath Standard 2.0r2 and Content Dictionaries - semantic representation of mathematical objects,
symbols, Commented Mathematical Properties, and Formal Mathematical Properties.
https://openmath.org/standard/om20-2019-07-01/
TPTP Language - annotated formula roles including axiom, hypothesis, definition, assumption, lemma,
theorem, corollary, conjecture, and type. https://tptp.org/UserDocs/TPTPLanguage/TPTPLanguage.shtml
OMDoc - document/theory-level distinction among axioms, definitions, assertions/theorems, proofs, and
related mathematical statements. https://www.omdoc.org/
SMT-LIB 2.7 - rigorous common languages and background theories for solver interaction. https://smt-lib.org/language.shtml
The proposal adopts the distinction between expression syntax and statement role. It does not require
serialization in OpenMath, TPTP, OMDoc, or SMT-LIB.
# 24. Supporting AI architecture references
The following sources are illustrative/supportive only:
OpenAI Agents SDK, agent orchestration, manager/agents-as-tools and handoff patterns.
https://openai.github.io/openai-agents-python/multi_agent/
CrewAI Crews, role-bearing agents, tasks, processes, manager and memory concepts.
https://docs.crewai.com/en/concepts/crews
AutoGen/ConversableAgent message-based agent communication.
https://microsoft.github.io/FLAML/docs/reference/autogen/agentchat/conversable_agent/
Tree of Thoughts: Deliberate Problem Solving with Large Language Models, NeurIPS 2023.
https://papers.nips.cc/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html
Graph of Thoughts: Solving Elaborate Problems with Large Language Models, AAAI 2024.
https://ojs.aaai.org/index.php/AAAI/article/view/29720
Draft 0.9 - project review; supporting external references are non-normative unless made applicable by Project Profile.
# 25. Supporting engineering references
Engineering standards and frameworks remain supportive/non-normative in this common proposal
unless a Project Profile makes them applicable. Examples include Automotive SPICE, APQP, ISO 26262-
family standards, INCOSE requirements guidance, NASA systems/software engineering guidance, and
project-specific V-model processes.
# 26. Project supporting material
The following project material informed this revision:
harness-hive-dialogue-recap.md - non-normative recap used to restore the state-centric Hive
architecture, bounded traversal, trade-space, trajectory, cluster, repair-cost, and non-actor design
direction. Later accepted decisions in this proposal take precedence where the recap is older.
resource_consumption_recap.md - decision recap for context/input, orchestration, polling waste, and
root/sub-agent resource use.
session_resource_analysis.xlsx - supporting workbook containing summary, category, phase, waste,
support, agent, sub-agent, timing, session, and daily pivots.
Compilation status
Draft 0.9 performs a structural rewrite rather than a local patch. It introduces formal definitions for
Hive, Swarm, Hive Mind, Product, Reshuffling, Waste, Resource Envelope, Extremum Exploration,
Proposition, Engineering Object, and formal statement roles. It moves algebra and Human ingress
definitions before the Foundation Axioms; rewrites AX-5 to preserve every discovered outcome while
rating active resource allocation; restores trade-space and trajectory concepts; separates the non-specialist proposal from the formal operational model; and places the operational chapters under one
Formal Proposal umbrella.
Review assumption. This draft distinguishes Hive (persistent problem-local semantic/governance
computation) from Swarm (transient execution population). This distinction is used consistently in
Draft 0.9 but remains the one terminology choice that requires project confirmation; if Hive and Swarm
are intended as exact synonyms, the Abstract and Dictionary need a controlled collapse.
