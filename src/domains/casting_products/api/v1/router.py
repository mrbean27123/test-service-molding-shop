from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.casting_products.dependencies import get_casting_product_service
from domains.casting_products.schemas import (
    CastingProductCreate,
    CastingProductUpdate,
    CastingProductLookupsListResponse,
    CastingProductShortResponse,
    CastingProductDetailResponse,
    CastingProductListResponse
)
from domains.casting_products.service import CastingProductService


router = APIRouter()


@router.get("/lookups", response_model=CastingProductLookupsListResponse)
async def get_casting_product_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    casting_product_service: CastingProductService = Depends(get_casting_product_service),
    current_user: UserData = Depends(require_login())
) -> CastingProductLookupsListResponse:
    return await casting_product_service.get_casting_product_lookups_list(
        page=page,
        per_page=per_page,
    )

# @router.get("/", response_model=CastingProductListResponse)
# async def get_casting_products_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     casting_product_service: CastingProductService = Depends(get_casting_product_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingProductListResponse:
#     return await casting_product_service.get_casting_products_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post("/", response_model=CastingProductDetailResponse, status_code=status.HTTP_201_CREATED)
# async def create_casting_product(
#     casting_product_data: CastingProductCreate,
#     casting_product_service: CastingProductService = Depends(get_casting_product_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingProductDetailResponse:
#     return await casting_product_service.create_casting_product(casting_product_data)
#
#
# @router.get("/{casting_product_id}", response_model=CastingProductDetailResponse)
# async def get_casting_product(
#     casting_product_id: UUID,
#     casting_product_service: CastingProductService = Depends(get_casting_product_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingProductDetailResponse:
#     return await casting_product_service.get_casting_product_by_id(casting_product_id)
#
#
# @router.put("/{casting_product_id}", response_model=CastingProductDetailResponse)
# async def update_casting_product(
#     casting_product_id: UUID,
#     casting_product_data: CastingProductUpdate,
#     casting_product_service: CastingProductService = Depends(get_casting_product_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingProductDetailResponse:
#     return await casting_product_service.update_casting_product(
#         casting_product_id,
#         casting_product_data
#     )
#
#
# @router.delete("/{casting_product_id}", response_model=CastingProductDetailResponse)
# async def delete_casting_product(
#     casting_product_id: UUID,
#     casting_product_service: CastingProductService = Depends(get_casting_product_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingProductShortResponse:
#     return await casting_product_service.delete_casting_product(casting_product_id)
#
#
# @router.post("/{casting_product_id}/restore", response_model=CastingProductDetailResponse)
# async def restore_casting_product(
#     casting_product_id: UUID,
#     casting_product_service: CastingProductService = Depends(get_casting_product_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingProductShortResponse:
#     return await casting_product_service.restore_casting_product(casting_product_id)
