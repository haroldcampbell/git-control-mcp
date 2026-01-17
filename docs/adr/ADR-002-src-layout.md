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
- `src/weather` for MCP server code
- `src/client` for local MCP client utilities

## Consequences
- Imports are clearer and less prone to accidental shadowing.
- Requires setting `PYTHONPATH=src` or using scripts when running from project root.
