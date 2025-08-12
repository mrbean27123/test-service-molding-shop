from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.molding_flasks.dependencies import get_molding_flask_service
from domains.molding_flasks.schemas import (
    MoldingFlaskCreate,
    MoldingFlaskLookupsListResponse, MoldingFlaskUpdate,
    MoldingFlaskDetailResponse,
    MoldingFlaskListResponse
)
from domains.molding_flasks.service import MoldingFlaskService


router = APIRouter()


@router.get("/lookups", response_model=MoldingFlaskLookupsListResponse)
async def get_molding_flask_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    molding_flask_service: MoldingFlaskService = Depends(get_molding_flask_service),
    current_user: UserData = Depends(require_login())
) -> MoldingFlaskLookupsListResponse:
    return await molding_flask_service.get_molding_flask_lookups_list(
        page=page,
        per_page=per_page
    )

# @router.get("/", response_model=MoldingFlaskListResponse)
# async def get_molding_flasks_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     molding_flask_service: MoldingFlaskService = Depends(get_molding_flask_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingFlaskListResponse:
#     return await molding_flask_service.get_molding_flasks_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post("/", response_model=MoldingFlaskDetailResponse, status_code=status.HTTP_201_CREATED)
# async def create_molding_flask(
#     molding_flask_data: MoldingFlaskCreate,
#     molding_flask_service: MoldingFlaskService = Depends(get_molding_flask_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingFlaskDetailResponse:
#     return await molding_flask_service.create_molding_flask(molding_flask_data)
#
#
# @router.get("/{molding_flask_id}", response_model=MoldingFlaskDetailResponse)
# async def get_molding_flask(
#     molding_flask_id: UUID,
#     molding_flask_service: MoldingFlaskService = Depends(get_molding_flask_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingFlaskDetailResponse:
#     return await molding_flask_service.get_molding_flask_by_id(molding_flask_id)
#
#
# @router.put("/{molding_flask_id}", response_model=MoldingFlaskDetailResponse)
# async def update_molding_flask(
#     molding_flask_id: UUID,
#     molding_flask_data: MoldingFlaskUpdate,
#     molding_flask_service: MoldingFlaskService = Depends(get_molding_flask_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingFlaskDetailResponse:
#     return await molding_flask_service.update_molding_flask(molding_flask_id, molding_flask_data)
#
#
# @router.delete("/{molding_flask_id}", response_model=MoldingFlaskDetailResponse)
# async def delete_molding_flask(
#     molding_flask_id: UUID,
#     molding_flask_service: MoldingFlaskService = Depends(get_molding_flask_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingFlaskDetailResponse:
#     return await molding_flask_service.delete_molding_flask(molding_flask_id)
#
#
# @router.post("/{molding_flask_id}/restore", response_model=MoldingFlaskDetailResponse)
# async def restore_molding_flask(
#     molding_flask_id: UUID,
#     molding_flask_service: MoldingFlaskService = Depends(get_molding_flask_service),
#     current_user: UserData = Depends(require_superuser())
# ) -> MoldingFlaskDetailResponse:
#     return await molding_flask_service.restore_molding_flask(molding_flask_id)
