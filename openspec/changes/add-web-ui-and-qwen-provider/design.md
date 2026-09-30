# Design: Add Web UI and Qwen Provider

## Context

Structura принимает сырое бизнес-требование и возвращает пакет проектной документации. MVP-спецификация описывает поведение генерации, но не фиксирует UI и не определяет провайдера LLM однозначно (в MVP указан GigaChat, проект использует Qwen через Polza.ai).

## Goals / Non-Goals

**Goals:**
- Дать PM веб-интерфейс: одна форма → одна страница результата
- Зафиксировать Qwen через Polza.ai как провайдера LLM
- Сохранить server-side rendering без Node.js и сборки
- Обеспечить обработку ошибок (пустой ввод, недоступность LLM, невалидный ответ)

**Non-Goals:**
- Авторизация и многопользовательский режим
- Сохранение истории генераций в БД (отдельный change)
- Экспорт в .docx (Markdown из MVP достаточно)
- JavaScript-фреймворки (React/Vue)

## Decisions

### UI: Jinja2 + FastAPI

- **Server-side rendering** через `Jinja2Templates`, без отдельного фронтенда
- **Шаблоны** в `frontend/`: `base.html`, `index.html`, `result.html`
- **Стили** в `frontend/styles.css` — чистый CSS с переменными, без Tailwind CDN
- **Причина:** MVP, один разработчик, нет Node.js, нет сборки

### LLM: Qwen через Polza.ai

- **Модель:** `qwen/qwen3.6-plus` (рекомендована для агентных задач, 1M контекст)
- **SDK:** `openai>=1.50` через `AsyncOpenAI` с `base_url=https://polza.ai/api/v1`
- **Формат ответа:** JSON, парсится через `StructuraOutput.model_validate_json`
- **Причина:** OpenAI-совместимый API, оплата в рублях, поддержка длинного контекста

### Формат запроса

- **HTML-форма** → `POST /generate` с `Form(...)` (не JSON)
- **Причина:** нет JS, работает нативно, FastAPI поддерживает через `python-multipart`

### Дизайн-палитра

| Элемент | HEX | Tailwind-аналог | Где |
|---|---|---|---|
| Фон | `#F8FAFC` | `slate-50` | body |
| Белый | `#FFFFFF` | `white` | карточки, поля |
| Основной акцент | `#2563EB` | `blue-600` | кнопки, ссылки |
| Hover | `#1D4ED8` | `blue-700` | hover на кнопках |
| Текст | `#1E293B` | `slate-800` | основной |
| Вторичный текст | `#64748B` | `slate-500` | подписи |
| Границы | `#E2E8F0` | `slate-200` | рамки |
| Успех | `#10B981` | `emerald-500` | статусы |
| Ошибка | `#EF4444` | `red-500` | ошибки |

### Структура кода
