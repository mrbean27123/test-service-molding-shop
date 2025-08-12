from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import MoldCoreMakingMachine
from infrastructure.repositories.base import (
    RepositoryBase,
    ExistsMixin,
    CountMixin,
    LookupMixin,
    ReadPaginatedMixin,
    ReadByIdMixin,
    CreateMixin,
    UpdateMixin,
    SoftDeleteMixin
)


class MoldCoreMakingMachineLoadOptions(str, Enum):
    """Loading options for the MoldCoreMakingMachine ORM model."""
    MOLD_CORE_BATCHES = "mold_core_batches"


class MoldCoreMakingMachineRepository(
    RepositoryBase[MoldCoreMakingMachine, MoldCoreMakingMachineLoadOptions],
    ExistsMixin[MoldCoreMakingMachine],
    CountMixin[MoldCoreMakingMachine],
    LookupMixin[MoldCoreMakingMachine],
    ReadPaginatedMixin[MoldCoreMakingMachine, MoldCoreMakingMachineLoadOptions],
    ReadByIdMixin[MoldCoreMakingMachine, MoldCoreMakingMachineLoadOptions],
    CreateMixin[MoldCoreMakingMachine],
    UpdateMixin[MoldCoreMakingMachine],
    SoftDeleteMixin[MoldCoreMakingMachine]
):
    _LOAD_OPTIONS_MAP: dict[MoldCoreMakingMachineLoadOptions, Load] = {
        MoldCoreMakingMachineLoadOptions.MOLD_CORE_BATCHES: selectinload(
            MoldCoreMakingMachine.mold_core_batches
        )
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, MoldCoreMakingMachine)
