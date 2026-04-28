#!/bin/bash

set -e

echo "Подготовка проекта RentHome для Linux/macOS"

if ! command -v uv >/dev/null 2>&1; then
    echo "uv не найден. Установка uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
else
    echo "uv уже установлен."
fi

echo "Создание виртуального окружения..."
uv venv

echo "Установка зависимостей..."
uv pip install Flask Flask-SQLAlchemy Flask-Login Flask-WTF email-validator Flask-Migrate

echo "Подготовка демонстрационной базы данных..."
uv run python seed_demo_data.py

echo "Запуск приложения..."
uv run python run.py
