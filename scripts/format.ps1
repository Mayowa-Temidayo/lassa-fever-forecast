Clear-Host

Write-Host "Formatting project..." -ForegroundColor Cyan

uv run ruff format .

uv run black .

Write-Host ""
Write-Host "Formatting complete." -ForegroundColor Green