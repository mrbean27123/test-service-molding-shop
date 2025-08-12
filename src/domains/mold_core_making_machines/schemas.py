from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.mold_core_making_machines.dto import (
    MoldCoreMakingMachineCreateDTO,
    MoldCoreMakingMachineUpdateDTO
)
from domains.shared.enums import AssetStatus
from infrastructure.schemas.base import (
    BusinessEntityMetadataSchemaMixin,
    InputBase,
    ListResponse,
    SoftDeleteMetadataSchemaMixin
)


class MoldCoreMakingMachineInputBase(InputBase):
    @field_validator("brand", mode="after", check_fields=False)
    @classmethod
    def validate_brand_name(cls, value: str) -> str:
        return value

    @field_validator("model", mode="after", check_fields=False)
    @classmethod
    def validate_model(cls, value: str) -> str:
        return value


class MoldCoreMakingMachineCreate(MoldCoreMakingMachineInputBase):
    brand: str
    model: str
    status: AssetStatus = AssetStatus.AVAILABLE

    def to_dto(self) -> MoldCoreMakingMachineCreateDTO:
        return MoldCoreMakingMachineCreateDTO(**self.model_dump())


class MoldCoreMakingMachineUpdate(MoldCoreMakingMachineInputBase):
    brand: str = Field(None)
    model: str = Field(None)
    status: AssetStatus = Field(None)

    def to_dto(self) -> MoldCoreMakingMachineUpdateDTO:
        return MoldCoreMakingMachineUpdateDTO(**self.model_dump(exclude_unset=True))


class MoldCoreMakingMachineResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class MoldCoreMakingMachineLookupResponse(MoldCoreMakingMachineResponseBase):
    brand: str
    model: str


class MoldCoreMakingMachineShortResponse(MoldCoreMakingMachineResponseBase):
    brand: str
    model: str
    status: AssetStatus


class MoldCoreMakingMachineDetailResponse(
    MoldCoreMakingMachineResponseBase,
    BusinessEntityMetadataSchemaMixin
):
    brand: str
    model: str
    status: AssetStatus


class MoldCoreMakingMachineListItemResponse(
    MoldCoreMakingMachineShortResponse,
    SoftDeleteMetadataSchemaMixin
):
    pass


class MoldCoreMakingMachineLookupsListResponse(ListResponse[MoldCoreMakingMachineLookupResponse]):
    pass


class MoldCoreMakingMachineListResponse(ListResponse[MoldCoreMakingMachineListItemResponse]):
    pass
