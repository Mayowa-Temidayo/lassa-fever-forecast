Clear-Host

Write-Host "Running Ruff..." -ForegroundColor Cyan

uv run ruff check .

Write-Host ""
Write-Host "Lint completed." -ForegroundColor Green