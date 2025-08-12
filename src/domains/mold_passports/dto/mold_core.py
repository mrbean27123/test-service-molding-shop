from uuid import UUID

from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class MoldCoreCreateDTO(CreateDTOBase):
    core_batch_id: UUID

    hardness: float


class MoldCoreUpdateDTO(UpdateDTOBase):
    core_batch_id: UUID | None = None

    hardness: float | None = None
