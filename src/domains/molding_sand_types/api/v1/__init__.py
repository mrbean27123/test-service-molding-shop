from fastapi import APIRouter

from domains.molding_sand_types.api.v1.router import router as molding_sand_types_router


router = APIRouter(prefix="/molding-sand-types", tags=["molding-sand-types"])
router.include_router(molding_sand_types_router)
