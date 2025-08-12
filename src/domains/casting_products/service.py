from domains.casting_products.models import CastingProduct
from domains.casting_products.schemas import (
    CastingProductLookupResponse,
    CastingProductLookupsListResponse
)
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class CastingProductService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_casting_product_lookups_list(
        self,
        page: int,
        per_page: int
    ) -> CastingProductLookupsListResponse:
        conditions = [CastingProduct.archived_at == None, ]

        total_casting_products = await self.uow.casting_products.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_casting_products + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        casting_product_entities = await self.uow.casting_products.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions,
        )
        response_items = [
            CastingProductLookupResponse.model_validate(casting_product)
            for casting_product in casting_product_entities
        ]

        return CastingProductLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_casting_products
        )
