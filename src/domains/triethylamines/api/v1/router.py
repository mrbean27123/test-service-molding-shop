from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.triethylamines.dependencies import get_triethylamine_service
from domains.triethylamines.schemas import (
    TriethylamineCreate,
    TriethylamineLookupsListResponse, TriethylamineUpdate,
    TriethylamineDetailResponse,
    TriethylamineListResponse
)
from domains.triethylamines.service import TriethylamineService


router = APIRouter()


@router.get("/lookups", response_model=TriethylamineLookupsListResponse)
async def get_triethylamine_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=20),
    triethylamine_service: TriethylamineService = Depends(get_triethylamine_service),
    current_user: UserData = Depends(require_login())
) -> TriethylamineLookupsListResponse:
    return await triethylamine_service.get_triethylamine_lookups_list(
        page=page,
        per_page=per_page
    )

# @router.get("/", response_model=TriethylamineListResponse)
# async def get_triethylamines_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     triethylamine_service: TriethylamineService = Depends(get_triethylamine_service),
#     current_user: UserData = Depends(require_login())
# ) -> TriethylamineListResponse:
#     return await triethylamine_service.get_triethylamines_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post("/", response_model=TriethylamineDetailResponse, status_code=status.HTTP_201_CREATED)
# async def create_triethylamine(
#     triethylamine_data: TriethylamineCreate,
#     triethylamine_service: TriethylamineService = Depends(get_triethylamine_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> TriethylamineDetailResponse:
#     return await triethylamine_service.create_triethylamine(triethylamine_data)
#
#
# @router.get("/{triethylamine_id}", response_model=TriethylamineDetailResponse)
# async def get_triethylamine(
#     triethylamine_id: UUID,
#     triethylamine_service: TriethylamineService = Depends(get_triethylamine_service),
#     current_user: UserData = Depends(require_login())
# ) -> TriethylamineDetailResponse:
#     return await triethylamine_service.get_triethylamine_by_id(triethylamine_id)
#
#
# @router.put("/{triethylamine_id}", response_model=TriethylamineDetailResponse)
# async def update_triethylamine(
#     triethylamine_id: UUID,
#     triethylamine_data: TriethylamineUpdate,
#     triethylamine_service: TriethylamineService = Depends(get_triethylamine_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> TriethylamineDetailResponse:
#     return await triethylamine_service.update_triethylamine(triethylamine_id, triethylamine_data)
#
#
# @router.delete("/{triethylamine_id}", response_model=TriethylamineDetailResponse)
# async def delete_triethylamine(
#     triethylamine_id: UUID,
#     triethylamine_service: TriethylamineService = Depends(get_triethylamine_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> TriethylamineDetailResponse:
#     return await triethylamine_service.delete_triethylamine(triethylamine_id)
#
#
# @router.post("/{triethylamine_id}/restore", response_model=TriethylamineDetailResponse)
# async def restore_triethylamine(
#     triethylamine_id: UUID,
#     triethylamine_service: TriethylamineService = Depends(get_triethylamine_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> TriethylamineDetailResponse:
#     return await triethylamine_service.restore_triethylamine(triethylamine_id)
