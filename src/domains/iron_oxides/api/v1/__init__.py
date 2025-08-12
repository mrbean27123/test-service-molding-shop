from fastapi import APIRouter

from domains.iron_oxides.api.v1.router import router as iron_oxides_router


router = APIRouter(prefix="/iron-oxides", tags=["iron-oxides"])
router.include_router(iron_oxides_router)
