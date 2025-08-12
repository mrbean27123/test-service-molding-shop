from uuid import UUID

from pydantic import BaseModel, EmailStr

from common.auth.schemas.permission_data import PermissionData


class UserData(BaseModel):
    id: UUID

    email: EmailStr

    is_active: bool
    is_superuser: bool

    roles: list[str] = []
    permissions: list[PermissionData] = []

    def has_role(self, role: str) -> bool:
        """Check if the user has the specified role"""
        return role in self.roles

    def has_any_role(self, roles: list[str]) -> bool:
        """Check if the user has any of the specified roles"""
        return any(role in self.roles for role in roles)

    def has_permission(self, permission_name: str, department: str = None) -> bool:
        """Check if the user has a specific permission (optionally within a department)"""
        for perm in self.permissions:
            if perm.name == permission_name:
                if department is None or perm.department == department:
                    return True

        return False

    def has_permissions(self, permission_names: list[str], department: str = None) -> bool:
        """Checks if the user has all the specified permissions (optionally within a department)"""
        return all(self.has_permission(perm_name, department) for perm_name in permission_names)

    def has_any_permission(self, permission_names: list[str], department: str = None) -> bool:
        """
        Checks if the user has at least one of the specified permissions (optionally within a
        department)
        """
        return any(self.has_permission(perm_name, department) for perm_name in permission_names)
