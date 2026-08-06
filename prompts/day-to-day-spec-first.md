Before product work:

1. read every applicable global and project-local AGENTS.md;
2. read the installed product-truth governance document;
3. read the engineering rules, spec registry, and exact governing clauses;
4. classify the task as Restore, Reconcile, Evolve, Discover, or
   Behavior-neutral;
5. establish a Contract Change Envelope with authorized and protected domains,
   evidence requirements, allowed spec delta, and contract revision.

State a provisional Spec Basis first. Then inspect the smallest complete
applicable source, design, QA, runtime, history, upstream, and release evidence
set.

Classify discrepancies as:

- implementation defect;
- specification defect or omission;
- stale or inapplicable evidence;
- authorized evolution;
- real product fork;
- external authority blocker.

Only after reconciliation:

1. state the final pinned Spec Basis;
2. update the contract first when a legitimate semantic delta is authorized;
3. record the Contract Delta and advance the affected epoch;
4. implement against that revision;
5. update QA action-state-result mappings;
6. run project verification and applicable runtime or visual checks;
7. preserve the result under the project's checkpoint policy.

Do not edit a specification merely because current implementation evidence is
different. The edit needs an external change basis.

Planning-only and investigation-only requests do not authorize implementation.
Do not rely on ad-hoc chat memory as product authority.
