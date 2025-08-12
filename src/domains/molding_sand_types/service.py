from domains.molding_sand_types.models import MoldingSandType
from domains.molding_sand_types.schemas import (
    MoldingSandTypeLookupResponse,
    MoldingSandTypeLookupsListResponse
)
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class MoldingSandTypeService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_molding_sand_type_lookups_list(
        self,
        page: int,
        per_page: int,
    ) -> MoldingSandTypeLookupsListResponse:
        conditions = [MoldingSandType.archived_at == None, ]

        total_molding_sand_types = await self.uow.molding_sand_types.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_molding_sand_types + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        molding_sand_type_entities = await self.uow.molding_sand_types.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions
        )
        response_items = [
            MoldingSandTypeLookupResponse.model_validate(molding_sand_type)
            for molding_sand_type in molding_sand_type_entities
        ]

        return MoldingSandTypeLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_molding_sand_types
        )
