from domains.triethylamines.models import Triethylamine
from domains.triethylamines.schemas import (
    TriethylamineLookupResponse,
    TriethylamineLookupsListResponse
)
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class TriethylamineService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_triethylamine_lookups_list(
        self,
        page: int,
        per_page: int,
    ) -> TriethylamineLookupsListResponse:
        conditions = [Triethylamine.deleted_at == None, ]

        total_triethylamines = await self.uow.triethylamines.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_triethylamines + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        triethylamine_entities = await self.uow.triethylamines.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions
        )
        response_items = [
            TriethylamineLookupResponse.model_validate(triethylamine)
            for triethylamine in triethylamine_entities
        ]

        return TriethylamineLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_triethylamines
        )
