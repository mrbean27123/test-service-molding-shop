import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Enum, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from domains.casting_products.enums import CastingProductType
from infrastructure.database.models.base import BaseORM, ReferenceEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.casting_patterns.models import CastingPattern
    from domains.mold_core_types.models import MoldCoreType


class CastingProduct(BaseORM, ReferenceEntityMetadataMixin):
    """SQLAlchemy ORM model for Casting Product [reference entity]."""
    __tablename__ = "casting_products"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    type_: Mapped[CastingProductType] = mapped_column(
        "type",
        Enum(CastingProductType, values_callable=lambda enum_cls: [e.value for e in enum_cls])
    )
    name: Mapped[str] = mapped_column(String(255), unique=True)
    blueprint_number: Mapped[str] = mapped_column(String(255), unique=True)
    is_casting_manual_only: Mapped[bool] = mapped_column(Boolean)

    casting_patterns: Mapped[list["CastingPattern"]] = safe_relationship(
        back_populates="casting_product"
    )
    mold_core_types: Mapped[list["MoldCoreType"]] = safe_relationship(
        back_populates="casting_product"
    )

    def __repr__(self) -> str:
        return (
            f"<CastingProduct id={self.id} type='{self.type_.value}' name='{self.name}' "
            f"blueprint_number='{self.blueprint_number}' "
            f"is_casting_manual_only={self.is_casting_manual_only}>"
        )
