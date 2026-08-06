# Browser QA Case Author

Use this as a lightweight guide for creating browser QA cases.

## Core concept

UI copy is not the feature.
UI copy usually documents the feature.

Write tests for behavior, not for static labels, unless text rendering itself
is the feature.

## Hard requirements

- Validate behavior in a real browser before writing the case.
- Prefer atomic cases with one clear responsibility.
- Prefer DOM-checkable expected results.
- Include these mandatory checks:
  - no uncaught console errors
  - no failed core network requests

## Write policy

- Create or update cases under:
  - `qa/cases/smoke/`
  - `qa/cases/regression/`
  - `qa/cases/experimental/`

## Dedupe rule

Before writing a new case, search for an existing one that already covers the
same behavior.

Update instead of duplicating when possible.
