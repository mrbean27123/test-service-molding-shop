from datetime import datetime
from uuid import UUID

from domains.shared.enums import ConsumableStatus
from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class MoldCoreBatchCreateDTO(CreateDTOBase):
    molding_sand_type_id: int
    mold_core_type_id: UUID

    machine_id: UUID
    inventory_box_number: str

    resin_id: UUID
    triethylamine_id: UUID | None = None
    iron_oxide_id: UUID | None = None

    sand_temperature: float
    control_mold_core_hardness: float

    manufacturing_timestamp: datetime
    batch_expiry_date: datetime | None = None

    status: ConsumableStatus


class MoldCoreBatchUpdateDTO(UpdateDTOBase):
    molding_sand_type_id: int | None = None
    mold_core_type_id: UUID | None = None

    machine_id: UUID | None = None
    inventory_box_number: str | None = None

    resin_id: UUID | None = None
    triethylamine_id: UUID | None = None
    iron_oxide_id: UUID | None = None

    sand_temperature: float | None = None
    control_mold_core_hardness: float | None = None

    manufacturing_timestamp: datetime | None = None
    batch_expiry_date: datetime | None = None

    status: ConsumableStatus | None = None
