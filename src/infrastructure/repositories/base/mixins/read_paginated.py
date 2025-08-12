from typing import Generic

from sqlalchemy import BinaryExpression, BooleanClauseList, and_, select

from infrastructure.repositories.base.criterias import PaginationCriteria
from infrastructure.repositories.base.types import IsBaseRepository, LoadOptionsT, ModelT


class ReadPaginatedMixin(Generic[ModelT, LoadOptionsT]):
    """
    Generic pagination mixin for SQLAlchemy-based CRUD repositories.

    This mixin adds a method to fetch paginated results from the database for any model `ModelT`,
    optionally including loader options (`LoadOptionsT`) such as joinedload or selectinload.

    Should be combined with a CRUD base class providing `self.model` and `self.db`.
    """

    async def get_all_paginated(
        self: IsBaseRepository[ModelT],
        pagination: PaginationCriteria,
        where_conditions: list[BinaryExpression | BooleanClauseList] | None = None,
        include: list[LoadOptionsT] | None = None
    ) -> list[ModelT]:
        """
        Retrieve a paginated list of `ModelT`.

        This method fetches a subset of SQLAlchemy ORM model instances of type `ModelT` from the
        database based on the given pagination parameters.
        """
        stmt = select(self.model)

        if where_conditions:
            stmt = stmt.where(and_(*where_conditions))

        stmt = self._apply_load_options(stmt, include)
        stmt = stmt.offset(pagination.offset).limit(pagination.limit)
        result = await self.db.execute(stmt)

        return list(result.scalars().all())
