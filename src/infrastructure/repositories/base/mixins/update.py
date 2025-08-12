from typing import Generic
from uuid import UUID

from infrastructure.dto.base import UpdateDTOBase
from infrastructure.repositories.base.types import IsBaseRepository, ModelT


class UpdateMixin(Generic[ModelT]):
    async def update(
        self: IsBaseRepository[ModelT],
        obj_id: UUID | int,
        obj_data: UpdateDTOBase
    ) -> ModelT | None:
        db_obj = await self.get_by_id(obj_id)

        if not db_obj:
            return None

        update_data = obj_data.model_dump(exclude_unset=True)

        if not update_data:
            return db_obj

        for field, value in update_data.items():
            setattr(db_obj, field, value)

        return db_obj
