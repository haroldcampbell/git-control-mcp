#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
DIST_PATH="${DIST_PATH:-}"

echo "Building git-control-mcp (onedir) from: ${ROOT_DIR}"

(
  cd "${ROOT_DIR}"

  uv sync --group dev

  rm -rf "${ROOT_DIR}/build" "${ROOT_DIR}/dist"

  if [[ -n "${DIST_PATH}" ]]; then
    uv run pyinstaller --distpath "${DIST_PATH}" git_control_onedir.spec
  else
    uv run pyinstaller git_control_onedir.spec
  fi
)
