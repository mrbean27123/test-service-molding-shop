from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.triethylamines.dto import TriethylamineCreateDTO, TriethylamineUpdateDTO
from infrastructure.schemas.base import (
    BusinessEntityMetadataSchemaMixin,
    InputBase,
    ListResponse,
    SoftDeleteMetadataSchemaMixin
)


class TriethylamineInputBase(InputBase):
    @field_validator("brand", mode="after", check_fields=False)
    @classmethod
    def validate_brand_name(cls, value: str) -> str:
        return value

    @field_validator("name", mode="after", check_fields=False)
    @classmethod
    def validate_name(cls, value: str) -> str:
        return value


class TriethylamineCreate(TriethylamineInputBase):
    brand: str
    name: str

    def to_dto(self) -> TriethylamineCreateDTO:
        return TriethylamineCreateDTO(**self.model_dump())


class TriethylamineUpdate(TriethylamineInputBase):
    brand: str = Field(None)
    name: str = Field(None)

    def to_dto(self) -> TriethylamineUpdateDTO:
        return TriethylamineUpdateDTO(**self.model_dump(exclude_unset=True))


class TriethylamineResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class TriethylamineLookupResponse(TriethylamineResponseBase):
    brand: str
    name: str


class TriethylamineShortResponse(TriethylamineResponseBase):
    brand: str
    name: str


class TriethylamineDetailResponse(TriethylamineResponseBase, BusinessEntityMetadataSchemaMixin):
    brand: str
    name: str


class TriethylamineListItemResponse(TriethylamineShortResponse, SoftDeleteMetadataSchemaMixin):
    pass


class TriethylamineLookupsListResponse(ListResponse[TriethylamineLookupResponse]):
    pass


class TriethylamineListResponse(ListResponse[TriethylamineListItemResponse]):
    pass
