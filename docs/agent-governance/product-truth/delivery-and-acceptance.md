# Product Truth Delivery And Acceptance

- Contract: `governance.product-truth.delivery@1`
- Clauses: `PT.DELIVERY.ORDER`, `PT.DELIVERY.DESIGN`, `PT.DELIVERY.QA`,
  `PT.DELIVERY.PROPORTIONALITY`, `PT.DELIVERY.COMPLETE`

## PT.DELIVERY.ORDER — Contract before implementation

Implement against the final reconciled Spec Basis, not chat memory. When
intended meaning legitimately changes, update the contract and Contract Delta
before the first implementation edit. Spec and code may share one checkpoint;
the rule concerns authority and working order.

Planning-only, question-only, review-only, and discovery-only work remains a
hard implementation boundary. If evidence reveals a real product fork or
protected dependency outside the envelope, stop the affected slice and
continue independent authorized work when safe.

## PT.DELIVERY.DESIGN — Product-significant UI structure

When visual or interaction behavior matters, the contract defines meaningful
zones, component relationships, visible states and transitions, adaptations,
accessibility/input invariants, and acceptance scenario IDs. Design evidence
maps canonical references, source/style owners, viewport and product state,
dynamic visibility provenance, and visual QA.

Generated concepts, screenshots, platform conventions, and component libraries
do not invent behavior outside the envelope. A structural or state discrepancy
must not be reduced to a cosmetic patch.

## PT.DELIVERY.QA — Pinned action-state-result verification

Material behavior maps to scenarios with preconditions, user actions, state
transitions, intermediate results, final results, failure/recovery behavior,
and platform or compatibility conditions. QA verifies a pinned contract and
does not define intent independently or weaken expectations to become green.

When contract, implementation, and QA differ: classify the discrepancy,
establish legitimate authority, update the contract first when meaning changes,
then update implementation and QA. Unit tests do not replace runtime or visual
evidence when the contract requires observable behavior.

## PT.DELIVERY.PROPORTIONALITY — Outcome-first support

Concrete user capability reachable from the product or release path is the
primary progress measure. Specifications, maps, diagnostics, tooling, evidence,
review, and QA are supporting work. They may be required but are reported
separately and never represented as delivered product functionality.

Use the smallest evidence and review sufficient for demonstrated risk. Every
support artifact names its next product decision or release-path consumer.
Do not build speculative evidence systems or production-harden temporary debug
tools. Conversely, do not skip checks required by demonstrated data-loss,
privacy, security, irreversible-action, or released-compatibility risk. A
truthful residual may preserve bounded uncertainty but cannot hide a known
acceptance failure or missing claimed capability.

## PT.DELIVERY.COMPLETE — Terminal conditions

A product task is complete only when:

- the requested release-path outcome exists when implementation was requested;
- the final routed contract basis and semantic revisions are current;
- every semantic edit has legitimate authority;
- implementation matches the pinned clauses;
- protected adjacent domains are preserved or dispositioned;
- required review, build, test, runtime, visual, compatibility, and QA evidence
  is terminal;
- release baseline changes are recorded when a release occurred;
- stale-epoch work is not accepted;
- residuals are explicit and truthful.

Forbidden patterns include spec-only reasoning that refuses required evidence,
code-first invention followed by a retroactive spec, editing expectations to
match a defect, treating stale tests as authority, changing adjacent domains
through shared files, accepting stale revisions, hiding behavior change as
cleanup, and using Active or green tests as proof of release.
