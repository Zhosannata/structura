# Tasks for Structura MVP

## 1. Contracts & Schema

- [ ] 1.1 Определить Pydantic-схему StructuraOutput (TechSpec, UserStory, AC, Task, TestCase)
- [ ] 1.2 Написать golden dataset: 2–3 эталонных требования
- [ ] 1.3 Написать тесты на валидацию схемы

## 2. Prompt Engineering

- [ ] 2.1 Написать промпт v1: генерация ТЗ + User Story + AC
- [ ] 2.2 Расширить промпт: декомпозиция задач по ролям
- [ ] 2.3 Расширить промпт: генерация тест-кейсов
- [ ] 2.4 Покрыть промпт тестами (golden dataset)

## 3. Backend

- [ ] 3.1 FastAPI: endpoint POST /api/generate
- [ ] 3.2 Интеграция с LLM (GigaChat/YandexGPT)
- [ ] 3.3 Валидация вывода через Pydantic
- [ ] 3.4 Сохранение генераций в PostgreSQL
- [ ] 3.5 Endpoint GET /api/health

## 4. Database

- [ ] 4.1 Таблица generations (версия промпта, LLM, статус)
- [ ] 4.2 Таблица artifacts (тип, external_id, content)
- [ ] 4.3 Таблица ac_test_links (связь AC ↔ тесты)

## 5. Frontend

- [ ] 5.1 Форма ввода требования
- [ ] 5.2 Отображение ТЗ, User Story, AC
- [ ] 5.3 Отображение задач по ролям
- [ ] 5.4 Отображение тест-кейсов
- [ ] 5.5 Экспорт в Markdown

## 6. QA

- [ ] 6.1 Тесты на генерацию User Story
- [ ] 6.2 Тесты на декомпозицию задач по ролям
- [ ] 6.3 Тесты на генерацию тест-кейсов
- [ ] 6.4 Тесты на валидацию контракта

## 7. Infrastructure

- [ ] 7.1 Dockerfile для API
- [ ] 7.2 docker-compose.yml (api, postgres, traefik)
- [ ] 7.3 Деплой на VPS
- [ ] 7.4 Traefik + HTTPS