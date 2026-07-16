import pandas as pd
import pytest

from lassa_fever_forecast.data.quality import (
    check_empty_dataset,
)


def test_check_empty_dataset() -> None:
    df = pd.DataFrame()

    with pytest.raises(ValueError):
        check_empty_dataset(df)
