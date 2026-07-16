from __future__ import annotations

from pathlib import Path

from lassa_fever_forecast.config.config_loader import load_data_sources
from lassa_fever_forecast.config.paths import PROJECT_ROOT


def get_dataset_path() -> Path:
    """
    Return the expected location of the epidemiology dataset.
    """

    config = load_data_sources()

    dataset = config["epidemiology"]

    return PROJECT_ROOT / dataset["raw_directory"] / dataset["filename"]


def fetch() -> Path:
    """
    Return the epidemiology dataset path.
    """

    dataset_path = get_dataset_path()

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found:\n{dataset_path}")

    return dataset_path
