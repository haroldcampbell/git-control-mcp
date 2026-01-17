#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=src uv run python - <<'PY'
import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> None:
    root = Path.cwd()
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "git_control.server"],
        env={"PYTHONPATH": str(root / "src")},
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(
                "commit_changes",
                arguments={"message": "docs: update README"},
            )
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
PY
