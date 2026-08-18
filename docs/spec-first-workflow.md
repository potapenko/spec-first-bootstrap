# Strict Markdown-First Spec Workflow

- Node type: root
- Read when: performing product work in a project using this Bootstrap.
- Do not read when: the task is proven non-product and behavior-neutral.
- Maximum size: 100 physical lines.

Specifications establish intended behavior before implementation choices shape
it. Evidence still completes the product picture; spec-first is not spec-only.

## Required entrypoints

Installed projects use these Markdown roots:

- `docs/agent/product-truth-governance.md` for the applicable governance path;
- `docs/specs/README.md` for the product contract tree.

Bootstrap sources keep governance under `docs/agent-governance/`.

## Mandatory order

1. Re-read applicable instruction layers.
2. Open the governance Markdown root and follow only the matching links.
3. Open the specification root `README.md`.
4. Follow child descriptions one Markdown node at a time.
5. Stop at the smallest governing leaf or hybrid node.
6. Open only explicit dependency links from selected nodes.
7. Record the traversal path, revisions, dependencies, and excluded siblings.
8. Classify the task and establish the Contract Change Envelope.
9. State the provisional Spec Basis.
10. Inspect the smallest complete source/design/QA/runtime/history evidence set.
11. Classify discrepancies and accept only a legitimate Contract Delta.
12. Pin the final basis, then implement and verify the authorized slice.

Until step 9, do not inspect implementation source, interpret runtime evidence,
form a failure hypothesis, recommend a repair, or infer product intent.

## Node and context boundary

A node is a Markdown root, branch, leaf, or hybrid. Every node is at most 100
physical lines; target 50–80. Branch summaries select links but never define
child behavior. Completeness is the selected path plus explicit dependencies,
not all siblings or all descendants.

If no link governs the task, record the missing node and use Discover. Do not
promote the first code or test found into intended behavior.

## Authority and evidence

Specifications are canonical but not infallible or self-authorizing. User
authority, accepted reconciliation, and explicit precedence may change meaning.
Source, design, QA, runtime, history, and release records establish realization,
observation, acceptance, and compatibility.

Modes are Restore, Reconcile, Evolve, Discover, and Behavior-neutral. Writable
files never enlarge the authorized domain.

## Restart

After startup, resume, clear, or compaction, re-read applicable instructions,
the latest traversal receipt and envelope, then reopen only the Markdown nodes
on the selected path and the next required evidence. Start from the root again
only if the task changed or the path is missing or ambiguous.

## Validation

Check Markdown links, reachability, duplicate responsibility, dependency
cycles, and the 100-line maximum. Technical checkers are optional and never
become a routing or authority format.
