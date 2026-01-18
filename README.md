# MCP Git Server

This project is a learning sandbox for a git MCP server.

## Structure

```
.
├── src
│   ├── git_control
│   │   ├── tools.py    # Git MCP tool implementations
│   │   └── server.py   # FastMCP wiring and entrypoint
```

## Run the server

Run from the project root so `uv` can resolve `pyproject.toml` and `uv.lock`.

```
uv sync
PYTHONPATH=src uv run python -m git_control.server
```

If you prefer running directly from the `src/` folder (so `PYTHONPATH` is implicit):

```
cd src
uv run python -m git_control.server
```

## Scripts

From the project root:

```
./scripts/run_server.sh
```

## Run the tests

From the project root:

```
uv sync
uv run pytest
```

## Codex CLI

See `docs/codex-cli.md` for MCP registration and verification steps.

## MCP test example

See `docs/git-control-test.md` for git-control verification steps.
