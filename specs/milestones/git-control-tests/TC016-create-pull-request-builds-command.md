# TC016: Create pull request builds command

## Title
Create pull request builds command

## Spec Summary
Validate `create_pull_request` assembles the correct gh args with and without title/body.

## Spec Goal
Ensure tool output stays compatible with GitHub CLI expectations.

## DoD checklist
- [ ] Default invocation includes `--fill`
- [ ] Title/body invocation uses `--title` and `--body` without `--fill`
