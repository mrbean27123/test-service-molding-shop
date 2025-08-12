from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from domains.molding_areas.models import molding_area_casting_technologies
from infrastructure.database.models.base import BaseORM, ReferenceEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.mold_passports.models import MoldPassport
    from domains.molding_areas.models import MoldingArea
    from domains.molding_sand_types.models import MoldingSandType


class CastingTechnology(BaseORM, ReferenceEntityMetadataMixin):
    """SQLAlchemy ORM model for Casting Technology [reference entity]."""
    __tablename__ = "casting_technologies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(255), unique=True)
    abbreviation: Mapped[str] = mapped_column(String(20), unique=True)

    molding_sand_types: Mapped[list["MoldingSandType"]] = safe_relationship(
        back_populates="casting_technology"
    )
    mold_passports: Mapped[list["MoldPassport"]] = safe_relationship(
        back_populates="casting_technology"
    )
    molding_areas: Mapped[list["MoldingArea"]] = safe_relationship(
        secondary=molding_area_casting_technologies,
        back_populates="casting_technologies"
    )

    def __repr__(self) -> str:
        return (
            f"<CastingTechnology id={self.id} name='{self.name}' "
            f"abbreviation='{self.abbreviation}'>"
        )
