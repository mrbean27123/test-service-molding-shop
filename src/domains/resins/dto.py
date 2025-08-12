from domains.resins.enums import ResinType
from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class ResinCreateDTO(CreateDTOBase):
    type: ResinType
    brand: str
    name: str
    serial_number: str


class ResinUpdateDTO(UpdateDTOBase):
    type: ResinType | None = None
    brand: str | None = None
    name: str | None = None
    serial_number: str | None = None
