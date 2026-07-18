from pathlib import Path

import pandas as pd

from lassa_fever_forecast.data.loaders import load_csv


def test_load_csv(tmp_path: Path) -> None:
    csv_file = tmp_path / "sample.csv"

    expected = pd.DataFrame(
        {
            "A": [1, 2],
            "B": [3, 4],
        }
    )

    expected.to_csv(
        csv_file,
        index=False,
    )

    actual = load_csv(csv_file)

    pd.testing.assert_frame_equal(
        expected,
        actual,
    )
