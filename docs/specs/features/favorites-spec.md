# Favorites Spec

## Goal

Define favorites as a user-managed set of saved phrase collections that can be
reused across search and reels.

## Scope

This spec covers:

- favorites collection slots
- collection switching behavior
- import and export behavior
- collection delete and empty-state behavior
- shuffle behavior for favorites-backed flows

## Non-goals

- general search query persistence outside favorites
- backend storage internals
- premium access rules for favorites entry points

## User-visible behavior

- Favorites are organized into visible collection slots rather than one flat
  list.
- A user should always be able to move between existing collections without
  losing the current collection identity.
- The UI should preserve one trailing empty slot when the visible collections
  are not yet at capacity.
- Visible favorites collection slots are capped at five.
- Import should append only recognized heading lines to the current collection
  and should not delete existing items.
- Favorites import is a merge or append flow, not a destructive replace flow.
  The product should protect the user's already saved phrases by default.
- Export should return only the current collection's saved heading entries.
- Deleting or clearing a collection should compact the visible slot layout and
  preserve exactly one empty slot. Because deletion acts on the currently
  active collection, the UI should then show that empty slot as the place for
  the next import or rebuild flow.
- Favorites shuffle should remain deterministic within the active seed and
  paging state and should reset correctly when the shuffle context changes.
- On desktop and mobile favorites surfaces, the collection selector dots
  should stay left-aligned while collection actions stay right-aligned in the
  same toolbar region, separated by flexible empty space instead of ad-hoc
  centering.
- The shared selector should keep its neutral current-dot styling across
  favorites and other selector consumers.

## Invariants

- Search and reels must agree on the active favorites collection.
- Collection switching in reels resets the active reel to the first item for
  that collection.
- Import and export must operate on the current collection only.
- Import must not silently discard the existing current collection before
  adding new items.
- Empty-state labeling must remain accurate after add, delete, and import
  flows.

## Edge cases and failure policy

- Import files may contain non-heading annotation text, which should be ignored
  instead of treated as favorites.
- Duplicate imported lines may be merged or deduplicated, but the user should
  get understandable feedback about what was added versus already present.
- Toolbar actions must remain usable on mobile layouts and at larger text zoom.
- If there are fewer than five collections, the UI should preserve the next
  empty slot rather than hiding collection creation capacity.

## Route / state / data implications

- Favorites collection identity affects both search-side and reels-side views.
- Import and export APIs operate on a language plus collection-id scope.
- Shuffle behavior uses seeded pagination semantics rather than unstable
  per-refresh randomness.

## Verification mapping

- Add project-specific tests or QA cases here.
