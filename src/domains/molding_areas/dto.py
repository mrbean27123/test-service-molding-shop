from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class MoldingAreaCreateDTO(CreateDTOBase):
    name: str
    description: str | None = None
    pressure_units: str | None = None


class MoldingAreaUpdateDTO(UpdateDTOBase):
    name: str | None = None
    description: str | None = None
    pressure_units: str | None = None
