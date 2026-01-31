# TC004: Stage deletions rejects empty list

## Title
Stage deletions rejects empty list

## Spec Summary
Validate `stage_deletions` rejects an empty file list.

## Spec Goal
Avoid silent no-op behavior when deletion inputs are missing.

## DoD checklist
- [x] Calling `stage_deletions([])` raises `ValueError`
