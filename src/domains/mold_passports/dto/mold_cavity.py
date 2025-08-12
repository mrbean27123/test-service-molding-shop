from uuid import UUID

from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class MoldCavityCreateDTO(CreateDTOBase):
    casting_pattern_id: UUID

    serial_number: str | None = None
    is_functional: bool = True


class MoldCavityUpdateDTO(UpdateDTOBase):
    casting_pattern_id: UUID | None = None

    serial_number: str | None = None
    is_functional: bool = True
