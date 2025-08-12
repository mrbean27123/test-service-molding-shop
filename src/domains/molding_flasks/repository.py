from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import MoldingFlask
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


class MoldingFlaskLoadOptions(str, Enum):
    """Loading options for the MoldingFlask ORM model."""
    MOLD_PASSPORTS = "mold_passports"
    MOLDING_AREAS = "molding_areas"


class MoldingFlaskRepository(
    RepositoryBase[MoldingFlask, MoldingFlaskLoadOptions],
    ExistsMixin[MoldingFlask],
    CountMixin[MoldingFlask],
    LookupMixin[MoldingFlask],
    ReadPaginatedMixin[MoldingFlask, MoldingFlaskLoadOptions],
    ReadByIdMixin[MoldingFlask, MoldingFlaskLoadOptions],
    CreateMixin[MoldingFlask],
    UpdateMixin[MoldingFlask],
    SoftDeleteMixin[MoldingFlask]
):
    _LOAD_OPTIONS_MAP: dict[MoldingFlaskLoadOptions, Load] = {
        MoldingFlaskLoadOptions.MOLD_PASSPORTS: selectinload(MoldingFlask.mold_passports),
        MoldingFlaskLoadOptions.MOLDING_AREAS: selectinload(MoldingFlask.molding_areas)
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, MoldingFlask)
