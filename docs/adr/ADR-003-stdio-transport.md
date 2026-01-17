# ADR-003: Use stdio Transport for MCP Server

## Status
Accepted

## Context
We need a transport that works well with Codex CLI and local testing.

## Decision
Run the MCP server with `FastMCP(...).run(transport="stdio")`.

## Consequences
- Compatible with Codex CLI and stdio-based clients.
- Requires a client process to manage the server lifecycle.
