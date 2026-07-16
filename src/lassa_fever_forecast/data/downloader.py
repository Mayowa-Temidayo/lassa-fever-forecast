from __future__ import annotations

from pathlib import Path

import requests


def download_file(
    *,
    url: str,
    destination: Path,
    timeout: int = 60,
) -> Path:
    """
    Download a file to disk.

    Returns
    -------
    Path
        Downloaded file.
    """

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    response = requests.get(
        url,
        timeout=timeout,
    )

    response.raise_for_status()

    destination.write_bytes(
        response.content,
    )

    return destination
