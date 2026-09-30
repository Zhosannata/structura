# Tasks for Add Web UI and Qwen Provider

## 1. Contracts & Schema

- [ ] 1.1 Pydantic-модели: `StructuraOutput`, `TechSpec`, `UserStory`, `AcceptanceCriteria`, `Task`, `TestCase`
- [ ] 1.2 Enum `Role` (designer/frontend/backend/qa) и `ACType` (main/edge)
- [ ] 1.3 Тесты на валидацию схемы (валидный и невалидный JSON)

## 2. Config & Dependencies

- [ ] 2.1 `api/config.py` — `Settings` через `pydantic-settings`
- [ ] 2.2 Обновить `pyproject.toml`: `openai`, `pydantic-settings`, `jinja2`, `python-multipart`
- [ ] 2.3 Обновить `.env.example`: `POLZA_API_KEY`, `POLZA_BASE_URL`, `LLM_MODEL`

## 3. Prompt Engineering

- [ ] 3.1 `prompts/v1/system.md` — системный промпт с инструкцией вернуть JSON по схеме
- [ ] 3.2 Убедиться, что промпт требует: ТЗ, User Stories, AC (main + edge), задачи по ролям, тест-кейсы, риски
- [ ] 3.3 Тест: промпт загружается и подставляется в запрос

## 4. Polza Client

- [ ] 4.1 `api/services/polza.py` — `AsyncOpenAI(base_url=..., api_key=...)`
- [ ] 4.2 Функция `generate_docs(requirement: str) -> StructuraOutput`
- [ ] 4.3 Обработка ошибок: `APIConnectionError`, `APIStatusError`, `ValidationError`
- [ ] 4.4 Тест с mock-клиентом: возвращает валидный `StructuraOutput`

## 5. FastAPI Routes

- [ ] 5.1 `api/main.py` — app, Jinja2Templates(directory="frontend"), mount `/static`
- [ ] 5.2 `GET /` — рендер `index.html` с пустой формой
- [ ] 5.3 `POST /generate` — приём `Form(requirement)`, вызов сервиса, рендер `result.html`
- [ ] 5.4 Обработка ошибок: пустой ввод → `index.html` с сообщением

## 6. UI

- [ ] 6.1 `frontend/base.html` — каркас, подключение `styles.css`
- [ ] 6.2 `frontend/index.html` — форма ввода требования
- [ ] 6.3 `frontend/result.html` — отображение ТЗ, US, AC, задач, тест-кейсов, рисков
- [ ] 6.4 `frontend/styles.css` — палитра slate/blue из `design.md`
- [ ] 6.5 Проверка: контраст текста, адаптивность на мобильном (минимум)

## 7. QA

- [ ] 7.1 `tests/conftest.py` — фикстуры (тестовый клиент, мок Polza)
- [ ] 7.2 `tests/test_models.py` — валидация схемы
- [ ] 7.3 `tests/test_polza.py` — сервис с mock-клиентом
- [ ] 7.4 `tests/test_routes.py` — GET / и POST /generate

## 8. Documentation

- [ ] 8.1 Обновить `README.md`: раздел про UI, переменные `.env`, локальный запуск