# TC015: Create pull request validates title/body

## Title
Create pull request validates title/body

## Spec Summary
Ensure title and body are provided together for PR creation.

## Spec Goal
Prevent partially specified PRs that could fail in gh.

## DoD checklist
- [x] Title without body raises `ValueError`
- [x] Body without title raises `ValueError`
