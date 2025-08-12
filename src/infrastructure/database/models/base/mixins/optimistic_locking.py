from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column


class OptimisticLockingMixin:
    """Mixin for optimistic locking mechanism."""
    version: Mapped[int] = mapped_column(Integer, server_default="1")
    __mapper_args__ = {"version_id_col": version}
