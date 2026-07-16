from __future__ import annotations

from datetime import datetime
from pathlib import Path


def create_version_directory(base_directory: Path) -> Path:
    """
    Create a timestamped version directory.

    Example
    -------
    data/raw/epidemiology/2026-07-15_103000/
    """

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

    version_directory = base_directory / timestamp

    version_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return version_directory
