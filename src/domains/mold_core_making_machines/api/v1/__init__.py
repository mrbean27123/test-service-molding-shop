from fastapi import APIRouter

from domains.mold_core_making_machines.api.v1.router import (
    router as mold_core_making_machines_router
)


router = APIRouter(prefix="/mold-core-making-machines", tags=["mold-core-making-machines"])
router.include_router(mold_core_making_machines_router)
