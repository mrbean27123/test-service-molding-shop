from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import CastingPattern
from infrastructure.repositories.base import (
    RepositoryBase,
    ExistsMixin,
    CountMixin,
    LookupMixin,
    ReadPaginatedMixin,
    ReadByIdMixin,
    CreateMixin,
    UpdateMixin,
    SoftDeleteMixin,
)


class CastingPatternLoadOptions(str, Enum):
    """Loading options for the CastingPattern ORM model."""
    CASTING_PRODUCT = "casting_product"


class CastingPatternRepository(
    RepositoryBase[CastingPattern, CastingPatternLoadOptions],
    ExistsMixin[CastingPattern],
    CountMixin[CastingPattern],
    LookupMixin[CastingPattern],
    ReadPaginatedMixin[CastingPattern, CastingPatternLoadOptions],
    ReadByIdMixin[CastingPattern, CastingPatternLoadOptions],
    CreateMixin[CastingPattern],
    UpdateMixin[CastingPattern],
    SoftDeleteMixin[CastingPattern]
):
    _LOAD_OPTIONS_MAP: dict[CastingPatternLoadOptions, Load] = {
        CastingPatternLoadOptions.CASTING_PRODUCT: selectinload(CastingPattern.casting_product)
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, CastingPattern)
