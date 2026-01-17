"""MCP tool implementations for git control."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess
from typing import Iterable


@dataclass(frozen=True)
class CommandResult:
    stdout: str
    stderr: str


def _run_command(args: list[str], cwd: Path) -> CommandResult:
    completed = subprocess.run(
        args,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        check=True,
    )
    return CommandResult(stdout=completed.stdout.strip(), stderr=completed.stderr.strip())


def _resolve_repo_root(repo_path: str | None) -> Path:
    start = Path(repo_path).expanduser().resolve() if repo_path else Path.cwd()
    completed = subprocess.run(
        ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=True,
    )
    return Path(completed.stdout.strip())


def _format_result(result: CommandResult) -> str:
    if result.stderr:
        return f"{result.stdout}\n{result.stderr}".strip()
    return result.stdout


def stage_files(files: Iterable[str], repo_path: str | None = None) -> str:
    """Stage files in a git repo.

    Args:
        files: Iterable of file paths relative to the repo root.
        repo_path: Optional path within the repo to target.
    """
    file_list = [str(path) for path in files]
    if not file_list:
        raise ValueError("files must include at least one path")

    repo_root = _resolve_repo_root(repo_path)
    result = _run_command(["git", "-C", str(repo_root), "add", "--", *file_list], cwd=repo_root)
    return _format_result(result) or "Files staged."


def commit_changes(message: str, repo_path: str | None = None) -> str:
    """Commit changes in a git repo.

    Args:
        message: Commit message.
        repo_path: Optional path within the repo to target.
    """
    if not message.strip():
        raise ValueError("message must be non-empty")

    repo_root = _resolve_repo_root(repo_path)
    status = _run_command(["git", "-C", str(repo_root), "status", "--porcelain"], cwd=repo_root)
    if not status.stdout:
        raise RuntimeError("No changes to commit.")

    result = _run_command(
        ["git", "-C", str(repo_root), "commit", "-m", message],
        cwd=repo_root,
    )
    return _format_result(result)


def create_pull_request(
    repo_path: str | None = None,
    base: str | None = None,
    head: str | None = None,
    title: str | None = None,
    body: str | None = None,
    draft: bool = False,
) -> str:
    """Create a pull request using the GitHub CLI.

    Args:
        repo_path: Optional path within the repo to target.
        base: Base branch name (defaults to repo default).
        head: Head branch name (defaults to current branch).
        title: PR title (requires body if provided).
        body: PR body (requires title if provided).
        draft: Create PR as draft.
    """
    if (title and not body) or (body and not title):
        raise ValueError("Provide both title and body, or neither to use defaults.")

    repo_root = _resolve_repo_root(repo_path)
    args = ["gh", "pr", "create"]

    if base:
        args.extend(["--base", base])
    if head:
        args.extend(["--head", head])
    if draft:
        args.append("--draft")

    if title and body:
        args.extend(["--title", title, "--body", body])
    else:
        args.append("--fill")

    result = _run_command(args, cwd=repo_root)
    return _format_result(result)
