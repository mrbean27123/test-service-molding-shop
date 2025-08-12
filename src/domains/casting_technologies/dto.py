from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class CastingTechnologyCreateDTO(CreateDTOBase):
    name: str
    abbreviation: str


class CastingTechnologyUpdateDTO(UpdateDTOBase):
    name: str | None = None
    abbreviation: str | None = None
