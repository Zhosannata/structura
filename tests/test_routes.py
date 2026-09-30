"""Тесты FastAPI-роутов."""

from fastapi.testclient import TestClient


def test_index_page(client: TestClient) -> None:
    """GET / отдаёт HTML-форму."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Опишите бизнес-требование" in response.text
    assert 'name="requirement"' in response.text


def test_generate_empty_requirement(client: TestClient) -> None:
    """POST /generate с пустым полем — 400 и сообщение об ошибке."""
    response = client.post("/generate", data={"requirement": "   "})
    assert response.status_code == 400
    assert "Введите требование" in response.text


def test_generate_success(client: TestClient, mock_polza) -> None:
    """POST /generate с валидным требованием — 200 и страница результата."""
    response = client.post(
        "/generate",
        data={"requirement": "Добавить сопутствующие товары"},
    )
    assert response.status_code == 200
    assert "Готовый пакет документации" in response.text
    assert "Техническое задание" in response.text
    mock_polza.assert_awaited_once()


def test_generate_llm_error(client: TestClient) -> None:
    """Ошибка LLM → 502 и сообщение."""
    from unittest.mock import AsyncMock, patch

    from api.services.polza import GenerationError

    with patch(
        "api.routes.generate.generate_docs",
        new_callable=AsyncMock,
        side_effect=GenerationError("LLM-провайдер вернул ошибку 402"),
    ):
        response = client.post("/generate", data={"requirement": "Что-то"})
    assert response.status_code == 502
    assert "LLM-провайдер" in response.text