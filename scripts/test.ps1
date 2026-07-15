Clear-Host

Write-Host "Running tests..." -ForegroundColor Cyan

uv run pytest

Write-Host ""
Write-Host "Tests completed." -ForegroundColor Green