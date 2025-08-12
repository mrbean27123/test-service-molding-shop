from pydantic import BaseModel


class PermissionData(BaseModel):
    id: int

    name: str
    department_name: str
