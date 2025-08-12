import uuid
from datetime import datetime

from sqlalchemy import DateTime, UUID, func
from sqlalchemy.orm import Mapped, mapped_column


class AuditMixin:
    """
    Audit mixin: creation and update timestamps with user IDs for each operation.

    Automatically populates user IDs through SQLAlchemy event listeners.
    """
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_by_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    updated_by_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))

# @event.listens_for(AuditMixin, "before_insert", propagate=True)
# def before_insert_listener(mapper, connection, target: AuditMixin):
#     """Event listener: populates audit fields before insert."""
#     user = context.get_current_user()
#
#     actor_id = user.id if user else settings.SYSTEM_USER_ID
#
#     target.created_by_id = actor_id
#     target.updated_by_id = actor_id
#
#
# @event.listens_for(AuditMixin, "before_update", propagate=True)
# def before_update_listener(mapper, connection, target: AuditMixin):
#     """Event listener: populates audit fields before update."""
#     user = context.get_current_user()
#
#     target.updated_by_id = user.id if user else settings.SYSTEM_USER_ID
