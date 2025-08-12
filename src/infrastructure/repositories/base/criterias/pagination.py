from dataclasses import dataclass


@dataclass(frozen=True)
class PaginationCriteria:
    """Pagination criteria for pagination."""
    limit: int
    offset: int = 0

    def __post_init__(self):
        if self.limit <= 0:
            raise ValueError("PaginationCriteria 'limit' must be positive")
        if self.offset < 0:
            raise ValueError("PaginationCriteria 'offset' cannot be negative")
