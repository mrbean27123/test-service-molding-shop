from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import MoldingSandType
from infrastructure.repositories.base import (
    RepositoryBase,
    ExistsMixin,
    CountMixin,
    LookupMixin,
    ReadPaginatedMixin,
    ReadByIdMixin,
    CreateMixin,
    UpdateMixin,
    SoftArchiveMixin
)


class MoldingSandTypeLoadOptions(str, Enum):
    """Loading options for the MoldingSandType ORM model."""
    CASTING_TECHNOLOGY = "casting_technology"
    MOLD_CORE_BATCHES = "mold_core_batches"


class MoldingSandTypeRepository(
    RepositoryBase[MoldingSandType, MoldingSandTypeLoadOptions],
    ExistsMixin[MoldingSandType],
    CountMixin[MoldingSandType],
    LookupMixin[MoldingSandType],
    ReadPaginatedMixin[MoldingSandType, MoldingSandTypeLoadOptions],
    ReadByIdMixin[MoldingSandType, MoldingSandTypeLoadOptions],
    CreateMixin[MoldingSandType],
    UpdateMixin[MoldingSandType],
    SoftArchiveMixin[MoldingSandType]
):
    _LOAD_OPTIONS_MAP: dict[MoldingSandTypeLoadOptions, Load] = {
        MoldingSandTypeLoadOptions.CASTING_TECHNOLOGY: selectinload(
            MoldingSandType.casting_technology
        ),
        MoldingSandTypeLoadOptions.MOLD_CORE_BATCHES: selectinload(
            MoldingSandType.mold_core_batches
        )
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, MoldingSandType)
