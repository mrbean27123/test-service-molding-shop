from datetime import datetime
from uuid import UUID

from pydantic import computed_field


class SoftDeleteMetadataSchemaMixin:
    deleted_at: datetime | None = None

    @computed_field
    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None


class BusinessEntityMetadataSchemaMixin(SoftDeleteMetadataSchemaMixin):
    created_at: datetime
    created_by_id: UUID | None = None
    updated_at: datetime
    updated_by_id: UUID | None = None
