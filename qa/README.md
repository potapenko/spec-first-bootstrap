# Verification Layer

This directory is reserved for verification artifacts.

Examples:
- QA cases
- test scenarios
- acceptance checks
- scripts used to validate behavior

This layer is intentionally separate from `docs/specs/`.
Specs define the product contract.
Verification artifacts provide evidence that the implementation matches that contract.

When the project has stable contract identifiers or revisions, cases should
pin them and record the relevant action-state-result chain. QA does not
independently create product intent or weaken expectations merely to obtain a
green run.

Verification does not need to be browser-based.
Use the form that best matches the project.

If your project has a browser UI and you want a lightweight starter pack for
browser QA, see:

- `qa/web/`
