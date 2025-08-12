import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.base import BaseORM, ComponentEntity
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.mold_core_batches.models import MoldCoreBatch
    from domains.mold_passports.models.mold_cavity import MoldCavity


class MoldCore(BaseORM, ComponentEntity):
    """SQLAlchemy ORM model for Mold Core [component entity]."""
    __tablename__ = "mold_cores"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    mold_cavity_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("mold_cavities.id", ondelete="CASCADE"),
        nullable=False
    )
    core_batch_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("mold_core_batches.id", ondelete="RESTRICT"),
        nullable=False
    )

    mold_cavity: Mapped["MoldCavity"] = safe_relationship(back_populates="mold_cores")
    core_batch: Mapped["MoldCoreBatch"] = safe_relationship()
    hardness: Mapped[float] = mapped_column(Float)

    def __repr__(self) -> str:
        return f"<MoldCore id={self.id} hardness={self.hardness}>"
