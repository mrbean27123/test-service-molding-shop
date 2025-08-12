from datetime import datetime, timezone
from typing import Generic
from uuid import UUID

from infrastructure.repositories.base.types import IsBaseRepository, ModelT


class SoftArchiveMixin(Generic[ModelT]):
    async def soft_archive(self: IsBaseRepository[ModelT], obj_id: UUID | int) -> ModelT | None:
        db_obj = await self.get_by_id(obj_id)

        if not db_obj:
            return None

        setattr(db_obj, "archived_at", datetime.now(timezone.utc))

        return db_obj

    async def restore(self: IsBaseRepository[ModelT], obj_id: UUID | int) -> ModelT | None:
        db_obj = await self.get_by_id(obj_id)

        if not db_obj:
            return None

        setattr(db_obj, "archived_at", None)

        return db_obj
