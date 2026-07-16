from pathlib import Path

from lassa_fever_forecast.data.versioning import (
    create_version_directory,
)


def test_create_version_directory(
    tmp_path: Path,
) -> None:
    version = create_version_directory(tmp_path)

    assert version.exists()

    assert version.is_dir()
