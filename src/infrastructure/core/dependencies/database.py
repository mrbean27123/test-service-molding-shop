from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from infrastructure.database import UnitOfWork, get_db_session_factory


async def get_uow(
    session_factory: sessionmaker[AsyncSession] = Depends(get_db_session_factory)
) -> AsyncGenerator[UnitOfWork, None]:
    async with UnitOfWork(session_factory) as uow:
        yield uow
