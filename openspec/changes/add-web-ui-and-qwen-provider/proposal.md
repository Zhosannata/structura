# Proposal: Add Web UI and Qwen Provider

## Why

MVP `structura-mvp` специфицирует генерацию проектной документации (ТЗ, User Story, AC, задачи по ролям, тест-кейсы) и валидацию через Pydantic, но оставляет открытыми два вопроса:

1. **Интерфейс.** В `tasks.md` пункт 5.1 «Форма ввода требования» есть, но не сказано, как именно выглядит UI, какие роуты, какие шаблоны и какая палитра. Без этого PM не может пользоваться сервисом без прямых вызовов API.
2. **Провайдер LLM.** В `design.md` MVP указан GigaChat, но для проекта выбран Qwen через Polza.ai: OpenAI-совместимый API, оплата в рублях, поддержка длинного контекста (1M токенов) и хорошая работа со структурированным выводом.

Этот change закрывает оба вопроса: добавляет capability `structura/ui` и фиксирует провайдера Qwen в дизайне.

## What Changes

- **ADDED** Capability `structura/ui`: веб-форма ввода бизнес-требования, страница результата, дизайн-палитра
- **ADDED** Клиент Polza.ai (`api/services/polza.py`) на базе `AsyncOpenAI`
- **ADDED** Конфигурация через `pydantic-settings` (`api/config.py`): `POLZA_API_KEY`, `POLZA_BASE_URL`, `LLM_MODEL`
- **ADDED** Pydantic-схема `StructuraOutput` и вложенные модели (`models/output.py`)
- **ADDED** Системный промпт v1 (`prompts/v1/system.md`)
- **MODIFIED** `design.md` MVP: провайдер LLM — Qwen через Polza.ai (вместо GigaChat)

## What Does Not Change

- Требования к генерации (`generation/spec.md`): состав документов, формат AC, декомпозиция по ролям
- Схема вывода (`schema/spec.md`): поля `StructuraOutput`, допустимые роли
- Экспорт в Markdown (пункт 5.5 MVP)
- Сохранение в PostgreSQL — отложено на отдельный change

## Impact

- Affected specs: `structura/ui` (новый), `structura/generation` (без изменений), `structura/schema` (без изменений)
- Affected code: `api/`, `models/`, `frontend/`, `prompts/`, `tests/`
- New dependencies: `openai>=1.50`, `pydantic-settings>=2.5`, `jinja2>=3.1`, `python-multipart>=0.0.12`

## Key Risks

- Polza.ai недоступен → обработка ошибок + понятное сообщение пользователю
- Qwen может вернуть невалидный JSON → повторная валидация через Pydantic + fallback
- Формат ответа Qwen может отличаться от GigaChat → тесты на парсинг и golden dataset
- UI без JS-фреймворка ограничен в интерактивности → приемлемо для MVP