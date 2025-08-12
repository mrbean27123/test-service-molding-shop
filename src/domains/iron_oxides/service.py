from domains.iron_oxides.models import IronOxide
from domains.iron_oxides.schemas import IronOxideLookupResponse, IronOxideLookupsListResponse
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class IronOxideService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_iron_oxide_lookups_list(
        self,
        page: int,
        per_page: int,
    ) -> IronOxideLookupsListResponse:
        conditions = [IronOxide.deleted_at == None, ]

        total_iron_oxides = await self.uow.iron_oxides.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_iron_oxides + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        iron_oxide_entities = await self.uow.iron_oxides.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions
        )
        response_items = [
            IronOxideLookupResponse.model_validate(iron_oxide)
            for iron_oxide in iron_oxide_entities
        ]

        return IronOxideLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_iron_oxides
        )
