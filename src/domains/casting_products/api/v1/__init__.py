from fastapi import APIRouter

from domains.casting_products.api.v1.router import router as casting_products_router


router = APIRouter(prefix="/casting-products", tags=["casting-products"])
router.include_router(casting_products_router)
