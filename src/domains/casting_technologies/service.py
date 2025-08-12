from domains.casting_technologies.models import CastingTechnology
from domains.casting_technologies.schemas import (
    CastingTechnologyLookupResponse,
    CastingTechnologyLookupsListResponse
)
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class CastingTechnologyService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_casting_technology_lookups_list(
        self,
        page: int,
        per_page: int,
    ) -> CastingTechnologyLookupsListResponse:
        conditions = [CastingTechnology.archived_at == None, ]

        total_casting_technologies = await self.uow.casting_technologies.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_casting_technologies + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        casting_technology_entities = await self.uow.casting_technologies.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions,
        )
        response_items = [
            CastingTechnologyLookupResponse.model_validate(casting_technology)
            for casting_technology in casting_technology_entities
        ]

        return CastingTechnologyLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_casting_technologies
        )
