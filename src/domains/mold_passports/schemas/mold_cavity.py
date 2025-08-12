from typing import Annotated, TYPE_CHECKING, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from domains.mold_passports.dto import MoldCavityCreateDTO, MoldCavityUpdateDTO
from infrastructure.schemas.base import (
    CompositeEntityMetadataSchemaMixin,
    CreateOperationBase,
    DeleteOperationBase,
    InputBase,
    UpdateOperationBase
)


if TYPE_CHECKING:
    from domains.casting_patterns.schemas import CastingPatternLookupResponse
    from domains.mold_passports.schemas.mold_core import (
        MoldCoreCreate,
        MoldCoreDetailResponse,
        MoldCoreOperationsList
    )


class MoldCavityInputBase(InputBase):
    pass


class MoldCavityCreate(MoldCavityInputBase):
    casting_pattern_id: UUID

    serial_number: str
    mold_cores: list["MoldCoreCreate"]

    is_functional: bool

    def to_dto(self) -> MoldCavityCreateDTO:
        return MoldCavityCreateDTO(**self.model_dump(exclude={"mold_cores"}))


class MoldCavityUpdate(MoldCavityInputBase):
    casting_pattern_id: UUID = Field(None)

    serial_number: str = Field(None)
    mold_core_operations: Union["MoldCoreOperationsList", None] = None

    is_functional: bool = Field(None)

    def to_dto(self) -> MoldCavityUpdateDTO:
        return MoldCavityUpdateDTO(
            **self.model_dump(exclude={"mold_core_operations"}, exclude_unset=True)
        )


class MoldCavityResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class MoldCavityDetailResponse(MoldCavityResponseBase, CompositeEntityMetadataSchemaMixin):
    casting_pattern: "CastingPatternLookupResponse"

    serial_number: str
    mold_cores: list["MoldCoreDetailResponse"]

    is_functional: bool


class MoldCavityCreateOperation(CreateOperationBase[MoldCavityCreate]):
    pass


class MoldCavityUpdateOperation(UpdateOperationBase[MoldCavityUpdate]):
    pass


class MoldCavityDeleteOperation(DeleteOperationBase):
    pass


MoldCavityOperation = Annotated[
    (
        MoldCavityCreateOperation
        | MoldCavityUpdateOperation
        | MoldCavityDeleteOperation
    ),
    Field(discriminator="action")
]
MoldCavityOperationsList = list[MoldCavityOperation]
