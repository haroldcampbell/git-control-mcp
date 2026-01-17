#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=src uv run python - "$@" <<'PY'
import asyncio
import subprocess
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def current_branch() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        text=True,
    ).strip()


async def main() -> None:
    root = Path.cwd()
    branch = sys.argv[1] if len(sys.argv) > 1 else current_branch()

    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "git_control.server"],
        env={"PYTHONPATH": str(root / "src")},
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(
                "push_branch",
                arguments={"branch": branch},
            )
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
PY
