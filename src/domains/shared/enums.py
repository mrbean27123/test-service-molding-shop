from enum import Enum


class AssetStatus(str, Enum):
    AVAILABLE = "available"
    UNDER_MAINTENANCE = "under_maintenance"
    DISMISSED = "dismissed"


class ConsumableStatus(str, Enum):
    AVAILABLE = "available"
    USED = "used"
    DEFECTIVE = "defective"
