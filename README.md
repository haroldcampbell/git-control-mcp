# MCP Server 1

This project is a learning sandbox for MCP servers/clients.

## Structure
```
.
├── src
│   ├── weather
│   │   ├── api.py      # NWS API helpers
│   │   ├── tools.py    # MCP tool implementations
│   │   └── server.py   # FastMCP wiring and entrypoint
│   └── client
│       └── weather_client.py  # Minimal stdio client
```

## Run the server
Run from the project root so `uv` can resolve `pyproject.toml` and `uv.lock`.

```
uv sync
PYTHONPATH=src uv run python -m weather.server
```

If you prefer running directly from the `src/` folder (so `PYTHONPATH` is implicit):
```
cd src
uv run python -m weather.server
```

## Run the client
Run from the project root:
```
PYTHONPATH=src uv run python -m client.weather_client
```

If you prefer running from `src/` so the `client` package is importable:
```
cd src
uv run python -m client.weather_client
```

## Scripts
From the project root:
```
./scripts/run_server.sh
./scripts/run_client.sh
```

## Codex CLI
See `docs/codex-cli.md` for MCP registration and verification steps.

## MCP test example
See `docs/mcp-test-example.md` for a minimal stdio client that calls `get_forecast`
and `get_alerts`.
