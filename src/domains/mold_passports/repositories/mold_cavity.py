import uuid
from enum import Enum
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load

from domains.mold_passports.dto import MoldCavityCreateDTO, MoldCavityUpdateDTO
from infrastructure.database.models.all_models import MoldCavity
from infrastructure.repositories.base import ExistsMixin, ReadByIdMixin, RepositoryBase


class MoldCavityLoadOptions(str, Enum):
    """Loading options for the MoldCavity ORM model."""
    ...


class MoldCavityRepository(
    RepositoryBase[MoldCavity, MoldCavityLoadOptions],
    ExistsMixin[MoldCavity],
    ReadByIdMixin[MoldCavity, MoldCavityLoadOptions]
):
    _LOAD_OPTIONS_MAP: dict[MoldCavityLoadOptions, Load] = {}

    def __init__(self, db: AsyncSession):
        super().__init__(db, MoldCavity)

    async def create(
        self,
        mold_passport_id: UUID,
        mold_cavity_data: MoldCavityCreateDTO
    ) -> MoldCavity:
        mold_cavity = MoldCavity(
            id=uuid.uuid4(),
            mold_passport_id=mold_passport_id,
            **mold_cavity_data.model_dump()
        )
        self.db.add(mold_cavity)

        return mold_cavity

    async def update(
        self,
        mold_cavity_id: UUID,
        mold_passport_id: UUID,
        mold_cavity_data: MoldCavityUpdateDTO
    ) -> MoldCavity | None:
        db_mold_cavity: MoldCavity = await self.get_by_id(mold_cavity_id)

        if not db_mold_cavity or db_mold_cavity.mold_passport_id != mold_passport_id:
            return None

        update_data = mold_cavity_data.model_dump(exclude_unset=True)

        if not update_data:
            return db_mold_cavity

        for field, value in update_data.items():
            setattr(db_mold_cavity, field, value)

        return db_mold_cavity

    async def delete(self, mold_cavity_id: UUID, mold_passport_id: UUID) -> MoldCavity | None:
        db_mold_cavity: MoldCavity = await self.get_by_id(mold_cavity_id)

        if not db_mold_cavity or db_mold_cavity.mold_passport_id != mold_passport_id:
            return None

        await self.db.delete(db_mold_cavity)

        return db_mold_cavity
