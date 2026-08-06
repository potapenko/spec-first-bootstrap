# Install Persistent-Goal Agent Architecture

Use this prompt to install the coordinator-only multi-agent architecture for
long-running Codex goals.

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

This installation does not create, resume, pause, block, or complete a goal.
Do not launch subagents while installing it.

## Choose one deployment scope

Set exactly one:

~~~text
Deployment scope: GLOBAL | PROJECT_ONLY
Target project: <absolute path, required only for PROJECT_ONLY>
~~~

If deployment scope is missing, ask one short question and wait. Do not install
both scopes by default.

GLOBAL means every Codex project for the current user.

PROJECT_ONLY means exactly one repository and no Codex-home mutation.

## Canonical source

Read completely from the bootstrap repository:

- docs/agent-governance/README.md;
- docs/agent-governance/agents-sections.md;
- docs/agent-governance/root-orchestration.md;
- docs/agent-governance/product-truth-governance.md.

If those files cannot be fetched or found, stop and request access or the
package path. Do not reconstruct a shorter architecture from memory.

## Product-truth dependency

The canonical root contract integrates Contract Change Envelopes and contract
epochs for product goals.

In the selected scope, inspect whether the matching product-truth gate and full
document are already installed.

If missing, install that canonical dependency in the same selected scope as
part of this invocation and report it explicitly. Do not create a second copy
in the other scope.

## Existing state

Before editing:

- read the applicable existing AGENTS.md completely;
- preserve every unrelated instruction and worktree change;
- detect equivalent or conflicting coordination sections;
- identify any current persistent-goal state without changing it;
- inspect instruction-size limits;
- do not alter model defaults, custom agent profiles, concurrency settings, or
  Codex config unless the user separately requests configuration changes.

## GLOBAL installation

For GLOBAL scope:

1. resolve the active Codex home;
2. install the canonical full root contract as
   <active-codex-home>/root-orchestration.md;
3. merge the exact Global persistent-goal section from
   docs/agent-governance/agents-sections.md into the Codex-home AGENTS.md;
4. keep the full contract outside automatically loaded instructions;
5. change no project repository.

## PROJECT_ONLY installation

For PROJECT_ONLY scope:

1. resolve and validate the exact target repository;
2. install the canonical full root contract as
   docs/agent/root-orchestration.md;
3. merge the exact Project-local persistent-goal section from
   docs/agent-governance/agents-sections.md into the repository-root
   AGENTS.md;
4. preserve project-specific coordination and safety rules;
5. change no Codex-home file.

Use apply_patch for edits.

## Required architecture

The installed result must preserve:

- when a persistent goal is running and the current request advances it, the
  primary agent is coordinator-only /root;
- there is no direct-execution exception for small, simple, urgent,
  mechanical, or supposedly faster work;
- /root protects complete goal context and delegates implementation,
  investigation, build, test, runtime, browser, device, and visual work;
- a paused or blocked goal remains idle until the user explicitly resumes it;
- a genuinely separate side task may be single-agent only when it does not
  inspect, decide, change, verify, unblock, or advance goal-owned work;
- workers receive finite packets with authority, dependencies, owners,
  writable scope, forbidden actions, checks, stop conditions, and receipt
  format;
- model and reasoning selection follow risk and judgment needs, with quality
  ahead of token usage;
- concurrency is used only for independent ownership;
- one writable owner exists per file or product owner;
- every product delta receives independent review;
- build and test evidence does not replace required runtime or visual evidence;
- terminal worker receipts are recorded before slots or dependencies advance;
- one restart-safe registry carries packet state, residuals, ownership, and
  contract epoch;
- stale running rows are reconciled before dispatch;
- rejected work returns as a focused repair rather than duplicate speculative
  implementations;
- pause, resume, and compaction preserve exact durable state;
- completion requires terminal review, verification, QA, residual, registry,
  and checkpoint status.

## Verification

Verify:

- the full root document matches the canonical source;
- the selected routing section appears exactly once;
- the opposite deployment scope was not changed;
- existing instructions remain intact;
- full governance documents remain conditionally loaded;
- the root contract contains Product Truth integration, worker packet,
  acceptance pipeline, terminal receipt, registry, retry, pause/resume, and
  completion sections;
- Markdown and whitespace pass;
- configured instruction-size limits are respected;
- no goal state and no model or concurrency configuration changed.

For PROJECT_ONLY scope, follow the target repository's docs-only checks and
checkpoint policy, staging only installer-owned paths.

Report:

- selected scope;
- changed paths;
- whether product-truth dependency was already present or installed;
- merge or replacement decisions;
- verification;
- exact residual.
