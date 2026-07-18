import pandas as pd

from lassa_fever_forecast.data.profiler import (
    profile_dataset,
)


def test_profile_dataset() -> None:
    df = pd.DataFrame(
        {
            "A": [1, 2],
            "B": [3, None],
        }
    )

    profile = profile_dataset(df)

    assert profile["rows"] == 2

    assert profile["columns"] == 2

    assert profile["duplicate_rows"] == 0

    assert profile["missing_values"]["B"] == 1
