from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.iron_oxides.dependencies import get_iron_oxide_service
from domains.iron_oxides.schemas import (
    IronOxideCreate,
    IronOxideLookupsListResponse, IronOxideUpdate,
    IronOxideDetailResponse,
    IronOxideListResponse
)
from domains.iron_oxides.service import IronOxideService


router = APIRouter()


@router.get("/lookups", response_model=IronOxideLookupsListResponse)
async def get_iron_oxide_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    iron_oxide_service: IronOxideService = Depends(get_iron_oxide_service),
    current_user: UserData = Depends(require_login())
) -> IronOxideLookupsListResponse:
    return await iron_oxide_service.get_iron_oxide_lookups_list(
        page=page,
        per_page=per_page
    )

# @router.get("/", response_model=IronOxideListResponse)
# async def get_iron_oxides_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     iron_oxide_service: IronOxideService = Depends(get_iron_oxide_service),
#     current_user: UserData = Depends(require_login())
# ) -> IronOxideListResponse:
#     return await iron_oxide_service.get_iron_oxides_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post("/", response_model=IronOxideDetailResponse, status_code=status.HTTP_201_CREATED)
# async def create_iron_oxide(
#     iron_oxide_data: IronOxideCreate,
#     iron_oxide_service: IronOxideService = Depends(get_iron_oxide_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> IronOxideDetailResponse:
#     return await iron_oxide_service.create_iron_oxide(iron_oxide_data)
#
#
# @router.get("/{iron_oxide_id}", response_model=IronOxideDetailResponse)
# async def get_iron_oxide(
#     iron_oxide_id: UUID,
#     iron_oxide_service: IronOxideService = Depends(get_iron_oxide_service),
#     current_user: UserData = Depends(require_login())
# ) -> IronOxideDetailResponse:
#     return await iron_oxide_service.get_iron_oxide_by_id(iron_oxide_id)
#
#
# @router.put("/{iron_oxide_id}", response_model=IronOxideDetailResponse)
# async def update_iron_oxide(
#     iron_oxide_id: UUID,
#     iron_oxide_data: IronOxideUpdate,
#     iron_oxide_service: IronOxideService = Depends(get_iron_oxide_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> IronOxideDetailResponse:
#     return await iron_oxide_service.update_iron_oxide(iron_oxide_id, iron_oxide_data)
#
#
# @router.delete("/{iron_oxide_id}", response_model=IronOxideDetailResponse)
# async def delete_iron_oxide(
#     iron_oxide_id: UUID,
#     iron_oxide_service: IronOxideService = Depends(get_iron_oxide_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> IronOxideDetailResponse:
#     return await iron_oxide_service.delete_iron_oxide(iron_oxide_id)
#
#
# @router.post("/{iron_oxide_id}/restore", response_model=IronOxideDetailResponse)
# async def restore_iron_oxide(
#     iron_oxide_id: UUID,
#     iron_oxide_service: IronOxideService = Depends(get_iron_oxide_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> IronOxideDetailResponse:
#     return await iron_oxide_service.restore_iron_oxide(iron_oxide_id)
