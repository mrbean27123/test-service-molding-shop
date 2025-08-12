from typing import Annotated, TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from domains.mold_passports.dto import MoldPassportDataGSCCreateDTO, MoldPassportDataGSCUpdateDTO
from domains.mold_passports.enums import MoldingSandSystem
from infrastructure.schemas.base import (
    CompositeEntityMetadataSchemaMixin,
    CreateOperationBase,
    DeleteOperationBase,
    InputBase,
    UpdateOperationBase
)


if TYPE_CHECKING:
    from domains.molding_sand_types.schemas import MoldingSandTypeLookupResponse


class MoldPassportDataGSCInputBase(InputBase):
    pass


class MoldPassportDataGSCCreate(MoldPassportDataGSCInputBase):
    molding_sand_system: MoldingSandSystem
    molding_sand_number: str

    mold_horizontal_density: float
    mold_vertical_density: float

    def to_dto(self) -> MoldPassportDataGSCCreateDTO:
        return MoldPassportDataGSCCreateDTO(**self.model_dump())


class MoldPassportDataGSCUpdate(MoldPassportDataGSCInputBase):
    molding_sand_system: MoldingSandSystem = Field(None)
    molding_sand_number: str = Field(None)

    mold_horizontal_density: float = Field(None)
    mold_vertical_density: float = Field(None)

    def to_dto(self) -> MoldPassportDataGSCUpdateDTO:
        return MoldPassportDataGSCUpdateDTO(**self.model_dump(exclude_unset=True))


class MoldPassportDataGSCResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    mold_passport_id: UUID


class MoldPassportDataGSCDetailResponse(
    MoldPassportDataGSCResponseBase,
    CompositeEntityMetadataSchemaMixin
):
    molding_sand_type: "MoldingSandTypeLookupResponse"
    molding_sand_system: MoldingSandSystem
    molding_sand_number: str

    mold_horizontal_density: float
    mold_vertical_density: float


class MoldPassportDataGSCCreateOperation(CreateOperationBase[MoldPassportDataGSCCreate]):
    pass


class MoldPassportDataGSCUpdateOperation(UpdateOperationBase[MoldPassportDataGSCUpdate]):
    pass


class MoldPassportDataGSCDeleteOperation(DeleteOperationBase):
    pass


MoldPassportDataGSCOperation = Annotated[
    (
        MoldPassportDataGSCCreateOperation
        | MoldPassportDataGSCUpdateOperation
        | MoldPassportDataGSCDeleteOperation
    ),
    Field(discriminator="action")
]
