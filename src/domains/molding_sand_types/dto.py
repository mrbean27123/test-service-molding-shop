from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class MoldingSandTypeCreateDTO(CreateDTOBase):
    casting_technology_id: int

    name: str
    abbreviation: str


class MoldingSandTypeUpdateDTO(UpdateDTOBase):
    casting_technology_id: int | None = None

    name: str | None = None
    abbreviation: str | None = None
