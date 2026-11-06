# АС расчёта KPI (`kpi-as`)

Курсовая работа по дисциплине **СИИ** (УлГТУ):  
«Разработка автоматизированной системы расчета ключевых показателей эффективности сотрудников».

**Стек:** Django + Django REST Framework + PostgreSQL + HTML/CSS/JS  
**Архитектура:** клиент-сервер (браузер ↔ Django REST/HTML ↔ PostgreSQL)

---

## Как устроен проект (клиент / сервер)

Отдельных папок `client/` и `server/` нет — это один Django-проект.

| Роль | Папки / компоненты |
|------|--------------------|
| **Клиент** (то, что в браузере) | `templates/` (HTML), `static/` (CSS, JS) |
| **Сервер приложений** | `config/`, `accounts/`, `org/`, `kpi/`, `calculation/`, `reports/` |
| **База данных** | PostgreSQL (сервис снаружи репозитория) |
| **Запуск** | `manage.py` → `runserver` (разработка) |

---

## Что нужно установить

1. **Python 3.12+** (на машине разработки — 3.14)
2. **PostgreSQL 12+** (локально) **или** Docker Desktop
3. Git (для репозитория)

---

## Первый запуск (Windows, PowerShell)

### 1. Перейти в проект и создать окружение

```powershell
cd c:\Study\SII\kpi-as
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Настроить окружение

```powershell
copy .env.example .env
```

Параметры БД по умолчанию в `.env`:

- БД: `kpi_as`
- пользователь: `kpi`
- пароль: `kpi`
- хост: `localhost`, порт: `5432`

### 3. Поднять PostgreSQL

**Вариант A — локальный PostgreSQL** (если служба уже установлена):

```powershell
.\.venv\Scripts\python scripts\init_db.py
```

Скрипт создаёт пользователя `kpi` и базу `kpi_as`  
(ожидает суперпользователя `postgres` / пароль `postgres`).  
Если пароль другой — поправьте `scripts\init_db.py` или создайте БД вручную.

**Вариант B — Docker:**

```powershell
docker compose up -d
```

**Вариант C — без PostgreSQL (только для быстрой проверки):**  
в `.env` поставьте:

```env
USE_SQLITE=1
```

### 4. Миграции и сервер

```powershell
.\.venv\Scripts\python manage.py migrate
.\.venv\Scripts\python manage.py runserver
```

Открыть в браузере: **http://127.0.0.1:8000/**

Остановка сервера: `Ctrl+C` в терминале.

---

## Обычный запуск (когда всё уже настроено)

```powershell
cd c:\Study\SII\kpi-as
.\.venv\Scripts\Activate.ps1
.\.venv\Scripts\python manage.py runserver
```

---

## Полезные URL

| URL | Назначение |
|-----|------------|
| http://127.0.0.1:8000/ | Главная |
| http://127.0.0.1:8000/cabinet/admin/ | Кабинет администратора |
| http://127.0.0.1:8000/cabinet/manager/ | Кабинет руководителя |
| http://127.0.0.1:8000/cabinet/employee/ | Кабинет сотрудника |
| http://127.0.0.1:8000/org/ | Модуль оргструктуры (заглушка) |
| http://127.0.0.1:8000/kpi/ | Модуль KPI (заглушка) |
| http://127.0.0.1:8000/calculation/ | Модуль расчёта (заглушка) |
| http://127.0.0.1:8000/reports/ | Модуль отчётов (заглушка) |
| http://127.0.0.1:8000/api/ | Корень REST API |
| http://127.0.0.1:8000/api/health/ | Health-check |
| http://127.0.0.1:8000/admin/ | Django Admin |

---

## Структура каталогов

```
kpi-as/
├── config/           # настройки Django, URL, API root
├── accounts/         # доступ, кабинеты ролей
├── org/              # сотрудники и подразделения
├── kpi/              # показатели, матрица, периоды
├── calculation/      # расчёт KPI
├── reports/          # отчёты и аналитика
├── templates/        # HTML (клиент)
├── static/           # CSS/JS (клиент)
├── scripts/          # вспомогательные скрипты (init_db)
├── manage.py
├── requirements.txt
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## Этапы реализации

| Этап | Содержание | Статус |
|------|------------|--------|
| 0 | Каркас проекта, UI ролей, API-заглушки | ✅ |
| 1 | Вход, роли, разграничение прав | ⏳ |
| 2 | Оргструктура | ⏳ |
| 3 | Конфигурация KPI | ⏳ |
| 4 | Ядро расчёта | ⏳ |
| 5 | Отчёты | ⏳ |
| 6 | Excel/PDF, аудит, полировка | ⏳ |

---

## Частые проблемы

**`could not connect to server` / ошибка БД**  
- Проверьте, что PostgreSQL запущен (служба Windows или `docker compose ps`)  
- Либо временно `USE_SQLITE=1` в `.env`

**Порт 8000 занят**

```powershell
.\.venv\Scripts\python manage.py runserver 127.0.0.1:8001
```

**PowerShell не активирует venv**

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
