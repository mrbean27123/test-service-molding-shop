from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import Triethylamine
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


class TriethylamineLoadOptions(str, Enum):
    """Loading options for the Triethylamine ORM model."""
    MOLD_CORE_BATCHES = "mold_core_batches"


class TriethylamineRepository(
    RepositoryBase[Triethylamine, TriethylamineLoadOptions],
    ExistsMixin[Triethylamine],
    CountMixin[Triethylamine],
    LookupMixin[Triethylamine],
    ReadPaginatedMixin[Triethylamine, TriethylamineLoadOptions],
    ReadByIdMixin[Triethylamine, TriethylamineLoadOptions],
    CreateMixin[Triethylamine],
    UpdateMixin[Triethylamine],
    SoftDeleteMixin[Triethylamine]
):
    _LOAD_OPTIONS_MAP: dict[TriethylamineLoadOptions, Load] = {
        TriethylamineLoadOptions.MOLD_CORE_BATCHES: selectinload(Triethylamine.mold_core_batches)
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, Triethylamine)
