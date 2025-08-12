from fastapi import Depends

from domains.molding_sand_types.service import MoldingSandTypeService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_molding_sand_type_service(uow: UnitOfWork = Depends(get_uow)) -> MoldingSandTypeService:
    return MoldingSandTypeService(uow)
