from fastapi import APIRouter

from domains.triethylamines.api.v1.router import router as triethylamines_router


router = APIRouter(prefix="/triethylamines", tags=["triethylamines"])
router.include_router(triethylamines_router)
