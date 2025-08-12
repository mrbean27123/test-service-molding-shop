from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import IronOxide
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


class IronOxideLoadOptions(str, Enum):
    """Loading options for the IronOxide ORM model."""
    MOLD_CORE_BATCHES = "mold_core_batches"


class IronOxideRepository(
    RepositoryBase[IronOxide, IronOxideLoadOptions],
    ExistsMixin[IronOxide],
    CountMixin[IronOxide],
    LookupMixin[IronOxide],
    ReadPaginatedMixin[IronOxide, IronOxideLoadOptions],
    ReadByIdMixin[IronOxide, IronOxideLoadOptions],
    CreateMixin[IronOxide],
    UpdateMixin[IronOxide],
    SoftDeleteMixin[IronOxide]
):
    _LOAD_OPTIONS_MAP: dict[IronOxideLoadOptions, Load] = {
        IronOxideLoadOptions.MOLD_CORE_BATCHES: selectinload(IronOxide.mold_core_batches)
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, IronOxide)
