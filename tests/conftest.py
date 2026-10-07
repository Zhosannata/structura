"""Общие фикстуры для тестов."""

from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from api.main import app
from models.output import (
    AcceptanceCriteria,
    ACType,
    Role,
    StructuraOutput,
    Task,
    TechSpec,
    TestCase,
    UserStory,
)


@pytest.fixture
def client() -> TestClient:
    """Тестовый клиент FastAPI."""
    return TestClient(app)


@pytest.fixture
def sample_output() -> StructuraOutput:
    """Пример валидного StructuraOutput для тестов."""
    return StructuraOutput(
        raw_requirement="Добавить блок сопутствующих товаров на карточку",
        tech_spec=TechSpec(
            goal="Увеличить средний чек",
            scope="Добавить блок рекомендаций на карточку товара",
            constraints=["Не более 5 товаров", "Загрузка не дольше 200 мс"],
        ),
        user_stories=[
            UserStory(
                role="Покупатель",
                action="видеть сопутствующие товары",
                value="быстрее собрать корзину",
            )
        ],
        acceptance_criteria=[
            AcceptanceCriteria(
                ac_id="AC-1",
                type=ACType.MAIN,
                given="пользователь на карточке товара",
                when="страница загружена",
                then="отображается блок из 5 сопутствующих товаров",
            ),
            AcceptanceCriteria(
                ac_id="AC-2",
                type=ACType.EDGE,
                given="нет сопутствующих товаров",
                when="страница загружена",
                then="блок скрыт",
            ),
        ],
        tasks=[
            Task(
                role=Role.FRONTEND,
                title="Верстка блока рекомендаций",
                description="Компонент с карточками товаров",
                story_points=3,
            ),
            Task(
                role=Role.BACKEND,
                title="Endpoint рекомендаций",
                description="GET /api/products/{id}/related",
                story_points=5,
            ),
        ],
        test_cases=[
            TestCase(
                ac_id="AC-1",
                name="test_block_visible",
                code="def test_block_visible():\n    assert True",
            )
        ],
        risks_and_questions=["Неизвестен источник рекомендаций"],
    )


@pytest.fixture
def mock_polza(sample_output: StructuraOutput):
    """Мок Polza.ai: патчит generate_docs там, где его используют роуты."""
    with patch(
        "api.routes.generate.generate_docs",
        new_callable=AsyncMock,
        return_value=sample_output,
    ) as mock:
        yield mock