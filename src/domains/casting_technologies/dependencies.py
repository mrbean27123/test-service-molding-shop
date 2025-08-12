from fastapi import Depends

from domains.casting_technologies.service import CastingTechnologyService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_casting_technology_service(uow: UnitOfWork = Depends(get_uow)) -> CastingTechnologyService:
    return CastingTechnologyService(uow)
