from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class TriethylamineCreateDTO(CreateDTOBase):
    brand: str
    name: str


class TriethylamineUpdateDTO(UpdateDTOBase):
    brand: str | None = None
    name: str | None = None
