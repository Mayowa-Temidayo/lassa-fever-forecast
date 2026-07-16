from __future__ import annotations


class DatasetManager:
    """
    Coordinate all project datasets.
    """

    def __init__(self) -> None:
        self.datasets: list[str] = []

    def register(self, dataset: str) -> None:
        self.datasets.append(dataset)

    def list_datasets(self) -> list[str]:
        return self.datasets.copy()
