from datetime import datetime
from typing import TYPE_CHECKING, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from domains.mold_passports.dto import MoldPassportCreateDTO, MoldPassportUpdateDTO
from domains.shared.enums import AssetStatus, ConsumableStatus
from infrastructure.schemas.base import (
    BusinessEntityMetadataSchemaMixin,
    InputBase,
    ListResponse,
    SoftDeleteMetadataSchemaMixin
)


if TYPE_CHECKING:
    from domains.casting_technologies.schemas import CastingTechnologyShortResponse
    from domains.mold_passports.schemas.mold_cavity import (
        MoldCavityCreate,
        MoldCavityDetailResponse,
        MoldCavityOperationsList
    )
    from domains.mold_passports.schemas.mold_passport_data_asc import (
        MoldPassportDataASCCreate,
        MoldPassportDataASCDetailResponse,
        MoldPassportDataASCOperation
    )
    from domains.mold_passports.schemas.mold_passport_data_gsc import (
        MoldPassportDataGSCCreate,
        MoldPassportDataGSCDetailResponse,
        MoldPassportDataGSCOperation
    )
    from domains.molding_areas.schemas import MoldingAreaShortResponse
    from domains.molding_flasks.schemas import MoldingFlaskLookupResponse
    from domains.pattern_plate_frames.schemas import PatternPlateFrameLookupResponse


class MoldPassportInputBase(InputBase):
    pass


class MoldPassportCreate(MoldPassportInputBase):
    molding_area_id: int
    casting_technology_id: int

    pattern_plate_frame_id: UUID | None = None
    molding_flask_id: UUID | None = None

    data_gsc: Union["MoldPassportDataGSCCreate", None] = None
    data_asc: Union["MoldPassportDataASCCreate", None] = None

    mold_cavities: list["MoldCavityCreate"]

    pressing_pressure: float | None = None

    sequence_in_shift: int | None = Field(None, ge=1)
    assembly_timestamp: datetime | None = None

    is_defective: bool = False

    notes: str | None = None

    def to_dto(self) -> MoldPassportCreateDTO:
        mold_passport_dict = self.model_dump(
            exclude={"data_gsc", "data_asc", "mold_cavities", "is_defective"}
        )
        mold_passport_dict["status"] = (
            ConsumableStatus.AVAILABLE
            if not self.is_defective
            else ConsumableStatus.DEFECTIVE
        )

        return MoldPassportCreateDTO(**mold_passport_dict)


class MoldPassportUpdate(MoldPassportInputBase):
    molding_area_id: int = Field(None)
    casting_technology_id: int = Field(None)

    pattern_plate_frame_id: UUID | None = None
    molding_flask_id: UUID | None = None

    data_gsc_operation: Union["MoldPassportDataGSCOperation", None] = None
    data_asc_operation: Union["MoldPassportDataASCOperation", None] = None

    mold_cavity_operations: Union["MoldCavityOperationsList", None] = None

    pressing_pressure: float | None = None

    sequence_in_shift: int | None = Field(None, ge=1)
    assembly_timestamp: datetime | None = None

    is_defective: bool = False

    notes: str | None = None

    def to_dto(self) -> MoldPassportUpdateDTO:
        mold_passport_dict = self.model_dump(
            exclude={
                "data_gsc_operation",
                "data_asc_operation",
                "mold_cavity_operations",
                "is_defective"
            },
            exclude_unset=True
        )
        mold_passport_dict["status"] = (
            ConsumableStatus.AVAILABLE
            if not self.is_defective
            else ConsumableStatus.DEFECTIVE
        )

        return MoldPassportUpdateDTO(**mold_passport_dict)


class MoldPassportResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class MoldPassportLookupResponse(MoldPassportResponseBase):
    is_complete: bool
    primary_casting_product_name: str
    reference_code: str  # vs passport_code
    marking_year: int


class MoldPassportShortResponse(MoldPassportLookupResponse):
    pass


class MoldPassportDetailResponse(MoldPassportResponseBase, BusinessEntityMetadataSchemaMixin):
    is_complete: bool

    primary_casting_product_name: str
    reference_code: str

    molding_area: "MoldingAreaShortResponse"
    casting_technology: "CastingTechnologyShortResponse"

    pattern_plate_frame: Union["PatternPlateFrameLookupResponse", None] = None
    molding_flask: Union["MoldingFlaskLookupResponse", None] = None

    data_gsc: Union["MoldPassportDataGSCDetailResponse", None] = None
    data_asc: Union["MoldPassportDataASCDetailResponse", None] = None

    marking_year: int
    mold_cavities: list["MoldCavityDetailResponse"]

    pressing_pressure: float | None = None

    sequence_in_shift: int | None = None
    assembly_timestamp: datetime | None = None

    status: AssetStatus

    notes: str | None = None

    # molding_experiments: list["MoldingExperiment"]


class MoldPassportListItemResponse(MoldPassportResponseBase, SoftDeleteMetadataSchemaMixin):
    is_complete: bool

    primary_casting_product_name: str
    reference_code: str
    marking_year: int

    molding_area: "MoldingAreaShortResponse"
    casting_technology: "CastingTechnologyShortResponse"

    pattern_plate_frame: Union["PatternPlateFrameLookupResponse", None] = None
    molding_flask: Union["MoldingFlaskLookupResponse", None] = None

    sequence_in_shift: int | None = None
    assembly_timestamp: datetime | None = None

    status: AssetStatus


class MoldPassportLookupsListResponse(ListResponse[MoldPassportLookupResponse]):
    pass


class MoldPassportListResponse(ListResponse[MoldPassportListItemResponse]):
    pass
