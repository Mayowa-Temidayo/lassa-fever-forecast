from __future__ import annotations

from pathlib import Path

import requests

from lassa_fever_forecast.config.logging import logger
from lassa_fever_forecast.config.paths import RAW_DIR

NASA_POWER_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"


def fetch_weather(
    latitude: float,
    longitude: float,
    start: str,
    end: str,
) -> Path:
    """
    Download weather observations from NASA POWER.
    """

    params = {
        "parameters": "T2M,PRECTOTCORR,RH2M,WS2M",
        "community": "AG",
        "latitude": latitude,
        "longitude": longitude,
        "start": start,
        "end": end,
        "format": "JSON",
    }

    logger.info("Downloading NASA POWER weather data...")

    response = requests.get(
        NASA_POWER_URL,
        params=params,
        timeout=60,
    )

    response.raise_for_status()

    output_dir = RAW_DIR / "weather"

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = output_dir / "weather.json"

    output_file.write_text(
        response.text,
        encoding="utf-8",
    )

    logger.success(f"Weather data saved to {output_file}")

    return output_file
