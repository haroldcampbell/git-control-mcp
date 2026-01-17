# ADR-005: Remove Legacy Entrypoints

## Status
Deprecated

## Date
2026-01-17

## Context
Root-level entrypoints can shadow package modules and become redundant once scripts exist.

## Decision Drivers
- Avoid import shadowing
- Remove redundant entrypoints

## Decision
Avoid root-level entrypoints when scripts or module runners cover the use cases.

## Consequences
- Avoids import shadowing issues.
- Users must use scripts or `PYTHONPATH=src` when running from root.
