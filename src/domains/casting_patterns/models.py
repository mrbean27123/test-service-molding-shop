import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from domains.shared.enums import AssetStatus
from infrastructure.database.models.base import BaseORM, BusinessEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.casting_products.models import CastingProduct


class CastingPattern(BaseORM, BusinessEntityMetadataMixin):
    """SQLAlchemy ORM model for Casting Pattern [business entity]."""
    __tablename__ = "casting_patterns"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    casting_product_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("casting_products.id"),
        nullable=False
    )

    casting_product: Mapped["CastingProduct"] = safe_relationship(back_populates="casting_patterns")
    serial_number: Mapped[str] = mapped_column(String(255), unique=True)
    status: Mapped[AssetStatus] = mapped_column(
        Enum(AssetStatus, values_callable=lambda enum_cls: [e.value for e in enum_cls])
    )

    def __repr__(self) -> str:
        return (
            f"<CastingPattern id={self.id} serial_number='{self.serial_number}' "
            f"status={self.status})>"
        )
