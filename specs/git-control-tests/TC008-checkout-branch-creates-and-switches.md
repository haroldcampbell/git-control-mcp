# TC008: Checkout branch creates and switches

## Title
Checkout branch creates and switches

## Spec Summary
Confirm `checkout_branch` creates a new branch and switches HEAD.

## Spec Goal
Guarantee branch creation uses validated ref names and switches context.

## DoD checklist
- [x] HEAD reports the new branch name after `checkout_branch`
