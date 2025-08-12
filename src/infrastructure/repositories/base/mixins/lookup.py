from typing import Generic

from sqlalchemy import select

from infrastructure.repositories.base.criterias import (
    OrderCriteria,
    PaginationCriteria,
    SearchCriteria
)
from infrastructure.repositories.base.types import IsBaseRepository, LoadOptionsT, ModelT


class LookupMixin(Generic[ModelT]):
    async def get_for_lookup(
        self: IsBaseRepository[ModelT],
        pagination: PaginationCriteria,
        search: SearchCriteria | None = None,
        order: OrderCriteria | None = None,
        include: list[LoadOptionsT] | None = None
    ) -> list[ModelT]:
        stmt = select(self.model)

        # TODO: move it inside SearchCriteria -> stmt = SearchCriteria.apply(stmt)
        if search and search.is_applicable:
            search_pattern = f"%{search.query}%"

            if search.is_case_sensitive:
                stmt = stmt.where(search.field.like(search_pattern))
            else:
                stmt = stmt.where(search.field.ilike(search_pattern))

        stmt = self._apply_load_options(stmt, include)

        # TODO: move it inside OrderCriteria -> stmt = OrderCriteria.apply(stmt)
        if order:
            stmt = stmt.order_by(order.field.asc() if order.ascending else order.field.desc())

        stmt = stmt.offset(pagination.offset).limit(pagination.limit)

        result = await self.db.execute(stmt)

        return list(result.scalars().all())
