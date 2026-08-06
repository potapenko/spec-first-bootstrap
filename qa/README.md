# Verification Layer

This directory is reserved for verification artifacts.

Examples:
- QA cases
- test scenarios
- acceptance checks
- scripts used to validate behavior

This layer is independent from `docs/specs/` and can be installed without a
specification layer. When specs exist, they define the product contract and QA
artifacts provide evidence that the implementation matches it. Without specs,
QA artifacts must name the available source of expected behavior and expose
authority gaps instead of inventing intent.

When the project has stable contract identifiers or revisions, cases should
pin them and record the relevant action-state-result chain. QA does not
independently create product intent or weaken expectations merely to obtain a
green run.

Verification does not need to be browser-based.
Use the form that best matches the project.

If your project has a browser UI and you want a lightweight starter pack for
browser QA, see:

- `qa/web/`
