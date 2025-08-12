from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.casting_patterns.dependencies import get_casting_pattern_service
from domains.casting_patterns.schemas import (
    CastingPatternCreate,
    CastingPatternLookupsListResponse,
    CastingPatternUpdate,
    CastingPatternDetailResponse,
    CastingPatternListResponse
)
from domains.casting_patterns.service import CastingPatternService


router = APIRouter()


@router.get("/lookups", response_model=CastingPatternLookupsListResponse)
async def get_casting_pattern_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    casting_product_id: UUID = Query(None, title="casting-product-id"),
    casting_pattern_service: CastingPatternService = Depends(get_casting_pattern_service),
    current_user: UserData = Depends(require_login())
) -> CastingPatternLookupsListResponse:
    return await casting_pattern_service.get_casting_pattern_lookups_list(
        page=page,
        per_page=per_page,
        casting_product_id=casting_product_id
    )

# @router.get("/", response_model=CastingPatternListResponse)
# async def get_casting_patterns_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     casting_pattern_service: CastingPatternService = Depends(get_casting_pattern_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingPatternListResponse:
#     return await casting_pattern_service.get_casting_patterns_list(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post("/", response_model=CastingPatternDetailResponse, status_code=status.HTTP_201_CREATED)
# async def create_casting_pattern(
#     casting_pattern_data: CastingPatternCreate,
#     casting_pattern_service: CastingPatternService = Depends(get_casting_pattern_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingPatternDetailResponse:
#     return await casting_pattern_service.create_casting_pattern(casting_pattern_data)
#
#
# @router.get("/{casting_pattern_id}", response_model=CastingPatternDetailResponse)
# async def get_casting_pattern(
#     casting_pattern_id: UUID,
#     casting_pattern_service: CastingPatternService = Depends(get_casting_pattern_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingPatternDetailResponse:
#     return await casting_pattern_service.get_casting_pattern_by_id(casting_pattern_id)
#
#
# @router.put("/{casting_pattern_id}", response_model=CastingPatternDetailResponse)
# async def update_casting_pattern(
#     casting_pattern_id: UUID,
#     casting_pattern_data: CastingPatternUpdate,
#     casting_pattern_service: CastingPatternService = Depends(get_casting_pattern_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingPatternDetailResponse:
#     return await casting_pattern_service.update_casting_pattern(
#         casting_pattern_id,
#         casting_pattern_data
#     )
#
#
# @router.delete("/{casting_pattern_id}", response_model=CastingPatternDetailResponse)
# async def delete_casting_pattern(
#     casting_pattern_id: UUID,
#     casting_pattern_service: CastingPatternService = Depends(get_casting_pattern_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingPatternDetailResponse:
#     return await casting_pattern_service.delete_casting_pattern(casting_pattern_id)
#
#
# @router.post("/{casting_pattern_id}/restore", response_model=CastingPatternDetailResponse)
# async def restore_casting_pattern(
#     casting_pattern_id: UUID,
#     casting_pattern_service: CastingPatternService = Depends(get_casting_pattern_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingPatternDetailResponse:
#     return await casting_pattern_service.restore_casting_pattern(casting_pattern_id)
