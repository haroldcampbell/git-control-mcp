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
    args = sys.argv[1:]
    extra_args: list[str] = []
    if "--" in args:
        split_index = args.index("--")
        extra_args = args[split_index + 1 :]
        args = args[:split_index]

    remote = "origin"
    set_upstream = True
    if "--no-upstream" in args:
        set_upstream = False
        args = [arg for arg in args if arg != "--no-upstream"]
    if "--remote" in args:
        remote_index = args.index("--remote")
        if remote_index + 1 >= len(args):
            raise SystemExit("Usage: git_control_push_branch.sh [branch] [--remote name] [--no-upstream] [-- <extra args>]")
        remote = args[remote_index + 1]
        args = args[:remote_index] + args[remote_index + 2 :]

    branch = args[0] if args else current_branch()
    if len(args) > 1:
        raise SystemExit("Usage: git_control_push_branch.sh [branch] [--remote name] [--no-upstream] [-- <extra args>]")

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
                arguments={
                    "branch": branch,
                    "remote": remote,
                    "set_upstream": set_upstream,
                    "extra_args": extra_args or None,
                },
            )
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
PY
