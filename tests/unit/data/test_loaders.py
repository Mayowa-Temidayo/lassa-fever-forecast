from pathlib import Path

import pandas as pd

from lassa_fever_forecast.data.loaders import load_csv


def test_load_csv(tmp_path: Path) -> None:
    """
    Ensure load_csv correctly loads a CSV file.
    """

    sample = pd.DataFrame(
        {
            "A": [1, 2],
            "B": [3, 4],
        }
    )

    csv_file = tmp_path / "sample.csv"

    sample.to_csv(
        csv_file,
        index=False,
    )

    loaded = load_csv(csv_file)

    pd.testing.assert_frame_equal(
        sample,
        loaded,
    )
