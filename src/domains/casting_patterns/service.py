from uuid import UUID

from domains.casting_patterns.models import CastingPattern
from domains.casting_patterns.repository import CastingPatternLoadOptions
from domains.casting_patterns.schemas import (
    CastingPatternLookupResponse,
    CastingPatternLookupsListResponse
)
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class CastingPatternService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_casting_pattern_lookups_list(
        self,
        page: int,
        per_page: int,
        casting_product_id: UUID
    ) -> CastingPatternLookupsListResponse:
        conditions = [CastingPattern.deleted_at == None, ]

        if casting_product_id:
            conditions.append(CastingPattern.casting_product_id == casting_product_id)

        total_casting_patterns = await self.uow.casting_patterns.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_casting_patterns + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        casting_pattern_entities = await self.uow.casting_patterns.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions,
            include=[CastingPatternLoadOptions.CASTING_PRODUCT]
        )
        response_items = [
            CastingPatternLookupResponse.model_validate(casting_pattern)
            for casting_pattern in casting_pattern_entities
        ]

        return CastingPatternLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_casting_patterns
        )
