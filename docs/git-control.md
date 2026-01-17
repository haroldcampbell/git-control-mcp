# Git Control MCP Server

This server exposes basic git operations over stdio.

## Run from project root
```
uv sync
PYTHONPATH=src uv run python -m git_control.server
```

Script alternative:
```
./scripts/run_git_control_server.sh
```

## Tools
### stage_files
Stages a list of files in the target repo.

Arguments:
- `files`: list of file paths relative to the repo root
- `repo_path`: optional path within the repo to infer the git root

### commit_changes
Commits staged and unstaged changes in the target repo.

Arguments:
- `message`: commit message
- `repo_path`: optional path within the repo to infer the git root

Notes:
- Empty commits are rejected (no changes detected).

### create_pull_request
Creates a GitHub pull request using the `gh` CLI.

Arguments:
- `repo_path`: optional path within the repo to infer the git root
- `base`: base branch name (optional)
- `head`: head branch name (optional)
- `title`: PR title (optional; requires `body`)
- `body`: PR body (optional; requires `title`)
- `draft`: create as draft (default false)

Notes:
- If `title`/`body` are omitted, the server uses `gh pr create --fill`.
