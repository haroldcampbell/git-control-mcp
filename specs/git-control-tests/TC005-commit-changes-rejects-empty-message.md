# TC005: Commit changes rejects empty message

## Title
Commit changes rejects empty message

## Spec Summary
Ensure `commit_changes` rejects blank commit messages.

## Spec Goal
Prevent low-quality or invalid commits that could harm history.

## DoD checklist
- [x] Calling `commit_changes` with blank message raises `ValueError`
