from pydantic import BaseModel


class DatasetMetadata(BaseModel):
    """Metadata describing a dataset used in the project."""

    dataset_id: str
    dataset_name: str
    category: str
    source: str
    acquisition: str
    frequency: str
    target: bool
    status: str
    version: str
