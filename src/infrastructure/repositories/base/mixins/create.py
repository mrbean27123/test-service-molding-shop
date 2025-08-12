from typing import Generic

from infrastructure.dto.base import CreateDTOBase
from infrastructure.repositories.base.types import IsBaseRepository, ModelT


class CreateMixin(Generic[ModelT]):
    async def create(self: IsBaseRepository[ModelT], obj_data: CreateDTOBase) -> ModelT:
        obj = self.model(**obj_data.model_dump())
        self.db.add(obj)

        return obj
