# Proposal: Structura MVP

## Why

PM/BA тратит 2–3 часа на создание проектной документации по одной задаче: ТЗ, User Story, Acceptance Criteria, декомпозицию задач для дизайнера, фронтенда, бэкенда и QA, а также тест-кейсы.
Это время можно потратить на работу с командой и стейкхолдерами.
Structura генерирует полный пакет документации из сырого требования — чтобы PM получал готовые артефакты за минуты, а не за часы.

## What Changes

- **ADDED** Генерация ТЗ из сырого требования
- **ADDED** Генерация User Story и Acceptance Criteria (GIVEN/WHEN/THEN)
- **ADDED** Декомпозиция задач по ролям: дизайнер, фронтенд, бэкенд, QA
- **ADDED** Генерация тест-кейсов из Acceptance Criteria
- **ADDED** Валидация вывода через Pydantic-схему
- **ADDED** Экспорт результата в Markdown

## What Does Not Change

- Формат получения сырых требований PM (Telegram/почта/встречи)

## Impact

- Affected specs: `structura/generation`, `structura/validation`
- Affected code: `api/`, `prompts/`, `models/`

## Key Risks

- LLM может генерировать неполную декомпозицию для некоторых ролей
- Формат AC может не совпадать с ожиданиями QA → нужен golden dataset
- Промпт может устаревать при смене модели → версионирование