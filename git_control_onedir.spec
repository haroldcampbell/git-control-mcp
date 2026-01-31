# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller.building.api import COLLECT, EXE, PYZ
from PyInstaller.building.build_main import Analysis
from PyInstaller.utils.hooks import (
    collect_data_files,
    collect_dynamic_libs,
    collect_submodules,
    copy_metadata,
)

BLOCK_CIPHER = None

ROOT_DIR = Path.cwd()
SRC_DIR = ROOT_DIR / "src"
ENTRYPOINT = SRC_DIR / "git_control" / "__main__.py"
NAME = "git-control-mcp"

seed_datas = []
seed_binaries = []
seed_hiddenimports = []

# Seed metadata for known dependencies before auto-collection.
seed_datas += copy_metadata("mcp")
seed_datas += copy_metadata("httpx")

analysis_seed = Analysis(
    [str(ENTRYPOINT)],
    pathex=[str(SRC_DIR)],
    binaries=seed_binaries,
    datas=seed_datas,
    hiddenimports=seed_hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=BLOCK_CIPHER,
    noarchive=False,
)

extra_datas = []
extra_binaries = []
extra_hiddenimports = []

for package in ["mcp", "httpx"]:
    extra_datas += collect_data_files(package)
    extra_binaries += collect_dynamic_libs(package)
    extra_hiddenimports += collect_submodules(package)

analysis = Analysis(
    [str(ENTRYPOINT)],
    pathex=[str(SRC_DIR)],
    binaries=seed_binaries + extra_binaries,
    datas=seed_datas + extra_datas,
    hiddenimports=seed_hiddenimports + extra_hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=BLOCK_CIPHER,
    noarchive=False,
)

pyz = PYZ(analysis.pure, analysis.zipped_data, cipher=BLOCK_CIPHER)

exe = EXE(
    pyz,
    analysis.scripts,
    exclude_binaries=True,
    name=NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)

coll = COLLECT(
    exe,
    analysis.binaries,
    analysis.zipfiles,
    analysis.datas,
    strip=False,
    upx=True,
    name=NAME,
)
