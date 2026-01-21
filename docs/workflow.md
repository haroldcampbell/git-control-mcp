# Workflow

This project uses a specs-driven loop for learning and implementation, constrained by ADRs.

## Guardrails
- ADRs are the source of truth for architectural and process decisions.
- Specs must align with ADRs; if a spec conflicts with an ADR, pause and consult the developer.
- ADRs must not be changed without explicit developer direction.
- Always work on a feature branch; do not do work directly on `main`.
- Never push or merge to `origin/main` without explicit developer direction.
- Only create a PR when the developer explicitly requests it.

## Steps
1. Choose a spec to work on.
2. Create a new branch for the work.
3. Check relevant ADRs and confirm constraints.
4. Make a plan to implement the spec.
5. Validate the plan with the user.
6. Do the work iteratively and ensure tests pass (default: `UV_CACHE_DIR=/tmp/uv-cache uv run pytest`).
7. Stage and commit the work on the new branch if everything passes.
8. When a spec's DoD is complete, check off the related item in `specs/plan.md`.
9. Push the branch and open a PR.
10. Move to the next spec and repeat the loop.
