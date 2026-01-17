# TC012: Run git rejects empty args

## Title
Run git rejects empty args

## Spec Summary
Ensure `run_git` requires a subcommand.

## Spec Goal
Prevent ambiguous or unsafe invocations.

## DoD checklist
- [ ] Calling `run_git([])` raises `ValueError`
