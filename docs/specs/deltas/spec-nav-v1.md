# Spec Nav v1 Contract Delta

- Change ID: `spec-nav-v1`
- Change mode: Evolve.
- Authorized by: the operator approved the preceding three-command Rust plan
  in this chat and requested implementation with tests and current-spec checks,
  explicitly excluding separate agent trials.
- Domain and clauses: `bootstrap.spec-nav`; `NAV.MAP`, `NAV.READ`, `NAV.DEPS`,
  `NAV.SOURCE`, `NAV.ERROR`.
- Previous behavior: Markdown traversal and the Python structural validator;
  no Rust navigation CLI.
- New behavior: optional read-only map/read/deps over the existing Markdown.
- Evidence basis: existing Markdown routing contracts, validator dependency
  section convention, and the user-approved plan; code does not create intent.
- Compatibility: additive, Evolving; no release or efficiency claim.
- Adjacent domains: installers, governance and the Python validator unchanged.
- QA impact: focused CLI tests and current-tree checks; no UI or agent trials.
- Specification paths: features/spec-nav.md, features/README.md, index.md.
- Review: focused author review for a local read-only tool; not independent
  acceptance. No additional agent or review session is authorized.
- New revision: `bootstrap.spec-nav@1`.

## Approved scope and implementation decisions

The approved bounded write set is tools/spec-nav/ (Cargo source, lockfile,
tests), README.md, the specification paths above, this delta and qa/spec-nav.md.
The current operator-selected branch remains in use. No global installation,
settings changes, persistent output directories, or additional agents.

The plan permits equivalent implementation details. Map resolves link paths
lexically without opening targets; deps reports unsupported external inputs as
incomplete. Full source remains readable even when an oversized declared node
cannot be traversed. These choices preserve the plan's read-only, full-source,
no-network and explicit-incompleteness boundaries.

## Discrepancy disposition

Authorized evolution: the new capability has no prior local implementation.
Agent efficiency is an explicitly deferred experiment, not an acceptance claim
for the CLI implementation. The chat contains the original plan and approval.
