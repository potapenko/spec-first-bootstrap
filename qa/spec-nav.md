# Spec Nav verification

Basis: [bootstrap.spec-nav@1](../docs/specs/features/spec-nav.md).
This file describes repeatable checks, not captured command output.
The operator authorized CLI implementation and current-spec checks only.

## Focused automated checks

Run `cargo test --locked --manifest-path tools/spec-nav/Cargo.toml` with
`CARGO_TARGET_DIR` in a task-owned system temporary directory.
The CLI integration tests create and remove their own text-only temp fixtures.

| Contract | Action and expected result |
| --- | --- |
| NAV.MAP | Default root and explicit branch expose only their own links; unopened targets may be absent. |
| NAV.MAP, NAV.SOURCE | Multiline items, reference links and table rows retain source context and line positions. |
| NAV.SOURCE | Code examples and image destinations do not become edges; unresolved references are diagnosed. |
| NAV.READ | Output matches original UTF-8 bytes, including CRLF and absent trailing newline; fragments still return the full source. |
| NAV.DEPS | A diamond lists each dependency once with every incoming reason; source order is deterministic. |
| NAV.DEPS | Only Dependency/Dependencies level-two sections and their subsections are traversed. Ordinary cycles are ignored. |
| NAV.ERROR | Dependency cycles, absent files, invalid fragments and unsupported targets produce incomplete reports and exit 1; independent edges continue. |
| NAV.SOURCE | Encoded paths/fragments and duplicate headings resolve; lexical and symlink escapes fail on opening. |
| NAV.SOURCE | Subsequent invocations read edited files; no cache state exists. |
| NAV.ERROR | Oversized declared nodes cannot be traversed, but read can expose the full source. |
| NAV.ERROR | Invalid UTF-8 and malformed paths fail; usage errors exit 2. |

## Current-tree checks

From the repository root, using the locally built binary:

1. `map`: root descriptions and outgoing paths match docs/specs/README.md.
2. `map docs/specs/features/README.md`: includes the optional navigator contract.
3. `read docs/specs/features/spec-nav.md`: compare output bytes with that file.
4. `deps docs/specs/features/spec-nav.md`: the two routing contracts are listed;
   the QA link outside Dependencies is not followed.
5. `deps docs/specs/features/legacy-spec-migration.md`: the existing routing and
   task-scope dependencies are listed without loading migration child bodies.
6. Run the existing Markdown structural checker on the specification root and
   the focused Python Markdown-checker tests. No rewrite of that checker.

Do not treat successful tests as evidence of reduced agent time or tokens.

## Deferred agent-efficiency pilot

Not authorized by the first implementation request; do not launch other chats,
workers or model calls to perform it. A later explicitly authorized experiment
may compare ordinary file/search tools with the same tools plus spec-nav.
Use fresh contexts, the same repository revision/model/settings and fixed
prompts. Both arms receive the same instructions and must read full selected
contracts; do not give one arm the answer or an already completed traversal.

Before running, pin expected contracts, required clauses, dependencies and
acceptable alternative routes for six tasks: node size, Markdown-routing
selection, mandatory dependency reading, a nontrivial dependency chain,
a damaged fixture route, and behavior absent from the selected branch.
Keep real-project tasks separate from synthetic error fixtures in analysis.

Measure correctness and omissions first, then all read context (including
instructions/errors), actions and time. Use exact token usage only when
available; otherwise report text bytes without calling them tokens. The proposed
continuation threshold is no correctness regression, at least 20% lower median
read volume and no higher median action count. This is a small pilot, not a
general productivity claim. Borderline results require evidence, not automatic
feature expansion. Run logs remain temporary; no logs are committed here.
