from enum import Enum
from typing import Protocol, Type, TypeVar, runtime_checkable
from uuid import UUID

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load

from infrastructure.database.models.base import BaseORM


ModelT = TypeVar("ModelT", bound=BaseORM)
LoadOptionsT = TypeVar("LoadOptionsT", bound=Enum)


@runtime_checkable
class IsBaseRepository(Protocol[ModelT]):
    db: AsyncSession
    model: Type[ModelT]

    _LOAD_OPTIONS_MAP: dict[Enum, Load]

    async def get_by_id(
        self,
        obj_id: UUID | int,
        include: list[LoadOptionsT] | None = None
    ) -> ModelT | None:
        pass

    def _apply_load_options(
        self,
        stmt: Select,
        include: list[LoadOptionsT] | None = None
    ) -> Select:
        pass
