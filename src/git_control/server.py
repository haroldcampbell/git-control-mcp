"""FastMCP server wiring for git control."""
from mcp.server.fastmcp import FastMCP

from . import tools

mcp = FastMCP("git-control")


@mcp.tool()
async def stage_files(files: list[str], repo_path: str | None = None) -> str:
    return tools.stage_files(files=files, repo_path=repo_path)


@mcp.tool()
async def commit_changes(message: str, repo_path: str | None = None) -> str:
    return tools.commit_changes(message=message, repo_path=repo_path)


@mcp.tool()
async def create_pull_request(
    repo_path: str | None = None,
    base: str | None = None,
    head: str | None = None,
    title: str | None = None,
    body: str | None = None,
    draft: bool = False,
) -> str:
    return tools.create_pull_request(
        repo_path=repo_path,
        base=base,
        head=head,
        title=title,
        body=body,
        draft=draft,
    )


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
