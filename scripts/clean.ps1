Clear-Host

Write-Host "Cleaning project..." -ForegroundColor Cyan

Get-ChildItem -Recurse -Directory `
    -Filter "__pycache__" |
Remove-Item -Force -Recurse

Get-ChildItem -Recurse -Directory `
    -Filter ".pytest_cache" |
Remove-Item -Force -Recurse

Get-ChildItem -Recurse -Directory `
    -Filter ".ipynb_checkpoints" |
Remove-Item -Force -Recurse

Write-Host ""
Write-Host "Cleanup complete." -ForegroundColor Green