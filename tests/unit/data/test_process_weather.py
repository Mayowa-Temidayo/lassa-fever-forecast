import json

from lassa_fever_forecast.data.process_weather import process_weather


def test_process_weather(tmp_path) -> None:
    raw = tmp_path / "weather.json"

    processed = tmp_path / "weather.csv"

    sample = {
        "properties": {
            "parameter": {
                "T2M": {
                    "20200101": 28.0,
                    "20200102": 29.0,
                },
                "PRECTOTCORR": {
                    "20200101": 0.5,
                    "20200102": 1.2,
                },
                "RH2M": {
                    "20200101": 80,
                    "20200102": 75,
                },
                "WS2M": {
                    "20200101": 2.1,
                    "20200102": 3.0,
                },
            }
        }
    }

    raw.write_text(
        json.dumps(sample),
        encoding="utf-8",
    )

    output = process_weather(
        input_file=raw,
        output_file=processed,
    )

    assert output.exists()
    assert output == processed
