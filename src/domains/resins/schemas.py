from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.resins.dto import ResinCreateDTO, ResinUpdateDTO
from domains.resins.enums import ResinType
from infrastructure.schemas.base import (
    BusinessEntityMetadataSchemaMixin,
    InputBase,
    ListResponse,
    SoftDeleteMetadataSchemaMixin
)


class ResinInputBase(InputBase):
    @field_validator("brand", mode="after", check_fields=False)
    @classmethod
    def validate_brand_name(cls, value: str) -> str:
        return value

    @field_validator("name", mode="after", check_fields=False)
    @classmethod
    def validate_name(cls, value: str) -> str:
        return value

    @field_validator("serial_number", mode="after", check_fields=False)
    @classmethod
    def validate_serial_number(cls, value: str) -> str:
        return value


class ResinCreate(ResinInputBase):
    type: ResinType
    brand: str
    name: str
    serial_number: str

    def to_dto(self) -> ResinCreateDTO:
        return ResinCreateDTO(**self.model_dump())


class ResinUpdate(ResinInputBase):
    type: ResinType = Field(None)
    brand: str = Field(None)
    name: str = Field(None)
    serial_number: str = Field(None)

    def to_dto(self) -> ResinUpdateDTO:
        return ResinUpdateDTO(**self.model_dump(exclude_unset=True))


class ResinResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class ResinLookupResponse(ResinResponseBase):
    brand: str
    name: str
    serial_number: str


class ResinShortResponse(ResinResponseBase):
    type: ResinType
    brand: str
    name: str
    serial_number: str


class ResinDetailResponse(ResinResponseBase, BusinessEntityMetadataSchemaMixin):
    type: ResinType
    brand: str
    name: str
    serial_number: str


class ResinListItemResponse(ResinShortResponse, SoftDeleteMetadataSchemaMixin):
    pass


class ResinLookupsListResponse(ListResponse[ResinLookupResponse]):
    pass


class ResinListResponse(ListResponse[ResinListItemResponse]):
    pass
