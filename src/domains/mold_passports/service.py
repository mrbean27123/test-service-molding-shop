from enum import Enum
from typing import Literal
from uuid import UUID

from common.auth.schemas import UserData
from domains.casting_products.enums import CastingProductType
from domains.mold_passports.models import MoldCavity
from domains.mold_passports.repositories.mold_passport import MoldPassportLoadOptions
from domains.mold_passports.schemas import (
    MoldPassportCreate,
    MoldPassportUpdate,
    MoldPassportDetailResponse,
    MoldPassportListItemResponse,
    MoldPassportListResponse,

    MoldPassportDataGSCCreateOperation,
    MoldPassportDataGSCOperation,

    MoldPassportDataASCCreateOperation,
    MoldPassportDataASCOperation,

    MoldCavityCreateOperation,
    MoldCavityUpdateOperation,
    MoldCavityDeleteOperation,

    MoldCoreCreateOperation,
    MoldCoreUpdateOperation,
    MoldCoreDeleteOperation
)
from infrastructure.core.exceptions import EntityNotFoundError
from infrastructure.database import UnitOfWork
from infrastructure.database.models.all_models import MoldPassport
from infrastructure.repositories.base import PaginationCriteria


class MoldPassportLoadSets(str, Enum):
    """Predefined sets of loading options for MoldPassport."""
    DETAIL = "detail"
    LIST_ITEM = "list_item"


class MoldPassportService:
    _LOAD_SETS_MAP: dict[MoldPassportLoadSets, list[MoldPassportLoadOptions]] = {
        MoldPassportLoadSets.DETAIL: [
            MoldPassportLoadOptions.MOLDING_AREA,
            MoldPassportLoadOptions.CASTING_TECHNOLOGY,

            MoldPassportLoadOptions.PATTERN_PLATE_FRAME,
            MoldPassportLoadOptions.MOLDING_FLASK,

            MoldPassportLoadOptions.MOLD_PASSPORT_DATA_GSC__MOLDING_SAND_TYPE,
            MoldPassportLoadOptions.MOLD_PASSPORT_DATA_ASC__MOLDING_SAND_TYPE,
            MoldPassportLoadOptions.MOLD_PASSPORT_DATA_ASC__RESIN,

            MoldPassportLoadOptions.MOLD_CAVITIES__CASTING_PATTERN__CASTING_PRODUCT,
            MoldPassportLoadOptions
            .MOLD_CAVITIES__MOLD_CORES__MOLD_CORE_BATCH__MOLDING_SAND_TYPE,
            MoldPassportLoadOptions
            .MOLD_CAVITIES__MOLD_CORES__MOLD_CORE_BATCH__MOLD_CORE_TYPE__CASTING_PRODUCT,
            MoldPassportLoadOptions
            .MOLD_CAVITIES__MOLD_CORES__MOLD_CORE_BATCH__MOLD_CORE_MOLD_CORE_MAKING_MACHINE
        ],
        MoldPassportLoadSets.LIST_ITEM: [
            MoldPassportLoadOptions.MOLDING_AREA,
            MoldPassportLoadOptions.CASTING_TECHNOLOGY,
            MoldPassportLoadOptions.PATTERN_PLATE_FRAME,
            MoldPassportLoadOptions.MOLDING_FLASK
        ]
    }

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_mold_passport_by_id(self, mold_passport_id: UUID) -> MoldPassportDetailResponse:
        mold_passport: MoldPassport = await self.uow.mold_passports.get_by_id(
            mold_passport_id,
            include=self._LOAD_SETS_MAP[MoldPassportLoadSets.DETAIL]
        )

        if not mold_passport:
            raise EntityNotFoundError(MoldPassport, mold_passport_id)

        return MoldPassportDetailResponse.model_validate(mold_passport)

    async def get_mold_passports_list(
        self,
        page: int,
        per_page: int,
        status: Literal["active", "deleted", "all"] | None,
        user: UserData
    ) -> MoldPassportListResponse:
        conditions = [MoldPassport.deleted_at == None, ]

        total_mold_passports = await self.uow.mold_passports.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_mold_passports + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        mold_passport_entities = await self.uow.mold_passports.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions,
            include=self._LOAD_SETS_MAP[MoldPassportLoadSets.LIST_ITEM]
        )
        response_items = [
            MoldPassportListItemResponse.model_validate(mold_passport)
            for mold_passport in mold_passport_entities
        ]

        return MoldPassportListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_mold_passports
        )

    async def create_mold_passport(
        self,
        mold_passport_data: MoldPassportCreate
    ) -> MoldPassportDetailResponse:
        mold_passport: MoldPassport = await self.uow.mold_passports.create(
            mold_passport_data.to_dto()
        )

        # await self.uow.flush()
        # Unnecessary to refresh: "id" is generated in repository .create()
        # await self.uow.refresh(mold_passport)

        if mold_passport_data.casting_technology_id == 1:
            if not mold_passport_data.data_gsc:
                raise ValueError(
                    "mold_passport_data.data_gsc is required for the selected casting_technology"
                )

            data_gsc_operation = MoldPassportDataGSCCreateOperation(
                action="create",
                data=mold_passport_data.data_gsc
            )
            await self._handle_mold_passport_data_gsc_operation(mold_passport, data_gsc_operation)

        if mold_passport_data.casting_technology_id == 2:
            if not mold_passport_data.data_asc:
                raise ValueError(
                    "mold_passport_data.data_asc is required for the selected casting_technology"
                )

            data_asc_operation = MoldPassportDataASCCreateOperation(
                action="create",
                data=mold_passport_data.data_asc
            )
            await self._handle_mold_passport_data_asc_operation(mold_passport, data_asc_operation)

        if mold_passport_data.mold_cavities:
            mold_cavities_operations = [
                MoldCavityCreateOperation(action="create", data=mold_cavity_create_data)
                for mold_cavity_create_data in mold_passport_data.mold_cavities
            ]
            await self._handle_mold_cavities_operations(mold_passport, mold_cavities_operations)
        else:
            raise ValueError("At least one primary Mold Cavity must be provided")

        await self.uow.flush()
        mold_passport = await self.uow.mold_passports.get_by_id(
            mold_passport.id,
            include=self._LOAD_SETS_MAP[MoldPassportLoadSets.DETAIL]
        )

        self._set_fields_based_on_cavities(mold_passport)
        self._set_mold_passport_completion_status(mold_passport)

        await self.uow.commit()

        # Impossible to use the mold_passport from above, since it's been updated, and "updated_at"
        # field is "server_default" -> requires loading
        return await self.get_mold_passport_by_id(mold_passport.id)

    async def update_mold_passport(
        self,
        mold_passport_id: UUID,
        mold_passport_data: MoldPassportUpdate
    ) -> MoldPassportDetailResponse:
        mold_passport = await self.uow.mold_passports.update(
            mold_passport_id,
            mold_passport_data.to_dto()
        )

        if not mold_passport:
            raise EntityNotFoundError(MoldPassport, mold_passport_id)

        await self.uow.refresh(
            mold_passport,
            attribute_names=["data_gsc", "data_asc"]
        )

        if mold_passport_data.casting_technology_id == 1 and mold_passport_data.data_gsc_operation:
            await self._handle_mold_passport_data_gsc_operation(
                mold_passport,
                mold_passport_data.data_asc_operation
            )

        if mold_passport_data.casting_technology_id == 2 and mold_passport_data.data_asc:
            await self._handle_mold_passport_data_asc_operation(
                mold_passport,
                mold_passport_data.data_asc
            )

        if mold_passport_data.mold_cavity_operations:
            await self._handle_mold_cavities_operations(
                mold_passport,
                mold_passport_data.mold_cavity_operations
            )

        mold_passport = await self.uow.mold_passports.get_by_id(
            mold_passport.id,
            include=self._LOAD_SETS_MAP[MoldPassportLoadSets.DETAIL]
        )

        self._set_fields_based_on_cavities(mold_passport)
        self._set_mold_passport_completion_status(mold_passport)

        await self.uow.commit()

        # Impossible to use the mold_passport from above, since it's been updated, and "updated_at"
        # field is "server_default" -> requires loading
        return await self.get_mold_passport_by_id(mold_passport.id)

    async def delete_mold_passport(self, mold_passport_id: UUID) -> MoldPassportDetailResponse:
        deleted_mold_passport = await self.uow.mold_passports.soft_delete(mold_passport_id)

        if not deleted_mold_passport:
            raise EntityNotFoundError(MoldPassport, mold_passport_id)

        await self.uow.commit()
        # logger.log_entity_action(deleted_mold_passport, "delete")

        return await self.get_mold_passport_by_id(deleted_mold_passport.id)

    async def restore_mold_passport(self, mold_passport_id: UUID) -> MoldPassportDetailResponse:
        restored_mold_passport = await self.uow.mold_passports.restore(mold_passport_id)

        if not restored_mold_passport:
            raise EntityNotFoundError(MoldPassport, mold_passport_id)

        await self.uow.commit()
        # logger.log_entity_action(restored_mold_passport, "restore")

        return await self.get_mold_passport_by_id(restored_mold_passport.id)

    @staticmethod
    def _set_fields_based_on_cavities(mold_passport: MoldPassport) -> None:
        mold_cavities = [
            mold_cavity
            for mold_cavity in mold_passport.mold_cavities
            if mold_cavity.casting_pattern.casting_product.type_ == CastingProductType.PRIMARY
        ]

        serial_numbers = [
            mc.serial_number
            for mc in mold_cavities
            if mc.serial_number
        ]
        reference_code = "/".join(serial_numbers)

        product_names = {mc.casting_pattern.casting_product.name for mc in mold_cavities}
        primary_casting_product_name = "/".join(sorted(product_names))

        marking_year = serial_numbers[0].split("-")[-1]

        mold_passport.reference_code = reference_code
        mold_passport.primary_casting_product_name = primary_casting_product_name
        mold_passport.marking_year = int(marking_year)

    @staticmethod
    def _set_mold_passport_completion_status(mold_passport: MoldPassport) -> None:
        mold_passport.is_complete = True

        attributes_to_check = [
            "pattern_plate_frame_id",
            "molding_flask_id",
            "sequence_in_shift",
            "assembly_timestamp",
            "status"
        ]

        for attribute in attributes_to_check:
            if not getattr(mold_passport, attribute):
                mold_passport.is_complete = False
                return

    async def _handle_mold_passport_data_gsc_operation(
        self,
        mold_passport: MoldPassport,
        operation: (
            MoldPassportDataGSCOperation
            | MoldPassportDataGSCOperation
            | MoldPassportDataGSCOperation
        )
    ) -> None:
        match operation.action:
            case "create":
                if mold_passport.data_gsc:
                    raise ValueError("Data GSC already exists for the specified Mold Passport")

                await self.uow.mold_passport_data_gsc.create(
                    mold_passport_id=mold_passport.id,
                    molding_sand_type_id=1,
                    mold_passport_data_gsc_data=operation.data.to_dto()
                )

            case "update":
                data_gsc = mold_passport.data_gsc

                await self.uow.mold_passport_data_gsc.update(
                    data_gsc,
                    mold_passport_data_gsc_data=operation.data.to_dto()
                )

            case "delete":
                data_gsc = mold_passport.data_gsc

                await self.uow.mold_passport_data_gsc.delete(data_gsc)

    async def _handle_mold_passport_data_asc_operation(
        self,
        mold_passport: MoldPassport,
        operation: (
            MoldPassportDataASCOperation
            | MoldPassportDataASCOperation
            | MoldPassportDataASCOperation
        )
    ) -> None:
        match operation.action:
            case "create":
                if mold_passport.data_asc:
                    raise ValueError("Data ASC already exists for the specified Mold Passport")

                await self.uow.mold_passport_data_asc.create(
                    mold_passport_id=mold_passport.id,
                    molding_sand_type_id=1,
                    mold_passport_data_asc_data=operation.data.to_dto()
                )

            case "update":
                data_asc = mold_passport.data_asc

                await self.uow.mold_passport_data_asc.update(
                    data_asc,
                    mold_passport_data_asc_data=operation.data.to_dto()
                )

            case "delete":
                data_asc = mold_passport.data_asc

                await self.uow.mold_passport_data_asc.delete(data_asc)

    async def _handle_mold_cavities_operations(
        self,
        mold_passport: MoldPassport,
        operations: list[
            MoldCavityCreateOperation
            | MoldCavityUpdateOperation
            | MoldCavityDeleteOperation
            ]
    ) -> None:
        for operation in operations:
            match operation.action:
                case "create":
                    mold_cavity_data = operation.data

                    created_mold_cavity = await self.uow.mold_cavities.create(
                        mold_passport.id,
                        mold_cavity_data=operation.data.to_dto()
                    )

                    if mold_cavity_data.mold_cores:
                        mold_core_operations = [
                            MoldCoreCreateOperation(action="create", data=mold_core_create_data)
                            for mold_core_create_data in mold_cavity_data.mold_cores
                        ]
                        await self._handle_mold_cores_operations(
                            created_mold_cavity,
                            mold_core_operations
                        )

                case "update":
                    mold_cavity_data = operation.data

                    updated_mold_cavity = await self.uow.mold_cavities.update(
                        mold_cavity_id=operation.id,
                        mold_passport_id=mold_passport.id,
                        mold_cavity_data=mold_cavity_data.to_dto()
                    )

                    if not updated_mold_cavity:
                        raise EntityNotFoundError(
                            message=(
                                f"Mold Cavity with id={operation.id} not found or does not belong "
                                f"to specified Mold Passport"
                            )
                        )

                    if mold_cavity_data.mold_core_operations:
                        await self._handle_mold_cores_operations(
                            updated_mold_cavity,
                            mold_cavity_data.mold_core_operations
                        )

                case "delete":
                    deleted_mold_cavity = await self.uow.mold_cavities.delete(
                        mold_cavity_id=operation.id,
                        mold_passport_id=mold_passport.id
                    )

                    if not deleted_mold_cavity:
                        raise EntityNotFoundError(
                            message=(
                                f"Mold Cavity with id={operation.id} not found or does not belong "
                                f"to specified Mold Passport"
                            )
                        )

    async def _handle_mold_cores_operations(
        self,
        mold_cavity: MoldCavity,
        operations: list[
            MoldCoreCreateOperation
            | MoldCoreUpdateOperation
            | MoldCoreDeleteOperation
            ]
    ) -> None:
        for operation in operations:
            match operation.action:
                case "create":
                    await self.uow.mold_cores.create(
                        mold_cavity_id=mold_cavity.id,
                        mold_core_data=operation.data.to_dto()
                    )

                case "update":
                    updated_mold_core = await self.uow.mold_cores.update(
                        operation.id,
                        mold_cavity_id=mold_cavity.id,
                        mold_core_data=operation.data.to_dto()
                    )

                    if not updated_mold_core:
                        raise EntityNotFoundError(
                            message=(
                                f"Mold Core with id={operation.id} not found or does not belong to "
                                f"specified Mold Cavity"
                            )
                        )

                case "delete":
                    deleted_mold_core = await self.uow.mold_cores.delete(
                        mold_core_id=operation.id,
                        mold_cavity_id=mold_cavity.id
                    )

                    if not deleted_mold_core:
                        raise EntityNotFoundError(
                            message=(
                                f"Mold Core with id={operation.id} not found or does not belong to "
                                f"specified Mold Cavity"
                            )
                        )
