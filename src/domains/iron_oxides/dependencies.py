from fastapi import Depends

from domains.iron_oxides.service import IronOxideService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_iron_oxide_service(uow: UnitOfWork = Depends(get_uow)) -> IronOxideService:
    return IronOxideService(uow)
