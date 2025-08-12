from fastapi import Depends

from domains.pattern_plate_frames.service import PatternPlateFrameService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_pattern_plate_frame_service(uow: UnitOfWork = Depends(get_uow)) -> PatternPlateFrameService:
    return PatternPlateFrameService(uow)
