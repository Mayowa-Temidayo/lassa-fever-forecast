from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from lassa_fever_forecast.config.logging import logger
from lassa_fever_forecast.config.paths import PROCESSED_DIR, RAW_DIR


def process_weather(
    input_file: Path | None = None,
    output_file: Path | None = None,
) -> Path:
    """
    Convert NASA POWER JSON data into a tidy CSV dataset.
    """

    input_file = input_file or (RAW_DIR / "weather" / "weather.json")

    if not input_file.exists():
        raise FileNotFoundError(f"Weather file not found:\n{input_file}")

    if output_file is None:
        output_dir = PROCESSED_DIR / "weather"
        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )
        output_file = output_dir / "weather.csv"
    else:
        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    with input_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        weather = json.load(file)

    parameters = weather["properties"]["parameter"]

    df = pd.DataFrame(
        {
            "date": parameters["T2M"].keys(),
            "temperature": parameters["T2M"].values(),
            "precipitation": parameters["PRECTOTCORR"].values(),
            "humidity": parameters["RH2M"].values(),
            "wind_speed": parameters["WS2M"].values(),
        }
    )

    df["date"] = pd.to_datetime(
        df["date"],
        format="%Y%m%d",
    )

    df = df.sort_values("date")

    df.to_csv(
        output_file,
        index=False,
    )

    logger.success(f"Processed weather data saved to {output_file}")

    return output_file
