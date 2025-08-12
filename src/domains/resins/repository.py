from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import Resin
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


class ResinLoadOptions(str, Enum):
    """Loading options for the Resin ORM model."""
    MOLD_CORE_BATCHES = "mold_core_batches"


class ResinRepository(
    RepositoryBase[Resin, ResinLoadOptions],
    ExistsMixin[Resin],
    CountMixin[Resin],
    LookupMixin[Resin],
    ReadPaginatedMixin[Resin, ResinLoadOptions],
    ReadByIdMixin[Resin, ResinLoadOptions],
    CreateMixin[Resin],
    UpdateMixin[Resin],
    SoftDeleteMixin[Resin]
):
    _LOAD_OPTIONS_MAP: dict[ResinLoadOptions, Load] = {
        ResinLoadOptions.MOLD_CORE_BATCHES: selectinload(Resin.mold_core_batches)
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, Resin)
