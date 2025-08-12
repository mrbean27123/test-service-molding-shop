from fastapi import APIRouter

from domains.casting_technologies.api.v1.router import router as casting_technologies_router


router = APIRouter(prefix="/casting-technologies", tags=["casting-technologies"])
router.include_router(casting_technologies_router)
