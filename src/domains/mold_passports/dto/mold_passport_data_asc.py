from uuid import UUID

from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class MoldPassportDataASCCreateDTO(CreateDTOBase):
    mold_hardness: float
    resin_id: UUID | None


class MoldPassportDataASCUpdateDTO(UpdateDTOBase):
    mold_hardness: float | None = None
    resin_id: UUID | None = None
