"""FastMCP server wiring for git control."""
import logging
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from . import tools

logger = logging.getLogger(__name__)
_LOGGING_CONFIGURED = False


def configure_logging() -> None:
    global _LOGGING_CONFIGURED
    log_dir = Path.cwd() / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "git-control.log"
    if _LOGGING_CONFIGURED:
        return

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")

    has_file_handler = False
    for handler in root_logger.handlers:
        if isinstance(handler, logging.FileHandler):
            try:
                if Path(handler.baseFilename) == log_file:
                    has_file_handler = True
            except Exception:
                continue

    if not has_file_handler:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

    if not any(
        isinstance(handler, logging.StreamHandler) and not isinstance(handler, logging.FileHandler)
        for handler in root_logger.handlers
    ):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        root_logger.addHandler(stream_handler)

    _LOGGING_CONFIGURED = True


configure_logging()

mcp = FastMCP("git-control")


@mcp.tool()
async def stage_files(files: list[str], repo_path: str | None = None) -> str:
    logger.info("Tool stage_files called. files=%s repo_path=%s", files, repo_path)
    result = tools.stage_files(files=files, repo_path=repo_path)
    logger.info("Tool stage_files completed.")
    return result


@mcp.tool()
async def stage_deletions(files: list[str], repo_path: str | None = None) -> str:
    logger.info("Tool stage_deletions called. files=%s repo_path=%s", files, repo_path)
    result = tools.stage_deletions(files=files, repo_path=repo_path)
    logger.info("Tool stage_deletions completed.")
    return result


@mcp.tool()
async def commit_changes(message: str, repo_path: str | None = None) -> str:
    logger.info("Tool commit_changes called. repo_path=%s message_len=%s", repo_path, len(message))
    result = tools.commit_changes(message=message, repo_path=repo_path)
    logger.info("Tool commit_changes completed.")
    return result


@mcp.tool()
async def fetch(prune: bool = False, repo_path: str | None = None) -> str:
    logger.info("Tool fetch called. prune=%s repo_path=%s", prune, repo_path)
    result = tools.fetch(prune=prune, repo_path=repo_path)
    logger.info("Tool fetch completed.")
    return result


@mcp.tool()
async def create_pull_request(
    repo_path: str | None = None,
    base: str | None = None,
    head: str | None = None,
    title: str | None = None,
    body: str | None = None,
    draft: bool = False,
) -> str:
    logger.info(
        "Tool create_pull_request called. repo_path=%s base=%s head=%s title=%s body_len=%s draft=%s",
        repo_path,
        base,
        head,
        title,
        len(body) if body is not None else None,
        draft,
    )
    result = tools.create_pull_request(
        repo_path=repo_path,
        base=base,
        head=head,
        title=title,
        body=body,
        draft=draft,
    )
    logger.info("Tool create_pull_request completed.")
    return result


@mcp.tool()
async def checkout_branch(branch: str, repo_path: str | None = None) -> str:
    logger.info("Tool checkout_branch called. repo_path=%s branch=%s", repo_path, branch)
    result = tools.checkout_branch(branch=branch, repo_path=repo_path)
    logger.info("Tool checkout_branch completed.")
    return result


@mcp.tool()
async def push_branch(branch: str, repo_path: str | None = None) -> str:
    logger.info("Tool push_branch called. repo_path=%s branch=%s", repo_path, branch)
    result = tools.push_branch(branch=branch, repo_path=repo_path)
    logger.info("Tool push_branch completed.")
    return result


def main() -> None:
    configure_logging()
    logger.info("Starting git-control MCP server.")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
