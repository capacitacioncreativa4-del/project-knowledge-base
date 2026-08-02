Write-Host ""
Write-Host "Cleaning..."

Remove-Item -Recurse -Force .pytest_cache -ErrorAction Ignore
Remove-Item -Recurse -Force .ruff_cache -ErrorAction Ignore
Remove-Item -Recurse -Force **/__pycache__ -ErrorAction Ignore
