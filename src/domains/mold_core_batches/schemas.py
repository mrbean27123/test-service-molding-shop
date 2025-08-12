from datetime import datetime
from typing import TYPE_CHECKING, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.mold_core_batches.dto import MoldCoreBatchCreateDTO, MoldCoreBatchUpdateDTO
from domains.shared.enums import ConsumableStatus
from infrastructure.schemas.base import (
    BusinessEntityMetadataSchemaMixin,
    InputBase,
    ListResponse,
    SoftDeleteMetadataSchemaMixin
)


if TYPE_CHECKING:
    from domains.iron_oxides.schemas import IronOxideShortResponse
    from domains.mold_core_making_machines.schemas import (
        MoldCoreMakingMachineLookupResponse,
        MoldCoreMakingMachineShortResponse
    )
    from domains.mold_core_types.schemas import (
        MoldCoreTypeLookupResponse,
        MoldCoreTypeShortResponse
    )
    from domains.molding_sand_types.schemas import (
        MoldingSandTypeLookupResponse,
        MoldingSandTypeShortResponse
    )
    from domains.resins.schemas import ResinShortResponse
    from domains.triethylamines.schemas import TriethylamineShortResponse


class MoldCoreBatchInputBase(InputBase):
    @field_validator("serial_number", mode="after", check_fields=False)
    @classmethod
    def validate_serial_number(cls, value: str) -> str:
        return value


class MoldCoreBatchCreate(MoldCoreBatchInputBase):
    molding_sand_type_id: int
    mold_core_type_id: UUID

    machine_id: UUID
    inventory_box_number: str

    resin_id: UUID
    # resin_component_a_dosage: float | None = None
    # resin_component_b_dosage: float | None = None

    triethylamine_id: UUID | None = None
    iron_oxide_id: UUID | None = None

    sand_temperature: float
    control_mold_core_hardness: float

    manufacturing_timestamp: datetime
    batch_expiry_date: datetime | None = None

    status: ConsumableStatus = ConsumableStatus.AVAILABLE

    def to_dto(self) -> MoldCoreBatchCreateDTO:
        return MoldCoreBatchCreateDTO(**self.model_dump())


class MoldCoreBatchUpdate(MoldCoreBatchInputBase):
    molding_sand_type_id: int = Field(None)
    mold_core_type_id: UUID = Field(None)

    machine_id: UUID = Field(None)
    inventory_box_number: str = Field(None)

    resin_id: UUID = Field(None)
    # resin_component_a_dosage: float | None = None
    # resin_component_b_dosage: float | None = None

    triethylamine_id: UUID | None = None
    iron_oxide_id: UUID | None = None

    sand_temperature: float = Field(None)
    control_mold_core_hardness: float = Field(None)

    manufacturing_timestamp: datetime = Field(None)
    batch_expiry_date: datetime = None

    status: ConsumableStatus = Field(None)

    def to_dto(self) -> MoldCoreBatchUpdateDTO:
        return MoldCoreBatchUpdateDTO(**self.model_dump(exclude_unset=True))


class MoldCoreBatchResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class MoldCoreBatchLookupResponse(MoldCoreBatchResponseBase):
    molding_sand_type: "MoldingSandTypeLookupResponse"
    mold_core_type: "MoldCoreTypeLookupResponse"

    mold_core_making_machine: "MoldCoreMakingMachineLookupResponse"

    manufacturing_timestamp: datetime
    batch_expiry_date: datetime

    status: ConsumableStatus


class MoldCoreBatchShortResponse(MoldCoreBatchResponseBase):
    molding_sand_type: "MoldingSandTypeLookupResponse"
    mold_core_type: "MoldCoreTypeLookupResponse"

    mold_core_making_machine: "MoldCoreMakingMachineLookupResponse"

    manufacturing_timestamp: datetime
    batch_expiry_date: datetime

    status: ConsumableStatus


class MoldCoreBatchDetailResponse(MoldCoreBatchResponseBase, BusinessEntityMetadataSchemaMixin):
    molding_sand_type: "MoldingSandTypeShortResponse"
    mold_core_type: "MoldCoreTypeShortResponse"

    mold_core_making_machine: "MoldCoreMakingMachineShortResponse"
    inventory_box_number: str

    resin: "ResinShortResponse"
    # resin_component_a_dosage: float | None = None
    # resin_component_b_dosage: float | None = None

    triethylamine: Union["TriethylamineShortResponse", None]
    iron_oxide: Union["IronOxideShortResponse", None]

    sand_temperature: float
    control_mold_core_hardness: float

    manufacturing_timestamp: datetime
    batch_expiry_date: datetime

    status: ConsumableStatus


class MoldCoreBatchListItemResponse(MoldCoreBatchLookupResponse, SoftDeleteMetadataSchemaMixin):
    pass


class MoldCoreBatchLookupsListResponse(ListResponse[MoldCoreBatchLookupResponse]):
    pass


class MoldCoreBatchListResponse(ListResponse[MoldCoreBatchListItemResponse]):
    pass
