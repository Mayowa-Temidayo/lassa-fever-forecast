from __future__ import annotations

from pathlib import Path

import yaml
from kaggle.api.kaggle_api_extended import KaggleApi

from lassa_fever_forecast.config.paths import PROJECT_ROOT

CONFIG_PATH = (
    PROJECT_ROOT / "src" / "lassa_fever_forecast" / "config" / "data_sources.yaml"
)


def _config() -> dict:
    with CONFIG_PATH.open(
        "r",
        encoding="utf-8",
    ) as file:
        return yaml.safe_load(file)


def fetch(
    dataset: str | None = None,
) -> Path:
    """
    Returns the requested epidemiology dataset.

    Downloads automatically if missing.
    """

    cfg = _config()["epidemiology"]

    raw_dir = PROJECT_ROOT / cfg["raw_directory"]

    raw_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    selected = dataset or cfg["default"]

    filename = cfg["files"][selected]

    dataset_path = raw_dir / filename

    if dataset_path.exists():
        return dataset_path

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        cfg["dataset_id"],
        path=raw_dir,
        unzip=True,
    )

    if not dataset_path.exists():
        raise FileNotFoundError(f"Downloaded dataset not found:\n{dataset_path}")

    return dataset_path
