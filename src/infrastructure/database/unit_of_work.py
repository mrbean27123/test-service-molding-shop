from typing import Iterable, TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.selectable import ForUpdateParameter


if TYPE_CHECKING:
    from domains.casting_patterns.repository import CastingPatternRepository
    from domains.casting_products.repository import CastingProductRepository
    from domains.casting_technologies.repository import CastingTechnologyRepository
    from domains.iron_oxides.repository import IronOxideRepository
    from domains.mold_core_batches.repository import MoldCoreBatchRepository
    from domains.mold_core_making_machines.repository import MoldCoreMakingMachineRepository
    from domains.mold_core_types.repository import MoldCoreTypeRepository
    from domains.mold_passports.repositories import (
        MoldPassportRepository,
        MoldPassportDataGSCRepository,
        MoldPassportDataASCRepository,
        MoldCavityRepository,
        MoldCoreRepository
    )
    from domains.molding_areas.repository import MoldingAreaRepository
    from domains.molding_flasks.repository import MoldingFlaskRepository
    from domains.molding_sand_types.repository import MoldingSandTypeRepository
    from domains.pattern_plate_frames.repository import PatternPlateFrameRepository
    from domains.resins.repository import ResinRepository
    from domains.triethylamines.repository import TriethylamineRepository


class UnitOfWork:
    def __init__(self, session_factory: sessionmaker[AsyncSession]):
        self._session_factory = session_factory

    async def __aenter__(self):
        self._db_session: AsyncSession = self._session_factory()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self._db_session.rollback()

        await self._db_session.close()

    async def refresh(
        self,
        instance: object,
        attribute_names: Iterable[str] | None = None,
        with_for_update: ForUpdateParameter = None
    ) -> None:
        await self._db_session.refresh(instance, attribute_names, with_for_update)

    async def flush(self):
        await self._db_session.flush()

    async def commit(self):
        await self._db_session.commit()

    async def rollback(self):
        await self._db_session.rollback()

    @property
    def mold_passports(self) -> "MoldPassportRepository":
        if not hasattr(self, "_mold_passport_repo"):
            from domains.mold_passports.repositories import MoldPassportRepository
            self._mold_passport_repo = MoldPassportRepository(self._db_session)

        return self._mold_passport_repo

    @property
    def mold_passport_data_gsc(self) -> "MoldPassportDataGSCRepository":
        if not hasattr(self, "_mold_passport_data_gsc_repo"):
            from domains.mold_passports.repositories import MoldPassportDataGSCRepository
            self._mold_passport_data_gsc_repo = MoldPassportDataGSCRepository(self._db_session)

        return self._mold_passport_data_gsc_repo

    @property
    def mold_passport_data_asc(self) -> "MoldPassportDataASCRepository":
        if not hasattr(self, "_mold_passport_data_asc_repo"):
            from domains.mold_passports.repositories import MoldPassportDataASCRepository
            self._mold_passport_data_asc_repo = MoldPassportDataASCRepository(self._db_session)

        return self._mold_passport_data_asc_repo

    @property
    def mold_cavities(self) -> "MoldCavityRepository":
        if not hasattr(self, "_mold_cavity_repo"):
            from domains.mold_passports.repositories import MoldCavityRepository
            self._mold_cavity_repo = MoldCavityRepository(self._db_session)

        return self._mold_cavity_repo

    @property
    def mold_cores(self) -> "MoldCoreRepository":
        if not hasattr(self, "_mold_core_repo"):
            from domains.mold_passports.repositories import MoldCoreRepository
            self._mold_core_repo = MoldCoreRepository(self._db_session)

        return self._mold_core_repo

    @property
    def casting_patterns(self) -> "CastingPatternRepository":
        if not hasattr(self, "_casting_pattern_repo"):
            from domains.casting_patterns.repository import CastingPatternRepository
            self._casting_pattern_repo = CastingPatternRepository(self._db_session)

        return self._casting_pattern_repo

    @property
    def casting_products(self) -> "CastingProductRepository":
        if not hasattr(self, "_casting_product_repo"):
            from domains.casting_products.repository import CastingProductRepository
            self._casting_product_repo = CastingProductRepository(self._db_session)

        return self._casting_product_repo

    @property
    def casting_technologies(self) -> "CastingTechnologyRepository":
        if not hasattr(self, "_casting_technology_repo"):
            from domains.casting_technologies.repository import CastingTechnologyRepository
            self._casting_technology_repo = CastingTechnologyRepository(self._db_session)

        return self._casting_technology_repo

    @property
    def iron_oxides(self) -> "IronOxideRepository":
        if not hasattr(self, "_iron_oxide_repo"):
            from domains.iron_oxides.repository import IronOxideRepository
            self._iron_oxide_repo = IronOxideRepository(self._db_session)

        return self._iron_oxide_repo

    @property
    def mold_core_batches(self) -> "MoldCoreBatchRepository":
        if not hasattr(self, "_mold_core_batch_repo"):
            from domains.mold_core_batches.repository import MoldCoreBatchRepository
            self._mold_core_batch_repo = MoldCoreBatchRepository(self._db_session)

        return self._mold_core_batch_repo

    @property
    def mold_core_making_machines(self) -> "MoldCoreMakingMachineRepository":
        if not hasattr(self, "_mold_core_making_machine_repo"):
            from domains.mold_core_making_machines.repository import MoldCoreMakingMachineRepository
            self._mold_core_making_machine_repo = MoldCoreMakingMachineRepository(self._db_session)

        return self._mold_core_making_machine_repo

    @property
    def mold_core_types(self) -> "MoldCoreTypeRepository":
        if not hasattr(self, "_mold_core_type_repo"):
            from domains.mold_core_types.repository import MoldCoreTypeRepository
            self._mold_core_type_repo = MoldCoreTypeRepository(self._db_session)

        return self._mold_core_type_repo

    @property
    def molding_areas(self) -> "MoldingAreaRepository":
        if not hasattr(self, "_molding_area_repo"):
            from domains.molding_areas.repository import MoldingAreaRepository
            self._molding_area_repo = MoldingAreaRepository(self._db_session)

        return self._molding_area_repo

    @property
    def molding_flasks(self) -> "MoldingFlaskRepository":
        if not hasattr(self, "_molding_flask_repo"):
            from domains.molding_flasks.repository import MoldingFlaskRepository
            self._molding_flask_repo = MoldingFlaskRepository(self._db_session)

        return self._molding_flask_repo

    @property
    def molding_sand_types(self) -> "MoldingSandTypeRepository":
        if not hasattr(self, "_molding_sand_type_repo"):
            from domains.molding_sand_types.repository import MoldingSandTypeRepository
            self._molding_sand_type_repo = MoldingSandTypeRepository(self._db_session)

        return self._molding_sand_type_repo

    @property
    def pattern_plate_frames(self) -> "PatternPlateFrameRepository":
        if not hasattr(self, "_pattern_plate_frame_repo"):
            from domains.pattern_plate_frames.repository import PatternPlateFrameRepository
            self._pattern_plate_frame_repo = PatternPlateFrameRepository(self._db_session)

        return self._pattern_plate_frame_repo

    @property
    def resins(self) -> "ResinRepository":
        if not hasattr(self, "_resin_repo"):
            from domains.resins.repository import ResinRepository
            self._resin_repo = ResinRepository(self._db_session)

        return self._resin_repo

    @property
    def triethylamines(self) -> "TriethylamineRepository":
        if not hasattr(self, "_triethylamine_repo"):
            from domains.triethylamines.repository import TriethylamineRepository
            self._triethylamine_repo = TriethylamineRepository(self._db_session)

        return self._triethylamine_repo
