from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import MoldingArea
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


class MoldingAreaLoadOptions(str, Enum):
    """Loading options for the MoldingArea ORM model."""
    MOLD_PASSPORTS = "mold_passports"
    CASTING_TECHNOLOGIES = "casting_technologies"
    PATTERN_PLATE_FRAMES = "pattern_plate_frames"
    MOLDING_FLASKS = "molding_flasks"


class MoldingAreaRepository(
    RepositoryBase[MoldingArea, MoldingAreaLoadOptions],
    ExistsMixin[MoldingArea],
    CountMixin[MoldingArea],
    LookupMixin[MoldingArea],
    ReadPaginatedMixin[MoldingArea, MoldingAreaLoadOptions],
    ReadByIdMixin[MoldingArea, MoldingAreaLoadOptions],
    CreateMixin[MoldingArea],
    UpdateMixin[MoldingArea],
    SoftArchiveMixin[MoldingArea]
):
    _LOAD_OPTIONS_MAP: dict[MoldingAreaLoadOptions, Load] = {
        MoldingAreaLoadOptions.MOLD_PASSPORTS: selectinload(MoldingArea.mold_passports),
        MoldingAreaLoadOptions.CASTING_TECHNOLOGIES: selectinload(MoldingArea.casting_technologies),
        MoldingAreaLoadOptions.PATTERN_PLATE_FRAMES: selectinload(MoldingArea.pattern_plate_frames),
        MoldingAreaLoadOptions.MOLDING_FLASKS: selectinload(MoldingArea.molding_flasks)
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, MoldingArea)
