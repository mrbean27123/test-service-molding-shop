from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.casting_patterns.dto import CastingPatternCreateDTO, CastingPatternUpdateDTO
from domains.shared.enums import AssetStatus
from infrastructure.schemas.base import (
    BusinessEntityMetadataSchemaMixin,
    InputBase,
    ListResponse,
    SoftDeleteMetadataSchemaMixin
)


if TYPE_CHECKING:
    from domains.casting_products.schemas import (
        CastingProductLookupResponse,
        CastingProductShortResponse
    )


class CastingPatternInputBase(InputBase):
    @field_validator("serial_number", mode="after", check_fields=False)
    @classmethod
    def validate_serial_number(cls, value: str) -> str:
        return value


class CastingPatternCreate(CastingPatternInputBase):
    casting_product_id: UUID

    serial_number: str
    status: AssetStatus = AssetStatus.AVAILABLE

    def to_dto(self) -> CastingPatternCreateDTO:
        return CastingPatternCreateDTO(**self.model_dump())


class CastingPatternUpdate(CastingPatternInputBase):
    casting_product_id: UUID = Field(None)

    serial_number: str = Field(None)
    status: AssetStatus = Field(None)

    def to_dto(self) -> CastingPatternUpdateDTO:
        return CastingPatternUpdateDTO(**self.model_dump(exclude_unset=True))


class CastingPatternResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class CastingPatternLookupResponse(CastingPatternResponseBase):
    casting_product: "CastingProductLookupResponse"
    serial_number: str


class CastingPatternShortResponse(CastingPatternResponseBase):
    casting_product: "CastingProductShortResponse"
    serial_number: str
    status: AssetStatus


class CastingPatternDetailResponse(CastingPatternResponseBase, BusinessEntityMetadataSchemaMixin):
    casting_product: "CastingProductShortResponse"
    serial_number: str
    status: AssetStatus


class CastingPatternListItemResponse(CastingPatternResponseBase, SoftDeleteMetadataSchemaMixin):
    casting_product: "CastingProductShortResponse"
    serial_number: str
    status: AssetStatus


class CastingPatternLookupsListResponse(ListResponse[CastingPatternLookupResponse]):
    pass


class CastingPatternListResponse(ListResponse[CastingPatternListItemResponse]):
    pass
