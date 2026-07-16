Clear-Host

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "          PHASE GATE CHECK"
Write-Host "======================================"
Write-Host ""

.\scripts\format.ps1

.\scripts\lint.ps1

.\scripts\test.ps1

Write-Host "Auto-fixing Ruff issues..."
uv run ruff check . --fix

Write-Host ""
Write-Host "Running Ruff..."
uv run ruff check .

Write-Host ""
Write-Host "Running Formatter..."
uv run ruff format .

Write-Host ""
Write-Host "Checking package..."

uv run python -c "import lassa_fever_forecast"

if ($LASTEXITCODE -ne 0) {
    throw "Package import failed."
}

Write-Host ""
Write-Host "Git Status"
git status

Write-Host ""
Write-Host "======================================"
Write-Host "READY TO PROCEED" -ForegroundColor Green
Write-Host "======================================"