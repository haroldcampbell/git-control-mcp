# Scripts

These scripts are thin wrappers for running the git-control MCP server and its tool wrappers from the repo root.

## run_server.sh
Runs the git-control MCP server over stdio.

Usage:
```
./scripts/run_server.sh
```

## git_control_stage_files.sh
Stages files in the repo.

Usage:
```
./scripts/git_control_stage_files.sh --files README.md
```

## git_control_stage_deletions.sh
Stages file deletions in the repo.

Usage:
```
./scripts/git_control_stage_deletions.sh --files README.md
```

## git_control_commit_changes.sh
Commits staged changes.

Usage:
```
./scripts/git_control_commit_changes.sh --message "docs: update README"
```

## git_control_fetch.sh
Fetches from the default remote (optionally with prune).

Usage:
```
./scripts/git_control_fetch.sh --prune
```

## git_control_checkout_branch.sh
Creates and checks out a new branch.

Usage:
```
./scripts/git_control_checkout_branch.sh --branch feature/example
```

## git_control_push_branch.sh
Pushes a branch to the remote with upstream tracking.

Usage:
```
./scripts/git_control_push_branch.sh --branch feature/example
```

## git_control_create_pull_request.sh
Creates a GitHub PR via `gh`.

Usage:
```
./scripts/git_control_create_pull_request.sh --title "Docs" --body "Update docs"
```

## git_control_run_git.sh
Runs an allowlisted git subcommand.

Usage:
```
./scripts/git_control_run_git.sh --args status -sb
```
