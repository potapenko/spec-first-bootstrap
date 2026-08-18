# Product Truth Core Contract
- Node type: leaf
- Status: Active
- Read when: any covered product task needs the canonical authority and truth-layer rules.
- Do not read when: work is proven mechanical, infrastructure-only, or behavior-neutral.
- Maximum size: 100 physical lines.
- Contract: `governance.product-truth.core@1`
- Clauses: `PT.CORE.AUTHORITY`, `PT.CORE.LAYERS`, `PT.CORE.DOMAINS`,
  `PT.CORE.STABILITY`, `PT.CORE.RELEASE`, `PT.CORE.ARTIFACTS`

## PT.CORE.AUTHORITY — Canonical but not self-authorizing
The specification system is the canonical statement of intended product
behavior. Canonical does not mean infallible: a specification can be missing,
stale, ambiguous, contradictory, or incorrectly transcribed.

A specification edit never creates its own semantic authority. User decisions,
accepted reconciliation, explicit precedence, and correction of a proven
internal contradiction are legitimate change bases. Current code, a test,
implementation convenience, platform convention, or agent preference is not.

This contract applies to work that investigates, defines, changes, implements,
reviews, or verifies user-visible behavior, state, actions, UX, routes, public
data, permissions, persistence, compatibility, defects, QA, release behavior,
ports, transfers, or migrations. Proven mechanical, infrastructure-only, and
behavior-neutral work may remain outside it.

## PT.CORE.LAYERS — Product truth system
The product truth system has distinct layers:

| Layer | Question answered |
| --- | --- |
| User objective or decision | What change is authorized now? |
| Active product contract | How should the product behave? |
| Design and product model | How is behavior expressed structurally and visually? |
| Implementation source | How is it realized and who owns it? |
| Runtime behavior | What actually happens in the relevant state? |
| QA and acceptance | Which action-state-result chains were verified? |
| Release baseline | Which behavior may users already rely on? |

These layers are not a flat vote. Source and runtime establish realization and
observation; QA establishes acceptance evidence; release records protect
compatibility. None silently replaces intended behavior. Spec-first is not
spec-only: the smallest complete applicable evidence set must still be
reconciled before non-trivial implementation or a product decision.

## PT.CORE.DOMAINS — Independent responsibility boundaries

A product domain is a stable responsibility boundary whose behavior can be
reasoned about and protected independently. It may be a feature, shared
service, data contract, access lifecycle, playback policy, or another product
responsibility.

A source file is not automatically a product domain. One source owner may
implement several contracts, and one domain may span several owners. Changing
a shared file does not authorize changing every consumer.

Every mature contract registry records domain ID, governing contract,
authority, stability, selection conditions, precedence, dependencies, and the
latest accepted or released baseline. Stable clause IDs identify meaning;
paths, headings, dates, and line numbers are not durable substitutes.

## PT.CORE.STABILITY — Authority and stability are separate

Authority values:

- `Draft`: incomplete or awaiting a decision; evidence, not implementation authority.
- `Active`: current normative intended behavior.
- `Superseded`: replaced by a named newer contract.
- `Historical`: retained only as context.

Stability values:

- `Evolving`: deliberately being designed or changed.
- `Accepted`: implementation and applicable QA were accepted.
- `Released`: externally consumable behavior exists.
- `Deprecated`: temporarily supported pending replacement or removal.

Authority selects which contract governs. Stability controls how strongly
existing behavior is protected.

## PT.CORE.RELEASE — Compatibility baseline

Released behavior must not be inferred from a branch name, green tests, an
Active label, or the existence of code. A release baseline records the release
identifier and date, implementation revision, contract revisions and clauses,
included domains, QA/runtime evidence, compatibility notes, and residuals.

Public behavior without an explicit historical baseline is conservatively
legacy-released. Its observed behavior, applicable specifications, user-facing
design, and QA remain protected evidence until reconciled. A request to change
one released behavior does not authorize unrelated breaking changes.

## PT.CORE.ARTIFACTS — Minimum product package
A mature project provides a Markdown specification root and authority index, Active
contracts, domain and precedence mapping, applicable design/product-model
contracts, evidence and ownership maps for complex domains, QA or acceptance
scenario mappings, durable envelopes for long-running work, and release
baselines for released behavior. These concepts may use project-specific paths
but remain distinct. Compact instruction files link to them and do not
duplicate the full contracts.
