"""Роут генерации документации."""

import logging

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse

from api.services.polza import GenerationError, generate_docs
from api.templates import templates

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    requirement: str = Form(...),
) -> HTMLResponse:
    """Принимает требование, вызывает Qwen, рендерит результат."""
    if not requirement.strip():
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"requirement": requirement, "error": "Введите требование"},
            status_code=400,
        )

    try:
        result = await generate_docs(requirement)
    except GenerationError as exc:
        logger.warning("Ошибка генерации: %s", exc)
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"requirement": requirement, "error": str(exc)},
            status_code=502,
        )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={"result": result},
    )