from datetime import datetime
from uuid import UUID

from domains.shared.enums import ConsumableStatus
from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class MoldPassportCreateDTO(CreateDTOBase):
    molding_area_id: int
    casting_technology_id: int

    pattern_plate_frame_id: UUID | None = None
    molding_flask_id: UUID | None = None

    pressing_pressure: float | None = None

    sequence_in_shift: int | None = None
    assembly_timestamp: datetime | None = None

    status: ConsumableStatus | None = None

    notes: str | None = None


class MoldPassportUpdateDTO(UpdateDTOBase):
    molding_area_id: int | None = None
    casting_technology_id: int | None = None

    pattern_plate_frame_id: UUID | None = None
    molding_flask_id: UUID | None = None

    pressing_pressure: float | None = None

    sequence_in_shift: int | None = None
    assembly_timestamp: datetime | None = None

    status: ConsumableStatus | None = None

    notes: str | None = None
