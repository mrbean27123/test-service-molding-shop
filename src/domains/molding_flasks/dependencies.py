from fastapi import Depends

from domains.molding_flasks.service import MoldingFlaskService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_molding_flask_service(uow: UnitOfWork = Depends(get_uow)) -> MoldingFlaskService:
    return MoldingFlaskService(uow)
