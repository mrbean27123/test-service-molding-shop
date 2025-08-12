from domains.shared.enums import AssetStatus
from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class PatternPlateFrameCreateDTO(CreateDTOBase):
    blueprint_number: str
    serial_number: str
    status: AssetStatus


class PatternPlateFrameUpdateDTO(UpdateDTOBase):
    blueprint_number: str | None = None
    serial_number: str | None = None
    status: AssetStatus | None = None
