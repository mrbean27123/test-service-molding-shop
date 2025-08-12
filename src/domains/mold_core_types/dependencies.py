from fastapi import Depends

from domains.mold_core_types.service import MoldCoreTypeService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_mold_core_type_service(uow: UnitOfWork = Depends(get_uow)) -> MoldCoreTypeService:
    return MoldCoreTypeService(uow)
