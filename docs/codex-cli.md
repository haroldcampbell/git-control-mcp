# Codex CLI MCP Integration

This guide shows how to register the local MCP weather server with Codex.

## Option A: Configure via CLI (recommended)
From any directory:
```
codex mcp add weather --env PYTHONPATH=src -- \
  uv run python -m weather.server
```

Verify:
```
codex mcp list
```

In the Codex TUI, run `/mcp` to see active servers.

## Option B: Configure via config.toml
Edit `~/.codex/config.toml` and add:
```
[mcp_servers.weather]
command = "uv"
args = ["run", "python", "-m", "weather.server"]

[mcp_servers.weather.env]
PYTHONPATH = "src"
```

Notes:
- `command` and `args` define the stdio server launch command.
- Environment variables go in the `[mcp_servers.<name>.env]` table.
- The CLI and IDE extension share the same config file.
