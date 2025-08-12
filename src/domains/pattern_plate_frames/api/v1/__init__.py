from fastapi import APIRouter

from domains.pattern_plate_frames.api.v1.router import router as pattern_plate_frames_router


router = APIRouter(prefix="/pattern-plate-frames", tags=["pattern-plate-frames"])
router.include_router(pattern_plate_frames_router)
