# Codex CLI MCP Integration

This guide shows how to register local MCP servers with Codex.

## Option A: Configure via CLI (recommended)
From any directory:
```
codex mcp add git-control --env PYTHONPATH=src -- \
  uv run python -m git_control.server
```

Verify:
```
codex mcp list
```

In the Codex TUI, run `/mcp` to see active servers.

## Option B: Configure via config.toml
Edit `~/.codex/config.toml` and add:
```
[mcp_servers.git-control]
command = "uv"
args = ["run", "python", "-m", "git_control.server"]

[mcp_servers.git-control.env]
PYTHONPATH = "src"
```

Notes:
- `command` and `args` define the stdio server launch command.
- Environment variables go in the `[mcp_servers.<name>.env]` table.
- The CLI and IDE extension share the same config file.
