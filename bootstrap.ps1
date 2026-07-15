# =============================================================================
# LASSA FEVER FORECAST PROJECT BOOTSTRAP
# =============================================================================

Write-Host ""
Write-Host "Bootstrapping project..." -ForegroundColor Cyan
Write-Host ""

# -----------------------------------------------------------------------------
# Remove old src if it exists
# -----------------------------------------------------------------------------

if (Test-Path "src") {
    Remove-Item -Recurse -Force "src"
}

# -----------------------------------------------------------------------------
# Create Directory Structure
# -----------------------------------------------------------------------------

$directories = @(
    ".vscode",

    "notebooks",

    "src/lassa_fever_forecast",

    "src/lassa_fever_forecast/config",
    "src/lassa_fever_forecast/data",
    "src/lassa_fever_forecast/features",
    "src/lassa_fever_forecast/models",
    "src/lassa_fever_forecast/evaluation",
    "src/lassa_fever_forecast/visualization",
    "src/lassa_fever_forecast/utils",

    "data",
    "data/raw",
    "data/interim",
    "data/processed",
    "data/external",

    "models",

    "reports",
    "reports/figures",

    "logs",

    "tests"
)

foreach ($dir in $directories) {
    New-Item `
        -ItemType Directory `
        -Force `
        -Path $dir | Out-Null
}

# -----------------------------------------------------------------------------
# Create Python Packages
# -----------------------------------------------------------------------------

$packages = @(
    "src/lassa_fever_forecast",
    "src/lassa_fever_forecast/config",
    "src/lassa_fever_forecast/data",
    "src/lassa_fever_forecast/features",
    "src/lassa_fever_forecast/models",
    "src/lassa_fever_forecast/evaluation",
    "src/lassa_fever_forecast/visualization",
    "src/lassa_fever_forecast/utils"
)

foreach ($pkg in $packages) {
    New-Item `
        -ItemType File `
        -Force `
        -Path "$pkg/__init__.py" | Out-Null
}

# -----------------------------------------------------------------------------
# Create Configuration Files
# -----------------------------------------------------------------------------

New-Item -ItemType File -Force src/lassa_fever_forecast/config/settings.py | Out-Null
New-Item -ItemType File -Force src/lassa_fever_forecast/config/paths.py | Out-Null
New-Item -ItemType File -Force src/lassa_fever_forecast/config/logging.py | Out-Null

# -----------------------------------------------------------------------------
# Create Environment Files
# -----------------------------------------------------------------------------

@"
PROJECT_NAME=Lassa Fever Forecast

LOG_LEVEL=INFO

NASA_POWER_API_KEY=
OPENWEATHER_API_KEY=
WHO_API_KEY=

DATABASE_URL=

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=

AZURE_STORAGE_CONNECTION_STRING=

GOOGLE_APPLICATION_CREDENTIALS=

MLFLOW_TRACKING_URI=
"@ | Set-Content ".env.example"

Copy-Item ".env.example" ".env"

# -----------------------------------------------------------------------------
# Create .gitignore
# -----------------------------------------------------------------------------

@"
# Python
__pycache__/
*.py[cod]
*.pyo

# Virtual Environment
.venv/

# Environment Variables
.env
.env.*
!.env.example

# Jupyter
.ipynb_checkpoints/

# VS Code
.vscode/settings.json

# Data
data/raw/*
data/interim/*
data/processed/*
!data/raw/.gitkeep
!data/interim/.gitkeep
!data/processed/.gitkeep

# Models
models/*
!models/.gitkeep

# Logs
logs/*
!logs/.gitkeep

# Reports
reports/figures/*
!reports/figures/.gitkeep

# OS
.DS_Store
Thumbs.db
"@ | Set-Content ".gitignore"

# -----------------------------------------------------------------------------
# Create .gitkeep Files
# -----------------------------------------------------------------------------

$gitkeep = @(
    "data/raw/.gitkeep",
    "data/interim/.gitkeep",
    "data/processed/.gitkeep",
    "models/.gitkeep",
    "logs/.gitkeep",
    "reports/figures/.gitkeep"
)

foreach ($file in $gitkeep) {
    New-Item -ItemType File -Force -Path $file | Out-Null
}

# -----------------------------------------------------------------------------
# Create pyproject.toml
# -----------------------------------------------------------------------------

@"
[project]
name = "lassa-fever-forecast"
version = "0.1.0"
description = "End-to-end machine learning pipeline for forecasting Lassa fever outbreaks in Nigeria."
readme = "README.md"
requires-python = ">=3.12"

dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/lassa_fever_forecast"]
"@ | Set-Content "pyproject.toml"

# -----------------------------------------------------------------------------
# Create README
# -----------------------------------------------------------------------------

@"
# Lassa Fever Forecast

End-to-end machine learning pipeline for forecasting Lassa fever outbreaks in Nigeria.
"@ | Set-Content "README.md"

Write-Host ""
Write-Host "Project bootstrapped successfully!" -ForegroundColor Green
Write-Host ""