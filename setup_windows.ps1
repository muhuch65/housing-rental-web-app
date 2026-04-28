Write-Host "Подготовка проекта RentHome для Windows"

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "uv не найден. Установка uv..."
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

    $env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
} else {
    Write-Host "uv уже установлен."
}

Write-Host "Создание виртуального окружения..."
uv venv

Write-Host "Установка зависимостей..."
uv pip install Flask Flask-SQLAlchemy Flask-Login Flask-WTF email-validator Flask-Migrate

Write-Host "Подготовка демонстрационной базы данных..."
uv run python seed_demo_data.py

Write-Host "Запуск приложения..."
uv run python run.py
