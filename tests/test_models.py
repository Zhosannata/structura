"""Тесты Pydantic-схемы StructuraOutput."""

import pytest
from pydantic import ValidationError

from models.output import Role, StructuraOutput


def test_valid_output(sample_output: StructuraOutput) -> None:
    """Валидный объект проходит валидацию."""
    assert sample_output.raw_requirement
    assert sample_output.tech_spec.goal
    assert len(sample_output.user_stories) == 1
    assert len(sample_output.acceptance_criteria) == 2
    assert len(sample_output.tasks) == 2
    assert len(sample_output.test_cases) == 1


def test_output_from_json(sample_output: StructuraOutput) -> None:
    """model_validate_json корректно парсит JSON."""
    json_str = sample_output.model_dump_json()
    parsed = StructuraOutput.model_validate_json(json_str)
    assert parsed.raw_requirement == sample_output.raw_requirement
    assert parsed.tech_spec.goal == sample_output.tech_spec.goal


def test_invalid_output_missing_field(sample_output: StructuraOutput) -> None:
    """Отсутствие обязательного поля — ошибка валидации."""
    data = sample_output.model_dump()
    del data["tech_spec"]
    with pytest.raises(ValidationError):
        StructuraOutput.model_validate(data)


def test_invalid_role(sample_output: StructuraOutput) -> None:
    """Неизвестная роль в задаче — ошибка валидации."""
    data = sample_output.model_dump()
    data["tasks"][0]["role"] = "manager"
    with pytest.raises(ValidationError):
        StructuraOutput.model_validate(data)


def test_story_points_bounds(sample_output: StructuraOutput) -> None:
    """Story Points должны быть в диапазоне 1–13."""
    data = sample_output.model_dump()
    data["tasks"][0]["story_points"] = 100
    with pytest.raises(ValidationError):
        StructuraOutput.model_validate(data)


def test_role_enum_values() -> None:
    """Все допустимые роли — из фиксированного списка."""
    assert {r.value for r in Role} == {"designer", "frontend", "backend", "qa"}