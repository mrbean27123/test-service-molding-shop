import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Enum, Float, ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from domains.mold_passports.enums import MoldingSandSystem
from infrastructure.database.models.base import BaseORM, ComponentEntity
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.mold_passports.models.mold_passport import MoldPassport
    from domains.molding_sand_types.models import MoldingSandType


class MoldPassportDataGSC(BaseORM, ComponentEntity):
    """SQLAlchemy ORM model for Mold Passport Data GSC (Green Sand Casting) [component entity]."""
    __tablename__ = "mold_passport_data_gsc"

    mold_passport_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("mold_passports.id", ondelete="CASCADE"),
        primary_key=True
    )
    molding_sand_type_id: Mapped[int] = mapped_column(
        ForeignKey("molding_sand_types.id", ondelete="RESTRICT"),
        nullable=False
    )

    molding_sand_type: Mapped["MoldingSandType"] = safe_relationship()
    molding_sand_system: Mapped[MoldingSandSystem] = mapped_column(
        Enum(MoldingSandSystem, values_callable=lambda enum_cls: [e.value for e in enum_cls])
    )
    molding_sand_number: Mapped[str] = mapped_column(String(20))

    mold_horizontal_density: Mapped[float] = mapped_column(Float)
    mold_vertical_density: Mapped[float] = mapped_column(Float)

    mold_passport: Mapped["MoldPassport"] = safe_relationship(back_populates="data_gsc")

    def __repr__(self) -> str:
        return (
            f"<MoldPassportDataGSC mold_passport_id={self.mold_passport_id} "
            f"molding_sand_system={self.molding_sand_system} "
            f"molding_sand_number='{self.molding_sand_number}' "
            f"mold_horizontal_density={self.mold_horizontal_density} "
            f"mold_vertical_density={self.mold_vertical_density}>"
        )
