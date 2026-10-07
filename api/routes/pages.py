"""Страницы UI."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from api.templates import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """Главная страница с формой ввода."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"requirement": "", "error": None},
    )