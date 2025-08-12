from datetime import datetime

from pydantic import computed_field


class SoftArchiveMetadataSchemaMixin:
    archived_at: datetime | None = None

    @computed_field
    @property
    def is_archived(self) -> bool:
        return self.archived_at is not None


class ReferenceEntityMetadataSchemaMixin(SoftArchiveMetadataSchemaMixin):
    created_at: datetime
    updated_at: datetime
