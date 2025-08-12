from fastapi import APIRouter

from domains.molding_flasks.api.v1.router import router as molding_flasks_router


router = APIRouter(prefix="/molding-flasks", tags=["molding-flasks"])
router.include_router(molding_flasks_router)
