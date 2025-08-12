from fastapi import APIRouter

from domains.mold_passports.api.v1.router import router as mold_passports_router


router = APIRouter(prefix="/mold-passports", tags=["mold-passports"])
router.include_router(mold_passports_router)
