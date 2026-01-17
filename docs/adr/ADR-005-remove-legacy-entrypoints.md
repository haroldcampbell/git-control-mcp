# ADR-005: Remove Legacy Entrypoints

## Status
Accepted

## Date
2026-01-17

## Context
Root-level `weather.py` shadowed the `weather` package, and `main.py` was redundant once scripts existed.

## Decision Drivers
- Avoid import shadowing
- Remove redundant entrypoints

## Decision
Delete root-level `weather.py` and `main.py`.

## Consequences
- Avoids import shadowing issues.
- Users must use scripts or `PYTHONPATH=src` when running from root.
