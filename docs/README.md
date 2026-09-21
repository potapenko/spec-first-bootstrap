# Documentation

This directory is the default entry point for the Bootstrap documentation.
The three layers below are independent: a project may install any one, any
two, or all three.

## Specification-first development

- [`spec-first-workflow.md`](spec-first-workflow.md) defines the compact
  specification-first workflow.
- [`specs/`](specs/) is a Markdown-only root/branch/leaf tree with ordinary
  links, bounded nodes, traversal receipts, and reusable templates.

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

## Context recovery

Use available, applicable, current context after lifecycle events; load required
content only when missing, potentially changed, or uncertain. The
[old adapter](../integrations/codex-lifecycle/) is retired. Existing hooks need
separately authorized [migration](../prompts/migrate-codex-lifecycle.md).
