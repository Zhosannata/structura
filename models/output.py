"""Pydantic-схемы вывода Structura."""

from enum import Enum

from pydantic import BaseModel, Field


class Role(str, Enum):
    """Роли в декомпозиции задач."""

    DESIGNER = "designer"
    FRONTEND = "frontend"
    BACKEND = "backend"
    QA = "qa"


class ACType(str, Enum):
    """Тип Acceptance Criteria."""

    MAIN = "main"
    EDGE = "edge"


class TechSpec(BaseModel):
    """Техническое задание."""

    goal: str = Field(..., description="Цель изменения")
    scope: str = Field(..., description="Что входит в scope")
    constraints: list[str] = Field(default_factory=list, description="Ограничения")


class UserStory(BaseModel):
    """User Story в формате role/action/value."""

    role: str = Field(..., description="Роль пользователя")
    action: str = Field(..., description="Действие")
    value: str = Field(..., description="Ценность")


class AcceptanceCriteria(BaseModel):
    """Acceptance Criteria в формате GIVEN/WHEN/THEN."""

    ac_id: str = Field(..., description="Идентификатор, например AC-1")
    type: ACType = Field(..., description="main или edge")
    given: str = Field(..., description="Предусловие")
    when: str = Field(..., description="Действие")
    then: str = Field(..., description="Ожидаемый результат")


class Task(BaseModel):
    """Задача в декомпозиции."""

    role: Role = Field(..., description="Роль исполнителя")
    title: str = Field(..., description="Заголовок задачи")
    description: str = Field(..., description="Описание")
    story_points: int = Field(..., ge=1, le=13, description="Оценка в SP")


class TestCase(BaseModel):
    """Тест-кейс."""

    ac_id: str = Field(..., description="Ссылка на AC")
    name: str = Field(..., description="Название теста")
    code: str = Field(..., description="Код на pytest")


class StructuraOutput(BaseModel):
    """Полный пакет проектной документации."""

    raw_requirement: str = Field(..., description="Исходное требование")
    tech_spec: TechSpec
    user_stories: list[UserStory] = Field(default_factory=list)
    acceptance_criteria: list[AcceptanceCriteria] = Field(default_factory=list)
    tasks: list[Task] = Field(default_factory=list)
    test_cases: list[TestCase] = Field(default_factory=list)
    risks_and_questions: list[str] = Field(default_factory=list)