Write-Host ""
Write-Host "==============================="
Write-Host "Preparing Development Environment"
Write-Host "==============================="
Write-Host ""

python -m pip install --upgrade pip
python -m pip install -e .

python -m pip install pytest
python -m pip install ruff
