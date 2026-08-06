# Install Product-Truth Governance Globally

Use this prompt when the governance should apply to every Codex project for the
current user.

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Install the checked-in product-truth governance globally. This is a
configuration and documentation task, not a product implementation task. Do
not launch subagents.

## Deployment scope

The scope is GLOBAL.

- Change the active Codex home.
- Do not change any project repository.
- Do not install persistent-goal root architecture in this invocation.

## Canonical source

Read completely from the bootstrap repository:

- docs/agent-governance/README.md;
- docs/agent-governance/agents-sections.md;
- docs/agent-governance/product-truth-governance.md.

If those files cannot be fetched or found, stop and request access or the
package path. Do not reconstruct a shorter substitute from memory.

## Existing state

Before editing:

1. resolve the active Codex home instead of assuming another user's path;
2. read its existing AGENTS.md completely if present;
3. inspect any configured project-instruction byte limit;
4. preserve every unrelated global instruction;
5. check whether an equivalent product-truth gate or full document already
   exists.

Never replace the complete global AGENTS.md.

Never copy project-specific product, language, framework, database, storage,
build, test, release, or repository-path rules into the global layer.

Do not expose credentials, tokens, environment values, or unrelated config
content while inspecting the Codex home.

## Installation

1. Install the canonical full document as
   <active-codex-home>/product-truth-governance.md.
2. Merge the exact Global product-truth section from
   docs/agent-governance/agents-sections.md into
   <active-codex-home>/AGENTS.md.
3. If an older equivalent section exists, reconcile or replace only that
   section. Do not append a contradictory duplicate.
4. Keep the full document out of AGENTS.md; only the compact conditional gate
   is automatically loaded.
5. Preserve the rule that primary agents, coordinating /root, authority
   workers, spec/reconciliation owners, and contract reviewers read the full
   document, while ordinary implementation, build, and runtime workers receive
   finite pinned packets.

Use apply_patch for edits.

## Required semantics

The installed result must preserve:

- the specification system is canonical product intent but is not infallible
  or self-authorizing;
- spec-first is not spec-only;
- applicable source, design, QA, runtime, history, and release evidence are
  reconciled before final implementation authority or a user decision;
- every covered task is Restore, Reconcile, Evolve, Discover, or
  Behavior-neutral;
- a Contract Change Envelope names the opened domain and protected neighbors;
- the user's request authorizes the behavior it actually names without opening
  unrelated domains;
- specification edits cannot launder agent preference, current defects, stale
  tests, or implementation convenience into intent;
- authority and stability are separate;
- Accepted and Released domains are protected;
- semantic contract changes advance a revision or epoch;
- affected stale worker packets are revalidated or retired;
- the user is asked only for a real material fork, protected cross-domain
  change, compatibility decision, or missing external authority after evidence
  closure.

## Verification

Verify:

- both target files exist and are regular files;
- the full document matches the canonical source;
- the global gate appears exactly once;
- existing global instructions remain present;
- Markdown fences and headings are valid;
- there is no trailing whitespace or unresolved placeholder;
- the global AGENTS.md remains within the configured instruction budget when
  combined with the active project's instruction layer, if such a budget is
  configured;
- no project file changed.

Report:

- resolved Codex-home path;
- changed files;
- whether an existing section was merged, replaced, or newly added;
- byte-budget result;
- verification performed;
- exact residual, if any.

Do not create a Git commit for files outside a Git repository.
