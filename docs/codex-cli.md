# Codex CLI MCP Integration

This guide shows how to register local MCP servers with Codex.

## Option A: Configure via CLI (recommended)
From any directory:
```
codex mcp add git-control --env PYTHONPATH=/path/to/git-control-mcp/src -- \
  uv --project /path/to/git-control-mcp run python -m git_control.server
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
args = ["--project", "/path/to/git-control-mcp", "run", "python", "-m", "git_control.server"]

[mcp_servers.git-control.env]
PYTHONPATH = "/path/to/git-control-mcp/src"
```

Notes:
- `command` and `args` define the stdio server launch command.
- Environment variables go in the `[mcp_servers.<name>.env]` table.
- The CLI and IDE extension share the same config file.
- Codex config runs local commands only; it cannot point directly at a GitHub repo URL. Clone the repo locally and reference the absolute path instead.
