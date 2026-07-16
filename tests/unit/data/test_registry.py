from pathlib import Path

import pandas as pd

from lassa_fever_forecast.data.registry import (
    update_registry,
)


def test_update_registry(
    tmp_path: Path,
) -> None:
    registry = tmp_path / "registry.csv"

    update_registry(
        registry,
        filename="sample.csv",
        checksum="abc123",
    )

    df = pd.read_csv(registry)

    assert len(df) == 1

    assert df.iloc[0]["filename"] == "sample.csv"
