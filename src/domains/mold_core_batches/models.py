import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Union

from sqlalchemy import DateTime, Enum, Float, ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from domains.shared.enums import ConsumableStatus
from infrastructure.database.models.base import BaseORM, BusinessEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.iron_oxides.models import IronOxide
    from domains.mold_core_making_machines.models import MoldCoreMakingMachine
    from domains.mold_core_types.models import MoldCoreType
    from domains.molding_sand_types.models import MoldingSandType
    from domains.resins.models import Resin
    from domains.triethylamines.models import Triethylamine


class MoldCoreBatch(BaseORM, BusinessEntityMetadataMixin):
    """SQLAlchemy ORM model for Mold Core Batch [business entity]."""
    __tablename__ = "mold_core_batches"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # === Foreign Keys ===
    molding_sand_type_id: Mapped[int] = mapped_column(
        ForeignKey("molding_sand_types.id", ondelete="RESTRICT"),
        nullable=False
    )
    mold_core_type_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("mold_core_types.id", ondelete="RESTRICT"),
        nullable=False
    )
    mold_core_making_machine_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("mold_core_making_machines.id", ondelete="RESTRICT"),
        nullable=False
    )
    resin_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("resins.id", ondelete="RESTRICT"),
        nullable=False
    )
    triethylamine_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("triethylamines.id", ondelete="RESTRICT"),
        nullable=False
    )
    iron_oxide_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("iron_oxides.id", ondelete="RESTRICT"),
        nullable=True
    )

    # === Fields ===
    molding_sand_type: Mapped["MoldingSandType"] = safe_relationship(
        back_populates="mold_core_batches"
    )
    mold_core_type: Mapped["MoldCoreType"] = safe_relationship(back_populates="mold_core_batches")

    mold_core_making_machine: Mapped["MoldCoreMakingMachine"] = safe_relationship(
        back_populates="mold_core_batches"
    )
    inventory_box_number: Mapped[str] = mapped_column(String(20))

    resin: Mapped["Resin"] = safe_relationship(back_populates="mold_core_batches")
    # resin_component_a_dosage: Mapped[float | None] = mapped_column(Float)
    # resin_component_b_dosage: Mapped[float | None] = mapped_column(Float)

    triethylamine: Mapped[Union["Triethylamine", None]] = safe_relationship(
        back_populates="mold_core_batches"
    )
    iron_oxide: Mapped[Union["IronOxide", None]] = safe_relationship(
        back_populates="mold_core_batches"
    )

    sand_temperature: Mapped[float] = mapped_column(Float)
    control_mold_core_hardness: Mapped[float] = mapped_column(Float)

    manufacturing_timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    batch_expiry_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    status: Mapped[ConsumableStatus] = mapped_column(
        Enum(ConsumableStatus, values_callable=lambda enum_cls: [e.value for e in enum_cls])
    )

    def __repr__(self) -> str:
        return (
            f"<MoldCoreBatch id={self.id} manufacturing_timestamp={self.manufacturing_timestamp} "
            f"batch_expiry_date={self.batch_expiry_date} status={self.status}>"
        )
