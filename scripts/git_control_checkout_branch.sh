#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=src uv run python - "$@" <<'PY'
import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> None:
    root = Path.cwd()
    args = sys.argv[1:]
    extra_args: list[str] = []
    if "--" in args:
        split_index = args.index("--")
        extra_args = args[split_index + 1 :]
        args = args[:split_index]

    if len(args) < 1:
        raise SystemExit("Usage: git_control_checkout_branch.sh <branch> [start-point] [-- <extra args>]")

    branch = args[0]
    start_point = args[1] if len(args) > 1 else None
    if len(args) > 2:
        raise SystemExit("Usage: git_control_checkout_branch.sh <branch> [start-point] [-- <extra args>]")
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "git_control.server"],
        env={"PYTHONPATH": str(root / "src")},
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(
                "checkout_branch",
                arguments={
                    "branch": branch,
                    "start_point": start_point,
                    "extra_args": extra_args or None,
                },
            )
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
PY
