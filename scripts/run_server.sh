#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
uv run env PYTHONPATH=src python -m git_control.server
