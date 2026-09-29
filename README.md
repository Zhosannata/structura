# Structura

AI-сервис, который из сырого бизнес-требования создаёт полный пакет проектной документации для команды: ТЗ, User Story, Acceptance Criteria, декомпозицию задач по ролям, тест-кейсы.

## OpenSpec

Артефакты проекта находятся в `openspec/changes/structura-mvp/`:

- `proposal.md` — зачем и что меняется
- `design.md` — архитектурные решения
- `tasks.md` — план работ
- `specs/structura/generation/spec.md` — требования к генерации
- `specs/structura/schema/spec.md` — схема вывода

## Стек

- Python 3.11+
- FastAPI
- Pydantic v2
- PostgreSQL
- LLM: Qwen (через Polza.ai)

## Запуск

```bash
pip install -e ".[dev]"
uvicorn api.main:app --reload