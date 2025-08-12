from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.molding_areas.dependencies import get_molding_area_service
from domains.molding_areas.schemas import (
    MoldingAreaCreate,
    MoldingAreaLookupsListResponse, MoldingAreaUpdate,
    MoldingAreaDetailResponse,
    MoldingAreaListResponse
)
from domains.molding_areas.service import MoldingAreaService


router = APIRouter()


@router.get("/lookups", response_model=MoldingAreaLookupsListResponse)
async def get_molding_area_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    molding_area_service: MoldingAreaService = Depends(get_molding_area_service),
    current_user: UserData = Depends(require_login())
) -> MoldingAreaLookupsListResponse:
    return await molding_area_service.get_molding_area_lookups_list(
        page=page,
        per_page=per_page
    )

# @router.get("/", response_model=MoldingAreaListResponse)
# async def get_molding_areas_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     molding_area_service: MoldingAreaService = Depends(get_molding_area_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingAreaListResponse:
#     return await molding_area_service.get_molding_areas_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post("/", response_model=MoldingAreaDetailResponse, status_code=status.HTTP_201_CREATED)
# async def create_molding_area(
#     molding_area_data: MoldingAreaCreate,
#     molding_area_service: MoldingAreaService = Depends(get_molding_area_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingAreaDetailResponse:
#     return await molding_area_service.create_molding_area(molding_area_data)
#
#
# @router.get("/{molding_area_id}", response_model=MoldingAreaDetailResponse)
# async def get_molding_area(
#     molding_area_id: UUID,
#     molding_area_service: MoldingAreaService = Depends(get_molding_area_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingAreaDetailResponse:
#     return await molding_area_service.get_molding_area_by_id(molding_area_id)
#
#
# @router.put("/{molding_area_id}", response_model=MoldingAreaDetailResponse)
# async def update_molding_area(
#     molding_area_id: UUID,
#     molding_area_data: MoldingAreaUpdate,
#     molding_area_service: MoldingAreaService = Depends(get_molding_area_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingAreaDetailResponse:
#     return await molding_area_service.update_molding_area(molding_area_id, molding_area_data)
#
#
# @router.delete("/{molding_area_id}", response_model=MoldingAreaDetailResponse)
# async def delete_molding_area(
#     molding_area_id: UUID,
#     molding_area_service: MoldingAreaService = Depends(get_molding_area_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingAreaDetailResponse:
#     return await molding_area_service.delete_molding_area(molding_area_id)
#
#
# @router.post("/{molding_area_id}/restore", response_model=MoldingAreaDetailResponse)
# async def restore_molding_area(
#     molding_area_id: UUID,
#     molding_area_service: MoldingAreaService = Depends(get_molding_area_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingAreaDetailResponse:
#     return await molding_area_service.restore_molding_area(molding_area_id)
