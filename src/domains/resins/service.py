from domains.resins.models import Resin
from domains.resins.schemas import ResinLookupResponse, ResinLookupsListResponse
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class ResinService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_resin_lookups_list(
        self,
        page: int,
        per_page: int,
    ) -> ResinLookupsListResponse:
        conditions = [Resin.deleted_at == None, ]

        total_resins = await self.uow.resins.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_resins + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        resin_entities = await self.uow.resins.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions
        )
        response_items = [
            ResinLookupResponse.model_validate(resin)
            for resin in resin_entities
        ]

        return ResinLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_resins
        )
