from domains.mold_core_batches.models import MoldCoreBatch
from domains.mold_core_batches.repository import MoldCoreBatchLoadOptions
from domains.mold_core_batches.schemas import (
    MoldCoreBatchLookupResponse,
    MoldCoreBatchLookupsListResponse
)
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class MoldCoreBatchService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_mold_core_batch_lookups_list(
        self,
        page: int,
        per_page: int
    ) -> MoldCoreBatchLookupsListResponse:
        conditions = [MoldCoreBatch.deleted_at == None, ]

        total_mold_core_batches = await self.uow.mold_core_batches.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_mold_core_batches + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        mold_core_batch_entities = await self.uow.mold_core_batches.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions,
            include=[
                MoldCoreBatchLoadOptions.MOLDING_SAND_TYPE,
                MoldCoreBatchLoadOptions.MOLD_CORE_TYPE__CASTING_PRODUCT,
                MoldCoreBatchLoadOptions.MOLD_CORE_MAKING_MACHINE,
            ]
        )
        response_items = [
            MoldCoreBatchLookupResponse.model_validate(mold_core_batch)
            for mold_core_batch in mold_core_batch_entities
        ]

        return MoldCoreBatchLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_mold_core_batches
        )
