"""Конфигурация приложения через pydantic-settings."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройки, читаются из .env."""

    polza_api_key: str = Field(..., description="API-ключ Polza.ai")
    polza_base_url: str = Field(
        default="https://polza.ai/api/v1",
        description="Базовый URL Polza.ai",
    )
    llm_model: str = Field(
        default="qwen/qwen3.6-plus",
        description="Идентификатор модели",
    )
    request_timeout: float = Field(default=120.0, description="Таймаут запроса, сек")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()