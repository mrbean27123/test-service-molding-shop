from typing import Any
from uuid import UUID

from pydantic import EmailStr


class AppException(Exception):
    status_code = 500
    default_message = "Internal server error"

    def __init__(self, message: str | None = None, details: dict[str, Any] | None = None):
        self.message = message or self.default_message
        self.details = details
        super().__init__(self.message)


class ClientError(AppException):
    status_code = 400
    default_message = "Bad request"


class ServerError(AppException):
    pass


class AuthenticationError(ClientError):
    status_code = 401
    default_message = "Authentication failed"


class UserNotFoundError(AuthenticationError):
    default_message = "User not found"

    def __init__(
        self, user_id: UUID | None = None,
        user_email: str | EmailStr | None = None,
        message: str | None = None,
        details: dict[str, Any] | None = None
    ):
        if user_id:
            message = f"User with ID '{user_id}' not found"
        elif user_email:
            message = f"User with email '{user_email}' not found"

        super().__init__(message, details)


class InsufficientPrivilegesError(AuthenticationError):
    status_code = 403
    default_message = "Superuser privileges required"

    def __init__(self, message: str | None = None):
        super().__init__(message)


class InsufficientRolesError(AuthenticationError):
    status_code = 403
    default_message = "Insufficient roles"

    def __init__(self, roles: list[str], details: dict[str, Any] | None = None):
        details = details or {}
        details["required_roles"] = roles

        roles_str = ", ".join(roles)
        message = f"One of the following roles is required: {roles_str}"

        super().__init__(message, details)


class InsufficientPermissionsError(AuthenticationError):
    status_code = 403
    default_message = "Insufficient permissions"

    def __init__(self, permissions: list[str], details: dict[str, Any] | None = None):
        details = details or {}
        details["required_permissions"] = permissions

        permissions_str = ", ".join(permissions)
        message = f"The following permissions are required: {permissions_str}"

        super().__init__(message, details)
