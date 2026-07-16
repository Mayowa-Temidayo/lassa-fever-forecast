from pathlib import Path

from lassa_fever_forecast.data.checksum import (
    calculate_sha256,
)


def test_calculate_sha256(
    tmp_path: Path,
) -> None:
    file = tmp_path / "hello.txt"

    file.write_text("hello")

    checksum = calculate_sha256(file)

    assert len(checksum) == 64
