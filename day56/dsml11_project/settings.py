import os

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",env_file_encoding="utf-8",
        extra = "ignore"
        )

    DB_URL: str = os.getenv("DB_url", "postgresql+asyncpg://postgres:Postgres#2026@localhost:5432/dsml11")