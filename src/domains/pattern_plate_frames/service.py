from domains.pattern_plate_frames.models import PatternPlateFrame
from domains.pattern_plate_frames.schemas import (
    PatternPlateFrameLookupResponse,
    PatternPlateFrameLookupsListResponse
)
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class PatternPlateFrameService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_pattern_plate_frame_lookups_list(
        self,
        page: int,
        per_page: int,
    ) -> PatternPlateFrameLookupsListResponse:
        conditions = [PatternPlateFrame.deleted_at == None, ]

        total_pattern_plate_frames = await self.uow.pattern_plate_frames.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_pattern_plate_frames + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        pattern_plate_frame_entities = await self.uow.pattern_plate_frames.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions
        )
        response_items = [
            PatternPlateFrameLookupResponse.model_validate(pattern_plate_frame)
            for pattern_plate_frame in pattern_plate_frame_entities
        ]

        return PatternPlateFrameLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_pattern_plate_frames
        )
