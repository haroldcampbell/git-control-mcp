"""Minimal stdio client for the weather server."""
import asyncio
from pathlib import Path
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "weather.server"],
        env={"PYTHONPATH": str(project_root / "src")},
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Tools:", [tool.name for tool in tools.tools])

            forecast = await session.call_tool(
                "get_forecast",
                arguments={"latitude": 37.7749, "longitude": -122.4194},
            )
            print(forecast)

            alerts = await session.call_tool(
                "get_alerts",
                arguments={"state": "CA"},
            )
            print(alerts)


if __name__ == "__main__":
    asyncio.run(main())
