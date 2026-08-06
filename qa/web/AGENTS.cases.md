# Browser QA Case Author

Use this as a lightweight guide for creating browser QA cases.

## Core concept

UI copy is not the feature.
UI copy usually documents the feature.

Write tests for behavior, not for static labels, unless text rendering itself
is the feature.

The governing product contract defines expected behavior. Source and live
browser behavior are evidence; neither may silently replace or rewrite the
contract.

## Hard requirements

- Validate behavior in a real browser before writing the case.
- Read the active governing spec and pin its contract revision or epoch and
  clause IDs in the case.
- Prefer atomic cases with one clear responsibility.
- Prefer DOM-checkable expected results.
- Record the complete precondition -> action -> state transition -> visible
  result chain, including a material intermediate state when one exists.
- Include these mandatory checks:
  - no uncaught console errors
  - no failed core network requests

If the contract, source, and live behavior disagree, record the discrepancy
instead of changing the expectation to match whichever artifact is easiest.
Do not invent product intent when no reliable contract exists.

## Write policy

- Create or update cases under:
  - `qa/cases/smoke/`
  - `qa/cases/regression/`
  - `qa/cases/experimental/`

## Dedupe rule

Before writing a new case, search for an existing one that already covers the
same behavior.

Update instead of duplicating when possible.
