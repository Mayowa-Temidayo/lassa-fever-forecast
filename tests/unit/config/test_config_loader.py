from lassa_fever_forecast.config.config_loader import (
    load_data_sources,
)


def test_load_data_sources() -> None:
    config = load_data_sources()

    assert isinstance(config, dict)

    assert "epidemiology" in config

    assert "weather" in config

    assert "population" in config
