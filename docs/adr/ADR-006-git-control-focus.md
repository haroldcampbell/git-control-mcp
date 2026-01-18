# ADR-006: Focus on Git-Control MCP Server

## Status
Accepted

## Date
2026-01-17

## Context
The project started as a learning sandbox with multiple example MCP servers and a client.
The scope has narrowed to focus on a single, production-quality git-control MCP server.

## Decision Drivers
- Reduce scope drift and maintenance burden
- Keep documentation and tooling aligned with the git-control server

## Decision
Treat this repository as a single-purpose git-control MCP server project.
Do not maintain additional example servers or clients in this repo.

## Consequences
- Docs and scripts should only reference the git-control server.
- Example clients should live outside this repository if needed.
