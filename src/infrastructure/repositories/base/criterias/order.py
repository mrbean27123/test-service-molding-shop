from dataclasses import dataclass

from sqlalchemy.orm import InstrumentedAttribute


@dataclass(frozen=True)
class OrderCriteria:
    """Ordering criteria for query results."""
    field: InstrumentedAttribute
    ascending: bool = True
