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

    prune = "--prune" in args
    args = [arg for arg in args if arg != "--prune"]
    if args:
        raise SystemExit("Usage: git_control_fetch.sh [--prune] [-- <extra args>]")
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "git_control.server"],
        env={"PYTHONPATH": str(root / "src")},
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(
                "fetch",
                arguments={"prune": prune, "extra_args": extra_args or None},
            )
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
PY
