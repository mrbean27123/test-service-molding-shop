from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.base import BaseORM, ReferenceEntityMetadataMixin
from infrastructure.database.utils import safe_relationship


if TYPE_CHECKING:
    from domains.casting_technologies.models import CastingTechnology
    from domains.mold_core_batches.models import MoldCoreBatch


class MoldingSandType(BaseORM, ReferenceEntityMetadataMixin):
    """SQLAlchemy ORM model for Molding Sand Type [reference entity]."""
    __tablename__ = "molding_sand_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    casting_technology_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("casting_technologies.id"),
        nullable=False
    )

    casting_technology: Mapped["CastingTechnology"] = safe_relationship(
        back_populates="molding_sand_types"
    )
    name: Mapped[str] = mapped_column(String(255), unique=True)
    abbreviation: Mapped[str] = mapped_column(String(50), unique=True)

    mold_core_batches: Mapped[list["MoldCoreBatch"]] = safe_relationship(
        back_populates="molding_sand_type"
    )

    def __repr__(self) -> str:
        return (
            f"<MoldingSandType id={self.id} name='{self.name}' abbreviation='{self.abbreviation}'>"
        )
