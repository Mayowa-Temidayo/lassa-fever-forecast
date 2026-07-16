from pathlib import Path

from lassa_fever_forecast.data.fetch_epidemiology import (
    get_dataset_path,
)


def test_dataset_directory_exists() -> None:
    path = get_dataset_path()

    assert isinstance(
        path,
        Path,
    )
