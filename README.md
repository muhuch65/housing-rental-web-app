# RentHome

RentHome — учебное web-приложение для управления арендой жилья.

Проект разработан в рамках курсовой работы на тему:

**«Разработка web-приложения для управления арендой жилья»**

## Описание проекта

Система предназначена для просмотра объектов аренды, регистрации пользователей, подачи заявок на аренду и администрирования данных.

Приложение позволяет:

- просматривать каталог жилья;
- выполнять поиск и фильтрацию объектов;
- регистрироваться и входить в систему;
- оставлять заявки на аренду;
- просматривать свои заявки;
- администратору управлять пользователями;
- администратору управлять объектами аренды;
- администратору обрабатывать заявки;
- просматривать статистику в админ-панели.

## Технологический стек

**Backend:**

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- Flask-Migrate
- SQLite

**Frontend:**

- HTML
- CSS
- JavaScript
- Jinja2 Templates

**Инструменты:**

- Git
- Git Flow
- uv

## Структура проекта

```text
rental-housing-web-app/
├── app/
│   ├── commands/
│   │   └── db_commands.py
│   ├── forms/
│   │   ├── housing_filter_form.py
│   │   ├── housing_form.py
│   │   ├── login_form.py
│   │   ├── register_form.py
│   │   ├── rental_request_form.py
│   │   └── user_edit_form.py
│   ├── models/
│   │   ├── rental_object.py
│   │   ├── rental_request.py
│   │   └── user.py
│   ├── routes/
│   │   ├── admin_routes.py
│   │   ├── auth_routes.py
│   │   ├── housing_routes.py
│   │   ├── main_routes.py
│   │   ├── request_routes.py
│   │   └── user_routes.py
│   ├── services/
│   │   ├── admin_service.py
│   │   ├── auth_service.py
│   │   ├── dashboard_service.py
│   │   ├── housing_service.py
│   │   ├── request_service.py
│   │   └── user_service.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   ├── templates/
│   ├── utils/
│   │   ├── decorators.py
│   │   └── error_handlers.py
│   ├── __init__.py
│   ├── config.py
│   └── database.py
├── seed_demo_data.py
├── setup_linux.sh
├── setup_windows.ps1
├── run.py
├── requirements.txt
└── README.md
````

## Модули системы

Проект состоит из 9 основных модулей:

1. Модуль пользовательского интерфейса
2. Модуль авторизации и регистрации
3. Модуль управления пользователями
4. Модуль управления объектами аренды
5. Модуль поиска и фильтрации жилья
6. Модуль заявок на аренду
7. Модуль базы данных
8. Модуль серверной логики
9. Модуль администрирования

## Установка и запуск через uv

### Linux/macOS

```bash
chmod +x setup_linux.sh
./setup_linux.sh
```

Скрипт выполнит:

```text
1. Установку uv
2. Создание виртуального окружения
3. Установку зависимостей
4. Подготовку демонстрационной базы данных
5. Запуск приложения
```

### Windows PowerShell

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\setup_windows.ps1
```

## Ручная установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/username/rental-housing-web-app.git
cd rental-housing-web-app
```

### 2. Создание виртуального окружения

```bash
uv venv
```

### 3. Установка зависимостей

```bash
uv pip install -r requirements.txt
```

или:

```bash
uv pip install Flask Flask-SQLAlchemy Flask-Login Flask-WTF email-validator Flask-Migrate
```

### 4. Подготовка базы данных

```bash
uv run python seed_demo_data.py
```

### 5. Запуск приложения

```bash
uv run python run.py
```

После запуска приложение будет доступно по адресу:

```text
http://127.0.0.1:5000
```

## Демонстрационные пользователи

### Администратор

```text
Email: admin@example.com
Password: admin123
```

### Обычные пользователи

```text
Email: ivan@example.com
Password: user123

Email: maria@example.com
Password: user123

Email: alexey@example.com
Password: user123
```

## Основные маршруты

```text
/                       Главная страница
/housing                Каталог жилья
/housing/<id>           Карточка объекта аренды
/login                  Вход
/register               Регистрация
/profile                Личный кабинет
/my-requests            Мои заявки

/admin/                 Админ-панель
/admin/users/           Управление пользователями
/admin/housing          Управление объектами аренды
/admin/requests         Управление заявками
```

## Работа с базой данных

Создать таблицы:

```bash
flask --app run.py create-db
```

Удалить таблицы:

```bash
flask --app run.py drop-db
```

Пересоздать базу данных:

```bash
flask --app run.py reset-db
```

Заполнить объектами аренды:

```bash
flask --app run.py seed-housing
```

Назначить администратора:

```bash
flask --app run.py make-admin user@example.com
```

## Миграции

Инициализация миграций:

```bash
flask --app run.py db init
```

Создание миграции:

```bash
flask --app run.py db migrate -m "create initial database tables"
```

Применение миграции:

```bash
flask --app run.py db upgrade
```

## Git Flow

В проекте используется упрощённая методология Git Flow.

Основные ветки:

```text
main      стабильная версия проекта
develop   основная ветка разработки
```

Для каждого модуля создаётся отдельная feature-ветка:

```bash
git checkout develop
git checkout -b feature/module-name
```

После завершения работы:

```bash
git add .
git commit -m "feature: add module name"
git checkout develop
git merge feature/module-name
git branch -d feature/module-name
```

## Пример feature-веток

```text
feature/ui-module
feature/auth-module
feature/user-management-module
feature/housing-module
feature/search-filter-module
feature/rental-requests-module
feature/database-module
feature/server-logic-module
feature/admin-module
feature/setup-scripts
```

## Основные сущности базы данных

### User

Хранит данные пользователей:

```text
id
name
email
password_hash
role
is_active_account
```

### RentalObject

Хранит объекты аренды:

```text
id
title
address
price
rooms
area
housing_type
status
description
```

### RentalRequest

Хранит заявки на аренду:

```text
id
user_id
rental_object_id
status
message
admin_comment
created_at
updated_at
```

## Роли пользователей

В системе предусмотрены две роли:

```text
user   обычный пользователь
admin  администратор
```

Обычный пользователь может:

```text
просматривать каталог;
фильтровать жильё;
оставлять заявки;
просматривать свои заявки;
отменять заявки на рассмотрении.
```

Администратор может:

```text
управлять пользователями;
блокировать пользователей;
удалять пользователей;
добавлять объекты аренды;
редактировать объекты аренды;
удалять объекты аренды;
просматривать заявки;
одобрять заявки;
отклонять заявки;
просматривать административную статистику.
```

## Статусы объектов аренды

```text
Доступно
Занято
На обслуживании
```

## Статусы заявок

```text
На рассмотрении
Одобрена
Отклонена
Отменена
```

## Авторизация

Для авторизации используется Flask-Login.

Доступ к личному кабинету и заявкам разрешён только авторизованным пользователям.

Доступ к административным страницам разрешён только пользователям с ролью:

```text
admin
```

## Назначение администратора

После регистрации пользователя можно назначить его администратором:

```bash
flask --app run.py make-admin user@example.com
```

## Демонстрационный запуск

Для демонстрации работы достаточно выполнить:

Linux/macOS:

```bash
./setup_linux.sh
```

Windows:

```powershell
.\setup_windows.ps1
```

После запуска можно войти под администратором:

```text
admin@example.com
admin123
```

## Назначение проекта

Проект предназначен для демонстрации базовых навыков разработки web-приложения:

```text
проектирование структуры Flask-приложения;
работа с шаблонами Jinja2;
создание моделей базы данных;
реализация CRUD-операций;
авторизация и разграничение прав доступа;
работа с формами;
обработка заявок;
организация административной панели;
использование Git Flow.
```

## Лицензия

Проект разработан в учебных целях.
