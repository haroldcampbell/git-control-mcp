# Git Control MCP Server

This server exposes basic git operations over stdio.

## Run from project root
```
uv sync
PYTHONPATH=src uv run python -m git_control.server
```

Script alternative:
```
./scripts/run_server.sh
```

## Tools
### run_git
Runs an allowlisted git subcommand with arguments.

WARNING: Destructive operations can discard or rewrite history.

Arguments:
- `args`: list of git arguments, starting with the subcommand (example: `["status", "-sb"]`)
- `repo_path`: optional path within the repo to infer the git root

Allowed subcommands:
`add`, `branch`, `checkout`, `cherry-pick`, `clean`, `commit`, `config`, `diff`, `fetch`, `grep`,
`init`, `log`, `merge`, `mv`, `pull`, `push`, `rebase`, `reflog`, `remote`, `reset`, `restore`,
`rev-parse`, `rm`, `show`, `status`, `stash`, `switch`, `tag`, `worktree`

Notes:
- `run_git` does not enforce absolute paths for worktree arguments.

### worktree
Runs git worktree subcommands with absolute-path enforcement for worktree path arguments.

Arguments:
- `args`: list of worktree arguments, starting with the subcommand (example: `["add", "/abs/path"]`)
- `repo_path`: optional path within the repo to infer the git root

Allowed subcommands:
`add`, `list`, `lock`, `move`, `prune`, `remove`, `repair`, `unlock`

Notes:
- Worktree path arguments must be absolute.

### stage_files
Stages a list of files in the target repo.

Arguments:
- `files`: list of file paths relative to the repo root
- `repo_path`: optional path within the repo to infer the git root
- `extra_args`: optional list of additional `git add` args

### stage_deletions
Stages deletions in the target repo.

Arguments:
- `files`: list of file or directory paths relative to the repo root
- `repo_path`: optional path within the repo to infer the git root
- `extra_args`: optional list of additional `git add` args

### commit_changes
Commits staged and unstaged changes in the target repo.

Arguments:
- `message`: commit message
- `repo_path`: optional path within the repo to infer the git root
- `extra_args`: optional list of additional `git commit` args

Notes:
- Empty commits are rejected (no changes detected).

### fetch
Fetches updates from the default remote in the target repo.

Arguments:
- `prune`: optional boolean to prune removed remote branches (default: false)
- `repo_path`: optional path within the repo to infer the git root
- `extra_args`: optional list of additional `git fetch` args

### create_pull_request
Creates a GitHub pull request using the `gh` CLI.

Arguments:
- `repo_path`: optional path within the repo to infer the git root
- `base`: base branch name (optional)
- `head`: head branch name (optional)
- `title`: PR title (optional; requires `body`)
- `body`: PR body (optional; requires `title`)
- `draft`: create as draft (default false)
- `extra_args`: optional list of additional `gh pr create` args

Notes:
- If `title`/`body` are omitted, the server uses `gh pr create --fill`.

### checkout_branch
Creates and checks out a new branch in the target repo.

Arguments:
- `branch`: name of the branch to create
- `repo_path`: optional path within the repo to infer the git root
- `start_point`: optional start point (commit, tag, or branch)
- `extra_args`: optional list of additional `git checkout` args

### push_branch
Pushes a branch to `origin` with upstream tracking.

Arguments:
- `branch`: name of the branch to push
- `repo_path`: optional path within the repo to infer the git root
- `remote`: remote name (default: origin)
- `set_upstream`: whether to set upstream tracking (default: true)
- `extra_args`: optional list of additional `git push` args
