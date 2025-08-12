from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class IronOxideCreateDTO(CreateDTOBase):
    brand: str
    name: str


class IronOxideUpdateDTO(UpdateDTOBase):
    brand: str | None = None
    name: str | None = None
