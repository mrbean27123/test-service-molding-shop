from enum import Enum
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, selectinload

from domains.mold_passports.dto import MoldCoreCreateDTO, MoldCoreUpdateDTO
from infrastructure.database.models.all_models import MoldCore, MoldCoreBatch
from infrastructure.repositories.base import ExistsMixin, ReadByIdMixin, RepositoryBase


class MoldCoreLoadOptions(str, Enum):
    """Loading options for the MoldCore ORM model."""
    MOLD_CORE_BATCH__MOLDING_SAND_TYPE = "mold_core_batch__molding_sand_type"
    MOLD_CORE_BATCH__MOLD_CORE_TYPE = "mold_core_batch__mold_core_type"
    MOLD_CORE_BATCH__MOLD_CORE_MAKING_MACHINE = "mold_core_batch__mold_core_making_machine"


class MoldCoreRepository(
    RepositoryBase[MoldCore, MoldCoreLoadOptions],
    ExistsMixin[MoldCore],
    ReadByIdMixin[MoldCore, MoldCoreLoadOptions]
):
    _LOAD_OPTIONS_MAP: dict[MoldCoreLoadOptions, Load] = {
        # MoldCoreLoadOptions.MOLD_CORE_BATCH__MOLDING_SAND_TYPE: (
        #     selectinload(MoldCore.mold_core_batch).selectinload(MoldCoreBatch.molding_sand_type)
        # ),
        # MoldCoreLoadOptions.MOLD_CORE_BATCH__MOLD_CORE_TYPE: (
        #     selectinload(MoldCore.mold_core_batch).selectinload(MoldCoreBatch.mold_core_type)
        # ),
        # MoldCoreLoadOptions.MOLD_CORE_BATCH__MOLD_CORE_MAKING_MACHINE: (
        #     selectinload(MoldCore.mold_core_batch)
        #     .selectinload(MoldCoreBatch.mold_core_making_machine)
        # )
    }

    def __init__(self, db: AsyncSession):
        super().__init__(db, MoldCore)

    async def create(self, mold_cavity_id: UUID, mold_core_data: MoldCoreCreateDTO) -> MoldCore:
        mold_core = MoldCore(mold_cavity_id=mold_cavity_id, **mold_core_data.model_dump())
        self.db.add(mold_core)

        return mold_core

    async def update(
        self,
        mold_core_id: UUID,
        mold_cavity_id: UUID,
        mold_core_data: MoldCoreUpdateDTO
    ) -> MoldCore | None:
        db_mold_core: MoldCore = await self.get_by_id(mold_core_id)

        if not db_mold_core or db_mold_core.mold_cavity_id != mold_cavity_id:
            return None

        update_data = mold_core_data.model_dump(exclude_unset=True)

        if not update_data:
            return db_mold_core

        for field, value in update_data.items():
            setattr(db_mold_core, field, value)

        return db_mold_core

    async def delete(self, mold_core_id: UUID, mold_cavity_id: UUID) -> MoldCore | None:
        db_mold_core: MoldCore = await self.get_by_id(mold_core_id)

        if not db_mold_core or db_mold_core.mold_cavity_id != mold_cavity_id:
            return None

        await self.db.delete(db_mold_core)

        return db_mold_core
