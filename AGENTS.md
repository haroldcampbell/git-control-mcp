# AGENTS

This project uses a specs-driven workflow with ADR guardrails.

- Specs live in `specs/` and are tracked in `specs/plan.md`.
- Each spec includes: Title, Spec Summary, Spec Goal, DoD checklist.
- Work items should reference the relevant spec ID (e.g., S001).
- ADRs live in `docs/adr/` and define constraints that specs must follow.
- Specs are not allowed to violate ADRs.
- ADRs must not be changed without explicit developer direction.
- Prefer git-control MCP tools over direct git commands when operating on the repo.
- Before running any change that deletes files, get user permission and explain why the deletion is needed and which files will be affected.
