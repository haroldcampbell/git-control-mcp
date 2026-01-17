# Git Control MCP Server Test Plan

This plan validates the git-control MCP server end-to-end: staging, committing, and PR creation.

## Run from project root
```
uv sync
PYTHONPATH=src uv run python -m git_control.server
```

Script alternative:
```
./scripts/run_git_control_server.sh
```

## Preconditions
- `gh` is installed and authenticated (`gh auth status`).
- You are on a non-protected branch or a new branch.
- The repo has at least one file you can safely modify.

## Test plan
1. Edit a file (example: append a line to `README.md`).
2. Stage the change via `stage_files`.
3. Commit the change via `commit_changes`.
4. Create a PR via `create_pull_request`.

## Example tool calls
Stage a file:
```
stage_files {"files": ["README.md"]}
```

Commit changes:
```
commit_changes {"message": "docs: update README"}
```

Create a PR (explicit title/body):
```
create_pull_request {"title": "Docs update", "body": "Update README content"}
```

Create a PR (auto-fill from commits):
```
create_pull_request {}
```

## Expected results
- `stage_files` reports the file staged.
- `commit_changes` reports a new commit SHA.
- `create_pull_request` returns a PR URL from GitHub.
