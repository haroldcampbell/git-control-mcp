# TC006: Commit changes requires changes

## Title
Commit changes requires changes

## Spec Summary
Validate `commit_changes` fails when there are no changes to commit.

## Spec Goal
Avoid empty commits that mask the real repository state.

## DoD checklist
- [x] Calling `commit_changes` on a clean repo raises `RuntimeError`
