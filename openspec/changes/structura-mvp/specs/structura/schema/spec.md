# Delta for Structura Schema

## ADDED Requirements

### Requirement: Схема StructuraOutput

The system SHALL определять Pydantic-схему со следующими полями:

- `raw_requirement: str`
- `tech_spec: TechSpec`
- `user_stories: list[UserStory]`
- `acceptance_criteria: list[AcceptanceCriteria]`
- `tasks: list[Task]`
- `test_cases: list[TestCase]`
- `risks_and_questions: list[str]`

#### Scenario: Полная схема
- **GIVEN** LLM вернул результат
- **WHEN** Pydantic валидирует
- **THEN** все поля присутствуют и корректны

### Requirement: Декомпозиция задач по ролям

The system SHALL хранить задачи с полем `role`:

- `designer`
- `frontend`
- `backend`
- `qa`

#### Scenario: Задача с ролью
- **GIVEN** есть задача
- **WHEN** она валидируется
- **THEN** поле role содержит одно из допустимых значений