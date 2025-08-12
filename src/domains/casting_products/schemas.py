from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.casting_products.dto import CastingProductCreateDTO, CastingProductUpdateDTO
from domains.casting_products.enums import CastingProductType
from infrastructure.schemas.base import (
    InputBase,
    ListResponse,
    ReferenceEntityMetadataSchemaMixin,
    SoftArchiveMetadataSchemaMixin
)


CASTING_PRODUCT_NAME_CONSTRAINTS = {"min_length": 3, "max_length": 255}


class CastingProductInputBase(InputBase):
    @field_validator("name", mode="after", check_fields=False)
    @classmethod
    def validate_name(cls, value: str) -> str:
        return value


class CastingProductCreate(CastingProductInputBase):
    type_: CastingProductType = Field(..., serialization_alias="type")
    name: str = Field(..., **CASTING_PRODUCT_NAME_CONSTRAINTS)
    blueprint_number: str
    is_casting_manual_only: bool = False

    def to_dto(self) -> CastingProductCreateDTO:
        return CastingProductCreateDTO(**self.model_dump())


class CastingProductUpdate(CastingProductInputBase):
    type_: CastingProductType = Field(None, serialization_alias="type")
    name: str = Field(None, **CASTING_PRODUCT_NAME_CONSTRAINTS)
    blueprint_number: str = Field(None)
    is_casting_manual_only: bool = Field(None)

    def to_dto(self) -> CastingProductUpdateDTO:
        return CastingProductUpdateDTO(**self.model_dump(exclude_unset=True))


class CastingProductResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class CastingProductLookupResponse(CastingProductResponseBase):
    type_: CastingProductType = Field(serialization_alias="type")
    name: str
    blueprint_number: str
    is_casting_manual_only: bool


class CastingProductShortResponse(CastingProductResponseBase):
    type_: CastingProductType = Field(serialization_alias="type")
    name: str
    blueprint_number: str
    is_casting_manual_only: bool


class CastingProductDetailResponse(CastingProductResponseBase, ReferenceEntityMetadataSchemaMixin):
    type_: CastingProductType = Field(serialization_alias="type")
    name: str
    blueprint_number: str
    is_casting_manual_only: bool


class CastingProductListItemResponse(CastingProductShortResponse, SoftArchiveMetadataSchemaMixin):
    pass


class CastingProductLookupsListResponse(ListResponse[CastingProductLookupResponse]):
    pass


class CastingProductListResponse(ListResponse[CastingProductListItemResponse]):
    pass
