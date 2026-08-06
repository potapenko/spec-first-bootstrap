# Specification-First Product Truth Workflow

This document is the canonical compact workflow for projects that use
spec-first-bootstrap.

Its purpose is to make product understanding the primary artifact, preserve
accepted and released behavior, keep specifications authoritative without
making them infallible, and prevent implementation convenience from becoming
product policy.

The full reusable governance contract lives in
docs/agent-governance/product-truth-governance.md.

## Core principle

The specification system is the canonical statement of intended product
behavior and the project's primary product artifact.

Canonical does not mean infallible. A specification may be incomplete, stale,
ambiguous, incorrectly transcribed, or based on evidence that later proves
inapplicable.

A specification edit cannot authorize itself.

Code is an implementation of product understanding. It is not a substitute for
that understanding.

Spec-first means the specification frames the investigation first. It does not
mean spec-only.

## Product truth system

Different layers answer different questions.

| Layer | Primary question |
| --- | --- |
| User objective or decision | What product change is authorized now? |
| Active product contract | How should the product behave? |
| Design and product model | How is the behavior expressed structurally and visually? |
| Implementation source | How is it currently realized, and who owns it? |
| Runtime behavior | What does the product actually do in the relevant state? |
| QA and acceptance evidence | Which action-state-result chains have been verified? |
| Release baseline | Which behavior may users or consumers already rely on? |

These layers are not a flat vote.

Source, design, tests, QA, runtime output, screenshots, and history may reveal a
missing, stale, or contradictory contract. They must not silently invent
intent.

The active contract must not be used to avoid reading the evidence required to
understand ownership, current behavior, compatibility, or a faithful transfer.

## Tasks covered by the gate

This workflow applies to:

- new product features;
- observable behavior changes;
- behavioral bugs and regressions;
- behavioral investigations and product-behavior planning;
- UX, visual behavior, state, route, persistence, permission, eligibility, or
  data-contract changes;
- multi-step user flows;
- product transfers, ports, rewrites, and migrations;
- refactors whose behavioral impact is possible or uncertain;
- product QA and release behavior.

It normally does not require a product contract change for formatting,
comments, documentation-only maintenance, or proven behavior-neutral internal
cleanup.

If behavioral impact is uncertain, the gate applies.

## Change modes

Every covered task has one primary change mode.

### Restore

Use Restore when implementation must be brought back to an already established
contract.

The active contract and applicable accepted or released baseline define
expected behavior.

A semantic specification change is normally outside the task. An editorial
clarification or separately accepted reconciliation may still be valid.

### Reconcile

Use Reconcile when an existing product truth must be recovered or transferred
into a complete, current contract.

This is the normal mode for faithful transfers, ports, brownfield contract
renewal, and correction of stale or incomplete specifications.

Reconciliation may update a contract without asking the user when the task
authorizes fidelity or reconciliation, the smallest complete evidence set
converges on one existing behavior, no product alternative is invented, and no
protected adjacent domain changes.

Reconciliation is not redesign.

### Evolve

Use Evolve when the user requests a new feature or semantic change to a named
domain.

The request itself opens that domain and behavior. Do not ask the user to
authorize every direct, evidence-backed consequence of the request.

Existing source, design, QA, runtime, and release evidence still constrain
ownership, compatibility, migration, and adjacent behavior.

### Discover

Use Discover when no reliable contract exists and the task is to understand the
product.

Record the missing or unreliable contract first. Inspect evidence, separate
observed from intended behavior, and produce first-pass contracts, maps,
unknowns, and a decision list.

Do not change product implementation during a discovery-only task.

### Behavior-neutral

Use Behavior-neutral only when observable behavior is proven not to change.

If ownership, state, timing, persistence, compatibility, or observable results
become uncertain, reclassify the task before continuing.

## Contract Change Envelope

Before product implementation, establish a Contract Change Envelope.

For a small bounded task it may be stated in the first progress update. For a
long-running, multi-agent, cross-domain, accepted, or released task it must be a
durable artifact or registry record.

~~~text
Contract Change Envelope
- Task:
- Change mode:
- User-authorized outcome:
- Authorized domains and clauses:
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

Writable paths do not enlarge the product domain.

The user's request authorizes semantic change only inside the domain and
behavior it actually names. It does not silently open neighboring domains,
shared-consumer behavior, or unrelated released contracts.

## Required start order

Before implementation for a covered task:

1. Read every applicable global and project-local instruction layer.
2. Read the project's spec README and authority registry.
3. Select the smallest active contract set that governs the task.
4. Classify the change mode and establish the Contract Change Envelope.
5. State a provisional Spec Basis.
6. Inspect the smallest complete applicable source, design, QA, runtime,
   history, upstream, and release evidence set.
7. Classify every material discrepancy.
8. Accept any authorized Contract Delta and update the specification first.
9. State the final reconciled Spec Basis with a pinned contract revision.
10. Only then implement the authorized slice.
11. Review and verify implementation against that pinned basis.

Use this provisional template:

~~~text
Provisional Spec Basis
- Task:
- Change mode:
- Authoritative specs and clauses:
- Expected behavior:
- Invariants and protected domains:
- Apparent gaps or conflicts:
- Required evidence:
- Allowed spec impact:
- Implementation authorized: yes / no
~~~

Use this final template:

~~~text
Final Reconciled Spec Basis
- Contract revision or epoch:
- Governing clauses:
- Resolved intended behavior:
- Evidence inspected and its role:
- Discrepancy dispositions:
- Accepted Contract Delta:
- Protected adjacent domains:
- Required acceptance scenarios:
- Implementation authorized: yes / no
~~~

The provisional basis frames the evidence pass. It is not permission to stop at
the specification and turn every mismatch into a user question.

## Evidence reconciliation

The applicable evidence set may include:

- current and donor implementation source;
- ownership and dependency paths;
- design contracts and visual references;
- tests and QA action-state-result chains;
- runtime behavior in relevant states;
- release records and deployed behavior;
- history needed to distinguish current from stale behavior;
- upstream product contracts;
- platform or external documentation.

Do not sample only the artifact that supports the easiest conclusion.

Do not run a broad audit when a bounded complete slice can settle the task.

A faithful transfer must inspect the complete applicable source behavior,
ownership, design, QA, runtime, and target adaptation evidence before claiming
a product fork or implementation readiness.

## Discrepancy classification

Every material mismatch is classified before repair.

### Implementation defect

The active contract and baseline remain correct, while source or runtime
differs.

Restore the implementation. Do not rewrite the contract to match the defect.

### Specification defect or omission

The contract is incomplete, stale, incorrectly transcribed, or internally
inconsistent, while accepted evidence and task authority establish one existing
behavior.

Use Reconcile. Correct the contract before implementation and record the
evidence basis.

### Stale or inapplicable evidence

A test, QA case, design artifact, fixture, historical source, or runtime
observation no longer governs the task.

Disposition it explicitly. Do not change the current product merely to satisfy
stale evidence.

### Authorized product evolution

The user's request intentionally changes behavior inside the open domain.

Update the contract first, record compatibility impact, then update
implementation and QA.

### Real product fork

After complete applicable evidence reconciliation, multiple materially
different valid outcomes remain and the user's request does not choose among
them.

Present the concrete alternatives, evidence, consequences, and recommended
option.

### External authority blocker

Continuation requires credentials, provider or store authority, legal or policy
input, destructive action, physical-device access, or another decision outside
agent authority.

Record the exact blocked slice and continue unrelated authorized work when
safe.

## Specification mutation authority

A semantic specification edit needs an external change basis.

Accepted bases are:

- an explicit user request or decision;
- an accepted Evolve envelope;
- an accepted Reconcile result for a faithful transfer, restoration, or
  contract-renewal task;
- explicit precedence from a higher-ranked active contract;
- correction of a proven internal contradiction without new product behavior.

Current implementation alone is not a change basis.

A current test alone is not a change basis.

An agent preference, platform convention, implementation convenience, or
plausible guess is not a change basis.

The specification edit itself is never a change basis.

The following circular sequence is forbidden:

1. invent behavior;
2. write it into the specification;
3. cite the edited specification as authority;
4. implement it;
5. call the result compliant.

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

Keep normative contracts readable. Put raw captures, hashes, source inventories,
and mechanical proof in evidence or QA artifacts.

## Authority and stability

Contract authority and domain stability are separate.

Authority status:

- Draft: incomplete and non-authoritative;
- Active: current intended behavior;
- Superseded: replaced by a named newer contract;
- Historical: retained only as context.

Stability status:

- Evolving: intentionally being designed or materially changed;
- Accepted: implementation and applicable QA have been accepted;
- Released: included in a public build, production deployment, or public API;
- Deprecated: still supported for a defined compatibility period.

An Active contract may be Evolving, Accepted, Released, or Deprecated.

Mature projects keep a spec registry, normally docs/specs/index.md, with:

- contract and domain identifiers;
- authority and stability;
- when to read each contract;
- precedence over overlapping contracts;
- upstream and shared dependencies;
- latest accepted or released baseline.

## Release baselines

Released behavior must be explicit rather than inferred from a branch name,
green tests, an Active label, or the existence of code.

A release contract baseline records:

- release, build, deployment, or API version;
- date;
- implementation revision;
- specification revisions or contract epochs;
- included domains and clauses;
- QA and runtime evidence;
- compatibility and migration notes;
- known exclusions or residuals.

A public product without a historical baseline is treated conservatively as
legacy-released until its behavior is reconciled.

An explicit user request may evolve a released domain. It does not
automatically authorize unrelated breaking changes.

## Cross-domain and shared-owner discipline

Product scope and source-file scope are different.

A task may modify a shared source owner while preserving every out-of-scope
consumer contract.

Before changing a shared owner:

- identify its product domains and real consumers;
- name the authorized consumer behavior;
- name protected consumer behavior;
- preserve accepted and released contracts outside the envelope;
- verify affected consumers in proportion to risk.

A technical dependency does not automatically open a product dependency.

If semantic change outside the envelope is required, return the exact
dependency. Do not create parallel state, duplicated services, or temporary
product rules to avoid it.

## When to ask the user

Ask only after the smallest complete applicable evidence pass proves one of the
following:

- active contracts materially conflict without precedence;
- required behavior is absent from all applicable authority and evidence;
- multiple valid outcomes would materially change the product;
- the change crosses a protected domain outside the envelope;
- material compatibility consequences are not covered by the request;
- continuation requires external authority.

Do not ask because one spec line appears inconsistent before source and QA have
been inspected, because the current context lacks a discoverable fact, or
because the agent invented alternatives unsupported by the product.

When asking, explain the exact unresolved rule, sources inspected, visible and
compatibility consequences, recommended option, and independent work that can
continue.

## Behavioral diagnosis

For a behavioral defect:

1. establish the active and accepted or released contract;
2. establish actual behavior from applicable evidence;
3. name the discrepancy;
4. classify it;
5. use Restore when the contract remains correct;
6. use Reconcile when the contract was proven stale or incomplete;
7. use Evolve only when the user requested new behavior.

Do not convert a bug into a spec change because editing the expectation is
easier than fixing implementation.

## Brownfield discovery

Brownfield discovery is the explicit exception to a complete-contract gate.

Before broad source inspection, record that the relevant contract is absent or
unreliable.

Then:

1. inspect code, routes, state, tests, docs, design, QA, runtime, history, and
   released behavior as evidence;
2. separate observed from intended behavior;
3. create a product map and spec backlog;
4. write first-pass contracts with unknowns and conflicts;
5. record legacy-released behavior conservatively;
6. do not modify product implementation during discovery.

Once first-pass contracts exist, subsequent slices use Restore, Reconcile, or
Evolve.

## Contract revisions and worker epochs

Every multi-agent or long-running packet that can affect product behavior is
pinned to stable clause IDs and a contract revision or epoch.

An accepted semantic contract change advances the affected epoch.

Open packets using affected clauses must be revalidated or retired. Their
implementation or QA receipts cannot be accepted against stale meaning.

Unaffected packets may continue when their clauses and dependencies did not
change.

Editorial changes need not advance the semantic epoch when review confirms that
meaning is unchanged.

## QA and acceptance

QA is an executable or observable extension of the contract.

Each material scenario should identify:

- preconditions;
- user actions;
- state transitions;
- material intermediate results;
- final visible or data result;
- failure and recovery;
- platform or compatibility conditions.

Tests and QA verify a pinned contract. They do not independently define intent.

When contract, implementation, and QA disagree, classify the discrepancy before
editing whichever artifact is easiest.

A green suite cannot authorize a product change or prove an unexercised user
journey.

Runtime and visual evidence cannot be replaced by unit tests when the contract
requires observable behavior.

## Global and project-local deployment

Global governance belongs in the active Codex home and applies across projects.

Project-local governance belongs in one repository and must work without a
custom global layer.

Do not install the same full document in both scopes by default.

Keep only compact routing gates in automatically loaded AGENTS.md files. Full
product-truth and root-orchestration documents remain conditionally loaded.

Project-local safety, language, framework, build, test, and release rules stay
local. They are never promoted globally merely because one project needs them.

## Repository enforcement

Put a compact Product Truth gate near the top of AGENTS.md.

Onboarding and prompts repeat routing, not weaker competing doctrine.

A first progress update for covered work states the Change Envelope and
provisional basis. The final response identifies governing clauses, accepted
contract deltas, verification, and residuals.

Long-running goals keep durable contract epochs and acceptance state.

## Migration audit

When installing or repairing this workflow:

1. read all applicable global and project-local instruction files;
2. preserve project-specific safety, build, test, release, Git, and operator
   rules;
3. choose GLOBAL or PROJECT_ONLY deployment explicitly;
4. install the compact gate and full governance document in only that scope;
5. replace spec-only or code-first wording with the provisional-basis,
   evidence-reconciliation, final-basis sequence;
6. establish authority and stability fields;
7. add Change Envelope, Contract Delta, release baseline, and epoch routing;
8. update day-to-day, brownfield, greenfield, and repair prompts;
9. do not change product implementation during workflow migration;
10. verify Markdown, links, instruction size, and changed-file scope;
11. follow the target repository's checkpoint policy.

Use the installer prompts under prompts/ for ready-to-send migration contracts.
