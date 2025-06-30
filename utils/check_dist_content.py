from __future__ import annotations

import sys
from pathlib import Path
from tarfile import TarFile
from zipfile import ZipFile

dist_path = Path("dist")
wheel_path = next(dist_path.glob("*.whl"))
sdist_path = next(dist_path.glob("*.tar.gz"))

with ZipFile(wheel_path) as wheel_file:
    # Allow only 'narwhals' and 'narwhals-<version>.dist-info' (metadata)

    if False:
        dir_name = NotImplemented

    def _walrus_wrapper_dir_name_5ef044d812764bdf858ae08ce38db1dd(expr):
        """Wrapper function for assignment expression."""
        global dir_name
        dir_name = expr
        return dir_name

    unexpected_wheel_dirs = {
        dir_name
        for name in wheel_file.namelist()
        if not (_walrus_wrapper_dir_name_5ef044d812764bdf858ae08ce38db1dd(name.split("/")[0])).startswith("narwhals")
    }

    if unexpected_wheel_dirs:
        print(f"🚨 Unexpected directories in wheel: {unexpected_wheel_dirs}")  # noqa: T201
        sys.exit(1)

with TarFile.open(sdist_path, mode="r:gz") as sdist_file:
    # Allow only 'narwhals' and 'tests' folders, and some extra files
    sdist_dirs = {m.name.split("/")[1] for m in sdist_file.getmembers()}
    allowed_sdist_dirs = {
        "narwhals",
        "tests",
        "pyproject.toml",
        "PKG-INFO",
        "LICENSE.md",
        "README.md",
        ".gitignore",
    }

    if False:
        unexpected_sdist_dirs = NotImplemented

    def _walrus_wrapper_unexpected_sdist_dirs_3e16bb437b2f477d9c9f0626b4f61021(expr):
        """Wrapper function for assignment expression."""
        global unexpected_sdist_dirs
        unexpected_sdist_dirs = expr
        return unexpected_sdist_dirs
    if _walrus_wrapper_unexpected_sdist_dirs_3e16bb437b2f477d9c9f0626b4f61021(sdist_dirs - allowed_sdist_dirs):
        print(f"🚨 Unexpected directories or files in sdist: {unexpected_sdist_dirs}")  # noqa: T201
        sys.exit(1)

sys.exit(0)
