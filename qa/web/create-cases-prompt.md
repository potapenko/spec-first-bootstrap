You are writing browser QA cases for a web product.

Your job is to extract functional behavior from the product and turn it into
small executable browser cases.

If the project has an active spec registry and governing product contract, read
them first. Otherwise identify the user objective and the project's existing
source of expected behavior. Treat source and browser behavior as evidence. If
no reliable authority exists, record that gap instead of inventing intent; do
not install a specification system as part of this QA task.

## Rules

- Use a real browser to validate behavior before writing a case.
- Do not write cases that only check static text visibility unless text
  rendering itself is the feature.
- Prefer one behavior per case.
- Prefer DOM-checkable expected results.
- Include:
  - stable QA scenario ID
  - governing contract revision or clause IDs when available
  - source reference
  - code reference
  - functional interpretation
  - preconditions
  - steps
  - expected results
  - no-console-errors check
  - no-failed-network-requests check

## Good sources of candidate cases

- routes
- filters
- playback controls
- forms
- modals
- deeplinks
- gating and permissions
- state transitions

## Output goal

Create a small set of meaningful browser cases that verify behavior instead of
copy.
