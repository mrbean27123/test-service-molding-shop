import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.base import BaseORM, ComponentEntity
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.casting_patterns.models import CastingPattern
    from domains.mold_passports.models.mold_core import MoldCore
    from domains.mold_passports.models.mold_passport import MoldPassport


class MoldCavity(BaseORM, ComponentEntity):
    """SQLAlchemy ORM model for Mold Cavity [component entity]."""
    __tablename__ = "mold_cavities"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    mold_passport_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("mold_passports.id", ondelete="RESTRICT"),
        nullable=False
    )
    casting_pattern_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("casting_patterns.id", ondelete="RESTRICT"),
        nullable=False
    )

    casting_pattern: Mapped["CastingPattern"] = safe_relationship()
    serial_number: Mapped[str | None] = mapped_column(String(255))
    mold_cores: Mapped[list["MoldCore"]] = safe_relationship(
        back_populates="mold_cavity",
        cascade="all, delete-orphan"
    )

    is_functional: Mapped[bool] = mapped_column(Boolean, default=True)

    mold_passport: Mapped["MoldPassport"] = safe_relationship(back_populates="mold_cavities")

    def __repr__(self) -> str:
        return (
            f"<MoldCavity id={self.id} serial_number='{self.serial_number}' "
            f"is_functional={self.is_functional}>"
        )
