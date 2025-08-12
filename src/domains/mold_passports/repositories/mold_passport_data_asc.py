from enum import Enum
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load

from domains.mold_passports.dto import MoldPassportDataASCCreateDTO, MoldPassportDataASCUpdateDTO
from infrastructure.database.models.all_models import MoldPassportDataASC
from infrastructure.repositories.base import ExistsMixin, ReadByIdMixin, RepositoryBase


class MoldPassportDataASCLoadOptions(str, Enum):
    """Loading options for the MoldPassportDataASC ORM model."""
    ...


class MoldPassportDataASCRepository(
    RepositoryBase[MoldPassportDataASC, MoldPassportDataASCLoadOptions],
    ExistsMixin[MoldPassportDataASC],
    ReadByIdMixin[MoldPassportDataASC, MoldPassportDataASCLoadOptions]
):
    _LOAD_OPTIONS_MAP: dict[MoldPassportDataASCLoadOptions, Load] = {}

    def __init__(self, db: AsyncSession):
        super().__init__(db, MoldPassportDataASC)

    async def create(
        self,
        mold_passport_id: UUID,
        molding_sand_type_id: int,
        mold_passport_data_asc_data: MoldPassportDataASCCreateDTO
    ) -> MoldPassportDataASC:
        mold_passport_data_asc = MoldPassportDataASC(
            mold_passport_id=mold_passport_id,
            molding_sand_type_id=molding_sand_type_id,
            **mold_passport_data_asc_data.model_dump()
        )
        self.db.add(mold_passport_data_asc)

        return mold_passport_data_asc

    @staticmethod
    async def update(
        mold_passport_data_asc: MoldPassportDataASC,
        mold_passport_data_asc_data: MoldPassportDataASCUpdateDTO
    ) -> MoldPassportDataASC:
        update_data = mold_passport_data_asc_data.model_dump(exclude_unset=True)

        if not update_data:
            return mold_passport_data_asc

        for field, value in update_data.items():
            setattr(mold_passport_data_asc, field, value)

        return mold_passport_data_asc

    async def delete(self, mold_passport_data_asc: MoldPassportDataASC) -> MoldPassportDataASC:
        await self.db.delete(mold_passport_data_asc)

        return mold_passport_data_asc
