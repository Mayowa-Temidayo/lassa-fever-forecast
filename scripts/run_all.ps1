Write-Host ""
Write-Host "========================================="
Write-Host "LASSA FEVER FORECAST"
Write-Host "DEVELOPER WORKFLOW"
Write-Host "========================================="
Write-Host ""

$ErrorActionPreference = "Stop"

Write-Host "Running Quality Gate..."
.\scripts\gate_check.ps1

Write-Host ""
Write-Host "Executing Pipeline..."
uv run python -m lassa_fever_forecast.tasks.run_pipeline

Write-Host ""
Write-Host "Opening Notebook..."
code notebooks\01_lassa_forecasting.ipynb

Write-Host ""
Write-Host "Workflow complete."