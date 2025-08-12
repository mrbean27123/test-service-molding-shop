from fastapi import Depends

from domains.mold_core_batches.service import MoldCoreBatchService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_mold_core_batch_service(uow: UnitOfWork = Depends(get_uow)) -> MoldCoreBatchService:
    return MoldCoreBatchService(uow)
