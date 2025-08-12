from fastapi import APIRouter

from domains.resins.api.v1.router import router as resins_router


router = APIRouter(prefix="/resins", tags=["resins"])
router.include_router(resins_router)
