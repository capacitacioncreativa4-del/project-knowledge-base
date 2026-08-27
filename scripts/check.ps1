Write-Host ""
Write-Host "==============================="
Write-Host "PKB Quality Check"
Write-Host "==============================="
Write-Host ""

python -m ruff check .

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Ruff OK"
