from __future__ import annotations

from pathlib import Path

import yaml

CONFIG_DIR = Path(__file__).resolve().parent

DATA_SOURCES = CONFIG_DIR / "data_sources.yaml"


def load_data_sources() -> dict:
    """
    Load the project's data source configuration.
    """

    with DATA_SOURCES.open(
        "r",
        encoding="utf-8",
    ) as stream:
        return yaml.safe_load(stream)
