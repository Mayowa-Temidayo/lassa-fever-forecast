from __future__ import annotations

from pathlib import Path

import pandas as pd

from lassa_fever_forecast.tasks.dataset_registry import DATASETS

PROJECT_ROOT = Path(__file__).resolve().parents[3]

METADATA_DIR = PROJECT_ROOT / "data" / "metadata"


def create_directory() -> None:
    """Create metadata directory if needed."""
    METADATA_DIR.mkdir(parents=True, exist_ok=True)


def create_registry() -> None:
    """Generate data_registry.csv."""

    rows = [dataset.model_dump() for dataset in DATASETS]

    df = pd.DataFrame(rows)

    df.to_csv(
        METADATA_DIR / "data_registry.csv",
        index=False,
    )


def create_dictionary() -> None:
    """Generate empty data_dictionary.csv."""

    df = pd.DataFrame(
        {
            "variable": pd.Series(dtype="string"),
            "description": pd.Series(dtype="string"),
            "dtype": pd.Series(dtype="string"),
            "units": pd.Series(dtype="string"),
            "dataset_id": pd.Series(dtype="string"),
        }
    )

    df.to_csv(
        METADATA_DIR / "data_dictionary.csv",
        index=False,
    )


def create_checksums() -> None:
    """Generate empty checksums.csv."""

    df = pd.DataFrame(
        {
            "file": pd.Series(dtype="string"),
            "sha256": pd.Series(dtype="string"),
            "created_at": pd.Series(dtype="string"),
        }
    )

    df.to_csv(
        METADATA_DIR / "checksums.csv",
        index=False,
    )


def main() -> None:
    create_directory()

    create_registry()

    create_dictionary()

    create_checksums()

    print()

    print("=" * 60)
    print("PROJECT METADATA CREATED")
    print("=" * 60)

    print()

    for file in sorted(METADATA_DIR.glob("*")):
        print(file.name)

    print()


if __name__ == "__main__":
    main()
