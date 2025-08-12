from typing import Annotated, TYPE_CHECKING, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from domains.mold_passports.dto import MoldPassportDataASCCreateDTO, MoldPassportDataASCUpdateDTO
from infrastructure.schemas.base import (
    CompositeEntityMetadataSchemaMixin,
    CreateOperationBase,
    DeleteOperationBase,
    InputBase,
    UpdateOperationBase
)


if TYPE_CHECKING:
    from domains.molding_sand_types.schemas import MoldingSandTypeLookupResponse
    from domains.resins.schemas import ResinShortResponse


class MoldPassportDataASCInputBase(InputBase):
    pass


class MoldPassportDataASCCreate(MoldPassportDataASCInputBase):
    mold_hardness: float
    resin_id: UUID | None = None

    def to_dto(self) -> MoldPassportDataASCCreateDTO:
        return MoldPassportDataASCCreateDTO(**self.model_dump())


class MoldPassportDataASCUpdate(MoldPassportDataASCInputBase):
    mold_hardness: float | None = None
    resin_id: UUID | None = None

    def to_dto(self) -> MoldPassportDataASCUpdateDTO:
        return MoldPassportDataASCUpdateDTO(**self.model_dump(exclude_unset=True))


class MoldPassportDataASCResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    mold_passport_id: UUID


class MoldPassportDataASCDetailResponse(
    MoldPassportDataASCResponseBase,
    CompositeEntityMetadataSchemaMixin
):
    molding_sand_type: "MoldingSandTypeLookupResponse"
    mold_hardness: float
    resin: Union["ResinShortResponse", None] = None


class MoldPassportDataASCCreateOperation(CreateOperationBase[MoldPassportDataASCCreate]):
    pass


class MoldPassportDataASCUpdateOperation(UpdateOperationBase[MoldPassportDataASCUpdate]):
    pass


class MoldPassportDataASCDeleteOperation(DeleteOperationBase):
    pass


MoldPassportDataASCOperation = Annotated[
    (
        MoldPassportDataASCCreateOperation
        | MoldPassportDataASCUpdateOperation
        | MoldPassportDataASCDeleteOperation
    ),
    Field(discriminator="action")
]
