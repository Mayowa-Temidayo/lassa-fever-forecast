from __future__ import annotations

import pandas as pd


def profile_dataset(
    df: pd.DataFrame,
) -> dict:
    """
    Return a lightweight profile of the dataset.
    """

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isna().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "memory_mb": round(
            df.memory_usage(deep=True).sum() / 1024**2,
            2,
        ),
    }
