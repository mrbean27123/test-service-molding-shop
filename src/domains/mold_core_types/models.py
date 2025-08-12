import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.base import BaseORM, ReferenceEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.casting_products.models import CastingProduct
    from domains.mold_core_batches.models import MoldCoreBatch


class MoldCoreType(BaseORM, ReferenceEntityMetadataMixin):
    """SQLAlchemy ORM model for Mold Core Type [reference entity]."""
    __tablename__ = "mold_core_types"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    casting_product_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("casting_products.id", ondelete="RESTRICT"),
        nullable=False
    )

    casting_product: Mapped["CastingProduct"] = safe_relationship(back_populates="mold_core_types")
    model_number: Mapped[str] = mapped_column(String(120))
    shelf_life_days: Mapped[int] = mapped_column(Integer)

    mold_core_batches: Mapped[list["MoldCoreBatch"]] = safe_relationship(
        back_populates="mold_core_type"
    )

    def __repr__(self) -> str:
        return (
            f"<MoldCoreType id={self.id} model_number='{self.model_number}' "
            f"shelf_life_days={self.shelf_life_days}>"
        )
