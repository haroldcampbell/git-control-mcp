# TC011: Fetch prune removes stale remote ref

## Title
Fetch prune removes stale remote ref

## Spec Summary
Verify `fetch` with `prune=True` removes deleted remote refs.

## Spec Goal
Prevent stale remote refs from persisting in local repos.

## DoD checklist
- [x] `origin/stale` appears after initial fetch
- [x] `origin/stale` disappears after `fetch(prune=True)`
