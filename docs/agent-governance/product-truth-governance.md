# Product Truth Governance

## Purpose

This document defines the global product-truth and specification-governance
contract for AI-assisted product work.

Its purpose is to make product understanding the primary output of product
development, keep specifications authoritative without making them
infallible, preserve accepted and released behavior, and prevent agents from
turning guesses or implementation convenience into product policy.

The specification system is the project's primary product artifact. Code,
design, QA, runtime behavior, and release records remain mandatory parts of the
truth system because they establish realization, structure, observed behavior,
acceptance, and compatibility.

Code is an implementation of product understanding. It is not a substitute for
that understanding.

## Activation and reading boundary

This contract applies to work that investigates, defines, changes, implements,
reviews, or verifies any of the following:

- user-visible behavior;
- product or feature state;
- actions, transitions, effects, and lifecycle rules;
- UX, visual behavior, information architecture, or interaction;
- routes, public data contracts, permissions, eligibility, persistence, or
  compatibility;
- behavioral defects or regressions;
- product QA, acceptance scenarios, or release behavior;
- transfers, ports, rewrites, or migrations of an existing product.

The primary single agent reads this entire document before product action.

For a persistent product goal, the coordinating /root reads this entire
document and carries its accepted state in the goal model.

An authority explorer, specification integrator, reconciliation owner, or
contract reviewer reads this document when its packet gives it one of those
roles.

Implementation, build, test, and runtime workers do not need this whole
document merely because their output affects a product. They receive the finite
Contract Change Envelope, pinned clauses, evidence paths, protected boundaries,
and acceptance conditions required by their packet. This keeps their context
focused and prevents them from reinterpreting the whole product.

Purely mechanical, proven behavior-neutral, infrastructure-only, or
non-product documentation work does not require the full protocol. If
behavioral impact is uncertain, the protocol applies.

Project instructions may add domain-specific evidence, paths, safety rules, and
stronger acceptance requirements. They do not weaken this contract unless the
user explicitly changes the governing rule for that project or task.

## Core principle

The specification system is the canonical statement of intended product
behavior.

Canonical does not mean infallible. A specification can be incomplete, stale,
ambiguous, internally inconsistent, incorrectly transcribed, or based on
evidence that later proves inapplicable.

No specification file is self-authorizing. Editing a specification does not by
itself create legitimate product intent.

Applicable implementation source, design, QA, runtime, history, and release
evidence must be reconciled with the specification before a non-trivial
product implementation or user decision.

Those layers answer different questions. They are not a flat vote and must not
be treated as interchangeable authorities.

## Product truth system

The product truth system contains these layers.

| Layer | Primary question |
| --- | --- |
| User objective or decision | What product change is authorized now? |
| Active product contract | How should the product behave? |
| Design and product model | How is that behavior expressed structurally and visually? |
| Implementation source | How is it currently realized, and who owns it? |
| Runtime behavior | What does the product actually do in the relevant state? |
| QA and acceptance evidence | Which action, state, and result chains have been verified? |
| Release baseline | Which behavior may users or consumers already rely on? |

The user objective opens a bounded change domain.

The active contract supplies intended behavior inside and outside that domain.

Design and source establish current component, state, ownership, and mechanics
evidence. In a faithful transfer task, the user objective may explicitly make a
named donor implementation and its behavior part of the normative transfer
basis.

Runtime distinguishes executable behavior from dead, stale, incomplete, or
misread source.

QA establishes acceptance evidence and repeatable behavior chains. It does not
create product intent merely because a test already exists.

A release baseline protects compatibility and user expectations. It does not
freeze a product forever; it makes change and migration explicit.

## Specification system

A mature specification system is a linked package, not necessarily one large
Markdown file.

It normally contains:

1. a product contract;
2. a design or product-model contract where structure or visual behavior is
   product-significant;
3. an evidence map pointing to source, design, runtime, history, and external
   authority;
4. an acceptance map linking behavior to QA scenarios.

The product contract remains the normative center. It should contain:

- product goal and vocabulary;
- scope and non-goals;
- user-visible behavior;
- states, actions, transitions, and effects where they affect the product;
- invariants;
- edge cases and failure policy;
- route, data, persistence, permission, and compatibility implications;
- cross-domain dependencies and precedence;
- unresolved product unknowns;
- acceptance scenario identifiers.

Deep implementation details belong in the evidence or ownership map unless the
detail itself preserves a required product rule.

Use stable domain and clause identifiers. Agents should be able to receive the
smallest governing slice by ID instead of loading an entire large
specification.

A path, heading, line number, or recent date is not a durable substitute for a
stable clause identifier.

## Product domains

A product domain is a named responsibility boundary whose behavior can be
reasoned about and protected independently.

A domain may be a feature, shared service, platform contract, data contract,
account or access lifecycle, playback policy, or another stable product
responsibility.

The project specification registry should record:

- domain identifier;
- governing contract;
- authority status;
- stability status;
- when to read it;
- precedence over overlapping contracts;
- named upstream or shared dependencies;
- latest accepted or released baseline.

A source file is not automatically a product domain. One shared source owner
may implement several domain contracts, and one domain may span several source
owners.

Changing a shared source path does not authorize changing every consumer's
behavior.

## Authority and stability are separate

Every contract has an authority status and every governed domain has a
stability status.

### Authority status

Draft means the contract is incomplete or awaiting a decision. It is evidence,
not implementation authority.

Active means the contract is the current normative statement of intended
behavior.

Superseded means a named newer contract has replaced it.

Historical means it is retained only as context.

### Stability status

Evolving means the domain is intentionally being designed or materially
changed.

Accepted means implementation and applicable QA have been accepted. Incidental
semantic changes are forbidden even if the product has not yet been publicly
released.

Released means the domain is included in a public build, production deployment,
published API, or another externally consumable release baseline.

Deprecated means the contract remains supported for a defined compatibility
period while replacement or removal is planned.

Authority answers which contract governs.

Stability answers how strongly existing behavior is protected.

An Active contract may be Evolving, Accepted, Released, or Deprecated.

## Release baselines

Released behavior must be explicit rather than inferred from a branch name,
green tests, an Active label, or the existence of code.

A release contract baseline records:

- release, build, deployment, or API version identifier;
- release date;
- implementation revision;
- specification revision or contract epochs;
- included product domains and clauses;
- acceptance and QA evidence;
- compatibility or migration notes;
- known exclusions or residuals.

A public deployment or distributed build without a historical baseline is
treated conservatively as legacy-released. Its observed behavior, applicable
specifications, user-facing design, and QA are protected evidence until they
are reconciled into an explicit baseline.

An explicit user request to change a released domain is change authority for
the behavior actually named. It does not automatically authorize unrelated
breaking changes or changes to adjacent released domains.

## Change modes

Every covered task has exactly one primary change mode before implementation.

### Restore

Use Restore when the task is to implement or repair an already established
contract.

Expected behavior comes from the active contract and applicable accepted or
released baseline.

Implementation and QA may change to restore that behavior.

Semantic specification change is normally forbidden. Editorial clarification
or a separately accepted reconciliation may still occur.

### Reconcile

Use Reconcile when the task is to align the specification system with the
complete, already existing product truth.

This is the normal mode for faithful transfers, ports, brownfield
contract renewal, and correction of stale or incomplete specifications.

Reconciliation may update the contract without asking the user when:

- the user objective authorizes fidelity, transfer, restoration, or
  reconciliation in the named domain;
- the smallest complete applicable evidence set has been inspected;
- the evidence converges on one existing product behavior or ownership model;
- no new product alternative is invented;
- no protected adjacent domain is semantically changed;
- the result receives the required independent review.

Reconciliation is not redesign.

### Evolve

Use Evolve when the user requests a new feature or a semantic change to a named
domain.

The request itself opens that domain and behavior for change. Do not repeatedly
ask the user to authorize direct, evidence-backed consequences of the request.

Update the product contract before implementation.

Existing source, design, QA, runtime, and release evidence still constrain
ownership, compatibility, migration, and adjacent behavior.

Ask the user only when a material unresolved fork remains or continuation
would change a protected domain outside the envelope.

### Discover

Use Discover when the relevant contract is absent or known to be unreliable
and the task is to understand the product.

Record the missing or unreliable contract before broad evidence inspection.

Inspect source, design, routes, state, QA, runtime, history, and released
behavior as evidence.

Separate observed behavior from intended behavior.

Produce a first-pass contract, evidence map, unknowns, and decision list.

Do not change product implementation during a discovery-only task unless the
user separately authorizes implementation.

### Behavior-neutral

Use Behavior-neutral only when observable behavior is proven not to change.

Examples may include formatting, comments, mechanical renames with complete
consumer updates, or internal cleanup whose behavioral equivalence is
demonstrated.

If impact becomes uncertain, reclassify the task before continuing.

Behavior-neutral must not be used to bypass contract review for a refactor that
changes ownership, state, timing, persistence, compatibility, or observable
results.

## Contract Change Envelope

Before product implementation, establish a Contract Change Envelope.

For a small single-agent task it may appear in a visible progress update.

For a persistent, multi-agent, long-running, released, or cross-domain task it
must be a durable artifact or registry record.

Use this minimum structure:

~~~text
Contract Change Envelope
- Task:
- Change mode:
- User-authorized outcome:
- Authorized domains:
- Authorized clauses:
- Protected adjacent domains:
- Shared owners that may be touched without changing consumer behavior:
- Authority status:
- Stability or release baseline:
- Required evidence:
- Allowed specification delta:
- Forbidden specification delta:
- Material decisions requiring the user:
- Current contract revision or epoch:
- Required review and QA:
~~~

The envelope describes authority, not merely file scope.

Writable paths are additional implementation constraints. They cannot enlarge
the product domain.

The initial envelope is derived from the user's actual request, governing
contracts, and explicit accepted decisions. Do not make it broader because a
broader refactor appears convenient.

If a newly discovered dependency requires semantic change outside the
envelope, return or record that exact dependency. Do not silently expand the
task.

## Interpreting user change authority

The user's request is direct product-change authority for the domain and
behavior it actually names.

Examples:

- Fixing a defect normally authorizes Restore, not a redesign.
- Faithfully transferring an existing feature normally authorizes Reconcile
  against the complete named source product.
- Redesigning onboarding authorizes Evolve for onboarding behavior and design,
  not unrelated billing or account-deletion policy.
- Replacing a shared implementation owner may be allowed while every
  out-of-scope consumer contract remains protected.
- Improving an entire named domain may authorize broad internal change inside
  that domain, but material changes to public data, compatibility, or adjacent
  domains still require explicit coverage.

Do not ask for a second permission that the user has already clearly granted.

Do not infer authority for a materially different product from a broad verb
such as improve, clean up, modernize, or optimize when the affected behavior is
not otherwise named.

## Provisional and final Spec Basis

Spec-first has two deliberate stages.

### Provisional basis

Read the active registry and smallest governing contract slice first.

State:

- current intended behavior;
- invariants and protected boundaries;
- apparent gaps or conflicts;
- task change mode;
- evidence required to test completeness;
- whether implementation is provisionally authorized.

The provisional basis frames the investigation. It is not permission to stop
at the specification and treat every mismatch as a user decision.

### Evidence reconciliation

Inspect the smallest complete applicable evidence set.

Depending on the task, it may include:

- current and donor implementation source;
- ownership and dependency paths;
- design contracts and references;
- tests and QA action-state-result chains;
- runtime behavior in the relevant states;
- release records and deployed behavior;
- history that explains removal, replacement, or stale evidence;
- platform or external contract documentation.

Do not sample only the artifact that supports the easiest conclusion.

Do not perform a broad audit when a bounded evidence slice can settle the task.

### Final reconciled basis

Classify every material discrepancy, accept the authorized contract delta, and
state the final basis before implementation.

The final basis contains:

- governing clauses and revision;
- resolved intended behavior;
- accepted evidence and its role;
- discrepancy dispositions;
- accepted contract delta;
- remaining protected boundaries;
- implementation authorization;
- required acceptance scenarios.

## Discrepancy classification

Every material mismatch belongs to one of these classes.

### Implementation defect

The active contract and applicable baseline remain correct, while source or
runtime differs.

Restore the implementation. Do not rewrite the contract to match the defect.

### Specification defect or omission

The contract is incomplete, stale, incorrectly transcribed, or internally
inconsistent, and accepted evidence plus the task authority establish one
existing intended behavior.

Use Reconcile. Correct the contract before implementation and record the
evidence basis.

### Stale or inapplicable evidence

A test, QA case, design artifact, historical source, comment, fixture, or
runtime observation no longer governs the task.

Disposition it explicitly. Do not change current product behavior merely to
satisfy stale evidence.

### Authorized product evolution

The user request intentionally changes behavior inside the open domain.

Update the contract first, record compatibility impact, then update
implementation and QA.

### Real product fork

After complete applicable evidence reconciliation, two or more materially
different valid outcomes remain and the user's request does not choose among
them.

Present the user with the concrete alternatives, evidence, consequences,
recommended option, and affected domains.

### External authority blocker

Continuation requires credentials, destructive action, provider or store
authority, legal or policy input, physical-device access, or another decision
outside agent authority.

Record the exact blocked slice. Continue unrelated authorized work when safe.

## Specification mutation authorization

A semantic specification edit requires an external change basis.

Accepted bases are:

- an explicit user request or decision;
- an accepted Contract Change Envelope for Evolve;
- an accepted Reconcile result for a faithful transfer, restoration, or
  contract-renewal task;
- explicit precedence from a higher-ranked active contract;
- correction of a proven internal contradiction without introducing new
  product behavior.

Current implementation alone is not a sufficient semantic change basis.

A current test alone is not a sufficient semantic change basis.

An agent preference, platform convention, implementation convenience, popular
pattern, or plausible guess is not a change basis.

The specification edit itself is never a change basis.

Do not:

1. invent behavior;
2. write it into the specification;
3. cite the edited specification as authority;
4. implement it;
5. call the result spec-compliant.

That sequence is circular self-authorization and is forbidden.

## Classes of specification change

### Editorial clarification

Changes wording, organization, links, or terminology without changing
observable behavior, compatibility, ownership responsibility, or acceptance.

It may be performed within assigned paths. If semantic impact is disputed,
reclassify it.

### Reconciliation delta

Corrects or completes the contract to describe one established product truth
under Reconcile authority.

It requires evidence, an explicit before-and-after delta, and review that no
redesign or cross-domain change was hidden inside it.

### Scoped evolution delta

Changes intended behavior inside the user-opened domain.

It requires an updated contract, compatibility assessment, updated acceptance
mapping, and implementation review.

### Protected or breaking delta

Changes an Accepted, Released, Deprecated, public, cross-domain, persistent
data, route, API, permission, or shared-consumer contract outside the existing
envelope.

It requires explicit user authority unless the original request already names
that exact change.

## Contract Delta

Every semantic change records a compact Contract Delta.

~~~text
Contract Delta
- Change ID:
- Change mode:
- Authorized by:
- Domain and clause IDs:
- Previous behavior:
- New or reconciled behavior:
- Evidence basis:
- Compatibility classification:
- Adjacent domains checked:
- QA and design impact:
- Specification paths changed:
- Independent review:
- New contract revision or epoch:
~~~

Git history is useful evidence but is not a substitute for this reasoning.

Keep the normative contract readable. Put hashes, raw captures, long source
inventories, and mechanical proof in the evidence map or QA artifacts.

## Cross-domain and shared-owner discipline

Product scope and source scope are different.

A task may need to modify a shared source owner while preserving every
out-of-scope consumer's behavior.

Before changing a shared owner:

- identify its product domains and real consumers;
- name the authorized consumer behavior;
- name the protected consumer behavior;
- preserve public and released contracts outside the envelope;
- verify the affected consumers in proportion to risk.

A technical dependency does not automatically open a product dependency.

If the required change would alter an adjacent protected contract, return the
exact semantic dependency to the primary agent or /root.

Do not create parallel state, duplicated services, fallback models, or
temporary product rules merely to avoid the dependency.

## When to ask the user

Ask the user for a product decision only after the smallest complete applicable
evidence pass proves one of the following:

- authoritative product contracts materially conflict without precedence;
- required behavior is absent from all applicable authority and evidence;
- multiple valid outcomes would materially change the product;
- the change crosses a protected domain outside the authorized envelope;
- compatibility or migration consequences are material and not covered by the
  request;
- continuation requires external authority.

Do not ask because:

- one specification line appears inconsistent before source and QA have been
  inspected;
- the primary agent's current context lacks a fact that a scoped evidence
  worker can obtain;
- an implementation detail has several equivalent forms;
- the user already authorized the named domain change;
- the agent invented alternatives unsupported by the product;
- asking is easier than completing reconciliation.

When asking, explain:

- the exact unresolved rule;
- every source inspected;
- why the conflict is real rather than provisional;
- user-visible and compatibility consequences;
- the recommended option and why;
- which work remains independent of the decision.

## Agent roles

### Primary single agent

For a bounded product task without a persistent goal, the primary agent may
perform the sequence itself.

It still establishes the envelope, performs the evidence pass, records any
semantic delta, implements only after final reconciliation, and verifies the
result.

### Coordinating /root

For a persistent product goal, /root:

- preserves the user objective and change envelope;
- tracks domain protection and contract epochs;
- dispatches finite evidence, specification, implementation, review, build,
  and QA packets;
- reconciles accepted receipts;
- asks the user only after accepted evidence proves a real decision;
- prevents stale packets from being accepted;
- records terminal state.

/root remains coordinator-only under root-orchestration.md.

### Authority or evidence explorer

An explorer:

- reads only the assigned authority and evidence;
- identifies ownership and action-state-result chains;
- classifies evidence without changing product intent;
- returns discrepancies and exact dependencies;
- does not edit the specification unless separately assigned as its owner.

### Specification or reconciliation owner

A specification owner:

- receives the accepted change mode and envelope;
- edits only named domains and clauses;
- preserves protected contracts;
- records the Contract Delta;
- does not implement product code unless the task is explicitly single-agent;
- stops on a material unresolved fork.

### Implementation owner

An implementation owner:

- receives a pinned final contract basis;
- reuses canonical owners;
- implements only the assigned outcome;
- does not reinterpret or broaden the contract;
- does not edit specifications unless its packet explicitly grants that role;
- returns a discrepancy instead of working around missing authority.

### Contract reviewer

A reviewer checks:

- the change basis is external and legitimate;
- the change mode is correct;
- the specification delta stays inside the envelope;
- protected adjacent domains remain unchanged;
- source, design, and QA evidence were interpreted consistently;
- implementation realizes the pinned contract;
- no invented behavior was laundered through the specification.

The reviewer returns accept, accept_with_residual, or reject.

### QA and runtime owner

A QA owner verifies exact action-state-result chains against the pinned
contract.

It does not weaken expectations to make the implementation pass.

It classifies failures as implementation defect, stale QA, environment
residual, contract discrepancy, or authorized evolution dependency.

## Product worker packet

Every product worker packet includes:

- packet ID and finite objective;
- change mode;
- authorized domains and clause IDs;
- protected adjacent domains;
- pinned contract revision or epoch;
- exact authority and evidence paths;
- accepted prior decisions;
- permitted specification delta, if any;
- canonical owners to reuse;
- writable and forbidden paths;
- required behavior and invariants;
- forbidden inventions;
- required checks or evidence;
- discrepancy and stop conditions;
- terminal receipt format.

The worker receives the smallest sufficient context.

Do not pass the complete root conversation merely to make a packet
self-contained.

## Contract revisions and epochs

Every packet that can affect product behavior is pinned to a contract revision
or epoch.

A revision may be represented by a Git commit, blob hash, content digest,
monotonic contract epoch, or another durable project-defined identity.

Stable clause IDs identify the governed slice. The revision proves which
meaning of those clauses the worker used.

An accepted semantic contract change advances the affected epoch.

After an epoch change:

- identify every open packet using affected clauses;
- revalidate it against the new contract or retire it;
- do not accept implementation or QA receipts produced against stale meaning;
- leave unaffected domain packets active when their clauses and dependencies
  did not change.

Editorial changes need not advance the semantic epoch when independent review
confirms that meaning is unchanged.

For a long-running goal, the restart-safe registry records contract epoch per
packet.

## Design integration

When visual or interaction behavior matters, design is part of the
specification system rather than decoration applied after implementation.

The product contract should define:

- user-visible zones and responsibilities;
- meaningful component relationships;
- visible states and transitions;
- required adaptations;
- accessibility and input invariants;
- acceptance scenario IDs.

The design evidence map should point to:

- canonical design references;
- source component and style owners;
- viewport and product state;
- dynamic visibility and state provenance;
- visual QA evidence.

Do not use a generated concept, screenshot, platform convention, or existing
component library to invent product behavior absent from the change envelope.

Do not reduce a structural or state discrepancy to a cosmetic patch.

## QA integration

QA is an executable or observable extension of the contract.

Each material behavior should map to one or more stable scenarios containing:

- preconditions;
- user actions;
- state transitions;
- intermediate visible results where material;
- final visible or data result;
- failure and recovery behavior;
- platform or compatibility conditions.

Tests and QA do not define intent independently. They verify a pinned contract.

When implementation, contract, and QA disagree:

1. do not edit whichever artifact is easiest;
2. classify the discrepancy;
3. establish the legitimate change basis;
4. update the contract first when intent changes;
5. update implementation and QA from the accepted delta.

A green suite cannot authorize a product change or prove an unexercised user
journey.

Runtime and visual evidence cannot be replaced by unit tests when the contract
requires observable behavior.

## Faithful transfer profile

A faithful transfer, port, or rewrite is normally Reconcile, not greenfield
design.

The user request establishes the named source product as transfer authority
within the declared target and adaptation boundaries.

The evidence set should include, as applicable:

- source product specifications;
- executable source and ownership structure;
- design and style ownership;
- QA action-state-result chains;
- real source-product runtime behavior;
- current target implementation and canonical owners;
- historical evidence needed to distinguish current from stale behavior;
- explicit target-platform adaptations.

The target specification is read first to frame the transfer, then corrected or
completed from the accepted source-truth packet before target implementation.

Do not:

- treat a provisional target-spec mismatch as an immediate user decision;
- sample only source snippets that support the current target;
- invent target alternatives when the source product already resolves them;
- copy browser or platform mechanics as product behavior;
- create parallel target models to avoid transferring source ownership;
- call a partial component or state transfer faithful.

Ask the user only for a real unresolved product or adaptation fork after the
complete applicable source-truth pass.

## Behavioral defect profile

For a behavioral defect:

1. establish the current active and accepted or released contract;
2. reproduce or otherwise establish actual behavior when feasible;
3. inspect the owning source and relevant QA;
4. classify the discrepancy;
5. use Restore when the contract remains correct;
6. use Reconcile when the contract was proven stale or incomplete;
7. use Evolve only when the user requested new behavior.

Do not convert a bug into a specification change merely because changing the
test or contract is easier than fixing the implementation.

## Brownfield profile

A brownfield product may lack reliable specifications.

Do not pretend an incomplete first-pass specification is already complete
authority.

Use Discover to record:

- observed domains and owners;
- existing public or released behavior;
- source and runtime evidence;
- QA coverage;
- contradictions and unknowns;
- provisional intended behavior;
- decisions that genuinely require the user.

After the first-pass contracts and domain registry exist, subsequent slices use
Restore, Reconcile, or Evolve.

Legacy public behavior is compatibility evidence, not automatic proof of ideal
intent.

## Proportionality

The protocol is risk-proportionate.

A small isolated behavior change may express its envelope and final basis in a
short progress update and use focused source and QA evidence.

A long-running, multi-agent, cross-domain, security-sensitive, data-contract,
released, migration, or UI transfer task requires durable artifacts, pinned
revisions, independent review, and applicable runtime or visual QA.

Do not create a large audit project for a bounded question.

Do not skip evidence or review merely to save tokens. Quality, product
continuity, and truthful acceptance have priority over token usage.

## Minimum project artifacts

A project with product behavior should provide:

1. a specification registry;
2. active product contracts;
3. domain and precedence mapping;
4. applicable design or product-model contracts;
5. evidence and ownership maps for complex domains;
6. QA or acceptance scenario mappings;
7. durable change envelopes for long-running work;
8. release contract baselines for released behavior.

The project may choose its paths, but the concepts must remain distinct.

A recommended specification-registry table is:

~~~text
contract | domain | authority | stability | read when | precedence | baseline
~~~

Project AGENTS files should route agents to these artifacts and add local
constraints. They should not duplicate or weaken the global doctrine in many
slightly different forms.

## Restart and context compaction

After a restart, resume, clear, or context compaction, the primary agent or
/root re-reads:

- applicable global and project instructions;
- this document for covered product work;
- the user objective;
- the current Contract Change Envelope;
- the project specification registry;
- exact governing clauses;
- current contract epochs;
- accepted Contract Deltas and unresolved discrepancies;
- only the action-specific evidence and QA instructions needed next.

A chat summary, agent list, remembered decision, old receipt, or green build
does not replace those artifacts.

Workers do not reconstruct authority from conversation history. They use their
pinned packet.

## Completion

A product task is complete only when:

- the authorized product outcome is explicit;
- the final reconciled contract basis is current;
- every semantic specification change has a legitimate change basis;
- implementation matches the pinned contract;
- protected adjacent domains remain preserved or explicitly dispositioned;
- applicable independent review is accepted;
- applicable build, test, runtime, visual, and compatibility evidence is
  terminal;
- QA mappings reflect the accepted behavior;
- release baseline changes are recorded when a release occurred;
- no stale-epoch packet is being treated as accepted;
- remaining residuals are explicit and truthfully classified.

Do not report completion merely because the code compiles, tests pass, the
specification was edited, or the current context is nearly exhausted.

## Forbidden patterns

The following patterns are forbidden:

- spec-only reasoning that refuses to inspect required product evidence;
- code-first product invention followed by a retroactive specification;
- editing a specification to make an implementation appear compliant;
- treating a stale test as product authority;
- treating current code as intended behavior without reconciliation;
- escalating provisional discrepancies to the user before evidence closure;
- asking the user to choose among agent-invented alternatives;
- changing a protected adjacent domain because the same source file is shared;
- accepting implementation against a stale contract epoch;
- hiding a semantic change under behavior-neutral cleanup;
- rewriting QA expectations solely to obtain a green result;
- using an Active label as proof that behavior is released;
- using a release as an excuse to make an explicitly authorized domain
  impossible to evolve.

## Compact discrepancy receipt

Use this minimum form for a bounded discrepancy:

~~~text
Discrepancy Receipt
- Packet:
- Contract revision and clauses:
- Change mode:
- Evidence inspected:
- Expected behavior:
- Actual or source behavior:
- Classification:
- Authorized resolution:
- Protected domains checked:
- Specification delta required:
- User decision required: yes | no
- Exact residual:
~~~

## Compact release baseline

Use this minimum form when recording a release:

~~~text
Release Contract Baseline
- Release or deployment:
- Date:
- Implementation revision:
- Specification revisions or epochs:
- Included domains and clauses:
- QA and runtime evidence:
- Compatibility and migration notes:
- Known exclusions or residuals:
~~~
