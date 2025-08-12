from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from common.auth.dependencies import require_permissions, require_superuser
from common.auth.schemas import UserData
from domains.mold_passports.dependencies import get_mold_passport_service
from domains.mold_passports.schemas.mold_passport import (
    MoldPassportCreate,
    MoldPassportUpdate,
    MoldPassportDetailResponse,
    MoldPassportListResponse
)
from domains.mold_passports.service import MoldPassportService


router = APIRouter()


@router.get("/", response_model=MoldPassportListResponse)
async def get_mold_passports_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=20),
    status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
    mold_passport_service: MoldPassportService = Depends(get_mold_passport_service),
    current_user: UserData = Depends(require_permissions(...))
) -> MoldPassportListResponse:
    return await mold_passport_service.get_mold_passports_list(
        page=page,
        per_page=per_page,
        status=status_,
        user=current_user
    )


@router.post("/", response_model=MoldPassportDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_mold_passport(
    mold_passport_data: MoldPassportCreate,
    mold_passport_service: MoldPassportService = Depends(get_mold_passport_service),
    current_user: UserData = Depends(require_superuser())
) -> MoldPassportDetailResponse:
    return await mold_passport_service.create_mold_passport(mold_passport_data)


@router.get("/{mold_passport_id}", response_model=MoldPassportDetailResponse)
async def get_mold_passport(
    mold_passport_id: UUID,
    mold_passport_service: MoldPassportService = Depends(get_mold_passport_service),
    current_user: UserData = Depends(require_superuser())
) -> MoldPassportDetailResponse:
    return await mold_passport_service.get_mold_passport_by_id(mold_passport_id)


@router.put("/{mold_passport_id}", response_model=MoldPassportDetailResponse)
async def update_mold_passport(
    mold_passport_id: UUID,
    mold_passport_data: MoldPassportUpdate,
    mold_passport_service: MoldPassportService = Depends(get_mold_passport_service),
    current_user: UserData = Depends(require_superuser())
) -> MoldPassportDetailResponse:
    return await mold_passport_service.update_mold_passport(mold_passport_id, mold_passport_data)


@router.delete("/{mold_passport_id}", response_model=MoldPassportDetailResponse)
async def delete_mold_passport(
    mold_passport_id: UUID,
    mold_passport_service: MoldPassportService = Depends(get_mold_passport_service),
    current_user: UserData = Depends(require_superuser())
) -> MoldPassportDetailResponse:
    return await mold_passport_service.delete_mold_passport(mold_passport_id)


@router.post("/{mold_passport_id}/restore", response_model=MoldPassportDetailResponse)
async def restore_mold_passport(
    mold_passport_id: UUID,
    mold_passport_service: MoldPassportService = Depends(get_mold_passport_service),
    current_user: UserData = Depends(require_superuser())
) -> MoldPassportDetailResponse:
    return await mold_passport_service.restore_mold_passport(mold_passport_id)
