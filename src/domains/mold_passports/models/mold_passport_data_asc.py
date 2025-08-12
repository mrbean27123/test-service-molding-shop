import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.base import BaseORM, ComponentEntity
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.mold_passports.models.mold_passport import MoldPassport
    from domains.molding_sand_types.models import MoldingSandType
    from domains.resins.models import Resin


class MoldPassportDataASC(BaseORM, ComponentEntity):
    """SQLAlchemy ORM model for Mold Passport Data ASC (Air Set Casting) [component entity]."""
    __tablename__ = "mold_passport_data_asc"

    mold_passport_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("mold_passports.id", ondelete="CASCADE"),
        primary_key=True
    )

    molding_sand_type_id: Mapped[int] = mapped_column(
        ForeignKey("molding_sand_types.id", ondelete="RESTRICT"),
        nullable=False
    )
    resin_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("resins.id", ondelete="RESTRICT"),
        nullable=True
    )

    molding_sand_type: Mapped["MoldingSandType"] = safe_relationship()
    mold_hardness: Mapped[float] = mapped_column(Float)
    resin: Mapped["Resin"] = safe_relationship()

    mold_passport: Mapped["MoldPassport"] = safe_relationship(back_populates="data_asc")

    def __repr__(self) -> str:
        return (
            f"<MoldPassportDataASC mold_passport_id={self.mold_passport_id} "
            f"mold_hardness={self.mold_hardness}>"
        )
