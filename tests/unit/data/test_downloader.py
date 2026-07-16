from pathlib import Path
from unittest.mock import Mock, patch

from lassa_fever_forecast.data.downloader import download_file


@patch("lassa_fever_forecast.data.downloader.requests.get")
def test_download_file(
    mock_get: Mock,
    tmp_path: Path,
) -> None:
    response = Mock()

    response.content = b"hello"

    response.raise_for_status.return_value = None

    mock_get.return_value = response

    destination = tmp_path / "example.txt"

    result = download_file(
        url="https://example.com/file.txt",
        destination=destination,
    )

    assert result.exists()

    assert result.read_bytes() == b"hello"
