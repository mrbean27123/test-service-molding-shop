from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.casting_technologies.dependencies import get_casting_technology_service
from domains.casting_technologies.schemas import (
    CastingTechnologyCreate,
    CastingTechnologyUpdate,
    CastingTechnologyLookupsListResponse,
    CastingTechnologyDetailResponse,
    CastingTechnologyListResponse
)
from domains.casting_technologies.service import CastingTechnologyService


router = APIRouter()


@router.get("/lookups", response_model=CastingTechnologyLookupsListResponse)
async def get_casting_technology_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    casting_technology_service: CastingTechnologyService = Depends(get_casting_technology_service),
    current_user: UserData = Depends(require_login())
) -> CastingTechnologyLookupsListResponse:
    return await casting_technology_service.get_casting_technology_lookups_list(
        page=page,
        per_page=per_page
    )

# @router.get("/", response_model=CastingTechnologyListResponse)
# async def get_casting_technologies_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     casting_technology_service: CastingTechnologyService = Depends(get_casting_technology_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingTechnologyListResponse:
#     return await casting_technology_service.get_casting_technologies_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post(
#     "/",
#     response_model=CastingTechnologyDetailResponse,
#     status_code=status.HTTP_201_CREATED
# )
# async def create_casting_technology(
#     casting_technology_data: CastingTechnologyCreate,
#     casting_technology_service: CastingTechnologyService = Depends(get_casting_technology_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingTechnologyDetailResponse:
#     return await casting_technology_service.create_casting_technology(casting_technology_data)
#
#
# @router.get("/{casting_technology_id}", response_model=CastingTechnologyDetailResponse)
# async def get_casting_technology(
#     casting_technology_id: int,
#     casting_technology_service: CastingTechnologyService = Depends(get_casting_technology_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingTechnologyDetailResponse:
#     return await casting_technology_service.get_casting_technology_by_id(casting_technology_id)
#
#
# @router.put("/{casting_technology_id}", response_model=CastingTechnologyDetailResponse)
# async def update_casting_technology(
#     casting_technology_id: int,
#     casting_technology_data: CastingTechnologyUpdate,
#     casting_technology_service: CastingTechnologyService = Depends(get_casting_technology_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingTechnologyDetailResponse:
#     return await casting_technology_service.update_casting_technology(
#         casting_technology_id,
#         casting_technology_data
#     )
#
#
# @router.delete("/{casting_technology_id}", response_model=CastingTechnologyDetailResponse)
# async def delete_casting_technology(
#     casting_technology_id: int,
#     casting_technology_service: CastingTechnologyService = Depends(get_casting_technology_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingTechnologyDetailResponse:
#     return await casting_technology_service.delete_casting_technology(casting_technology_id)
#
#
# @router.post("/{casting_technology_id}/restore", response_model=CastingTechnologyDetailResponse)
# async def restore_casting_technology(
#     casting_technology_id: int,
#     casting_technology_service: CastingTechnologyService = Depends(get_casting_technology_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> CastingTechnologyDetailResponse:
#     return await casting_technology_service.restore_casting_technology(casting_technology_id)
