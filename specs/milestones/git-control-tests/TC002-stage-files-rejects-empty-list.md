# TC002: Stage files rejects empty list

## Title
Stage files rejects empty list

## Spec Summary
Validate `stage_files` rejects an empty file list.

## Spec Goal
Prevent silent no-op behavior that could mask missing inputs.

## DoD checklist
- [x] Calling `stage_files([])` raises `ValueError`
