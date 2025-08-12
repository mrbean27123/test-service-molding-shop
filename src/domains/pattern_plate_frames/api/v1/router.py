from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from common.auth.dependencies import require_login, require_superuser
from common.auth.schemas import UserData
from domains.pattern_plate_frames.dependencies import get_pattern_plate_frame_service
from domains.pattern_plate_frames.schemas import (
    PatternPlateFrameCreate,
    PatternPlateFrameLookupsListResponse, PatternPlateFrameUpdate,
    PatternPlateFrameDetailResponse,
    PatternPlateFrameListResponse
)
from domains.pattern_plate_frames.service import PatternPlateFrameService


router = APIRouter()


@router.get("/lookups", response_model=PatternPlateFrameLookupsListResponse)
async def get_pattern_plate_frame_lookups_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    pattern_plate_frame_service: PatternPlateFrameService = (
        Depends(get_pattern_plate_frame_service)
    ),
    current_user: UserData = Depends(require_login())
) -> PatternPlateFrameLookupsListResponse:
    return await pattern_plate_frame_service.get_pattern_plate_frame_lookups_list(
        page=page,
        per_page=per_page
    )

# @router.get("/", response_model=PatternPlateFrameListResponse)
# async def get_pattern_plate_frames_list(
#     page: int = Query(1, ge=1),
#     per_page: int = Query(10, ge=1, le=20),
#     status_: Literal["active", "deleted", "all"] | None = Query(None, title="status"),
#     pattern_plate_frame_service: PatternPlateFrameService = (
#         Depends(get_pattern_plate_frame_service)
#     ),
#     current_user: UserData = Depends(require_superuser())
# ) -> PatternPlateFrameListResponse:
#     return await pattern_plate_frame_service.get_pattern_plate_frames_paginated(
#         page=page,
#         per_page=per_page,
#         status=status_,
#         user=current_user
#     )
#
#
# @router.post(
#     "/",
#     response_model=PatternPlateFrameDetailResponse,
#     status_code=status.HTTP_201_CREATED
# )
# async def create_pattern_plate_frame(
#     pattern_plate_frame_data: PatternPlateFrameCreate,
#     pattern_plate_frame_service: PatternPlateFrameService = (
#         Depends(get_pattern_plate_frame_service)
#     ),
#     current_user: UserData = Depends(require_superuser())
# ) -> PatternPlateFrameDetailResponse:
#     return await pattern_plate_frame_service.create_pattern_plate_frame(pattern_plate_frame_data)
#
#
# @router.get("/{pattern_plate_frame_id}", response_model=PatternPlateFrameDetailResponse)
# async def get_pattern_plate_frame(
#     pattern_plate_frame_id: UUID,
#     pattern_plate_frame_service: PatternPlateFrameService = (
#         Depends(get_pattern_plate_frame_service)
#     ),
#     current_user: UserData = Depends(require_superuser())
# ) -> PatternPlateFrameDetailResponse:
#     return await pattern_plate_frame_service.get_pattern_plate_frame_by_id(pattern_plate_frame_id)
#
#
# @router.put("/{pattern_plate_frame_id}", response_model=PatternPlateFrameDetailResponse)
# async def update_pattern_plate_frame(
#     pattern_plate_frame_id: UUID,
#     pattern_plate_frame_data: PatternPlateFrameUpdate,
#     pattern_plate_frame_service: PatternPlateFrameService = (
#         Depends(get_pattern_plate_frame_service)
#     ),
#     current_user: UserData = Depends(require_superuser())
# ) -> PatternPlateFrameDetailResponse:
#     return await pattern_plate_frame_service.update_pattern_plate_frame(
#         pattern_plate_frame_id,
#         pattern_plate_frame_data
#     )
#
#
# @router.delete("/{pattern_plate_frame_id}", response_model=PatternPlateFrameDetailResponse)
# async def delete_pattern_plate_frame(
#     pattern_plate_frame_id: UUID,
#     pattern_plate_frame_service: PatternPlateFrameService = (
#         Depends(get_pattern_plate_frame_service)
#     ),
#     current_user: UserData = Depends(require_superuser())
# ) -> PatternPlateFrameDetailResponse:
#     return await pattern_plate_frame_service.delete_pattern_plate_frame(pattern_plate_frame_id)
#
#
# @router.post("/{pattern_plate_frame_id}/restore", response_model=PatternPlateFrameDetailResponse)
# async def restore_pattern_plate_frame(
#     pattern_plate_frame_id: UUID,
#     pattern_plate_frame_service: PatternPlateFrameService = (
#         Depends(get_pattern_plate_frame_service)
#     ),
#     current_user: UserData = Depends(require_superuser())
# ) -> PatternPlateFrameDetailResponse:
#     return await pattern_plate_frame_service.restore_pattern_plate_frame(pattern_plate_frame_id)
