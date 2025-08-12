from fastapi import Depends

from domains.casting_patterns.service import CastingPatternService
from infrastructure.core.dependencies import get_uow
from infrastructure.database import UnitOfWork


def get_casting_pattern_service(uow: UnitOfWork = Depends(get_uow)) -> CastingPatternService:
    return CastingPatternService(uow)
