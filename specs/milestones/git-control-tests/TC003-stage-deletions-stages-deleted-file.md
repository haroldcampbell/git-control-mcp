# TC003: Stage deletions stages deleted file

## Title
Stage deletions stages deleted file

## Spec Summary
Confirm `stage_deletions` stages a removal.

## Spec Goal
Ensure deletions are captured in the index to prevent accidental loss.

## DoD checklist
- [ ] `stage_deletions` returns a success message
- [ ] `git diff --cached --name-status` includes `D` for the deleted file
