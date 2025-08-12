from typing import Literal

from fastapi import APIRouter, Depends, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.molding_sand_types.dependencies import get_molding_sand_type_service
from domains.molding_sand_types.schemas import (
    MoldingSandTypeCreate,
    MoldingSandTypeLookupsListResponse, MoldingSandTypeUpdate,
    MoldingSandTypeDetailResponse,
    MoldingSandTypeListResponse
)
from domains.molding_sand_types.service import MoldingSandTypeService


router = APIRouter()


@router.get("/lookups", response_model=MoldingSandTypeLookupsListResponse)
async def get_molding_sand_type_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    molding_sand_type_service: MoldingSandTypeService = Depends(get_molding_sand_type_service),
    current_user: UserData = Depends(require_login())
) -> MoldingSandTypeLookupsListResponse:
    return await molding_sand_type_service.get_molding_sand_type_lookups_list(
        page=page,
        per_page=per_page
    )

# @router.get("/", response_model=MoldingSandTypeListResponse)
# async def get_molding_sand_types_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     molding_sand_type_service: MoldingSandTypeService = Depends(get_molding_sand_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingSandTypeListResponse:
#     return await molding_sand_type_service.get_molding_sand_types_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post(
#     "/",
#     response_model=MoldingSandTypeDetailResponse,
#     status_code=status.HTTP_201_CREATED
# )
# async def create_molding_sand_type(
#     molding_sand_type_data: MoldingSandTypeCreate,
#     molding_sand_type_service: MoldingSandTypeService = Depends(get_molding_sand_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingSandTypeDetailResponse:
#     return await molding_sand_type_service.create_molding_sand_type(molding_sand_type_data)
#
#
# @router.get("/{molding_sand_type_id}", response_model=MoldingSandTypeDetailResponse)
# async def get_molding_sand_type(
#     molding_sand_type_id: int,
#     molding_sand_type_service: MoldingSandTypeService = Depends(get_molding_sand_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingSandTypeDetailResponse:
#     return await molding_sand_type_service.get_molding_sand_type_by_id(molding_sand_type_id)
#
#
# @router.put("/{molding_sand_type_id}", response_model=MoldingSandTypeDetailResponse)
# async def update_molding_sand_type(
#     molding_sand_type_id: int,
#     molding_sand_type_data: MoldingSandTypeUpdate,
#     molding_sand_type_service: MoldingSandTypeService = Depends(get_molding_sand_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingSandTypeDetailResponse:
#     return await molding_sand_type_service.update_molding_sand_type(
#         molding_sand_type_id,
#         molding_sand_type_data
#     )
#
#
# @router.delete("/{molding_sand_type_id}", response_model=MoldingSandTypeDetailResponse)
# async def delete_molding_sand_type(
#     molding_sand_type_id: int,
#     molding_sand_type_service: MoldingSandTypeService = Depends(get_molding_sand_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingSandTypeDetailResponse:
#     return await molding_sand_type_service.delete_molding_sand_type(molding_sand_type_id)
#
#
# @router.post("/{molding_sand_type_id}/restore", response_model=MoldingSandTypeDetailResponse)
# async def restore_molding_sand_type(
#     molding_sand_type_id: int,
#     molding_sand_type_service: MoldingSandTypeService = Depends(get_molding_sand_type_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingSandTypeDetailResponse:
#     return await molding_sand_type_service.restore_molding_sand_type(molding_sand_type_id)
