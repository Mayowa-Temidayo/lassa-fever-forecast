Write-Host ""
Write-Host "Creating documentation structure..." -ForegroundColor Green

$folders = @(
    "docs",
    "docs/diagrams"
)

foreach ($folder in $folders) {
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "Created $folder"
    }
}

$files = @(
    "docs/00_Project_Master_Map.md",
    "docs/01_Project_Architecture.md",
    "docs/02_Data_Dictionary.md",
    "docs/03_Model_Registry.md",
    "docs/04_API_Documentation.md",
    "docs/CHANGELOG.md"
)

foreach ($file in $files) {
    if (!(Test-Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
        Write-Host "Created $file"
    }
}

Write-Host ""
Write-Host "Documentation scaffold completed." -ForegroundColor Cyan