from datetime import datetime, timezone
from typing import Generic
from uuid import UUID

from infrastructure.core.config import settings
from infrastructure.repositories.base.types import IsBaseRepository, ModelT


class SoftDeleteMixin(Generic[ModelT]):
    async def soft_delete(self: IsBaseRepository[ModelT], obj_id: UUID | int) -> ModelT | None:
        db_obj = await self.get_by_id(obj_id)

        if not db_obj:
            return None

        user = context.get_current_user()
        actor_id = user.id if user else settings.SYSTEM_USER_ID

        setattr(db_obj, "deleted_at", datetime.now(timezone.utc))
        setattr(db_obj, "deleted_by_id", actor_id)

        return db_obj

    async def restore(self: IsBaseRepository[ModelT], obj_id: UUID | int) -> ModelT | None:
        db_obj = await self.get_by_id(obj_id)

        if not db_obj:
            return None

        setattr(db_obj, "deleted_at", None)
        setattr(db_obj, "deleted_by_id", None)

        return db_obj
