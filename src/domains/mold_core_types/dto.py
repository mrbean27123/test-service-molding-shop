from uuid import UUID

from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class MoldCoreTypeCreateDTO(CreateDTOBase):
    casting_product_id: UUID

    model_number: str
    shelf_life_days: int


class MoldCoreTypeUpdateDTO(UpdateDTOBase):
    casting_product_id: UUID | None = None

    model_number: str | None = None
    shelf_life_days: int | None = None
