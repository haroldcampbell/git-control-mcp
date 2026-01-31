# TC001: Stage files stages new file

## Title
Stage files stages new file

## Spec Summary
Verify `stage_files` stages a newly created file in a repo.

## Spec Goal
Ensure the staging tool reliably adds files without requiring shell git.

## DoD checklist
- [x] `stage_files` returns a success message
- [x] `git diff --cached --name-only` includes the new file
