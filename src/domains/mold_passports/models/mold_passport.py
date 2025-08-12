import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Union

from sqlalchemy import Boolean, DateTime, Enum, Float, ForeignKey, Integer, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from domains.shared.enums import ConsumableStatus
from infrastructure.database.models.base import BaseORM, BusinessEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.casting_technologies.models import CastingTechnology
    from domains.mold_passports.models.mold_cavity import MoldCavity
    from domains.mold_passports.models.mold_passport_data_asc import MoldPassportDataASC
    from domains.mold_passports.models.mold_passport_data_gsc import MoldPassportDataGSC
    from domains.molding_areas.models import MoldingArea
    from domains.molding_flasks.models import MoldingFlask
    from domains.pattern_plate_frames.models import PatternPlateFrame


class MoldPassport(BaseORM, BusinessEntityMetadataMixin):
    """SQLAlchemy ORM model for Mold Passport [business entity]."""
    __tablename__ = "mold_passports"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # === Foreign Keys ===
    molding_area_id: Mapped[int] = mapped_column(
        ForeignKey("molding_areas.id", ondelete="RESTRICT"),
        nullable=False
    )
    casting_technology_id: Mapped[int] = mapped_column(
        ForeignKey("casting_technologies.id", ondelete="RESTRICT"),
        nullable=False
    )

    pattern_plate_frame_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("pattern_plate_frames.id", ondelete="RESTRICT"),
        nullable=True
    )
    molding_flask_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("molding_flasks.id", ondelete="RESTRICT"),
        nullable=True
    )

    # === Fields ===
    is_complete: Mapped[bool] = mapped_column(Boolean, default=False)

    primary_casting_product_name: Mapped[str | None] = mapped_column(String(255))
    reference_code: Mapped[str | None] = mapped_column(String(255))

    molding_area: Mapped["MoldingArea"] = safe_relationship(back_populates="mold_passports")
    casting_technology: Mapped["CastingTechnology"] = safe_relationship(
        back_populates="mold_passports"
    )

    pattern_plate_frame: Mapped[Union["PatternPlateFrame", None]] = safe_relationship(
        back_populates="mold_passports"
    )
    molding_flask: Mapped[Union["MoldingFlask", None]] = safe_relationship(
        back_populates="mold_passports"
    )

    marking_year: Mapped[int | None] = mapped_column(Integer)
    mold_cavities: Mapped[list["MoldCavity"]] = safe_relationship(back_populates="mold_passport")

    data_gsc: Mapped[Union["MoldPassportDataGSC", None]] = safe_relationship(
        back_populates="mold_passport"
    )
    data_asc: Mapped[Union["MoldPassportDataASC", None]] = safe_relationship(
        back_populates="mold_passport"
    )
    pressing_pressure: Mapped[float | None] = mapped_column(Float)

    sequence_in_shift: Mapped[int | None] = mapped_column(Integer)
    assembly_timestamp: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    status: Mapped[ConsumableStatus | None] = mapped_column(
        Enum(ConsumableStatus, values_callable=lambda enum_cls: [e.value for e in enum_cls])
    )

    notes: Mapped[str | None] = mapped_column(String(1000), default=None)

    def __repr__(self) -> str:
        return (
            f"<MoldPassport id={self.id} is_complete='{self.is_complete}' "
            f"mold_sequence_in_shift={self.sequence_in_shift} "
            f"mold_assembly_timestamp={self.assembly_timestamp} status={self.status}>"
        )
