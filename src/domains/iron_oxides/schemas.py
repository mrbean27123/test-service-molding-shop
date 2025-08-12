from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.iron_oxides.dto import IronOxideCreateDTO, IronOxideUpdateDTO
from infrastructure.schemas.base import (
    BusinessEntityMetadataSchemaMixin,
    InputBase,
    ListResponse,
    SoftDeleteMetadataSchemaMixin
)


class IronOxideInputBase(InputBase):
    @field_validator("brand", mode="after", check_fields=False)
    @classmethod
    def validate_brand_name(cls, value: str) -> str:
        return value

    @field_validator("name", mode="after", check_fields=False)
    @classmethod
    def validate_name(cls, value: str) -> str:
        return value


class IronOxideCreate(IronOxideInputBase):
    brand: str
    name: str

    def to_dto(self) -> IronOxideCreateDTO:
        return IronOxideCreateDTO(**self.model_dump())


class IronOxideUpdate(IronOxideInputBase):
    brand: str = Field(None)
    name: str = Field(None)

    def to_dto(self) -> IronOxideUpdateDTO:
        return IronOxideUpdateDTO(**self.model_dump(exclude_unset=True))


class IronOxideResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class IronOxideLookupResponse(IronOxideResponseBase):
    brand: str
    name: str


class IronOxideShortResponse(IronOxideResponseBase):
    brand: str
    name: str


class IronOxideDetailResponse(IronOxideResponseBase, BusinessEntityMetadataSchemaMixin):
    brand: str
    name: str


class IronOxideListItemResponse(IronOxideShortResponse, SoftDeleteMetadataSchemaMixin):
    pass


class IronOxideLookupsListResponse(ListResponse[IronOxideLookupResponse]):
    pass


class IronOxideListResponse(ListResponse[IronOxideListItemResponse]):
    pass
