# TC014: Run git adds destructive warning

## Title
Run git adds destructive warning

## Spec Summary
Verify destructive subcommands return a warning prefix.

## Spec Goal
Ensure users are warned before potentially data-destroying operations.

## DoD checklist
- [ ] `run_git(["reset", ...])` output starts with warning text
