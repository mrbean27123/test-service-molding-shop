from domains.casting_products.enums import CastingProductType
from infrastructure.dto.base import CreateDTOBase, UpdateDTOBase


class CastingProductCreateDTO(CreateDTOBase):
    type: CastingProductType
    name: str
    blueprint_number: str
    is_casting_manual_only: bool


class CastingProductUpdateDTO(UpdateDTOBase):
    type: CastingProductType | None = None
    name: str | None = None
    blueprint_number: str | None = None
    is_casting_manual_only: bool
