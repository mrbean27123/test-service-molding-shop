from fastapi import Depends

from domains.casting_products.service import CastingProductService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_casting_product_service(uow: UnitOfWork = Depends(get_uow)) -> CastingProductService:
    return CastingProductService(uow)
