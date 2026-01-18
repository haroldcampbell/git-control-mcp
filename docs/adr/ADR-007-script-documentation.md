# ADR-007: Document Scripts

## Status
Accepted

## Date
2026-01-17

## Context
The repository includes multiple scripts for running the server and invoking git-control tools.
Without documentation, usage details are easy to miss.

## Decision Drivers
- Reduce onboarding friction
- Keep script behavior discoverable

## Decision
Maintain `scripts/README.md` describing the purpose and usage of each script.

## Consequences
- Script additions or changes must update `scripts/README.md`.
- Docs remain consistent with actual script inventory.
