from pathlib import Path

import pandas as pd


def load_csv(path: Path) -> pd.DataFrame:
    """
    Load a CSV file.
    """

    return pd.read_csv(path)
