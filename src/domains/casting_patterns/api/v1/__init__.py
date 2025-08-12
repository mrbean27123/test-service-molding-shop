from fastapi import APIRouter

from domains.casting_patterns.api.v1.router import router as casting_patterns_router


router = APIRouter(prefix="/casting-patterns", tags=["casting-patterns"])
router.include_router(casting_patterns_router)
