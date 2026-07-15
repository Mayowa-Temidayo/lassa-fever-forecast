# =============================================================================
# LASSA FEVER FORECAST
# Developer Environment Doctor
# =============================================================================

Clear-Host

$ErrorActionPreference = "SilentlyContinue"

function Test-Command {
    param(
        [string]$Name,
        [string]$Command
    )

    Invoke-Expression $Command | Out-Null

    if ($LASTEXITCODE -eq 0) {
        Write-Host ("{0,-35}" -f $Name) -NoNewline
        Write-Host "[PASS]" -ForegroundColor Green
    }
    else {
        Write-Host ("{0,-35}" -f $Name) -NoNewline
        Write-Host "[FAIL]" -ForegroundColor Red
    }
}

function Test-PathExists {
    param(
        [string]$Name,
        [string]$Path
    )

    if (Test-Path $Path) {
        Write-Host ("{0,-35}" -f $Name) -NoNewline
        Write-Host "[PASS]" -ForegroundColor Green
    }
    else {
        Write-Host ("{0,-35}" -f $Name) -NoNewline
        Write-Host "[FAIL]" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "          LASSA FEVER FORECAST - SYSTEM DOCTOR"
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Development Tools" -ForegroundColor Yellow
Write-Host "------------------------------------------------------------"

Test-Command "Python" "python --version"
Test-Command "uv" "uv --version"
Test-Command "Git" "git --version"

Write-Host ""

Write-Host "Virtual Environment" -ForegroundColor Yellow
Write-Host "------------------------------------------------------------"

Test-PathExists ".venv" ".venv"

Write-Host ""

Write-Host "Project Files" -ForegroundColor Yellow
Write-Host "------------------------------------------------------------"

Test-PathExists "pyproject.toml" "pyproject.toml"
Test-PathExists ".gitignore" ".gitignore"
Test-PathExists ".env" ".env"
Test-PathExists ".env.example" ".env.example"

Write-Host ""

Write-Host "Project Structure" -ForegroundColor Yellow
Write-Host "------------------------------------------------------------"

Test-PathExists "src package" "src/lassa_fever_forecast"
Test-PathExists "notebooks" "notebooks"
Test-PathExists "data" "data"
Test-PathExists "models" "models"
Test-PathExists "reports" "reports"
Test-PathExists "logs" "logs"
Test-PathExists "tests" "tests"

Write-Host ""

Write-Host "Git Repository" -ForegroundColor Yellow
Write-Host "------------------------------------------------------------"

git rev-parse --is-inside-work-tree | Out-Null

if ($LASTEXITCODE -eq 0) {

    Write-Host ("{0,-35}" -f "Git Repository") -NoNewline
    Write-Host "[PASS]" -ForegroundColor Green

    $branch = git branch --show-current

    Write-Host ("{0,-35} {1}" -f "Current Branch", $branch)

}
else {

    Write-Host ("{0,-35}" -f "Git Repository") -NoNewline
    Write-Host "[FAIL]" -ForegroundColor Red

}

Write-Host ""

Write-Host "GitHub SSH" -ForegroundColor Yellow
Write-Host "------------------------------------------------------------"

ssh -T git@github.com 2>&1 | Out-String | Out-Null

if ($LASTEXITCODE -eq 1) {

    Write-Host ("{0,-35}" -f "GitHub SSH") -NoNewline
    Write-Host "[PASS]" -ForegroundColor Green

}
else {

    Write-Host ("{0,-35}" -f "GitHub SSH") -NoNewline
    Write-Host "[FAIL]" -ForegroundColor Red

}

Write-Host ""

Write-Host "Python Package" -ForegroundColor Yellow
Write-Host "------------------------------------------------------------"

uv run python -c "import lassa_fever_forecast"

if ($LASTEXITCODE -eq 0) {

    Write-Host ("{0,-35}" -f "Package Import") -NoNewline
    Write-Host "[PASS]" -ForegroundColor Green

}
else {

    Write-Host ("{0,-35}" -f "Package Import") -NoNewline
    Write-Host "[FAIL]" -ForegroundColor Red

}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Doctor Finished"
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""