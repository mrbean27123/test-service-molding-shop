from domains.mold_core_types.models import MoldCoreType
from domains.mold_core_types.repository import MoldCoreTypeLoadOptions
from domains.mold_core_types.schemas import (
    MoldCoreTypeLookupResponse,
    MoldCoreTypeLookupsListResponse
)
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class MoldCoreTypeService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_mold_core_type_lookups_list(
        self,
        page: int,
        per_page: int
    ) -> MoldCoreTypeLookupsListResponse:
        conditions = [MoldCoreType.archived_at == None, ]

        total_mold_core_types = await self.uow.mold_core_types.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_mold_core_types + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        mold_core_type_entities = await self.uow.mold_core_types.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions,
            include=[MoldCoreTypeLoadOptions.CASTING_PRODUCT]
        )
        response_items = [
            MoldCoreTypeLookupResponse.model_validate(mold_core_type)
            for mold_core_type in mold_core_type_entities
        ]

        return MoldCoreTypeLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_mold_core_types
        )
