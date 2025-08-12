from contextvars import ContextVar
from typing import TYPE_CHECKING, Union


if TYPE_CHECKING:
    from common.auth.schemas import UserData

# Context variable for correlation ID to trace logs per request
_correlation_id_var: ContextVar[str | None] = ContextVar("correlation_id", default=None)

# Context variable for authenticated user data
_current_user_var: ContextVar[Union["UserData", None]] = (ContextVar("current_user", default=None))


def get_correlation_id() -> str:
    """Get correlation id from context."""
    corr_id = _correlation_id_var.get() or "<???>"

    return corr_id


def set_correlation_id(correlation_id: str) -> None:
    """Set correlation id to context."""
    _correlation_id_var.set(correlation_id)
    print(f"Correlation id set to {get_correlation_id()}")


def get_current_user() -> Union["UserData", None]:
    """Get current authenticated user from context."""
    return _current_user_var.get()


def set_current_user(user_data: "UserData") -> None:
    """Set current authenticated user to context."""
    _current_user_var.set(user_data)
