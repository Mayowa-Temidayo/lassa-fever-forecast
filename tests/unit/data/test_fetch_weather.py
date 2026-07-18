from pathlib import Path

from lassa_fever_forecast.data.fetch_weather import NASA_POWER_URL


def test_nasa_url() -> None:
    assert NASA_POWER_URL.startswith("https://")


def test_output_path() -> None:
    path = Path("data/raw/weather/weather.json")
    assert path.suffix == ".json"
