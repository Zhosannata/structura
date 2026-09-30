"""Тесты сервиса Polza.ai (с мок-клиентом)."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from api.services.polza import GenerationError, generate_docs


def _make_mock_response(json_content: str) -> MagicMock:
    """Собирает mock-ответ от AsyncOpenAI."""
    response = MagicMock()
    response.choices = [MagicMock()]
    response.choices[0].message.content = json_content
    return response


async def test_generate_docs_success(sample_output) -> None:
    """Успешный вызов возвращает StructuraOutput."""
    mock_client = MagicMock()
    mock_client.chat.completions.create = AsyncMock(
        return_value=_make_mock_response(sample_output.model_dump_json())
    )

    with patch("api.services.polza._get_client", return_value=mock_client):
        result = await generate_docs("Добавить сопутствующие товары")

    assert result.raw_requirement == sample_output.raw_requirement
    assert result.tech_spec.goal == sample_output.tech_spec.goal
    mock_client.chat.completions.create.assert_awaited_once()


async def test_generate_docs_empty_requirement() -> None:
    """Пустое требование — GenerationError без вызова LLM."""
    with pytest.raises(GenerationError, match="пустым"):
        await generate_docs("   ")


async def test_generate_docs_invalid_json(sample_output) -> None:
    """Невалидный JSON от LLM → GenerationError."""
    mock_client = MagicMock()
    mock_client.chat.completions.create = AsyncMock(
        return_value=_make_mock_response('{"broken": "json"}')
    )

    with patch("api.services.polza._get_client", return_value=mock_client):
        with pytest.raises(GenerationError, match="невалидный"):
            await generate_docs("Любое требование")