from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.resins.dependencies import get_resin_service
from domains.resins.schemas import (
    ResinCreate,
    ResinLookupsListResponse, ResinUpdate,
    ResinDetailResponse,
    ResinListResponse
)
from domains.resins.service import ResinService


router = APIRouter()


@router.get("/lookups", response_model=ResinLookupsListResponse)
async def get_resin_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    resin_service: ResinService = Depends(get_resin_service),
    current_user: UserData = Depends(require_login())
) -> ResinLookupsListResponse:
    return await resin_service.get_resin_lookups_list(
        page=page,
        per_page=per_page,
    )

# @router.get("/", response_model=ResinListResponse)
# async def get_resins_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     resin_service: ResinService = Depends(get_resin_service),
#     current_user: UserData = Depends(require_login())
# ) -> ResinListResponse:
#     return await resin_service.get_resins_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post("/", response_model=ResinDetailResponse, status_code=status.HTTP_201_CREATED)
# async def create_resin(
#     resin_data: ResinCreate,
#     resin_service: ResinService = Depends(get_resin_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> ResinDetailResponse:
#     return await resin_service.create_resin(resin_data)
#
#
# @router.get("/{resin_id}", response_model=ResinDetailResponse)
# async def get_resin(
#     resin_id: UUID,
#     resin_service: ResinService = Depends(get_resin_service),
#     current_user: UserData = Depends(require_login())
# ) -> ResinDetailResponse:
#     return await resin_service.get_resin_by_id(resin_id)
#
#
# @router.put("/{resin_id}", response_model=ResinDetailResponse)
# async def update_resin(
#     resin_id: UUID,
#     resin_data: ResinUpdate,
#     resin_service: ResinService = Depends(get_resin_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> ResinDetailResponse:
#     return await resin_service.update_resin(resin_id, resin_data)
#
#
# @router.delete("/{resin_id}", response_model=ResinDetailResponse)
# async def delete_resin(
#     resin_id: UUID,
#     resin_service: ResinService = Depends(get_resin_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> ResinDetailResponse:
#     return await resin_service.delete_resin(resin_id)
#
#
# @router.post("/{resin_id}/restore", response_model=ResinDetailResponse)
# async def restore_resin(
#     resin_id: UUID,
#     resin_service: ResinService = Depends(get_resin_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> ResinDetailResponse:
#     return await resin_service.restore_resin(resin_id)
