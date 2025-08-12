import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, UUID, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.base import BaseORM, BusinessEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.mold_core_batches.models import MoldCoreBatch


class IronOxide(BaseORM, BusinessEntityMetadataMixin):
    """SQLAlchemy ORM model for Iron Oxide [business entity]."""
    __tablename__ = "iron_oxides"
    __table_args__ = (UniqueConstraint("brand", "name", name="uq_iron_oxide_brand_name"),)

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    brand: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))

    mold_core_batches: Mapped[list["MoldCoreBatch"]] = safe_relationship(
        back_populates="iron_oxide"
    )

    def __repr__(self) -> str:
        return f"<IronOxide id={self.id} brand='{self.brand}' name='{self.name}'>"
