# ADR-003: Use stdio Transport for MCP Server

## Status
Accepted

## Date
2026-01-17

## Context
We need a transport that works well with Codex CLI and local testing.

## Decision Drivers
- Compatibility with Codex CLI
- Simple local testing and tooling

## Decision
Run the MCP server with `FastMCP(...).run(transport="stdio")`.

## Consequences
- Compatible with Codex CLI and stdio-based clients.
- Requires a client process to manage the server lifecycle.
