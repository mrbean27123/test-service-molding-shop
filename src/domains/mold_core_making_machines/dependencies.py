from fastapi import Depends

from domains.mold_core_making_machines.service import MoldCoreMakingMachineService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_mold_core_making_machine_service(
    uow: UnitOfWork = Depends(get_uow)
) -> MoldCoreMakingMachineService:
    return MoldCoreMakingMachineService(uow)
