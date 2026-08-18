# Product Truth Change Control
- Node type: leaf
- Status: Active
- Read when: planning product implementation, changing a contract, or protecting adjacent domains.
- Do not read when: work is proven behavior-neutral and changes no product contract.
- Maximum size: 100 physical lines.
- Contract: `governance.product-truth.change@1`
- Clauses: `PT.CHANGE.MODE`, `PT.CHANGE.ENVELOPE`, `PT.CHANGE.AUTHORITY`,
  `PT.CHANGE.DELTA`, `PT.CHANGE.SCOPE`

## PT.CHANGE.MODE — One primary mode

Every covered task has one primary mode before implementation:

- `Restore`: bring implementation back to an established contract. Semantic
  specification change is normally forbidden.
- `Reconcile`: align the contract with one existing product truth established
  by complete evidence. Reconciliation is not redesign.
- `Evolve`: implement a user-authorized semantic change inside a named domain.
- `Discover`: understand a product whose contract is absent or unreliable;
  implementation remains unauthorized.
- `Behavior-neutral`: make a proven non-behavioral change. Reclassify if state,
  timing, persistence, compatibility, ownership, or observable results may change.

## PT.CHANGE.ENVELOPE — Bounded authority

Before implementation, establish a Contract Change Envelope containing:

- task, mode, and user-authorized outcome;
- authorized domains and clause IDs;
- protected adjacent domains;
- shared owners that may be touched without changing other consumers;
- authority, stability, and release baseline;
- required evidence;
- allowed and forbidden specification delta;
- material decisions requiring the user;
- current Markdown path and contract revisions;
- required review and QA;
- task-owned paths when a plan is required.

The envelope describes semantic authority, not merely writable files. A path
cannot enlarge the product domain. Newly discovered cross-domain change is a
scope dependency to return, not permission to expand silently.

## PT.CHANGE.AUTHORITY — Legitimate semantic basis

Accepted semantic change bases are:

- an explicit user request or decision;
- an accepted Evolve envelope;
- accepted Reconcile evidence for fidelity, transfer, restoration, or renewal;
- explicit precedence from a higher-ranked Active contract;
- correction of a proven internal contradiction without new behavior.

Do not invent behavior, write it into a spec, cite the edit as authority, and
then implement it. Current code, a current test, convention, convenience, or an
agent preference cannot authorize product meaning.

The user's request opens only the behavior and domain it actually names. A fix
normally authorizes Restore, a faithful transfer authorizes Reconcile, and a
redesign authorizes Evolve only inside the named surface. Do not ask for a
second permission already clearly granted.

## PT.CHANGE.DELTA — Semantic revision record

Every semantic change records a compact Contract Delta:

- change ID, mode, and external authorization;
- domain and clause IDs;
- previous and new or reconciled behavior;
- evidence basis;
- compatibility classification;
- adjacent domains checked;
- design and QA impact;
- changed specification paths;
- required review;
- new node and contract revision or epoch.

Editorial clarification may leave the semantic epoch unchanged after review.
Reconciliation and evolution advance affected revisions. Protected or breaking
changes to Accepted, Released, Deprecated, public, persistent, permission, API,
or shared-consumer contracts require explicit authority unless already named.

## PT.CHANGE.SCOPE — Shared owners and user decisions

Before changing a shared owner, identify real consumers, authorized behavior,
protected consumer behavior, and proportional verification. Technical
dependency does not automatically open product scope. Do not create parallel
state, fallback product rules, or duplicate services merely to avoid returning
a real dependency.

Ask the user only after complete evidence proves a material contract conflict,
missing behavior, multiple valid outcomes, protected cross-domain change,
material compatibility consequence, or need for external authority. State the
exact unresolved rule, evidence, consequences, recommended option, and work
that remains independent.
