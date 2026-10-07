"""Клиент Polza.ai для вызова Qwen."""

import logging
from pathlib import Path

from openai import APIConnectionError, APIStatusError, AsyncOpenAI
from pydantic import ValidationError

from api.config import settings
from models.output import StructuraOutput

logger = logging.getLogger(__name__)

PROMPT_PATH = Path(__file__).resolve().parent.parent.parent / "prompts" / "v1" / "system.md"


class GenerationError(Exception):
    """Ошибка генерации документации."""


def _load_system_prompt() -> str:
    """Читает системный промпт v1."""
    if not PROMPT_PATH.exists():
        raise GenerationError(f"Промпт не найден: {PROMPT_PATH}")
    return PROMPT_PATH.read_text(encoding="utf-8")


def _get_client() -> AsyncOpenAI:
    """Создаёт async-клиент Polza.ai."""
    return AsyncOpenAI(
        api_key=settings.polza_api_key,
        base_url=settings.polza_base_url,
        timeout=settings.request_timeout,
    )


async def generate_docs(requirement: str) -> StructuraOutput:
    """Генерирует пакет документации по сырому требованию.

    Args:
        requirement: сырое бизнес-требование от PM.

    Returns:
        Валидированный StructuraOutput.

    Raises:
        GenerationError: если LLM недоступен, вернул ошибку или невалидный JSON.
    """
    if not requirement or not requirement.strip():
        raise GenerationError("Требование не может быть пустым")

    system_prompt = _load_system_prompt()
    client = _get_client()

    try:
        response = await client.chat.completions.create(
            model=settings.llm_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": requirement.strip()},
            ],
            response_format={"type": "json_object"},
            temperature=0.3,
        )
    except APIConnectionError as exc:
        logger.exception("Polza.ai недоступен")
        raise GenerationError("LLM-провайдер недоступен. Попробуйте позже.") from exc
    except APIStatusError as exc:
        logger.exception("Polza.ai вернул ошибку %s", exc.status_code)
        raise GenerationError(
            f"LLM-провайдер вернул ошибку {exc.status_code}. Попробуйте позже."
        ) from exc

    content = response.choices[0].message.content or ""

    try:
        return StructuraOutput.model_validate_json(content)
    except ValidationError as exc:
        logger.error("Невалидный ответ LLM: %s", exc)
        raise GenerationError(
            "LLM вернул невалидный ответ. Попробуйте переформулировать требование."
        ) from exc