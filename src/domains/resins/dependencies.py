from fastapi import Depends

from domains.resins.service import ResinService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_resin_service(uow: UnitOfWork = Depends(get_uow)) -> ResinService:
    return ResinService(uow)
