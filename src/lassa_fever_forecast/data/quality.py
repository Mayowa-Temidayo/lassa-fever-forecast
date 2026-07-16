from __future__ import annotations

import pandas as pd


def check_empty_dataset(
    df: pd.DataFrame,
) -> None:
    if df.empty:
        raise ValueError("Dataset is empty.")


def check_missing_columns(
    df: pd.DataFrame,
    required: list[str],
) -> None:
    missing = set(required) - set(df.columns)

    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
