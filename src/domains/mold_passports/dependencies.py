from fastapi import Depends

from domains.mold_passports.service import MoldPassportService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_mold_passport_service(uow: UnitOfWork = Depends(get_uow)) -> MoldPassportService:
    return MoldPassportService(uow)
