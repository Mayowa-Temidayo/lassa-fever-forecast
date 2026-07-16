from __future__ import annotations

from lassa_fever_forecast.data.fetch_epidemiology import fetch


def main() -> None:
    """
    Execute the project data pipeline.
    """

    print("\n" + "=" * 70)
    print("LASSA FEVER FORECAST")
    print("DATA ENGINEERING PIPELINE")
    print("=" * 70)

    fetch()

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()
