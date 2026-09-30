"""Точка входа FastAPI-приложения."""

import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routes import generate, pages

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Structura", version="0.1.0")

app.include_router(pages.router)
app.include_router(generate.router)

STATIC_DIR = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")