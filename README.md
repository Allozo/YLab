# YLab

## Жизнь без Docker

### Установка зависимостей

Для установки всех необходимых зависимостей (из файла `pyproject.toml`) воспользуйтесь командой:

```shell
poetry install
```

### Запуск приложения

Отредактируйте файл `menu/database.py`, закомментировав там блок кода с `PostgreSQL` и расскомментировав блок кода с `sqlite`.

Для запуска приложения воспользуйтесь командой:

```shell
poetry run uvicorn menu.main:app
```

### Запуск тестов Postman

Для запуска тестов скачайте Postman, импортируйте туда два файла из папки `tests`, выберите окружение и запустите все тесты.

## Жизнь с Docker

### Запуск контейнера с приложением (БД sqlite)

Отредактируйте файл `menu/database.py`, закомментировав там блок кода с `PostgreSQL` и расскомментировав блок кода с `sqlite`.

Сборка образа:

```shell
docker build -t menu_app .
```

Запуск контейнера:

```shell
docker run --name flask_app_menu -p 8000:8000 -d menu_app
```

### Запуск через Docker-Compose

Используется `PostgreSQL`. По умолчанию ничего менять не надо.

Если изменяли БД на `sqlite`, то отредактируйте файл `menu/database.py`, закомментировав там блок кода с `sqlite` и расскомментировав блок кода с `PostgreSQL`.

Создание и запуск всех контейнеров осуществляется командой:

```shell
docker-compose up --build
```