from pydantic import BaseModel

from domains.casting_patterns.schemas import (  # noqa: F401
    CastingPatternCreate,
    CastingPatternUpdate,

    CastingPatternLookupResponse,
    CastingPatternShortResponse,
    CastingPatternDetailResponse,
    CastingPatternListItemResponse,

    CastingPatternLookupsListResponse,
    ListResponse
)
from domains.casting_products.schemas import (  # noqa: F401
    CastingProductCreate,
    CastingProductUpdate,

    CastingProductLookupResponse,
    CastingProductShortResponse,
    CastingProductDetailResponse,
    CastingProductListItemResponse,

    CastingProductLookupsListResponse,
    CastingProductListResponse
)
from domains.casting_technologies.schemas import (  # noqa: F401
    CastingTechnologyCreate,
    CastingTechnologyUpdate,

    CastingTechnologyLookupResponse,
    CastingTechnologyShortResponse,
    CastingTechnologyDetailResponse,
    CastingTechnologyListItemResponse,

    CastingTechnologyLookupsListResponse,
    CastingTechnologyListResponse
)
from domains.iron_oxides.schemas import (  # noqa: F401
    IronOxideCreate,
    IronOxideUpdate,

    IronOxideLookupResponse,
    IronOxideShortResponse,
    IronOxideDetailResponse,
    IronOxideListItemResponse,

    IronOxideLookupsListResponse,
    IronOxideListResponse
)
from domains.mold_core_batches.schemas import (  # noqa: F401
    MoldCoreBatchCreate,
    MoldCoreBatchUpdate,

    MoldCoreBatchLookupResponse,
    MoldCoreBatchShortResponse,
    MoldCoreBatchDetailResponse,
    MoldCoreBatchListItemResponse,

    MoldCoreBatchLookupsListResponse,
    MoldCoreBatchListResponse
)
from domains.mold_core_making_machines.schemas import (  # noqa: F401
    MoldCoreMakingMachineCreate,
    MoldCoreMakingMachineUpdate,

    MoldCoreMakingMachineLookupResponse,
    MoldCoreMakingMachineShortResponse,
    MoldCoreMakingMachineDetailResponse,
    MoldCoreMakingMachineListItemResponse,

    MoldCoreMakingMachineLookupsListResponse,
    MoldCoreMakingMachineListResponse
)
from domains.mold_core_making_machines.schemas import (  # noqa: F401
    MoldCoreMakingMachineCreate,
    MoldCoreMakingMachineUpdate,

    MoldCoreMakingMachineLookupResponse,
    MoldCoreMakingMachineShortResponse,
    MoldCoreMakingMachineDetailResponse,
    MoldCoreMakingMachineListItemResponse,

    MoldCoreMakingMachineLookupsListResponse,
    MoldCoreMakingMachineListResponse
)
from domains.mold_core_types.schemas import (  # noqa: F401
    MoldCoreTypeCreate,
    MoldCoreTypeUpdate,

    MoldCoreTypeLookupResponse,
    MoldCoreTypeShortResponse,
    MoldCoreTypeDetailResponse,
    MoldCoreTypeListItemResponse,

    MoldCoreTypeLookupsListResponse,
    MoldCoreTypeListResponse
)
from domains.molding_areas.schemas import (  # noqa: F401
    MoldingAreaCreate,
    MoldingAreaUpdate,

    MoldingAreaLookupResponse,
    MoldingAreaShortResponse,
    MoldingAreaDetailResponse,
    MoldingAreaListItemResponse,

    MoldingAreaLookupsListResponse,
    MoldingAreaListResponse
)
from domains.molding_flasks.schemas import (  # noqa: F401
    MoldingFlaskCreate,
    MoldingFlaskUpdate,

    MoldingFlaskLookupResponse,
    MoldingFlaskShortResponse,
    MoldingFlaskDetailResponse,
    MoldingFlaskListItemResponse,

    MoldingFlaskLookupsListResponse,
    MoldingFlaskListResponse
)
from domains.molding_sand_types.schemas import (  # noqa: F401
    MoldingSandTypeCreate,
    MoldingSandTypeUpdate,

    MoldingSandTypeLookupResponse,
    MoldingSandTypeShortResponse,
    MoldingSandTypeDetailResponse,
    MoldingSandTypeListItemResponse,

    MoldingSandTypeLookupsListResponse,
    MoldingSandTypeListResponse
)
from domains.pattern_plate_frames.schemas import (  # noqa: F401
    PatternPlateFrameCreate,
    PatternPlateFrameUpdate,

    PatternPlateFrameLookupResponse,
    PatternPlateFrameShortResponse,
    PatternPlateFrameDetailResponse,
    PatternPlateFrameListItemResponse,

    PatternPlateFrameLookupsListResponse,
    PatternPlateFrameListResponse
)
from domains.resins.schemas import (  # noqa: F401
    ResinCreate,
    ResinUpdate,

    ResinLookupResponse,
    ResinShortResponse,
    ResinDetailResponse,
    ResinListItemResponse,

    ResinLookupsListResponse,
    ResinListResponse
)
from domains.triethylamines.schemas import (  # noqa: F401
    TriethylamineCreate,
    TriethylamineUpdate,

    TriethylamineLookupResponse,
    TriethylamineShortResponse,
    TriethylamineDetailResponse,
    TriethylamineListItemResponse,

    TriethylamineLookupsListResponse,
    TriethylamineListResponse
)
from domains.mold_passports.schemas import (  # noqa: F401
    # MoldPassport schemas
    MoldPassportCreate,
    MoldPassportUpdate,

    MoldPassportDetailResponse,
    MoldPassportListItemResponse,
    MoldPassportLookupResponse,
    MoldPassportShortResponse,

    MoldPassportLookupsListResponse,
    MoldPassportListResponse,

    # MoldPassportDataGSC schemas
    MoldPassportDataGSCCreate,
    MoldPassportDataGSCUpdate,

    MoldPassportDataGSCDetailResponse,
    MoldPassportDataGSCCreateOperation,
    MoldPassportDataGSCUpdateOperation,
    MoldPassportDataGSCDeleteOperation,

    MoldPassportDataGSCOperation,

    # MoldPassportDataASC schemas
    MoldPassportDataASCCreate,
    MoldPassportDataASCUpdate,

    MoldPassportDataASCDetailResponse,
    MoldPassportDataASCCreateOperation,
    MoldPassportDataASCUpdateOperation,
    MoldPassportDataASCDeleteOperation,

    MoldPassportDataASCOperation,

    # MoldCavity schemas
    MoldCavityCreate,
    MoldCavityUpdate,

    MoldCavityDetailResponse,
    MoldCavityCreateOperation,
    MoldCavityUpdateOperation,
    MoldCavityDeleteOperation,

    MoldCavityOperation,
    MoldCavityOperationsList,

    # MoldCore schemas
    MoldCoreCreate,
    MoldCoreUpdate,

    MoldCoreDetailResponse,
    MoldCoreCreateOperation,
    MoldCoreUpdateOperation,
    MoldCoreDeleteOperation,

    MoldCoreOperation,
    MoldCoreOperationsList
)


# Rebuild Pydantic models to resolve forward references (string annotations)
# This is required for schemas that use string type hints to avoid circular imports and ensure
# proper OpenAPI schema generation
schemas_to_rebuild: list[type[BaseModel]] = [
    CastingPatternLookupResponse,
    CastingPatternShortResponse,
    CastingPatternDetailResponse,
    CastingPatternListItemResponse,

    MoldCoreBatchLookupResponse,
    MoldCoreBatchShortResponse,
    MoldCoreBatchDetailResponse,
    MoldCoreBatchListItemResponse,

    MoldCoreTypeLookupResponse,
    MoldCoreTypeShortResponse,
    MoldCoreTypeDetailResponse,
    MoldCoreTypeListItemResponse,

    MoldingAreaDetailResponse,
    MoldingAreaListItemResponse,

    MoldingFlaskShortResponse,
    MoldingFlaskDetailResponse,
    MoldingFlaskListItemResponse,

    MoldingSandTypeShortResponse,
    MoldingSandTypeDetailResponse,
    MoldingSandTypeListItemResponse,

    PatternPlateFrameShortResponse,
    PatternPlateFrameDetailResponse,
    PatternPlateFrameListItemResponse,

    MoldCoreDetailResponse,
    MoldCoreCreateOperation,
    MoldCoreUpdateOperation,
    MoldCoreDeleteOperation,

    MoldCavityCreate,
    MoldCavityUpdate,
    MoldCavityDetailResponse,
    MoldCavityCreateOperation,
    MoldCavityUpdateOperation,
    MoldCavityDeleteOperation,

    MoldPassportDataGSCDetailResponse,
    MoldPassportDataGSCCreateOperation,
    MoldPassportDataGSCUpdateOperation,
    MoldPassportDataGSCDeleteOperation,

    MoldPassportDataASCDetailResponse,
    MoldPassportDataASCCreateOperation,
    MoldPassportDataASCUpdateOperation,
    MoldPassportDataASCDeleteOperation,

    MoldPassportCreate,
    MoldPassportUpdate,
    MoldPassportDetailResponse,
    MoldPassportListItemResponse
]

for schema in schemas_to_rebuild:
    try:
        schema.model_rebuild()
    except Exception as e:
        print(f"Failed to rebuild {schema.__name__}: {e}")
