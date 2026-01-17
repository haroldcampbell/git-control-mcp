# ADR-005: Remove Legacy Entrypoints

## Status
Accepted

## Context
Root-level `weather.py` shadowed the `weather` package, and `main.py` was redundant once scripts existed.

## Decision
Delete root-level `weather.py` and `main.py`.

## Consequences
- Avoids import shadowing issues.
- Users must use scripts or `PYTHONPATH=src` when running from root.
