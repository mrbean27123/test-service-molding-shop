from sqlalchemy import Column, DateTime, ForeignKey, Table, func

from infrastructure.database.models.base import BaseORM


molding_area_casting_technologies = Table(
    "molding_area_casting_technologies",
    BaseORM.metadata,
    Column("molding_area_id", ForeignKey("molding_areas.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "casting_technology_id",
        ForeignKey("casting_technologies.id", ondelete="CASCADE"),
        primary_key=True
    ),
    Column("created_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
)
