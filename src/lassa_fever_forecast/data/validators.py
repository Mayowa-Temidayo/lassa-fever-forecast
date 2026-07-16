from __future__ import annotations

import pandas as pd


def validate_required_columns(
    df: pd.DataFrame,
    required_columns: list[str],
) -> None:
    """
    Ensure required columns exist.
    """

    missing = set(required_columns) - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def validate_duplicate_rows(
    df: pd.DataFrame,
) -> None:
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        raise ValueError(f"Dataset contains {duplicates} duplicate rows.")
