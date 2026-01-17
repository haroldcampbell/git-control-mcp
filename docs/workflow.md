# Workflow

This project uses a specs-driven loop for learning and implementation, constrained by ADRs.

## Guardrails
- ADRs are the source of truth for architectural and process decisions.
- Specs must align with ADRs; if a spec conflicts with an ADR, pause and consult the developer.
- ADRs must not be changed without explicit developer direction.

## Steps
1. Choose a spec to work on.
2. Ensure you are on a clean branch.
3. Check relevant ADRs and confirm constraints.
4. Make a plan to implement the spec.
5. Validate the plan with the user.
6. Do the work iteratively and ensure tests pass.
7. Commit the work if everything passes.
8. When a spec's DoD is complete, check off the related item in `specs/plan.md`.
9. Move to the next spec and repeat the loop.
