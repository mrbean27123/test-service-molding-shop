from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.mold_core_types.dependencies import get_mold_core_type_service
from domains.mold_core_types.schemas import (
    MoldCoreTypeCreate,
    MoldCoreTypeLookupsListResponse, MoldCoreTypeUpdate,
    MoldCoreTypeDetailResponse,
    MoldCoreTypeListResponse
)
from domains.mold_core_types.service import MoldCoreTypeService


router = APIRouter()


@router.get("/lookups", response_model=MoldCoreTypeLookupsListResponse)
async def get_mold_core_type_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    mold_core_type_service: MoldCoreTypeService = Depends(get_mold_core_type_service),
    current_user: UserData = Depends(require_login())
) -> MoldCoreTypeLookupsListResponse:
    return await mold_core_type_service.get_mold_core_type_lookups_list(
        page=page,
        per_page=per_page
    )

# @router.get("/", response_model=MoldCoreTypeListResponse)
# async def get_mold_core_types_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     mold_core_type_service: MoldCoreTypeService = Depends(get_mold_core_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreTypeListResponse:
#     return await mold_core_type_service.get_mold_core_types_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post("/", response_model=MoldCoreTypeDetailResponse, status_code=status.HTTP_201_CREATED)
# async def create_mold_core_type(
#     mold_core_type_data: MoldCoreTypeCreate,
#     mold_core_type_service: MoldCoreTypeService = Depends(get_mold_core_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreTypeDetailResponse:
#     return await mold_core_type_service.create_mold_core_type(mold_core_type_data)
#
#
# @router.get("/{mold_core_type_id}", response_model=MoldCoreTypeDetailResponse)
# async def get_mold_core_type(
#     mold_core_type_id: UUID,
#     mold_core_type_service: MoldCoreTypeService = Depends(get_mold_core_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreTypeDetailResponse:
#     return await mold_core_type_service.get_mold_core_type_by_id(mold_core_type_id)
#
#
# @router.put("/{mold_core_type_id}", response_model=MoldCoreTypeDetailResponse)
# async def update_mold_core_type(
#     mold_core_type_id: UUID,
#     mold_core_type_data: MoldCoreTypeUpdate,
#     mold_core_type_service: MoldCoreTypeService = Depends(get_mold_core_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreTypeDetailResponse:
#     return await mold_core_type_service.update_mold_core_type(
#         mold_core_type_id,
#         mold_core_type_data
#     )
#
#
# @router.delete("/{mold_core_type_id}", response_model=MoldCoreTypeDetailResponse)
# async def delete_mold_core_type(
#     mold_core_type_id: UUID,
#     mold_core_type_service: MoldCoreTypeService = Depends(get_mold_core_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreTypeDetailResponse:
#     return await mold_core_type_service.delete_mold_core_type(mold_core_type_id)
#
#
# @router.post("/{mold_core_type_id}/restore", response_model=MoldCoreTypeDetailResponse)
# async def restore_mold_core_type(
#     mold_core_type_id: UUID,
#     mold_core_type_service: MoldCoreTypeService = Depends(get_mold_core_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreTypeDetailResponse:
#     return await mold_core_type_service.restore_mold_core_type(mold_core_type_id)
