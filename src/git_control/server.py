"""FastMCP server wiring for git control."""
import logging
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from . import tools

logger = logging.getLogger(__name__)
_LOGGING_CONFIGURED = False


def configure_logging() -> None:
    global _LOGGING_CONFIGURED
    if _LOGGING_CONFIGURED or logging.getLogger().handlers:
        _LOGGING_CONFIGURED = True
        return

    log_dir = Path.cwd() / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "git-control.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )
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
async def commit_changes(message: str, repo_path: str | None = None) -> str:
    logger.info("Tool commit_changes called. repo_path=%s message_len=%s", repo_path, len(message))
    result = tools.commit_changes(message=message, repo_path=repo_path)
    logger.info("Tool commit_changes completed.")
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


def main() -> None:
    configure_logging()
    logger.info("Starting git-control MCP server.")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
