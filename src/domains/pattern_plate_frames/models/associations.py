from sqlalchemy import Column, DateTime, ForeignKey, Table, func

from infrastructure.database.models.base import BaseORM


pattern_plate_frame_molding_areas = Table(
    "pattern_plate_frame_molding_areas",
    BaseORM.metadata,
    Column(
        "pattern_plate_frame_id",
        ForeignKey("pattern_plate_frames.id", ondelete="CASCADE"),
        primary_key=True
    ),
    Column("molding_area_id", ForeignKey("molding_areas.id", ondelete="CASCADE"), primary_key=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
)
