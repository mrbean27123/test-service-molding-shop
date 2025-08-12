from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from domains.molding_areas.models.associations import molding_area_casting_technologies
from domains.molding_flasks.models import molding_flask_areas
from domains.pattern_plate_frames.models import pattern_plate_frame_molding_areas
from infrastructure.database.models.base import BaseORM, ReferenceEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.casting_technologies.models import CastingTechnology
    from domains.mold_passports.models import MoldPassport
    from domains.molding_flasks.models import MoldingFlask
    from domains.pattern_plate_frames.models import PatternPlateFrame


class MoldingArea(BaseORM, ReferenceEntityMetadataMixin):
    """SQLAlchemy ORM model for Molding Area [reference entity]."""
    __tablename__ = "molding_areas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[str | None] = mapped_column(String(255))
    pressure_units: Mapped[str | None] = mapped_column(String(20))

    mold_passports: Mapped[list["MoldPassport"]] = safe_relationship(back_populates="molding_area")
    casting_technologies: Mapped[list["CastingTechnology"]] = safe_relationship(
        secondary=molding_area_casting_technologies,
        back_populates="molding_areas"
    )
    pattern_plate_frames: Mapped[list["PatternPlateFrame"]] = safe_relationship(
        secondary=pattern_plate_frame_molding_areas,
        back_populates="molding_areas"
    )
    molding_flasks: Mapped[list["MoldingFlask"]] = safe_relationship(
        secondary=molding_flask_areas,
        back_populates="molding_areas"
    )

    def __repr__(self) -> str:
        return (
            f"<MoldingArea id={self.id} name='{self.name}' pressure_units='{self.pressure_units}'>"
        )
