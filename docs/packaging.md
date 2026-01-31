# Packaging

This repo supports PyInstaller builds using `uv` and spec files. The onedir build is the default recommendation for faster startup.

## One-time setup

Install PyInstaller into the dev group and sync:

```
uv add --dev pyinstaller
uv sync --group dev
```

## Build (onedir, faster startup)

Use the onedir spec to avoid onefile extraction overhead:

```
uv sync --group dev
uv run pyinstaller git_control_onedir.spec
```

Run the bundled binary:

```
./dist/git-control-mcp/git-control-mcp
```

Script alternative:

```
./scripts/build_dist_onedir.sh
```

## Build (onefile)

If you need a single-file binary, use the dedicated onefile spec:

```
uv sync --group dev
uv run pyinstaller git_control_onefile.spec
```

Run the binary:

```
./dist/git-control-mcp
```

## Notes

- Build on the same CPU architecture you want to support (arm64 vs x86_64).
- Run build commands from the repo root so the spec resolves paths correctly.
- Specs auto-collect package data and hidden imports from the PyInstaller analysis graph.
- Check `build/git-control-mcp/warn-git-control-mcp.txt` after a build if the binary fails at runtime.
