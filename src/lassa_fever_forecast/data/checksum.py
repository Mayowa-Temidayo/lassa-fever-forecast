from __future__ import annotations

import hashlib
from pathlib import Path


def calculate_sha256(file_path: Path) -> str:
    """
    Calculate SHA256 checksum for a file.
    """

    sha256 = hashlib.sha256()

    with file_path.open("rb") as stream:
        while chunk := stream.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()
