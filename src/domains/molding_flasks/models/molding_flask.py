import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Enum, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from domains.molding_flasks.models.associations import molding_flask_areas
from domains.shared.enums import AssetStatus
from infrastructure.database.models.base import BaseORM, BusinessEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.mold_passports.models import MoldPassport
    from domains.molding_areas.models import MoldingArea


class MoldingFlask(BaseORM, BusinessEntityMetadataMixin):
    """SQLAlchemy ORM model for Molding Flask [business entity]."""
    __tablename__ = "molding_flasks"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    blueprint_number: Mapped[str] = mapped_column(String(255), unique=True)
    serial_number: Mapped[str] = mapped_column(String(255), unique=True)
    status: Mapped[AssetStatus] = mapped_column(
        Enum(AssetStatus, values_callable=lambda enum_cls: [e.value for e in enum_cls])
    )

    mold_passports: Mapped[list["MoldPassport"]] = safe_relationship(back_populates="molding_flask")
    molding_areas: Mapped[list["MoldingArea"]] = safe_relationship(
        secondary=molding_flask_areas,
        back_populates="molding_flasks"
    )

    def __repr__(self) -> str:
        return (
            f"<MoldingFlask id={self.id} blueprint_number='{self.blueprint_number}' "
            f"serial_number='{self.serial_number}' status={self.status}>"
        )
