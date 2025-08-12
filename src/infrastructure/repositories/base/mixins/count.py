from typing import Any, Generic

from sqlalchemy import BinaryExpression, and_, func, select

from infrastructure.repositories.base.types import IsBaseRepository, ModelT


class CountMixin(Generic[ModelT]):
    async def get_count(
        self: IsBaseRepository[ModelT],
        where_conditions: list[Any] | None = None
    ) -> int:
        stmt = select(func.count(self.model.id)).where(and_(*where_conditions))
        result = await self.db.execute(stmt)

        return result.scalar_one()
