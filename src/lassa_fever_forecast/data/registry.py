from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd


def update_registry(
    registry_path: Path,
    *,
    filename: str,
    checksum: str,
) -> None:
    """
    Append dataset information to registry.
    """

    if registry_path.exists():
        registry = pd.read_csv(registry_path)

    else:
        registry = pd.DataFrame(
            {
                "filename": pd.Series(dtype="string"),
                "checksum": pd.Series(dtype="string"),
                "timestamp": pd.Series(dtype="string"),
            }
        )

    registry.loc[len(registry)] = [
        filename,
        checksum,
        datetime.now().isoformat(),
    ]

    registry.to_csv(
        registry_path,
        index=False,
    )
