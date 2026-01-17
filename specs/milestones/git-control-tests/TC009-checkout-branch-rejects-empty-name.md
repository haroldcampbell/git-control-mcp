# TC009: Checkout branch rejects empty name

## Title
Checkout branch rejects empty name

## Spec Summary
Ensure `checkout_branch` rejects blank branch names.

## Spec Goal
Prevent invalid branches that could corrupt git history.

## DoD checklist
- [ ] Calling `checkout_branch` with blank branch name raises `ValueError`
