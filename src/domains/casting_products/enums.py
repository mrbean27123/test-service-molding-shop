from enum import Enum


class CastingProductType(str, Enum):
    PRIMARY = "primary"
    AUXILIARY = "auxiliary"
    HEAVY_SECTION = "heavy_section"
