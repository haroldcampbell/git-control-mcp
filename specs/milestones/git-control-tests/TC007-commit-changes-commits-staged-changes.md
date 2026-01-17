# TC007: Commit changes commits staged changes

## Title
Commit changes commits staged changes

## Spec Summary
Verify `commit_changes` creates a commit when staged changes exist.

## Spec Goal
Ensure commit flow works end-to-end for staged files.

## DoD checklist
- [x] `commit_changes` writes a commit with the provided message
- [x] `git log -1` shows the expected subject
