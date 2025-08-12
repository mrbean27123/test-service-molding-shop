from fastapi import APIRouter, FastAPI

from domains.casting_patterns.api import router as casting_patterns_api_router
from domains.casting_products.api import router as casting_products_api_router
from domains.casting_technologies.api import router as casting_technologies_api_router
from domains.iron_oxides.api import router as iron_oxides_api_router
from domains.mold_core_batches.api import router as mold_core_batches_api_router
from domains.mold_core_making_machines.api import router as mold_core_making_machines_api_router
from domains.mold_core_types.api import router as mold_core_types_api_router
from domains.mold_passports.api import router as mold_passports_api_router
from domains.molding_areas.api import router as molding_areas_api_router
from domains.molding_flasks.api import router as molding_flasks_api_router
from domains.molding_sand_types.api import router as molding_sand_types_api_router
from domains.pattern_plate_frames.api import router as pattern_plate_frames_api_router
from domains.resins.api import router as resins_api_router
from domains.triethylamines.api import router as triethylamines_api_router
from infrastructure.core.config import settings

# Rebuild Schemas
import infrastructure.schemas.to_rebuild  # noqa: F401

# Register ORM Models
import infrastructure.database.models.all_models  # noqa: F401


app = FastAPI(title=settings.SERVICE_NAME)

app_router = APIRouter(prefix="/api")
app_router.include_router(casting_patterns_api_router)
app_router.include_router(casting_products_api_router)
app_router.include_router(casting_technologies_api_router)
app_router.include_router(iron_oxides_api_router)
app_router.include_router(mold_core_batches_api_router)
app_router.include_router(mold_core_making_machines_api_router)
app_router.include_router(mold_core_types_api_router)
app_router.include_router(mold_passports_api_router)
app_router.include_router(molding_areas_api_router)
app_router.include_router(molding_flasks_api_router)
app_router.include_router(molding_sand_types_api_router)
app_router.include_router(pattern_plate_frames_api_router)
app_router.include_router(resins_api_router)
app_router.include_router(triethylamines_api_router)

app.include_router(app_router)
