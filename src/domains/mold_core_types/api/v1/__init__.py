from fastapi import APIRouter

from domains.mold_core_types.api.v1.router import router as mold_core_types_router


router = APIRouter(prefix="/mold-core-types", tags=["mold-core-types"])
router.include_router(mold_core_types_router)
