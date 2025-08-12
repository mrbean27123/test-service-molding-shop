from typing import Generic, Type

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load

from infrastructure.repositories.base.types import LoadOptionsT, ModelT


class RepositoryBase(Generic[ModelT, LoadOptionsT]):
    _LOAD_OPTIONS_MAP: dict[LoadOptionsT, Load] = {}

    def __init__(self, db: AsyncSession, model: Type[ModelT]):
        self.db = db
        self.model = model

    def _apply_load_options(
        self,
        stmt: Select,
        include: list[LoadOptionsT] | None = None
    ) -> Select:
        """Apply SQLAlchemy load options (e.g. joinedload, selectinload) to the statement."""
        if not include or not self._LOAD_OPTIONS_MAP:
            return stmt

        options = [self._LOAD_OPTIONS_MAP[option] for option in include]
        stmt = stmt.options(*options)

        return stmt
