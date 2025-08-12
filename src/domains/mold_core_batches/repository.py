from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import MoldCoreBatch, MoldCoreType
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


class MoldCoreBatchLoadOptions(str, Enum):
    """Loading options for the MoldCoreBatch ORM model."""
    MOLDING_SAND_TYPE = "molding_sand_type"
    MOLD_CORE_TYPE__CASTING_PRODUCT = "mold_core_type__casting_product"
    MOLD_CORE_MAKING_MACHINE = "mold_core_making_machine"
    RESIN = "resin"
    TRIETHYLAMINE = "triethylamine"
    IRON_OXIDE = "iron_oxide"


class MoldCoreBatchRepository(
    RepositoryBase[MoldCoreBatch, MoldCoreBatchLoadOptions],
    ExistsMixin[MoldCoreBatch],
    CountMixin[MoldCoreBatch],
    LookupMixin[MoldCoreBatch],
    ReadPaginatedMixin[MoldCoreBatch, MoldCoreBatchLoadOptions],
    ReadByIdMixin[MoldCoreBatch, MoldCoreBatchLoadOptions],
    CreateMixin[MoldCoreBatch],
    UpdateMixin[MoldCoreBatch],
    SoftDeleteMixin[MoldCoreBatch]
):
    _LOAD_OPTIONS_MAP: dict[MoldCoreBatchLoadOptions, Load] = {
        MoldCoreBatchLoadOptions.MOLDING_SAND_TYPE: selectinload(MoldCoreBatch.molding_sand_type),
        MoldCoreBatchLoadOptions.MOLD_CORE_TYPE__CASTING_PRODUCT: (
            selectinload(MoldCoreBatch.mold_core_type)
            .selectinload(MoldCoreType.casting_product)
        ),
        MoldCoreBatchLoadOptions.MOLD_CORE_MAKING_MACHINE: selectinload(
            MoldCoreBatch.mold_core_making_machine
        ),
        MoldCoreBatchLoadOptions.RESIN: selectinload(MoldCoreBatch.resin),
        MoldCoreBatchLoadOptions.TRIETHYLAMINE: selectinload(MoldCoreBatch.triethylamine),
        MoldCoreBatchLoadOptions.IRON_OXIDE: selectinload(MoldCoreBatch.iron_oxide)
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, MoldCoreBatch)
