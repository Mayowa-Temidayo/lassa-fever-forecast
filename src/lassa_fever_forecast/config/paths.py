from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

DATA_DIR = PROJECT_ROOT / "data"

RAW_DIR = DATA_DIR / "raw"

INTERIM_DIR = DATA_DIR / "interim"

PROCESSED_DIR = DATA_DIR / "processed"

EXTERNAL_DIR = DATA_DIR / "external"

MODELS_DIR = PROJECT_ROOT / "models"

REPORTS_DIR = PROJECT_ROOT / "reports"

FIGURES_DIR = REPORTS_DIR / "figures"

LOGS_DIR = PROJECT_ROOT / "logs"
