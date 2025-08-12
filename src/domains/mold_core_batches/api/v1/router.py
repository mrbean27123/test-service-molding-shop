from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.mold_core_batches.dependencies import get_mold_core_batch_service
from domains.mold_core_batches.schemas import (
    MoldCoreBatchCreate,
    MoldCoreBatchUpdate,
    MoldCoreBatchLookupsListResponse,
    MoldCoreBatchDetailResponse,
    MoldCoreBatchListResponse
)
from domains.mold_core_batches.service import MoldCoreBatchService


router = APIRouter()


@router.get("/lookups", response_model=MoldCoreBatchLookupsListResponse)
async def get_mold_core_batch_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    mold_core_batch_service: MoldCoreBatchService = Depends(get_mold_core_batch_service),
    current_user: UserData = Depends(require_login())
) -> MoldCoreBatchLookupsListResponse:
    return await mold_core_batch_service.get_mold_core_batch_lookups_list(
        page=page,
        per_page=per_page
    )

# @router.get("/", response_model=MoldCoreBatchListResponse)
# async def get_mold_core_batches_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     mold_core_batch_service: MoldCoreBatchService = Depends(get_mold_core_batch_service),
#     current_user: UserData = Depends(require_login())
# ) -> MoldCoreBatchListResponse:
#     return await mold_core_batch_service.get_mold_core_batches_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post("/", response_model=MoldCoreBatchDetailResponse, status_code=status.HTTP_201_CREATED)
# async def create_mold_core_batch(
#     mold_core_batch_data: MoldCoreBatchCreate,
#     mold_core_batch_service: MoldCoreBatchService = Depends(get_mold_core_batch_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreBatchDetailResponse:
#     return await mold_core_batch_service.create_mold_core_batch(mold_core_batch_data)
#
#
# @router.get("/{mold_core_batch_id}", response_model=MoldCoreBatchDetailResponse)
# async def get_mold_core_batch(
#     mold_core_batch_id: UUID,
#     mold_core_batch_service: MoldCoreBatchService = Depends(get_mold_core_batch_service),
#     current_user: UserData = Depends(require_login())
# ) -> MoldCoreBatchDetailResponse:
#     return await mold_core_batch_service.get_mold_core_batch_by_id(mold_core_batch_id)
#
#
# @router.put("/{mold_core_batch_id}", response_model=MoldCoreBatchDetailResponse)
# async def update_mold_core_batch(
#     mold_core_batch_id: UUID,
#     mold_core_batch_data: MoldCoreBatchUpdate,
#     mold_core_batch_service: MoldCoreBatchService = Depends(get_mold_core_batch_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreBatchDetailResponse:
#     return await mold_core_batch_service.update_mold_core_batch(
#         mold_core_batch_id,
#         mold_core_batch_data
#     )
#
#
# @router.delete("/{mold_core_batch_id}", response_model=MoldCoreBatchDetailResponse)
# async def delete_mold_core_batch(
#     mold_core_batch_id: UUID,
#     mold_core_batch_service: MoldCoreBatchService = Depends(get_mold_core_batch_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreBatchDetailResponse:
#     return await mold_core_batch_service.delete_mold_core_batch(mold_core_batch_id)
#
#
# @router.post("/{mold_core_batch_id}/restore", response_model=MoldCoreBatchDetailResponse)
# async def restore_mold_core_batch(
#     mold_core_batch_id: UUID,
#     mold_core_batch_service: MoldCoreBatchService = Depends(get_mold_core_batch_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreBatchDetailResponse:
#     return await mold_core_batch_service.restore_mold_core_batch(mold_core_batch_id)
