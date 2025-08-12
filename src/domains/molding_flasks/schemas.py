from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.molding_flasks.dto import MoldingFlaskCreateDTO, MoldingFlaskUpdateDTO
from domains.shared.enums import AssetStatus
from infrastructure.schemas.base import (
    BusinessEntityMetadataSchemaMixin,
    InputBase,
    ListResponse,
    SoftDeleteMetadataSchemaMixin
)


if TYPE_CHECKING:
    from domains.molding_areas.schemas import MoldingAreaLookupResponse


class MoldingFlaskInputBase(InputBase):
    @field_validator("serial_number", mode="after", check_fields=False)
    @classmethod
    def validate_serial_number(cls, value: str) -> str:
        return value

    @field_validator("blueprint_number", mode="after", check_fields=False)
    @classmethod
    def validate_blueprint_number(cls, value: str) -> str:
        return value


class MoldingFlaskCreate(MoldingFlaskInputBase):
    blueprint_number: str
    serial_number: str
    status: AssetStatus = AssetStatus.AVAILABLE

    molding_area_ids: list[UUID] | None = None

    def to_dto(self) -> MoldingFlaskCreateDTO:
        return MoldingFlaskCreateDTO(**self.model_dump(exclude={"molding_area_ids"}))


class MoldingFlaskUpdate(MoldingFlaskInputBase):
    blueprint_number: str = Field(None)
    serial_number: str = Field(None)
    status: AssetStatus = Field(None)

    molding_area_ids: list[UUID] | None = Field(None)

    def to_dto(self) -> MoldingFlaskUpdateDTO:
        return MoldingFlaskUpdateDTO(
            **self.model_dump(exclude={"molding_area_ids"}, exclude_unset=True)
        )


class MoldingFlaskResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class MoldingFlaskLookupResponse(MoldingFlaskResponseBase):
    blueprint_number: str
    serial_number: str


class MoldingFlaskShortResponse(MoldingFlaskResponseBase):
    blueprint_number: str
    serial_number: str
    status: AssetStatus

    molding_areas: list["MoldingAreaLookupResponse"]


class MoldingFlaskDetailResponse(MoldingFlaskResponseBase, BusinessEntityMetadataSchemaMixin):
    blueprint_number: str
    serial_number: str
    status: AssetStatus

    molding_areas: list["MoldingAreaLookupResponse"]


class MoldingFlaskListItemResponse(MoldingFlaskShortResponse, SoftDeleteMetadataSchemaMixin):
    pass


class MoldingFlaskLookupsListResponse(ListResponse[MoldingFlaskLookupResponse]):
    pass


class MoldingFlaskListResponse(ListResponse[MoldingFlaskListItemResponse]):
    pass
