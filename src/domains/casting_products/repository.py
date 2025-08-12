from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from infrastructure.database.models.all_models import CastingProduct
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


class CastingProductLoadOptions(str, Enum):
    """Loading options for the CastingProduct ORM model."""
    CASTING_PATTERNS = "casting_patterns"
    MOLD_CORE_TYPES = "mold_core_types"


class CastingProductRepository(
    RepositoryBase[CastingProduct, CastingProductLoadOptions],
    ExistsMixin[CastingProduct],
    CountMixin[CastingProduct],
    LookupMixin[CastingProduct],
    ReadPaginatedMixin[CastingProduct, CastingProductLoadOptions],
    ReadByIdMixin[CastingProduct, CastingProductLoadOptions],
    CreateMixin[CastingProduct],
    UpdateMixin[CastingProduct],
    SoftArchiveMixin[CastingProduct]
):
    _LOAD_OPTIONS_MAP: dict[CastingProductLoadOptions, Load] = {
        CastingProductLoadOptions.CASTING_PATTERNS: selectinload(CastingProduct.casting_patterns),
        CastingProductLoadOptions.MOLD_CORE_TYPES: selectinload(CastingProduct.mold_core_types)
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, CastingProduct)
