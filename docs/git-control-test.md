# Git Control MCP Server Test Plan

This plan validates the git-control MCP server end-to-end: fetching, branch creation, staging, deletion staging, committing, pushing, and PR creation.

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
- You are on a base branch (example: `main`).
- The repo has at least one file you can safely modify.

## Test plan
1. Fetch latest changes via `fetch`.
2. Create a new branch via `checkout_branch`.
3. Edit a file (example: append a line to `README.md`).
4. Stage the change via `stage_files`.
5. Delete a file and stage the deletion via `stage_deletions`.
6. Commit the change via `commit_changes`.
7. Push the branch via `push_branch`.
8. Create a PR via `create_pull_request`.

## Example tool calls
Fetch latest changes:
```
fetch {}
```

Create a branch:
```
checkout_branch {"branch": "feature/test-pr"}
```

Stage a file:
```
stage_files {"files": ["README.md"]}
```

Stage deletions:
```
stage_deletions {"files": ["README.md"]}
```

Commit changes:
```
commit_changes {"message": "docs: update README"}
```

Push branch:
```
push_branch {"branch": "feature/test-pr"}
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
- `fetch` reports remote updates or completes with no changes.
- `checkout_branch` switches to the new branch.
- `stage_files` reports the file staged.
- `stage_deletions` reports deletions staged.
- `commit_changes` reports a new commit SHA.
- `push_branch` reports the push result.
- `create_pull_request` returns a PR URL from GitHub.
