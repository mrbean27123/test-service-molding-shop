from fastapi import Depends

from domains.molding_areas.service import MoldingAreaService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_molding_area_service(uow: UnitOfWork = Depends(get_uow)) -> MoldingAreaService:
    return MoldingAreaService(uow)
