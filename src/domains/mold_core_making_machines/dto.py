from domains.shared.enums import AssetStatus
from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class MoldCoreMakingMachineCreateDTO(CreateDTOBase):
    brand: str
    model: str
    status: AssetStatus


class MoldCoreMakingMachineUpdateDTO(UpdateDTOBase):
    brand: str | None = None
    model: str | None = None
    status: AssetStatus | None = None
