from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict


ModelT = TypeVar("ModelT", bound=BaseModel)


class ListResponse(BaseModel, Generic[ModelT]):
    model_config = ConfigDict(from_attributes=True)

    data: list[ModelT]
    page: int
    total_pages: int
    total_items: int
