import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Enum, String, UUID, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from domains.shared.enums import AssetStatus
from infrastructure.database.models.base import BaseORM, BusinessEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.mold_core_batches.models import MoldCoreBatch


class MoldCoreMakingMachine(BaseORM, BusinessEntityMetadataMixin):
    """SQLAlchemy ORM model for Mold Core Making Machine [business entity]."""
    __tablename__ = "mold_core_making_machines"
    __table_args__ = (
        UniqueConstraint("brand", "model", name="uq_mold_core_making_machine_brand_model"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    brand: Mapped[str] = mapped_column(String(255))
    model: Mapped[str] = mapped_column(String(255))

    status: Mapped[AssetStatus] = mapped_column(
        Enum(AssetStatus, values_callable=lambda enum_cls: [e.value for e in enum_cls])
    )

    mold_core_batches: Mapped[list["MoldCoreBatch"]] = safe_relationship(
        back_populates="mold_core_making_machine"
    )

    def __repr__(self) -> str:
        return (
            f"<MoldCoreMakingMachine id={self.id} brand='{self.brand}' model='{self.model}' "
            f"status={self.status}>"
        )
