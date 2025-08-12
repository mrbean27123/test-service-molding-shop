from sqlalchemy import Column, DateTime, ForeignKey, Table, func

from infrastructure.database.models.base import BaseORM


molding_flask_areas = Table(
    "molding_flask_areas",
    BaseORM.metadata,
    Column(
        "molding_flask_id",
        ForeignKey("molding_flasks.id", ondelete="CASCADE"),
        primary_key=True
    ),
    Column("molding_area_id", ForeignKey("molding_areas.id", ondelete="CASCADE"), primary_key=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
)
