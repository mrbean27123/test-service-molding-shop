import uuid
from datetime import datetime

from sqlalchemy import DateTime, UUID
from sqlalchemy.orm import Mapped, mapped_column


class SoftDeleteMixin:
    """Mixin for soft delete fields."""
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_by_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
