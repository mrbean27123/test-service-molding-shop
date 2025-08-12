from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.pattern_plate_frames.dto import PatternPlateFrameCreateDTO, PatternPlateFrameUpdateDTO
from domains.shared.enums import AssetStatus
from infrastructure.schemas.base import (
    BusinessEntityMetadataSchemaMixin,
    InputBase,
    ListResponse,
    SoftDeleteMetadataSchemaMixin
)


if TYPE_CHECKING:
    from domains.molding_areas.schemas import MoldingAreaLookupResponse


class PatternPlateFrameInputBase(InputBase):
    @field_validator("serial_number", mode="after", check_fields=False)
    @classmethod
    def validate_serial_number(cls, value: str) -> str:
        return value

    @field_validator("blueprint_number", mode="after", check_fields=False)
    @classmethod
    def validate_blueprint_number(cls, value: str) -> str:
        return value


class PatternPlateFrameCreate(PatternPlateFrameInputBase):
    blueprint_number: str
    serial_number: str
    status: AssetStatus = AssetStatus.AVAILABLE

    molding_area_ids: list[UUID] | None = None

    def to_dto(self) -> PatternPlateFrameCreateDTO:
        return PatternPlateFrameCreateDTO(**self.model_dump(exclude={"molding_area_ids"}))


class PatternPlateFrameUpdate(PatternPlateFrameInputBase):
    blueprint_number: str = Field(None)
    serial_number: str = Field(None)
    status: AssetStatus = Field(None)

    molding_area_ids: list[UUID] | None = Field(None)

    def to_dto(self) -> PatternPlateFrameUpdateDTO:
        return PatternPlateFrameUpdateDTO(
            **self.model_dump(exclude={"molding_area_ids"}, exclude_unset=True)
        )


class PatternPlateFrameResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class PatternPlateFrameLookupResponse(PatternPlateFrameResponseBase):
    blueprint_number: str
    serial_number: str


class PatternPlateFrameShortResponse(PatternPlateFrameResponseBase):
    blueprint_number: str
    serial_number: str
    status: AssetStatus

    molding_areas: list["MoldingAreaLookupResponse"]


class PatternPlateFrameDetailResponse(
    PatternPlateFrameResponseBase,
    BusinessEntityMetadataSchemaMixin
):
    blueprint_number: str
    serial_number: str
    status: AssetStatus

    molding_areas: list["MoldingAreaLookupResponse"]


class PatternPlateFrameListItemResponse(
    PatternPlateFrameShortResponse,
    SoftDeleteMetadataSchemaMixin
):
    pass


class PatternPlateFrameLookupsListResponse(ListResponse[PatternPlateFrameLookupResponse]):
    pass


class PatternPlateFrameListResponse(ListResponse[PatternPlateFrameListItemResponse]):
    pass
