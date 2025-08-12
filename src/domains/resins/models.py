import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Enum, String, UUID, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from domains.resins.enums import ResinType
from infrastructure.database.models.base import BaseORM, BusinessEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.mold_core_batches.models import MoldCoreBatch


class Resin(BaseORM, BusinessEntityMetadataMixin):
    """SQLAlchemy ORM model for Resin [business entity]."""
    __tablename__ = "resins"
    __table_args__ = (
        UniqueConstraint("brand", "name", name="uq_resin_brand_name"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    type_: Mapped[ResinType] = mapped_column(
        "type",
        Enum(ResinType, values_callable=lambda enum_cls: [e.value for e in enum_cls])
    )
    brand: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    serial_number: Mapped[str] = mapped_column(String(3))

    mold_core_batches: Mapped[list["MoldCoreBatch"]] = safe_relationship(back_populates="resin")

    def __repr__(self) -> str:
        return (
            f"<Resin id={self.id} brand='{self.brand}' name='{self.name}' "
            f"serial_number='{self.serial_number}'>"
        )
