from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.mold_core_making_machines.dependencies import get_mold_core_making_machine_service
from domains.mold_core_making_machines.schemas import (
    MoldCoreMakingMachineCreate,
    MoldCoreMakingMachineLookupsListResponse, MoldCoreMakingMachineUpdate,
    MoldCoreMakingMachineDetailResponse,
    MoldCoreMakingMachineListResponse
)
from domains.mold_core_making_machines.service import MoldCoreMakingMachineService


router = APIRouter()


@router.get("/lookups", response_model=MoldCoreMakingMachineLookupsListResponse)
async def get_mold_core_making_machine_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    mold_core_making_machine_service: MoldCoreMakingMachineService = (
        Depends(get_mold_core_making_machine_service)
    ),
    current_user: UserData = Depends(require_login())
) -> MoldCoreMakingMachineLookupsListResponse:
    return await mold_core_making_machine_service.get_mold_core_making_machine_lookups_list(
        page=page,
        per_page=per_page,
    )

# @router.get("/", response_model=MoldCoreMakingMachineListResponse)
# async def get_mold_core_making_machines_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     mold_core_making_machine_service: MoldCoreMakingMachineService = (
#         Depends(get_mold_core_making_machine_service)
#     ),
#     current_user: UserData = Depends(require_login())
# ) -> MoldCoreMakingMachineListResponse:
#     return await mold_core_making_machine_service.get_mold_core_making_machines_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post(
#     "/",
#     response_model=MoldCoreMakingMachineDetailResponse,
#     status_code=status.HTTP_201_CREATED
# )
# async def create_mold_core_making_machine(
#     mold_core_making_machine_data: MoldCoreMakingMachineCreate,
#     mold_core_making_machine_service: MoldCoreMakingMachineService = (
#         Depends(get_mold_core_making_machine_service)
#     ),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreMakingMachineDetailResponse:
#     return await mold_core_making_machine_service.create_mold_core_making_machine(
#         mold_core_making_machine_data
#     )
#
#
# @router.get("/{mold_core_making_machine_id}", response_model=MoldCoreMakingMachineDetailResponse)
# async def get_mold_core_making_machine(
#     mold_core_making_machine_id: UUID,
#     mold_core_making_machine_service: MoldCoreMakingMachineService = (
#         Depends(get_mold_core_making_machine_service)
#     ),
#     current_user: UserData = Depends(require_login())
# ) -> MoldCoreMakingMachineDetailResponse:
#     return await mold_core_making_machine_service.get_mold_core_making_machine_by_id(
#         mold_core_making_machine_id
#     )
#
#
# @router.put("/{mold_core_making_machine_id}", response_model=MoldCoreMakingMachineDetailResponse)
# async def update_mold_core_making_machine(
#     mold_core_making_machine_id: UUID,
#     mold_core_making_machine_data: MoldCoreMakingMachineUpdate,
#     mold_core_making_machine_service: MoldCoreMakingMachineService = (
#         Depends(get_mold_core_making_machine_service)
#     ),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreMakingMachineDetailResponse:
#     return await mold_core_making_machine_service.update_mold_core_making_machine(
#         mold_core_making_machine_id,
#         mold_core_making_machine_data
#     )
#
#
# @router.delete("/{mold_core_making_machine_id}", response_model=MoldCoreMakingMachineDetailResponse)
# async def delete_mold_core_making_machine(
#     mold_core_making_machine_id: UUID,
#     mold_core_making_machine_service: MoldCoreMakingMachineService = (
#         Depends(get_mold_core_making_machine_service)
#     ),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreMakingMachineDetailResponse:
#     return await mold_core_making_machine_service.delete_mold_core_making_machine(
#         mold_core_making_machine_id
#     )
#
#
# @router.post(
#     "/{mold_core_making_machine_id}/restore",
#     response_model=MoldCoreMakingMachineDetailResponse
# )
# async def restore_mold_core_making_machine(
#     mold_core_making_machine_id: UUID,
#     mold_core_making_machine_service: MoldCoreMakingMachineService = (
#         Depends(get_mold_core_making_machine_service)
#     ),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldCoreMakingMachineDetailResponse:
#     return await mold_core_making_machine_service.restore_mold_core_making_machine(
#         mold_core_making_machine_id
#     )
