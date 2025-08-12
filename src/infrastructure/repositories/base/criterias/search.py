from dataclasses import dataclass

from sqlalchemy.orm import InstrumentedAttribute


@dataclass(frozen=True)
class SearchCriteria:
    """Search criteria for text-based filtering."""
    query: str | None
    field: InstrumentedAttribute
    min_query_length: int | None = None
    is_case_sensitive: bool = False

    def __post_init__(self):
        if (self.min_query_length is not None) and not (1 <= self.min_query_length <= 7):
            raise ValueError("SearchCriteria 'min_query_length' must be in range 1-7")

        if self.query is not None:
            normalized_query = self.query.strip()

            if not normalized_query:
                object.__setattr__(self, "query", None)
                return

            if self.min_query_length is not None and len(normalized_query) < self.min_query_length:
                object.__setattr__(self, "query", None)
                return

            if not self.is_case_sensitive:
                normalized_query = normalized_query.lower()

            object.__setattr__(self, "query", normalized_query)

    @property
    def is_applicable(self) -> bool:
        """Check if search criteria should be applied."""
        return self.query is not None
