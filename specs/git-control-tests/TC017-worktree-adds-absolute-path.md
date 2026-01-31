# TC017: Worktree add requires absolute path

## Title
Worktree add requires absolute path

## Spec Summary
Verify `worktree` rejects relative paths and succeeds with absolute paths when adding a worktree.

## Spec Goal
Ensure worktree tooling enforces absolute paths and creates a new worktree.

## DoD checklist
- [ ] `worktree` rejects a relative path for `add`
- [ ] `worktree` succeeds with an absolute path and creates the worktree
