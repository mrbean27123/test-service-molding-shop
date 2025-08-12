from typing import Generic, Literal, TypeVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from infrastructure.schemas.base.input import InputBase


ModelT = TypeVar("ModelT", bound=InputBase)


class AtomicOperationBase(BaseModel):
    model_config = ConfigDict(extra="forbid")


class CreateOperationBase(AtomicOperationBase, Generic[ModelT]):
    """Represents a single atomic 'create' operation within a batch request to create 'ModelT'."""
    action: Literal["create"]
    data: ModelT


class UpdateOperationBase(AtomicOperationBase, Generic[ModelT]):
    """Represents a single atomic 'update' operation within a batch request to modify 'ModelT'."""
    action: Literal["update"]
    data: ModelT
    id: UUID


class DeleteOperationBase(AtomicOperationBase):
    """Represents a single atomic 'delete' operation within a batch request to delete 'ModelT'."""
    action: Literal["delete"]
    id: UUID
