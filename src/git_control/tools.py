"""MCP tool implementations for git control."""
from __future__ import annotations

from dataclasses import dataclass
import logging
from pathlib import Path
import subprocess
from typing import Iterable, Sequence

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class CommandResult:
    stdout: str
    stderr: str


def _run_command(args: list[str], cwd: Path) -> CommandResult:
    logger.info("Running command: %s (cwd=%s)", " ".join(args), cwd)
    try:
        completed = subprocess.run(
            args,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        stdout = (exc.stdout or "").strip()
        stderr = (exc.stderr or "").strip()
        logger.error("Command failed: %s (cwd=%s)", " ".join(args), cwd)
        if stdout:
            logger.error("stdout: %s", stdout)
        if stderr:
            logger.error("stderr: %s", stderr)
        raise RuntimeError(
            "Command failed.\n"
            f"cmd: {' '.join(args)}\n"
            f"cwd: {cwd}\n"
            f"stdout: {stdout}\n"
            f"stderr: {stderr}".strip()
        ) from exc
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

def _normalize_args(extra_args: Sequence[str] | None) -> list[str]:
    return [str(arg) for arg in extra_args] if extra_args else []


def _contains_any(values: Sequence[str], candidates: set[str]) -> bool:
    return any(value in candidates for value in values)


def _validate_branch_name(branch: str, repo_root: Path) -> None:
    if not branch.strip():
        raise ValueError("branch must be non-empty")
    _run_command(["git", "-C", str(repo_root), "check-ref-format", "--branch", branch], cwd=repo_root)


def _format_result(result: CommandResult) -> str:
    if result.stderr:
        return f"{result.stdout}\n{result.stderr}".strip()
    return result.stdout


def stage_files(
    files: Iterable[str],
    repo_path: str | None = None,
    extra_args: Sequence[str] | None = None,
) -> str:
    """Stage files in a git repo.

    Args:
        files: Iterable of file paths relative to the repo root.
        repo_path: Optional path within the repo to target.
        extra_args: Optional list of additional git add args.
    """
    file_list = [str(path) for path in files]
    if not file_list:
        raise ValueError("files must include at least one path")

    repo_root = _resolve_repo_root(repo_path)
    args = _normalize_args(extra_args)
    result = _run_command(["git", "-C", str(repo_root), "add", *args, "--", *file_list], cwd=repo_root)
    return _format_result(result) or "Files staged."


def stage_deletions(
    files: Iterable[str],
    repo_path: str | None = None,
    extra_args: Sequence[str] | None = None,
) -> str:
    """Stage deletions in a git repo.

    Args:
        files: Iterable of file or directory paths relative to the repo root.
        repo_path: Optional path within the repo to target.
        extra_args: Optional list of additional git add args.
    """
    file_list = [str(path) for path in files]
    if not file_list:
        raise ValueError("files must include at least one path")

    repo_root = _resolve_repo_root(repo_path)
    args = _normalize_args(extra_args)
    result = _run_command(
        ["git", "-C", str(repo_root), "add", "-u", *args, "--", *file_list],
        cwd=repo_root,
    )
    return _format_result(result) or "Deletions staged."


def commit_changes(
    message: str,
    repo_path: str | None = None,
    extra_args: Sequence[str] | None = None,
) -> str:
    """Commit changes in a git repo.

    Args:
        message: Commit message.
        repo_path: Optional path within the repo to target.
        extra_args: Optional list of additional git commit args.
    """
    if not message.strip():
        raise ValueError("message must be non-empty")

    repo_root = _resolve_repo_root(repo_path)
    status = _run_command(["git", "-C", str(repo_root), "status", "--porcelain"], cwd=repo_root)
    if not status.stdout:
        raise RuntimeError("No changes to commit.")

    args = _normalize_args(extra_args)
    result = _run_command(
        ["git", "-C", str(repo_root), "commit", *args, "-m", message],
        cwd=repo_root,
    )
    return _format_result(result)


def fetch(
    prune: bool = False,
    repo_path: str | None = None,
    extra_args: Sequence[str] | None = None,
) -> str:
    """Fetch updates from the default remote in a git repo.

    Args:
        prune: Whether to prune removed remote branches.
        repo_path: Optional path within the repo to target.
        extra_args: Optional list of additional git fetch args.
    """
    repo_root = _resolve_repo_root(repo_path)
    args = _normalize_args(extra_args)
    command = ["git", "-C", str(repo_root), "fetch", *args]
    if prune and "--prune" not in args:
        command.append("--prune")
    result = _run_command(command, cwd=repo_root)
    return _format_result(result) or "Fetch completed."


def create_pull_request(
    repo_path: str | None = None,
    base: str | None = None,
    head: str | None = None,
    title: str | None = None,
    body: str | None = None,
    draft: bool = False,
    extra_args: Sequence[str] | None = None,
) -> str:
    """Create a pull request using the GitHub CLI.

    Args:
        repo_path: Optional path within the repo to target.
        base: Base branch name (defaults to repo default).
        head: Head branch name (defaults to current branch).
        title: PR title (requires body if provided).
        body: PR body (requires title if provided).
        draft: Create PR as draft.
        extra_args: Optional list of additional gh pr create args.
    """
    if (title and not body) or (body and not title):
        raise ValueError("Provide both title and body, or neither to use defaults.")

    repo_root = _resolve_repo_root(repo_path)
    args = ["gh", "pr", "create"]
    extra = _normalize_args(extra_args)
    if title and body and _contains_any(extra, {"--title", "--body", "--fill"}):
        raise ValueError("extra_args cannot include --title, --body, or --fill when title/body are provided.")
    if not title and not body and _contains_any(extra, {"--title", "--body"}):
        raise ValueError("extra_args cannot include --title or --body unless title/body are provided.")

    if base:
        args.extend(["--base", base])
    if head:
        args.extend(["--head", head])
    if draft:
        args.append("--draft")

    if title and body:
        args.extend(["--title", title, "--body", body])
    else:
        if "--fill" not in extra:
            args.append("--fill")

    if extra:
        args.extend(extra)

    result = _run_command(args, cwd=repo_root)
    return _format_result(result)


def checkout_branch(
    branch: str,
    repo_path: str | None = None,
    start_point: str | None = None,
    extra_args: Sequence[str] | None = None,
) -> str:
    """Create and switch to a new branch in a git repo.

    Args:
        branch: Name of the branch to create.
        repo_path: Optional path within the repo to target.
        start_point: Optional start point (commit, tag, or branch).
        extra_args: Optional list of additional git checkout args.
    """
    repo_root = _resolve_repo_root(repo_path)
    _validate_branch_name(branch, repo_root)
    args = _normalize_args(extra_args)
    command = ["git", "-C", str(repo_root), "checkout", "-b", branch, *args]
    if start_point:
        command.append(start_point)
    result = _run_command(command, cwd=repo_root)
    return _format_result(result)


def push_branch(
    branch: str,
    repo_path: str | None = None,
    remote: str = "origin",
    set_upstream: bool = True,
    extra_args: Sequence[str] | None = None,
) -> str:
    """Push a branch to origin with upstream tracking.

    Args:
        branch: Name of the branch to push.
        repo_path: Optional path within the repo to target.
        remote: Remote name (default: origin).
        set_upstream: Whether to set upstream tracking.
        extra_args: Optional list of additional git push args.
    """
    repo_root = _resolve_repo_root(repo_path)
    _validate_branch_name(branch, repo_root)
    if not remote.strip():
        raise ValueError("remote must be non-empty")
    args = _normalize_args(extra_args)
    command = ["git", "-C", str(repo_root), "push", *args]
    if set_upstream:
        command.append("-u")
    command.extend([remote, branch])
    result = _run_command(command, cwd=repo_root)
    return _format_result(result)
