from pathlib import Path

from lassa_fever_forecast.data.fetch_epidemiology import fetch


def test_fetch_returns_path() -> None:
    """
    Ensure the epidemiology fetcher returns a pathlib.Path.
    """
    dataset = fetch()

    assert isinstance(dataset, Path)


def test_dataset_exists() -> None:
    """
    Ensure the epidemiology dataset exists after fetching.
    """
    dataset = fetch()

    assert dataset.exists()
