from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.molding_sand_types.dto import MoldingSandTypeCreateDTO, MoldingSandTypeUpdateDTO
from infrastructure.schemas.base import (
    InputBase,
    ListResponse,
    ReferenceEntityMetadataSchemaMixin,
    SoftArchiveMetadataSchemaMixin
)


if TYPE_CHECKING:
    from domains.casting_technologies.schemas import CastingTechnologyLookupResponse


class MoldingSandTypeInputBase(InputBase):
    @field_validator("name", mode="after", check_fields=False)
    @classmethod
    def validate_name(cls, value: str) -> str:
        return value

    @field_validator("abbreviation", mode="after", check_fields=False)
    @classmethod
    def validate_abbreviation(cls, value: str) -> str:
        return value


class MoldingSandTypeCreate(MoldingSandTypeInputBase):
    casting_technology_id: int

    name: str
    abbreviation: str

    def to_dto(self) -> MoldingSandTypeCreateDTO:
        return MoldingSandTypeCreateDTO(**self.model_dump())


class MoldingSandTypeUpdate(MoldingSandTypeInputBase):
    casting_technology_id: int = Field(None)

    name: str = Field(None)
    abbreviation: str = Field(None)

    def to_dto(self) -> MoldingSandTypeUpdateDTO:
        return MoldingSandTypeUpdateDTO(**self.model_dump(exclude_unset=True))


class MoldingSandTypeResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int


class MoldingSandTypeLookupResponse(MoldingSandTypeResponseBase):
    name: str
    abbreviation: str


class MoldingSandTypeShortResponse(MoldingSandTypeResponseBase):
    casting_technology: "CastingTechnologyLookupResponse"
    name: str
    abbreviation: str


class MoldingSandTypeDetailResponse(
    MoldingSandTypeResponseBase,
    ReferenceEntityMetadataSchemaMixin
):
    casting_technology: "CastingTechnologyLookupResponse"
    name: str
    abbreviation: str


class MoldingSandTypeListItemResponse(MoldingSandTypeShortResponse, SoftArchiveMetadataSchemaMixin):
    pass


class MoldingSandTypeLookupsListResponse(ListResponse[MoldingSandTypeLookupResponse]):
    pass


class MoldingSandTypeListResponse(ListResponse[MoldingSandTypeListItemResponse]):
    pass
