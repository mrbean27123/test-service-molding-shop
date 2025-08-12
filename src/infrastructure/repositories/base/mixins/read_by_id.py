from typing import Generic
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import InstrumentedAttribute

from infrastructure.repositories.base.types import IsBaseRepository, LoadOptionsT, ModelT


class ReadByIdMixin(Generic[ModelT, LoadOptionsT]):
    async def get_by_id(
        self: IsBaseRepository[ModelT],
        obj_id: UUID | int,
        include: list[LoadOptionsT] | None = None
    ) -> ModelT | None:
        """Retrieve a single object of `ModelT` by its ID."""
        model_id_field: InstrumentedAttribute = self.model.id

        stmt = select(self.model).where(model_id_field == obj_id)
        stmt = self._apply_load_options(stmt, include)
        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_many_by_ids(
        self: IsBaseRepository[ModelT],
        obj_ids: list[UUID] | list[int],
        include: list[LoadOptionsT] | None = None
    ) -> list[ModelT]:
        """Retrieve a list of `ModelT` objects by their IDs."""
        model_id_field: InstrumentedAttribute = self.model.id

        stmt = select(self.model).where(model_id_field.in_(obj_ids))
        stmt = self._apply_load_options(stmt, include)
        result = await self.db.execute(stmt)

        return list(result.scalars().all())
