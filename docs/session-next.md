# Next Session Notes

This document is a compact handoff checklist for the next agent run, separating human setup steps from agent-run validation tasks.

## Goal

Validate the git-control MCP server tools using the S006 test plan.

## Human actions (outside the agent)

1. Install dependencies:
    ```
    uv sync
    ```
2. Register the MCP server in Codex CLI:

    ```
    codex mcp add git-control --env PYTHONPATH=src -- \
      uv run python -m git_control.server
    ```

3. Verify servers are active:
    ```
    codex mcp list
    ```

### Outcomes

- [x] Installed dependencies
- [x] Registered servers
- [x] Verified servers

## Agent actions (next session)

- Follow the test plan in `docs/git-control-test.md` (S006).
- Run the git-control server from project root:
    ```
    PYTHONPATH=src uv run python -m git_control.server
    ```
- Execute tool calls to validate behavior:
    ```
    stage_files {"files": ["README.md"]}
    commit_changes {"message": "docs: update README"}
    create_pull_request {"title": "Docs update", "body": "Update README content"}
    ```

### Outcomes

- [ ] Completed S006 tool validation
- [ ] Ran server
- [ ] Executed tool calls
    - [ ] stage_files
    - [ ] commit_changes
    - [ ] create_pull_request

## Next spec

No next spec queued.
