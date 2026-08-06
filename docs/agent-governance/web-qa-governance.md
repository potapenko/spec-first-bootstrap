# Optional Browser QA Governance

## Purpose

This document defines a lightweight browser-QA layer for web UI projects.

Browser QA is optional. It is used when a project has browser-visible behavior
that benefits from repeatable real-browser cases, run reports, and bug
evidence. It is not a universal testing framework and must not be imposed on
backend, CLI, data, desktop, mobile, or infrastructure projects merely because
the guidance is globally available.

## Activation

Read this document when the user asks to install browser QA, create or update
browser QA cases, execute a browser QA run, diagnose a browser-visible
regression, or review browser QA evidence.

Do not load it for ordinary implementation work that has no browser-QA scope.

## Relationship to product truth

When a project has active product specifications, they define intended
behavior and QA cases should link to them.

The browser-QA layer does not require or install a specification system. When
no such system exists, use the user objective and the project's established
requirements, release behavior, and other named authority; record material
authority gaps instead of inventing expected behavior.

Source and design establish implementation and ownership evidence.

Real browser behavior establishes observed behavior.

QA cases and run reports establish repeatable acceptance evidence.

These roles are separate. A passing or failing browser case does not
independently create product intent. When a spec, implementation, case, and
runtime disagree, classify the discrepancy before editing whichever artifact
is easiest.

Never weaken an expected result merely to obtain a green run.

## Project installation

A project browser-QA layer should remain small and recognizable. Adapt the
starter pack under `qa/web/` to the project's existing conventions instead of
creating a competing test system.

Normally provide:

- routing instructions for case-authoring and run tasks;
- smoke, regression, and experimental case locations;
- one case template;
- one run-report template;
- one bug-report template;
- a stable behavior-authority-to-case mapping convention, using spec-to-case
  links when specifications already exist.

Preserve existing QA and test tooling. Do not replace a mature project system
with this starter pack.

## Case contract

Each material case records:

- a stable case or scenario identifier;
- the governing product contract and revision when available;
- relevant clause or behavior identifiers;
- preconditions and test data boundaries;
- user actions;
- state transitions and material intermediate results;
- final expected visible or data result;
- failure and recovery expectations where relevant;
- URL, viewport, browser, platform, and permission conditions;
- required console and core-network checks;
- safe evidence expectations.

Prefer one coherent behavior per case. Do not create cases that only assert
static copy unless text rendering itself is the behavior under test.

When no reliable product contract exists, record the gap. Current UI behavior
may support discovery, but it must not be silently promoted into intended
behavior.

## Running cases

Use a real browser through the environment's supported browser tooling.

For each case:

1. establish the requested environment and preconditions;
2. execute the recorded actions;
3. observe intermediate and final results;
4. inspect uncaught console errors and failed core requests;
5. record `PASS`, `FAIL`, `FLAKY`, `SKIPPED`, or `BLOCKED` truthfully;
6. preserve safe evidence and exact residuals.

Do not edit the case while executing it merely to match current behavior.

Automated browser output is supporting evidence. When the acceptance contract
requires real interaction or visual comparison, perform that exact runtime
work rather than substituting DOM assertions.

## Failure classification

A failed case should be classified as one of:

- implementation defect;
- stale or inapplicable QA case;
- product-contract discrepancy;
- test-data or environment residual;
- browser-runner defect;
- missing external authority.

If classification is not yet established, say so. Do not guess.

## Safety and privacy

- Do not expose credentials, cookies, session tokens, private account data, or
  payment details in cases, logs, screenshots, or reports.
- Do not perform destructive, billable, publishing, messaging, or irreversible
  actions unless the user explicitly authorizes them.
- Use bounded timeouts for browser and network operations.
- Keep verbose traces opt-in and keep normal reports short and scannable.
- Preserve unrelated browser tabs, sessions, profiles, and user-owned
  processes.

## Global installation

Global installation makes this conditional guidance available to future
projects. It does not copy `qa/` into every repository and does not make
browser QA mandatory.

It also does not install specification governance or persistent-goal agent
architecture. Those independent layers are preserved when present and remain
absent when not selected.

The global routing block must activate only for browser-QA tasks. Project
artifacts are still created inside a target repository only when the user asks
for that project to receive the QA layer.

## Completion

An installation is complete when the selected scope is exact, existing rules
are preserved, routing is non-duplicated, and no product implementation changed.

A QA run is complete when every selected case has a truthful terminal status,
safe evidence, discrepancy classification when known, and an exact residual.
