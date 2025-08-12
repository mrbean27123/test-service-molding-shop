from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import MoldCoreType
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


class MoldCoreTypeLoadOptions(str, Enum):
    """Loading options for the MoldCoreType ORM model."""
    CASTING_PRODUCT = "casting_product"
    MOLD_CORE_BATCHES = "mold_core_batches"


class MoldCoreTypeRepository(
    RepositoryBase[MoldCoreType, MoldCoreTypeLoadOptions],
    ExistsMixin[MoldCoreType],
    CountMixin[MoldCoreType],
    LookupMixin[MoldCoreType],
    ReadPaginatedMixin[MoldCoreType, MoldCoreTypeLoadOptions],
    ReadByIdMixin[MoldCoreType, MoldCoreTypeLoadOptions],
    CreateMixin[MoldCoreType],
    UpdateMixin[MoldCoreType],
    SoftArchiveMixin[MoldCoreType]
):
    _LOAD_OPTIONS_MAP: dict[MoldCoreTypeLoadOptions, Load] = {
        MoldCoreTypeLoadOptions.CASTING_PRODUCT: selectinload(MoldCoreType.casting_product),
        MoldCoreTypeLoadOptions.MOLD_CORE_BATCHES: selectinload(MoldCoreType.mold_core_batches)
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, MoldCoreType)
