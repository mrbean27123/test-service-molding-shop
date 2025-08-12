from pathlib import Path
from typing import Literal
from uuid import UUID

from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_DIR = Path(__file__).resolve().parents[3]  # service-molding-shop/

ENV_PATH = ROOT_DIR / ".env"
BASE_DIR = ROOT_DIR / "src/"  # src/


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore"
    )

    # Application
    ENVIRONMENT: Literal["local", "testing", "staging", "production"] = "local"
    SERVICE_NAME: str = "Molding Shop Service"
    DEPARTMENT_NAME: str = "molding_shop"

    BASE_DIR: Path = BASE_DIR

    # Database
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    SYSTEM_USER_ID: UUID

    # pgAdmin
    # PGADMIN_DEFAULT_EMAIL: str
    # PGADMIN_DEFAULT_PASSWORD: str

    # Logging
    LOG_LEVEL: str = "INFO"

    # Testing
    PATH_TO_TESTING_DB: str = ":memory:"


settings = Settings()
