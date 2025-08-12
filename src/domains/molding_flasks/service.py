from domains.molding_flasks.models import MoldingFlask
from domains.molding_flasks.schemas import (
    MoldingFlaskLookupResponse,
    MoldingFlaskLookupsListResponse
)
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class MoldingFlaskService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_molding_flask_lookups_list(
        self,
        page: int,
        per_page: int,
    ) -> MoldingFlaskLookupsListResponse:
        conditions = [MoldingFlask.deleted_at == None, ]

        total_molding_flasks = await self.uow.molding_flasks.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_molding_flasks + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        molding_flask_entities = await self.uow.molding_flasks.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions
        )
        response_items = [
            MoldingFlaskLookupResponse.model_validate(molding_flask)
            for molding_flask in molding_flask_entities
        ]

        return MoldingFlaskLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_molding_flasks
        )
