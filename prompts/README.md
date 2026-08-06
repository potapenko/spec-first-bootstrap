# Prompt Pack

Use these prompts with Codex or another coding agent.

The pack distinguishes global Codex governance from project-local governance.
Choose one product-truth deployment scope instead of copying the same full
document everywhere.

## Install product-truth governance

### Option A: globally for every project

Use [`install-global-product-truth-governance.md`](install-global-product-truth-governance.md).

```text
Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Run the contract in prompts/install-global-product-truth-governance.md. Install product-truth governance in the active Codex home for every project. Do not modify the current project repository and do not install persistent-goal architecture in this invocation.
```

### Option B: only in one project

Use [`install-project-product-truth-governance.md`](install-project-product-truth-governance.md).

```text
Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Run the contract in prompts/install-project-product-truth-governance.md for this repository. Keep the install self-contained and do not modify the active Codex home or product implementation.
```

## Install persistent-goal agent architecture

Use
[`install-persistent-goal-agent-architecture.md`](install-persistent-goal-agent-architecture.md)
after choosing GLOBAL or PROJECT_ONLY scope.

```text
Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Run prompts/install-persistent-goal-agent-architecture.md.
Deployment scope: GLOBAL
Do not create or resume a goal during installation.
```

Replace GLOBAL with PROJECT_ONLY and provide the target path when architecture
should belong to one repository.

The architecture installer adds the product-truth dependency in the same scope
when it is missing. It does not change model defaults or concurrency config
unless the user separately requests that configuration.

## Project-work prompts

- [`greenfield-bootstrap.md`](greenfield-bootstrap.md): establish a new
  project-local specification system before feature implementation.
- [`brownfield-discovery.md`](brownfield-discovery.md): map an existing
  product without changing implementation.
- [`brownfield-interview.md`](brownfield-interview.md): prepare only the real
  product decisions left after evidence reconciliation.
- [`generate-first-specs.md`](generate-first-specs.md): create first-pass
  contracts without inventing authority.
- [`day-to-day-spec-first.md`](day-to-day-spec-first.md): run provisional
  basis, evidence reconciliation, final basis, implementation, and QA.
- [`repair-spec-first-workflow.md`](repair-spec-first-workflow.md): migrate an
  existing weaker or spec-only workflow.
- [`optional-web-qa.md`](optional-web-qa.md): add browser QA only to a web UI
  project.

Canonical full governance documents and compact AGENTS.md merge sections live
under [`docs/agent-governance/`](../docs/agent-governance/).
