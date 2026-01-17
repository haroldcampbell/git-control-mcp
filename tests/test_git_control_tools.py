import subprocess
from pathlib import Path

import pytest

from git_control import tools


def run_git(cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        check=True,
        capture_output=True,
        text=True,
    )


def init_repo(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    run_git(path, "init", "-b", "main")
    run_git(path, "config", "user.name", "Test User")
    run_git(path, "config", "user.email", "test@example.com")
    return path


def commit_file(repo: Path, filename: str, content: str, message: str) -> None:
    file_path = repo / filename
    file_path.write_text(content, encoding="utf-8")
    run_git(repo, "add", filename)
    run_git(repo, "commit", "-m", message)


def init_bare_repo(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    run_git(path, "init", "--bare")
    return path


def test_stage_files_stages_new_file(tmp_path: Path) -> None:
    repo = init_repo(tmp_path / "repo")
    file_path = repo / "new.txt"
    file_path.write_text("hello", encoding="utf-8")

    result = tools.stage_files(["new.txt"], repo_path=str(repo))

    assert "Files staged" in result
    staged = run_git(repo, "diff", "--cached", "--name-only").stdout.strip().splitlines()
    assert "new.txt" in staged


def test_stage_files_rejects_empty_list() -> None:
    with pytest.raises(ValueError):
        tools.stage_files([])


def test_stage_deletions_stages_deleted_file(tmp_path: Path) -> None:
    repo = init_repo(tmp_path / "repo")
    commit_file(repo, "delete.txt", "bye", "add delete.txt")
    (repo / "delete.txt").unlink()

    result = tools.stage_deletions(["delete.txt"], repo_path=str(repo))

    assert "Deletions staged" in result
    staged = run_git(repo, "diff", "--cached", "--name-status").stdout.strip().splitlines()
    assert "D\tdelete.txt" in staged


def test_stage_deletions_rejects_empty_list() -> None:
    with pytest.raises(ValueError):
        tools.stage_deletions([])


def test_commit_changes_rejects_empty_message(tmp_path: Path) -> None:
    repo = init_repo(tmp_path / "repo")
    (repo / "file.txt").write_text("data", encoding="utf-8")
    tools.stage_files(["file.txt"], repo_path=str(repo))

    with pytest.raises(ValueError):
        tools.commit_changes(" ", repo_path=str(repo))


def test_commit_changes_requires_changes(tmp_path: Path) -> None:
    repo = init_repo(tmp_path / "repo")

    with pytest.raises(RuntimeError):
        tools.commit_changes("no changes", repo_path=str(repo))


def test_commit_changes_commits_staged_changes(tmp_path: Path) -> None:
    repo = init_repo(tmp_path / "repo")
    (repo / "file.txt").write_text("data", encoding="utf-8")
    tools.stage_files(["file.txt"], repo_path=str(repo))

    tools.commit_changes("add file", repo_path=str(repo))

    subject = run_git(repo, "log", "-1", "--pretty=%s").stdout.strip()
    assert subject == "add file"


def test_checkout_branch_creates_and_switches(tmp_path: Path) -> None:
    repo = init_repo(tmp_path / "repo")
    tools.checkout_branch("feature/test", repo_path=str(repo))

    branch = run_git(repo, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    assert branch == "feature/test"


def test_checkout_branch_rejects_empty_name(tmp_path: Path) -> None:
    repo = init_repo(tmp_path / "repo")

    with pytest.raises(ValueError):
        tools.checkout_branch(" ", repo_path=str(repo))


def test_push_branch_pushes_to_remote(tmp_path: Path) -> None:
    repo = init_repo(tmp_path / "repo")
    commit_file(repo, "file.txt", "data", "initial")
    run_git(repo, "checkout", "-b", "feature/push")
    remote = init_bare_repo(tmp_path / "remote.git")
    run_git(repo, "remote", "add", "origin", str(remote))

    tools.push_branch("feature/push", repo_path=str(repo))

    refs = run_git(remote, "show-ref", "--verify", "refs/heads/feature/push").stdout.strip()
    assert "refs/heads/feature/push" in refs


def test_fetch_prune_removes_stale_remote_ref(tmp_path: Path) -> None:
    remote = init_bare_repo(tmp_path / "remote.git")
    seed = init_repo(tmp_path / "seed")
    commit_file(seed, "seed.txt", "seed", "seed")
    run_git(seed, "remote", "add", "origin", str(remote))
    run_git(seed, "push", "-u", "origin", "main")
    run_git(seed, "checkout", "-b", "stale")
    commit_file(seed, "stale.txt", "stale", "stale")
    run_git(seed, "push", "origin", "stale")

    client = init_repo(tmp_path / "client")
    run_git(client, "remote", "add", "origin", str(remote))
    tools.fetch(repo_path=str(client))
    remotes_before = run_git(client, "branch", "-r").stdout
    assert "origin/stale" in remotes_before

    run_git(seed, "push", "origin", "--delete", "stale")

    tools.fetch(prune=True, repo_path=str(client))
    remotes_after = run_git(client, "branch", "-r").stdout
    assert "origin/stale" not in remotes_after


def test_run_git_rejects_empty_args() -> None:
    with pytest.raises(ValueError):
        tools.run_git([])


def test_run_git_rejects_disallowed_subcommand() -> None:
    with pytest.raises(ValueError):
        tools.run_git(["clone", "https://example.com/repo.git"])


def test_run_git_adds_destructive_warning(tmp_path: Path) -> None:
    repo = init_repo(tmp_path / "repo")
    commit_file(repo, "file.txt", "data", "initial")
    warning = tools.run_git(["reset", "--hard", "HEAD"], repo_path=str(repo))

    assert warning.startswith(tools._DESTRUCTIVE_WARNING)


def test_create_pull_request_validates_title_body_pairing(tmp_path: Path) -> None:
    repo = init_repo(tmp_path / "repo")

    with pytest.raises(ValueError):
        tools.create_pull_request(repo_path=str(repo), title="title")
    with pytest.raises(ValueError):
        tools.create_pull_request(repo_path=str(repo), body="body")


def test_create_pull_request_builds_fill_command(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = init_repo(tmp_path / "repo")
    captured: dict[str, list[str]] = {}

    def fake_run(args: list[str], cwd: Path) -> tools.CommandResult:
        captured["args"] = args
        return tools.CommandResult(stdout="ok", stderr="")

    monkeypatch.setattr(tools, "_run_command", fake_run)

    tools.create_pull_request(repo_path=str(repo))

    assert captured["args"][0:3] == ["gh", "pr", "create"]
    assert "--fill" in captured["args"]


def test_create_pull_request_builds_title_body_command(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = init_repo(tmp_path / "repo")
    captured: dict[str, list[str]] = {}

    def fake_run(args: list[str], cwd: Path) -> tools.CommandResult:
        captured["args"] = args
        return tools.CommandResult(stdout="ok", stderr="")

    monkeypatch.setattr(tools, "_run_command", fake_run)

    tools.create_pull_request(repo_path=str(repo), title="Title", body="Body")

    assert "--fill" not in captured["args"]
    assert "--title" in captured["args"]
    assert "--body" in captured["args"]
