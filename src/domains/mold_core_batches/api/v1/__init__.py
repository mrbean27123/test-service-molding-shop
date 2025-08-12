from fastapi import APIRouter

from domains.mold_core_batches.api.v1.router import router as mold_core_batches_router


router = APIRouter(prefix="/mold-core-batches", tags=["mold-core-batches"])
router.include_router(mold_core_batches_router)
