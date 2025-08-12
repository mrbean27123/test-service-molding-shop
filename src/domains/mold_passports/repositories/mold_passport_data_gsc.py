from enum import Enum
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load

from domains.mold_passports.dto import MoldPassportDataGSCCreateDTO, MoldPassportDataGSCUpdateDTO
from infrastructure.database.models.all_models import MoldPassportDataGSC
from infrastructure.repositories.base import ExistsMixin, ReadByIdMixin, RepositoryBase


class MoldPassportDataGSCLoadOptions(str, Enum):
    """Loading options for the MoldPassportDataGSC ORM model."""
    ...


class MoldPassportDataGSCRepository(
    RepositoryBase[MoldPassportDataGSC, MoldPassportDataGSCLoadOptions],
    ExistsMixin[MoldPassportDataGSC],
    ReadByIdMixin[MoldPassportDataGSC, MoldPassportDataGSCLoadOptions]
):
    _LOAD_OPTIONS_MAP: dict[MoldPassportDataGSCLoadOptions, Load] = {}

    def __init__(self, db: AsyncSession):
        super().__init__(db, MoldPassportDataGSC)

    async def create(
        self,
        mold_passport_id: UUID,
        molding_sand_type_id: int,
        mold_passport_data_gsc_data: MoldPassportDataGSCCreateDTO
    ) -> MoldPassportDataGSC:
        mold_passport_data_gsc = MoldPassportDataGSC(
            mold_passport_id=mold_passport_id,
            molding_sand_type_id=molding_sand_type_id,
            **mold_passport_data_gsc_data.model_dump()
        )
        self.db.add(mold_passport_data_gsc)

        return mold_passport_data_gsc

    @staticmethod
    async def update(
        mold_passport_data_gsc: MoldPassportDataGSC,
        mold_passport_data_gsc_data: MoldPassportDataGSCUpdateDTO
    ) -> MoldPassportDataGSC:
        update_data = mold_passport_data_gsc_data.model_dump(exclude_unset=True)

        if not update_data:
            return mold_passport_data_gsc

        for field, value in update_data.items():
            setattr(mold_passport_data_gsc, field, value)

        return mold_passport_data_gsc

    async def delete(self, mold_passport_data_gsc: MoldPassportDataGSC) -> MoldPassportDataGSC:
        await self.db.delete(mold_passport_data_gsc)

        return mold_passport_data_gsc
