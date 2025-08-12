from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import CastingTechnology
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


class CastingTechnologyLoadOptions(str, Enum):
    """Loading options for the CastingTechnology ORM model."""
    MOLDING_SAND_TYPES = "molding_sand_types"
    MOLD_PASSPORTS = "mold_passports"
    MOLDING_AREAS = "molding_areas"


class CastingTechnologyRepository(
    RepositoryBase[CastingTechnology, CastingTechnologyLoadOptions],
    ExistsMixin[CastingTechnology],
    CountMixin[CastingTechnology],
    LookupMixin[CastingTechnology],
    ReadPaginatedMixin[CastingTechnology, CastingTechnologyLoadOptions],
    ReadByIdMixin[CastingTechnology, CastingTechnologyLoadOptions],
    CreateMixin[CastingTechnology],
    UpdateMixin[CastingTechnology],
    SoftArchiveMixin[CastingTechnology]
):
    _LOAD_OPTIONS_MAP: dict[CastingTechnologyLoadOptions, Load] = {
        CastingTechnologyLoadOptions.MOLDING_SAND_TYPES: selectinload(
            CastingTechnology.molding_sand_types
        ),
        CastingTechnologyLoadOptions.MOLD_PASSPORTS: selectinload(CastingTechnology.mold_passports),
        CastingTechnologyLoadOptions.MOLDING_AREAS: selectinload(CastingTechnology.molding_areas)
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, CastingTechnology)
