from typing import Annotated, TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from domains.mold_passports.dto import MoldCoreCreateDTO, MoldCoreUpdateDTO
from infrastructure.schemas.base import (
    CompositeEntityMetadataSchemaMixin,
    CreateOperationBase,
    DeleteOperationBase,
    InputBase,
    UpdateOperationBase
)


if TYPE_CHECKING:
    from domains.mold_core_batches.schemas import MoldCoreBatchLookupResponse


class MoldCoreInputBase(InputBase):
    pass


class MoldCoreCreate(MoldCoreInputBase):
    core_batch_id: UUID

    hardness: float

    def to_dto(self) -> MoldCoreCreateDTO:
        return MoldCoreCreateDTO(**self.model_dump())


class MoldCoreUpdate(MoldCoreInputBase):
    core_batch_id: UUID = Field(None)

    hardness: float = Field(None)

    def to_dto(self) -> MoldCoreUpdateDTO:
        return MoldCoreUpdateDTO(**self.model_dump(exclude_unset=True))


class MoldCoreResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class MoldCoreDetailResponse(MoldCoreResponseBase, CompositeEntityMetadataSchemaMixin):
    core_batch: "MoldCoreBatchLookupResponse"
    hardness: float


class MoldCoreCreateOperation(CreateOperationBase[MoldCoreCreate]):
    pass


class MoldCoreUpdateOperation(UpdateOperationBase[MoldCoreUpdate]):
    pass


class MoldCoreDeleteOperation(DeleteOperationBase):
    pass


MoldCoreOperation = Annotated[
    (
        MoldCoreCreateOperation
        | MoldCoreUpdateOperation
        | MoldCoreDeleteOperation
    ),
    Field(discriminator="action")
]
MoldCoreOperationsList = list[MoldCoreOperation]
