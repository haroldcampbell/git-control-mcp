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
./scripts/git_control_stage_files.sh
./scripts/git_control_stage_files.sh . -- --intent-to-add
```

Notes:
The script accepts a list of paths to stage. If you provide `--`, everything after it is passed directly to `git add`.

The two lines above are separate examples: the first uses the default `.` pathspec; the second shows how to pass extra git flags (like `--intent-to-add`) while still staging `.`.

## git_control_stage_deletions.sh

Stages file deletions in the repo.

Usage:

```
./scripts/git_control_stage_deletions.sh README.md
./scripts/git_control_stage_deletions.sh README.md -- --intent-to-add
```

Notes:
Provide one or more paths. Use `--` to pass additional `git add -u` flags. Each line is a separate example invocation.

## git_control_commit_changes.sh

Commits staged changes.

Usage:

```
./scripts/git_control_commit_changes.sh "docs: update README" README.md
./scripts/git_control_commit_changes.sh "docs: update README" README.md -- --signoff
```

Notes:
Provide a commit message followed by one or more paths to stage. Use `--` to pass extra `git commit` flags. Each line is an alternative example, not a sequence.

## git_control_fetch.sh

Fetches from the default remote (optionally with prune).

Usage:

```
./scripts/git_control_fetch.sh
./scripts/git_control_fetch.sh -- --prune --tags
```

Notes:
The second line shows passing extra `git fetch` flags via `--`. These are separate example invocations.

## git_control_checkout_branch.sh

Creates and checks out a new branch.

Usage:

```
./scripts/git_control_checkout_branch.sh feature/example
./scripts/git_control_checkout_branch.sh feature/example -- origin/main
```

Notes:
The second line shows passing the start point after `--`. Each line is a standalone example.

## git_control_push_branch.sh

Pushes a branch to the remote with upstream tracking.

Usage:

```
./scripts/git_control_push_branch.sh feature/example
./scripts/git_control_push_branch.sh feature/example -- --force-with-lease
```

Notes:
Use `--` to pass extra `git push` flags. Each line is an alternative example.

## git_control_create_pull_request.sh

Creates a GitHub PR via `gh`.

Usage:

```
./scripts/git_control_create_pull_request.sh "Docs" "Update docs"
./scripts/git_control_create_pull_request.sh "Docs" "Update docs" -- --label docs
```

Notes:
Use `--` to pass extra `gh pr create` flags. Each line is an alternative example.

## git_control_run_git.sh

Runs an allowlisted git subcommand.

Usage:

```
./scripts/git_control_run_git.sh status -sb
```
