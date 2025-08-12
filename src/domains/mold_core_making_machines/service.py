from domains.mold_core_making_machines.models import MoldCoreMakingMachine
from domains.mold_core_making_machines.schemas import (
    MoldCoreMakingMachineLookupResponse,
    MoldCoreMakingMachineLookupsListResponse
)
from infrastructure.database import UnitOfWork
from infrastructure.repositories.base import PaginationCriteria


class MoldCoreMakingMachineService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_mold_core_making_machine_lookups_list(
        self,
        page: int,
        per_page: int
    ) -> MoldCoreMakingMachineLookupsListResponse:
        conditions = [MoldCoreMakingMachine.deleted_at == None, ]

        total_mold_core_making_machines = await self.uow.mold_core_making_machines.get_count(
            where_conditions=conditions
        )
        total_pages = max((total_mold_core_making_machines + per_page - 1) // per_page, 1)
        offset = (page - 1) * per_page

        mold_core_making_machine_entities = await self.uow.mold_core_making_machines.get_all_paginated(
            PaginationCriteria(per_page, offset),
            where_conditions=conditions
        )
        response_items = [
            MoldCoreMakingMachineLookupResponse.model_validate(mold_core_making_machine)
            for mold_core_making_machine in mold_core_making_machine_entities
        ]

        return MoldCoreMakingMachineLookupsListResponse(
            data=response_items,
            page=page,
            total_pages=total_pages,
            total_items=total_mold_core_making_machines
        )
