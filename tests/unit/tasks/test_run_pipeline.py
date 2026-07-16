from unittest.mock import patch

from lassa_fever_forecast.tasks.run_pipeline import main


@patch("lassa_fever_forecast.tasks.run_pipeline.fetch")
def test_main(mock_fetch) -> None:
    """
    Ensure the pipeline calls the epidemiology fetch task.
    """

    main()

    mock_fetch.assert_called_once()
