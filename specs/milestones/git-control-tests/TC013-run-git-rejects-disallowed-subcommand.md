# TC013: Run git rejects disallowed subcommand

## Title
Run git rejects disallowed subcommand

## Spec Summary
Validate `run_git` enforces the allowlist of subcommands.

## Spec Goal
Prevent unsafe or unsupported git operations.

## DoD checklist
- [ ] Calling `run_git(["clone", ...])` raises `ValueError`
