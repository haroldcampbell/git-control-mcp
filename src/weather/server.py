"""FastMCP server wiring."""
from mcp.server.fastmcp import FastMCP

from . import tools

mcp = FastMCP("weather")


@mcp.tool()
async def get_alerts(state: str) -> str:
    return await tools.get_alerts(state)


@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    return await tools.get_forecast(latitude, longitude)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
