from typing import Generic
from uuid import UUID

from sqlalchemy import BinaryExpression, BooleanClauseList, and_, exists, select
from sqlalchemy.orm import InstrumentedAttribute

from infrastructure.repositories.base.types import IsBaseRepository, ModelT


class ExistsMixin(Generic[ModelT]):
    async def exists_by_id(self: IsBaseRepository[ModelT], obj_id: UUID | int) -> bool:
        model_id_field: InstrumentedAttribute = self.model.id

        stmt = select(exists().where(model_id_field == obj_id))
        result = await self.db.execute(stmt)

        return result.scalar()

    async def exists_where(
        self: IsBaseRepository[ModelT],
        *conditions: BinaryExpression | BooleanClauseList
    ) -> bool:
        """
        Check if any record exists matching the given conditions.

        Args:
            *conditions: SQLAlchemy conditions for WHERE clause

        Example:
            # Check if User exists with specific ID
            exists = await repo.exists_where(User.id == user_id)

            # Check if User exists with specific email and is active
            exists = await repo.exists_where(
                User.email == "test@example.com",
                User.is_active == True
            )

            # Check uniqueness during update (exclude current record)
            exists = await repo.exists_where(
                User.email == "new@example.com",
                User.id != current_user_id
            )
        """
        stmt = select(exists().where(and_(*conditions)))
        result = await self.db.execute(stmt)

        return result.scalar()
