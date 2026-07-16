from lassa_fever_forecast.data.dataset_manager import (
    DatasetManager,
)


def test_register_dataset() -> None:
    manager = DatasetManager()

    manager.register("epidemiology")

    assert manager.list_datasets() == [
        "epidemiology",
    ]
