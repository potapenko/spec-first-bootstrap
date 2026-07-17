Use the strict spec-first workflow at:

https://github.com/potapenko/spec-first-bootstrap/blob/master/docs/spec-first-workflow.md

Repair this project's spec-first development workflow. This is a workflow and
documentation migration only: do not change product implementation code.

First read, in this order:

1. every applicable `AGENTS.md`, `AGENTS.override.md`, or equivalent agent
   instruction file;
2. the project's onboarding, planning, development, and Git workflow docs;
3. `docs/specs/README.md`, the spec index or registry, and the smallest sample
   of active and historical specs needed to audit authority and precedence;
4. existing day-to-day, greenfield, brownfield, and implementation prompts.

Preserve all project-specific safety, permissions, build, test, release, Git,
and operator rules. Do not replace the whole instruction system with the
bootstrap template.

Then make the smallest coherent changes needed so that:

1. a Mandatory Spec Gate appears near the top of the main agent entry point;
2. the gate covers product features, behavioral bugs, behavioral
   investigations, product-behavior plans, and potentially behavioral
   refactors;
3. before implementation source is opened, the agent must read the spec README,
   index, and all active relevant specs;
4. the agent must state a visible Spec Basis containing authoritative paths,
   expected behavior, invariants, gaps or conflicts, spec impact, and whether
   implementation is authorized;
5. missing or conflicting behavior is settled in specs before implementation;
6. any behavior-changing spec edit occurs before the first implementation edit;
7. code, tests, runtime output, screenshots, and Git history are explicitly
   treated as evidence of current behavior, not as product intent;
8. behavioral diagnosis derives expected behavior from specs first, actual
   behavior from evidence second, and names the discrepancy before a fix;
9. planning-only and investigation-only requests are hard stops on
   implementation until the user explicitly authorizes it;
10. explicit brownfield discovery may inspect source only after recording that
    reliable specs are missing, and must create first-pass specs without
    changing product code;
11. wording such as `before or alongside implementation` is removed;
12. the spec index clearly distinguishes active contracts from historical,
    legacy, deferred, and superseded evidence and defines precedence where
    active specs overlap;
13. onboarding and prompt files repeat the same routing without creating a
    weaker competing version of the gate.

Do not invent or rewrite product decisions merely to clean the documentation.
If active specs conflict and the correct product decision is not already clear,
record the conflict and ask the user instead of choosing from current code.

Verify the migration by:

- searching for contradictory `before or alongside` or code-first instructions;
- checking every changed Markdown file for internal consistency and valid local
  links;
- running the repository's lightweight docs checks and `git diff --check`;
- reviewing the final diff to ensure no product implementation files changed;
- following the target repository's checkpoint and branch rules.

In the final response, report:

1. the files changed;
2. where the Mandatory Spec Gate now lives;
3. how active versus historical specs are selected;
4. any unresolved product-contract conflicts;
5. verification performed;
6. the checkpoint commit, when the repository requires one.
