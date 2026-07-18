from __future__ import annotations

from pathlib import Path

import pandas as pd

from lassa_fever_forecast.config.logging import logger
from lassa_fever_forecast.config.paths import PROCESSED_DIR
from lassa_fever_forecast.data.fetch_epidemiology import fetch
from lassa_fever_forecast.data.loaders import load_csv


def merge_datasets() -> Path:
    """
    Merge epidemiology and weather datasets into one
    forecasting dataset.
    """

    epi = load_csv(fetch())

    weather = load_csv(PROCESSED_DIR / "weather" / "weather.csv")

    epi["week_start_date"] = pd.to_datetime(epi["week_start_date"])

    weather["date"] = pd.to_datetime(weather["date"])

    weather["week_start_date"] = weather["date"] - pd.to_timedelta(
        weather["date"].dt.weekday,
        unit="D",
    )

    weekly_weather = (
        weather.groupby("week_start_date")
        .agg(
            {
                "temperature": "mean",
                "precipitation": "sum",
                "humidity": "mean",
                "wind_speed": "mean",
            }
        )
        .reset_index()
    )

    merged = epi.merge(
        weekly_weather,
        on="week_start_date",
        how="left",
    )

    output = PROCESSED_DIR / "forecast_dataset.csv"

    merged.to_csv(
        output,
        index=False,
    )

    logger.success(f"Forecast dataset saved to {output}")

    return output
