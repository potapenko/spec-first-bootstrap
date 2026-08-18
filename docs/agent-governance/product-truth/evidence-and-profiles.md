# Product Truth Evidence And Profiles
- Node type: leaf
- Contract: `governance.product-truth.evidence@1`
- Clauses: `PT.EVIDENCE.SET`, `PT.EVIDENCE.DISCREPANCY`, `PT.PROFILE.DEFECT`,
  `PT.PROFILE.TRANSFER`, `PT.PROFILE.BROWNFIELD`

## PT.EVIDENCE.SET — Smallest complete evidence

After the provisional basis, inspect the smallest complete evidence set that
can settle the task. Depending on the domain it may include current and donor
source, ownership paths, design, QA chains, runtime states, release records,
history, upstream contracts, and platform documentation.

Do not sample only the artifact supporting the easiest conclusion. Do not
create a broad audit when a bounded slice can decide the question. Source,
tests, runtime, screenshots, history, and release behavior remain observed
evidence until reconciled with the active contract and user authority.

## PT.EVIDENCE.DISCREPANCY — Required classification

Every material mismatch is one of:

- `implementation defect`: the contract remains correct; Restore implementation.
- `specification defect or omission`: evidence establishes one existing truth;
  Reconcile the contract before implementation.
- `stale or inapplicable evidence`: explicitly disposition the old artifact.
- `authorized product evolution`: update contract, compatibility, implementation,
  and QA inside the open domain.
- `real product fork`: complete evidence leaves materially different valid outcomes.
- `external authority blocker`: continuation needs credentials, destructive
  action, policy, physical access, or another outside decision.

Never edit whichever artifact is easiest merely to obtain consistency or a
green result.

## PT.PROFILE.DEFECT — Behavioral diagnosis

For a behavioral defect:

1. establish expected behavior from the selected Active contract and accepted or
   released baseline;
2. reproduce or otherwise establish actual behavior when feasible;
3. inspect the owning source and relevant QA;
4. classify the discrepancy;
5. use Restore when the contract remains correct;
6. use Reconcile only when the contract is proven stale or incomplete;
7. use Evolve only when the user requested changed behavior.

Do not convert a bug into a spec change because changing the expectation is
easier than fixing implementation.

## PT.PROFILE.TRANSFER — Faithful ports and rewrites

A faithful transfer is normally Reconcile. The named source product is part of
the transfer authority inside declared adaptation boundaries. Evidence should
cover source contracts, executable ownership, design/style ownership, QA
chains, real runtime behavior, target owners, relevant history, and explicit
platform adaptations.

Do not treat a provisional mismatch as an immediate user decision, sample only
supportive snippets, invent target alternatives already resolved by the source,
copy platform mechanics as product behavior, create parallel target models, or
call a partial state/component transfer faithful.

## PT.PROFILE.BROWNFIELD — Missing or unreliable contracts

Brownfield discovery is the narrow exception to a complete-contract gate.
First record that the Markdown path or contract is absent or unreliable. Then inspect
source, design, routes, state, QA, runtime, history, and released behavior as
evidence without changing implementation.

Produce a linked domain map, observed behavior separated from intended
behavior, first-pass contracts, evidence/ownership mappings, a prioritized
backlog, contradictions, unknowns, and legacy-released behavior requiring
protection. Draft contracts are not implementation authority merely because
code exists. After reliable first-pass contracts exist, subsequent slices use
Restore, Reconcile, or Evolve.
