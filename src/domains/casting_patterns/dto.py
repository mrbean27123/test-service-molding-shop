from uuid import UUID

from domains.shared.enums import AssetStatus
from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class CastingPatternCreateDTO(CreateDTOBase):
    casting_product_id: UUID

    serial_number: str
    status: AssetStatus


class CastingPatternUpdateDTO(UpdateDTOBase):
    casting_product_id: UUID | None = None

    serial_number: str | None = None
    status: AssetStatus | None = None
