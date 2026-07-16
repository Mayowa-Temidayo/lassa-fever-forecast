from lassa_fever_forecast.config.config_loader import (
    load_data_sources,
)


def test_epidemiology_configuration_exists() -> None:
    config = load_data_sources()

    assert "epidemiology" in config

    assert config["epidemiology"]["enabled"] is True
