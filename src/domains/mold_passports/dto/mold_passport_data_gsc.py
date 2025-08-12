from domains.mold_passports.enums import MoldingSandSystem
from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class MoldPassportDataGSCCreateDTO(CreateDTOBase):
    molding_sand_system: MoldingSandSystem
    molding_sand_number: str

    mold_horizontal_density: float
    mold_vertical_density: float


class MoldPassportDataGSCUpdateDTO(UpdateDTOBase):
    molding_sand_system: MoldingSandSystem | None = None
    molding_sand_number: str | None = None

    mold_horizontal_density: float | None = None
    mold_vertical_density: float | None = None
