from typing import Generic
from uuid import UUID

from infrastructure.repositories.base.types import IsBaseRepository, ModelT


class HardDeleteMixin(Generic[ModelT]):
    async def hard_delete(self: IsBaseRepository[ModelT], obj_id: UUID | int) -> ModelT | None:
        db_obj = await self.get_by_id(obj_id)

        if not db_obj:
            return None

        await self.db.delete(db_obj)

        return db_obj
