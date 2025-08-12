from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class SoftArchiveMixin:
    """Mixin for an 'active/archived' status instead of soft delete (for reference entities)."""
    archived_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
