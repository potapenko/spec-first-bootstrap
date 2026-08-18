# Documentation

This directory is the default entry point for the Bootstrap documentation.
The three layers below are independent: a project may install any one, any
two, or all three.

## Specification-first development

- [`spec-first-workflow.md`](spec-first-workflow.md) defines the compact
  specification-first workflow.
- [`specs/`](specs/) explains hierarchical route manifests, contract closures,
  Route Receipts, and reusable templates.

## Agent work governance

[`agent-governance/`](agent-governance/) contains the installer-facing
sources for current-branch discipline, implementation-request planning,
approved-scope execution, implementation economics, coordinator-and-workers
architecture, and the explicit no-delegation single-agent exception. Start with
its README before opening the individual contracts.

## Optional browser QA

Browser QA is an independent, optional layer for browser-facing projects. Its
governance source is
[`agent-governance/web-qa-governance.md`](agent-governance/web-qa-governance.md),
and the project starter pack is under [`../qa/web/`](../qa/web/).

## Human setup entry point

For the six copy-paste setup prompts—three project-local and three global—use
the repository-root [`README.md`](../README.md).

## Optional Codex lifecycle enforcement

[`../integrations/codex-lifecycle/`](../integrations/codex-lifecycle/) contains
an optional Codex-only adapter that restores the active reading gate after
startup, resume, clear, context compaction, and worker start. It does not
install or couple the three governance layers.
