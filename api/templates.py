"""Общий экземпляр Jinja2Templates."""

from pathlib import Path

from fastapi.templating import Jinja2Templates

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

templates = Jinja2Templates(directory=str(FRONTEND_DIR))