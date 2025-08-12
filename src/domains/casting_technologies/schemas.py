from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.casting_technologies.dto import CastingTechnologyCreateDTO, CastingTechnologyUpdateDTO
from infrastructure.schemas.base import (
    InputBase,
    ListResponse,
    ReferenceEntityMetadataSchemaMixin,
    SoftArchiveMetadataSchemaMixin
)


class CastingTechnologyInputBase(InputBase):
    @field_validator("name", mode="after", check_fields=False)
    @classmethod
    def validate_name(cls, value: str) -> str:
        return value

    @field_validator("abbreviation", mode="after", check_fields=False)
    @classmethod
    def validate_abbreviation(cls, value: str) -> str:
        return value


class CastingTechnologyCreate(CastingTechnologyInputBase):
    name: str
    abbreviation: str

    def to_dto(self) -> CastingTechnologyCreateDTO:
        return CastingTechnologyCreateDTO(**self.model_dump())


class CastingTechnologyUpdate(CastingTechnologyInputBase):
    name: str = Field(None)
    abbreviation: str = Field(None)

    def to_dto(self) -> CastingTechnologyUpdateDTO:
        return CastingTechnologyUpdateDTO(**self.model_dump(exclude_unset=True))


class CastingTechnologyResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int


class CastingTechnologyLookupResponse(CastingTechnologyResponseBase):
    name: str
    abbreviation: str


class CastingTechnologyShortResponse(CastingTechnologyResponseBase):
    name: str
    abbreviation: str


class CastingTechnologyDetailResponse(
    CastingTechnologyResponseBase,
    ReferenceEntityMetadataSchemaMixin
):
    name: str
    abbreviation: str


class CastingTechnologyListItemResponse(
    CastingTechnologyShortResponse,
    SoftArchiveMetadataSchemaMixin
):
    pass


class CastingTechnologyLookupsListResponse(ListResponse[CastingTechnologyLookupResponse]):
    pass


class CastingTechnologyListResponse(ListResponse[CastingTechnologyListItemResponse]):
    pass
