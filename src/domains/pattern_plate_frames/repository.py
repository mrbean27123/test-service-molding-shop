from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import PatternPlateFrame
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


class PatternPlateFrameLoadOptions(str, Enum):
    """Loading options for the PatternPlateFrame ORM model."""
    MOLD_PASSPORTS = "mold_passports"
    MOLDING_AREAS = "molding_areas"


class PatternPlateFrameRepository(
    RepositoryBase[PatternPlateFrame, PatternPlateFrameLoadOptions],
    ExistsMixin[PatternPlateFrame],
    CountMixin[PatternPlateFrame],
    LookupMixin[PatternPlateFrame],
    ReadPaginatedMixin[PatternPlateFrame, PatternPlateFrameLoadOptions],
    ReadByIdMixin[PatternPlateFrame, PatternPlateFrameLoadOptions],
    CreateMixin[PatternPlateFrame],
    UpdateMixin[PatternPlateFrame],
    SoftDeleteMixin[PatternPlateFrame]
):
    _LOAD_OPTIONS_MAP: dict[PatternPlateFrameLoadOptions, Load] = {
        PatternPlateFrameLoadOptions.MOLD_PASSPORTS: selectinload(PatternPlateFrame.mold_passports),
        PatternPlateFrameLoadOptions.MOLDING_AREAS: selectinload(PatternPlateFrame.molding_areas)
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, PatternPlateFrame)
