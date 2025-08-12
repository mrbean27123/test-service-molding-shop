from fastapi import Depends

from domains.triethylamines.service import TriethylamineService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_triethylamine_service(uow: UnitOfWork = Depends(get_uow)) -> TriethylamineService:
    return TriethylamineService(uow)
