# Documentation

This directory is the default entry point for the Bootstrap documentation.
The three layers below are independent: a project may install any one, any
two, or all three.

## Specification-first development

- [`spec-first-workflow.md`](spec-first-workflow.md) defines the compact
  specification-first workflow.
- [`specs/`](specs/) explains the product-specification structure and provides
  reusable templates.

## Persistent-goal agent work

[`agent-governance/`](agent-governance/) contains the installer-facing
governance sources for coordinator-and-workers architecture. Start with its
README before opening the individual contracts.

## Optional browser QA

Browser QA is an independent, optional layer for browser-facing projects. Its
governance source is
[`agent-governance/web-qa-governance.md`](agent-governance/web-qa-governance.md),
and the project starter pack is under [`../qa/web/`](../qa/web/).

## Human setup entry point

For the six copy-paste setup prompts—three project-local and three global—use
the repository-root [`README.md`](../README.md).
