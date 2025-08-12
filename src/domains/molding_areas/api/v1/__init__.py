from fastapi import APIRouter

from domains.molding_areas.api.v1.router import router as molding_areas_router


router = APIRouter(prefix="/molding-areas", tags=["molding-areas"])
router.include_router(molding_areas_router)
