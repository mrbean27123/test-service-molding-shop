from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.mold_core_types.dto import MoldCoreTypeCreateDTO, MoldCoreTypeUpdateDTO
from infrastructure.schemas.base import (
    InputBase,
    ListResponse,
    ReferenceEntityMetadataSchemaMixin,
    SoftArchiveMetadataSchemaMixin
)


if TYPE_CHECKING:
    from domains.casting_products.schemas import (
        CastingProductLookupResponse,
        CastingProductShortResponse
    )

MODEL_NUMBER_CONSTRAINTS = {"min_length": 3, "max_length": 255}


class MoldCoreTypeInputBase(InputBase):
    @field_validator("model_number", mode="after", check_fields=False)
    @classmethod
    def validate_model_number(cls, value: str) -> str:
        return value

    @field_validator("inventory_box_number", mode="after", check_fields=False)
    @classmethod
    def validate_inventory_box_number(cls, value: str) -> str:
        return value

    @field_validator("shelf_life_days", mode="after", check_fields=False)
    @classmethod
    def validate_shelf_life_days(cls, value: int) -> int:
        return value


class MoldCoreTypeCreate(MoldCoreTypeInputBase):
    casting_product_id: UUID

    model_number: str = Field(..., **MODEL_NUMBER_CONSTRAINTS)
    shelf_life_days: int

    def to_dto(self) -> MoldCoreTypeCreateDTO:
        return MoldCoreTypeCreateDTO(**self.model_dump())


class MoldCoreTypeUpdate(MoldCoreTypeInputBase):
    casting_product_id: UUID = Field(None)

    model_number: str = Field(None, **MODEL_NUMBER_CONSTRAINTS)
    shelf_life_days: int = Field(None)

    def to_dto(self) -> MoldCoreTypeUpdateDTO:
        return MoldCoreTypeUpdateDTO(**self.model_dump(exclude_unset=True))


class MoldCoreTypeResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class MoldCoreTypeLookupResponse(MoldCoreTypeResponseBase):
    casting_product: "CastingProductLookupResponse"
    model_number: str


class MoldCoreTypeShortResponse(MoldCoreTypeResponseBase):
    casting_product: "CastingProductShortResponse"
    model_number: str
    shelf_life_days: int


class MoldCoreTypeDetailResponse(MoldCoreTypeResponseBase, ReferenceEntityMetadataSchemaMixin):
    casting_product: "CastingProductShortResponse"
    model_number: str
    shelf_life_days: int


class MoldCoreTypeListItemResponse(MoldCoreTypeShortResponse, SoftArchiveMetadataSchemaMixin):
    pass


class MoldCoreTypeLookupsListResponse(ListResponse[MoldCoreTypeLookupResponse]):
    pass


class MoldCoreTypeListResponse(ListResponse[MoldCoreTypeListItemResponse]):
    pass
