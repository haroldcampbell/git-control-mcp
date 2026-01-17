# MCP Server Test Example

This example shows a minimal stdio client that starts the server and calls both tools.
The full version lives in `src/client/weather_client.py`.

## Minimal Python client
```python
import asyncio
import sys
from pathlib import Path

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
            await session.call_tool(
                "get_forecast",
                arguments={"latitude": 37.7749, "longitude": -122.4194},
            )
            await session.call_tool(
                "get_alerts",
                arguments={"state": "CA"},
            )


if __name__ == "__main__":
    asyncio.run(main())
```

## Run from project root
```
uv sync
PYTHONPATH=src uv run python -m client.weather_client
```

Script alternative:
```
./scripts/run_client.sh
```

## Agent usage note
When calling the server via the MCP client, use the tool name and pass arguments as JSON.
For example, to fetch California alerts, call `get_alerts` with `{"state": "CA"}`.

## Suggested prompt
Use this prompt to avoid repeating JSON details:

```
Call the MCP weather server for California alerts.
Use the get_alerts tool with state CA.
Summarize the results.
```

Forecast example:
```
Call the MCP weather server for a forecast in San Francisco.
Use the get_forecast tool with latitude 37.7749 and longitude -122.4194.
Summarize the results.
```
