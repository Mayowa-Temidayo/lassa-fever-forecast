import pandas as pd
import pytest

from lassa_fever_forecast.data.validators import (
    validate_duplicate_rows,
    validate_required_columns,
)


def test_validate_required_columns_success() -> None:
    df = pd.DataFrame(
        {
            "A": [1],
            "B": [2],
        }
    )

    validate_required_columns(
        df,
        ["A", "B"],
    )


def test_validate_required_columns_failure() -> None:
    df = pd.DataFrame(
        {
            "A": [1],
        }
    )

    with pytest.raises(ValueError):
        validate_required_columns(
            df,
            ["A", "B"],
        )


def test_validate_duplicate_rows_success() -> None:
    df = pd.DataFrame(
        {
            "A": [1, 2],
            "B": [3, 4],
        }
    )

    validate_duplicate_rows(df)


def test_validate_duplicate_rows_failure() -> None:
    df = pd.DataFrame(
        {
            "A": [1, 1],
            "B": [2, 2],
        }
    )

    with pytest.raises(ValueError):
        validate_duplicate_rows(df)
