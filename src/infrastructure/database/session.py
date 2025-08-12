from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.core.config import settings


def get_database_url(async_driver: bool) -> str:
    driver = "postgresql+asyncpg" if async_driver else "postgresql+psycopg2"

    return (
        f"{driver}://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
        f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
    )


# Asynchronous database engine and session factory
POSTGRES_DATABASE_URL = get_database_url(async_driver=True)
postgresql_engine = create_async_engine(POSTGRES_DATABASE_URL, echo=False)
AsyncPostgresqlSessionLocal = sessionmaker(  # type: ignore
    bind=postgresql_engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)

# Synchronous engine for Alembic and migrations
sync_database_url = get_database_url(async_driver=False)
sync_postgresql_engine = create_engine(sync_database_url, echo=False)


def get_postgresql_db_session_factory() -> sessionmaker[AsyncSession]:
    return AsyncPostgresqlSessionLocal
