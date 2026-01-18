# ADR-002: Use src/ Layout for Packages

## Status
Accepted

## Date
2026-01-17

## Context
We want clean separation between application packages and top-level project files.

## Decision Drivers
- Avoid import shadowing and ambiguous modules
- Keep packages and project files clearly separated

## Decision
Place Python packages under `src/`:
- `src/git_control` for the MCP server code
- additional packages may be added under `src/` as needed

## Consequences
- Imports are clearer and less prone to accidental shadowing.
- Requires setting `PYTHONPATH=src` or using scripts when running from project root.
