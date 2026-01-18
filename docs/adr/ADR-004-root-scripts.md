# ADR-004: Provide Root Scripts for Running

## Status
Accepted

## Date
2026-01-17

## Context
Running modules from the project root requires `PYTHONPATH=src`, which is easy to forget.

## Decision Drivers
- Reduce friction when running from project root
- Keep commands consistent for new contributors

## Decision
Add root scripts:
- `scripts/run_server.sh`
- `scripts/git_control_stage_files.sh`
- `scripts/git_control_stage_deletions.sh`
- `scripts/git_control_commit_changes.sh`
- `scripts/git_control_fetch.sh`
- `scripts/git_control_checkout_branch.sh`
- `scripts/git_control_push_branch.sh`
- `scripts/git_control_create_pull_request.sh`
- `scripts/git_control_run_git.sh`

## Consequences
- Consistent root-level commands with no manual `PYTHONPATH` setup.
- Adds small maintenance overhead for script updates.
