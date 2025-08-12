from domains.molding_areas.models import MoldingArea
from domains.molding_areas.schemas import MoldingAreaLookupResponse, MoldingAreaLookupsListResponse
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class MoldingAreaService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_molding_area_lookups_list(
        self,
        page: int,
        per_page: int
    ) -> MoldingAreaLookupsListResponse:
        conditions = [MoldingArea.archived_at == None, ]

        total_molding_areas = await self.uow.molding_areas.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_molding_areas + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        molding_area_entities = await self.uow.molding_areas.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions
        )
        response_items = [
            MoldingAreaLookupResponse.model_validate(molding_area)
            for molding_area in molding_area_entities
        ]

        return MoldingAreaLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_molding_areas
        )
