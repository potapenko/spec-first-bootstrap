# Browser QA Runner

Use this as a lightweight runner guide for browser-based QA work.

## Base URL

Set the correct base URL for the project before running.

## Hard requirements

- Use a real browser.
- Prefer Playwright or an equivalent browser automation tool.
- Prefer DOM-checkable assertions over visual guesses.
- After each major step, check:
  - uncaught console errors
  - failed network requests for the core flow

## Write policy

- Do not modify QA case files during a run.
- Write run output only to a dedicated `qa/runs/<date>-.../` directory.

## Run rules

- Execute smoke cases first.
- Mark each case as `PASS`, `FAIL`, `FLAKY`, or `SKIPPED`.
- For `FAIL` and `FLAKY`, include:
  - URL
  - expected vs actual
  - console errors
  - failed requests
  - screenshot paths

## Blockers

- Retry once after reload.
- Retry once in a fresh browser context.
- If still broken, record evidence and continue.
