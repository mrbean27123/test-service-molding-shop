import uuid
from enum import Enum

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from domains.mold_passports.dto import MoldPassportCreateDTO
from infrastructure.database.models.all_models import (
    CastingPattern,
    MoldCavity,
    MoldCore,
    MoldCoreBatch,
    MoldCoreType,
    MoldPassport,
    MoldPassportDataASC,
    MoldPassportDataGSC
)
from infrastructure.repositories.base import (
    RepositoryBase,
    ExistsMixin,
    CountMixin,
    LookupMixin,
    ReadPaginatedMixin,
    ReadByIdMixin,
    UpdateMixin,
    SoftDeleteMixin
)


class MoldPassportLoadOptions(str, Enum):
    """Loading options for the MoldPassport ORM model."""
    MOLDING_AREA = "molding_area"
    CASTING_TECHNOLOGY = "casting_technology"
    PATTERN_PLATE_FRAME = "pattern_plate_frame"
    MOLDING_FLASK = "molding_flask"
    MOLD_PASSPORT_DATA_GSC__MOLDING_SAND_TYPE = "mold_passport_data_gsc__molding_sand_type"
    MOLD_PASSPORT_DATA_ASC__MOLDING_SAND_TYPE = "mold_passport_data_asc__molding_sand_type"
    MOLD_PASSPORT_DATA_ASC__RESIN = "mold_passport_data_asc__resin"

    MOLD_CAVITIES__CASTING_PATTERN__CASTING_PRODUCT = (
        "mold_cavities__casting_pattern_casting_product"
    )
    MOLD_CAVITIES__MOLD_CORES__MOLD_CORE_BATCH__MOLDING_SAND_TYPE = (
        "mold_cavities__mold_cores__mold_core_batch__molding_sand_type"
    )
    MOLD_CAVITIES__MOLD_CORES__MOLD_CORE_BATCH__MOLD_CORE_TYPE__CASTING_PRODUCT = (
        "mold_cavities__mold_cores__mold_core_batch__mold_core_type__casting_product"
    )
    MOLD_CAVITIES__MOLD_CORES__MOLD_CORE_BATCH__MOLD_CORE_MOLD_CORE_MAKING_MACHINE = (
        "mold_cavities__mold_cores__mold_core_batch__mold_core_making_machine"
    )


class MoldPassportRepository(
    RepositoryBase[MoldPassport, MoldPassportLoadOptions],
    ExistsMixin[MoldPassport],
    CountMixin[MoldPassport],
    LookupMixin[MoldPassport],
    ReadPaginatedMixin[MoldPassport, MoldPassportLoadOptions],
    ReadByIdMixin[MoldPassport, MoldPassportLoadOptions],
    UpdateMixin[MoldPassport],
    SoftDeleteMixin[MoldPassport]
):
    _LOAD_OPTIONS_MAP: dict[MoldPassportLoadOptions, Load] = {
        MoldPassportLoadOptions.MOLDING_AREA: selectinload(MoldPassport.molding_area),
        MoldPassportLoadOptions.CASTING_TECHNOLOGY: selectinload(MoldPassport.casting_technology),
        MoldPassportLoadOptions.PATTERN_PLATE_FRAME: selectinload(MoldPassport.pattern_plate_frame),
        MoldPassportLoadOptions.MOLDING_FLASK: selectinload(MoldPassport.molding_flask),
        MoldPassportLoadOptions.MOLD_PASSPORT_DATA_GSC__MOLDING_SAND_TYPE: (
            selectinload(MoldPassport.data_gsc)
            .selectinload(MoldPassportDataGSC.molding_sand_type)
        ),
        MoldPassportLoadOptions.MOLD_PASSPORT_DATA_ASC__MOLDING_SAND_TYPE: (
            selectinload(MoldPassport.data_asc)
            .selectinload(MoldPassportDataASC.molding_sand_type)
        ),
        MoldPassportLoadOptions.MOLD_PASSPORT_DATA_ASC__RESIN: (
            selectinload(MoldPassport.data_asc)
            .selectinload(MoldPassportDataASC.resin)
        ),

        MoldPassportLoadOptions.MOLD_CAVITIES__CASTING_PATTERN__CASTING_PRODUCT: (
            selectinload(MoldPassport.mold_cavities)
            .selectinload(MoldCavity.casting_pattern)
            .selectinload(CastingPattern.casting_product)
        ),
        MoldPassportLoadOptions.MOLD_CAVITIES__MOLD_CORES__MOLD_CORE_BATCH__MOLDING_SAND_TYPE: (
            selectinload(MoldPassport.mold_cavities)
            .selectinload(MoldCavity.mold_cores)
            .selectinload(MoldCore.core_batch)
            .selectinload(MoldCoreBatch.molding_sand_type)
        ),
        MoldPassportLoadOptions
        .MOLD_CAVITIES__MOLD_CORES__MOLD_CORE_BATCH__MOLD_CORE_TYPE__CASTING_PRODUCT: (
            selectinload(MoldPassport.mold_cavities)
            .selectinload(MoldCavity.mold_cores)
            .selectinload(MoldCore.core_batch)
            .selectinload(MoldCoreBatch.mold_core_type)
            .selectinload(MoldCoreType.casting_product)
        ),
        MoldPassportLoadOptions
        .MOLD_CAVITIES__MOLD_CORES__MOLD_CORE_BATCH__MOLD_CORE_MOLD_CORE_MAKING_MACHINE: (
            selectinload(MoldPassport.mold_cavities)
            .selectinload(MoldCavity.mold_cores)
            .selectinload(MoldCore.core_batch)
            .selectinload(MoldCoreBatch.mold_core_making_machine)
        )
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, MoldPassport)

    async def create(self, mold_passport_data: MoldPassportCreateDTO) -> MoldPassport:
        mold_passport = MoldPassport(id=uuid.uuid4(), **mold_passport_data.model_dump())
        self.db.add(mold_passport)

        return mold_passport
