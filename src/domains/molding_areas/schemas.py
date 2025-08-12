from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field, field_validator

from domains.molding_areas.dto import MoldingAreaCreateDTO, MoldingAreaUpdateDTO
from infrastructure.schemas.base import (
    InputBase,
    ListResponse,
    ReferenceEntityMetadataSchemaMixin,
    SoftArchiveMetadataSchemaMixin
)


if TYPE_CHECKING:
    from domains.casting_technologies.schemas import (
        CastingTechnologyLookupResponse,
        CastingTechnologyShortResponse
    )


class MoldingAreaInputBase(InputBase):
    @field_validator("name", mode="after", check_fields=False)
    @classmethod
    def validate_name(cls, value: str) -> str:
        return value

    @field_validator("description", mode="after", check_fields=False)
    @classmethod
    def validate_description(cls, value: str | None) -> str | None:
        return value

    @field_validator("pressure_units", mode="after", check_fields=False)
    @classmethod
    def validate_pressure_units(cls, value: str | None) -> str | None:
        return value


class MoldingAreaCreate(MoldingAreaInputBase):
    name: str
    description: str | None = None
    pressure_units: str | None = None

    casting_technology_ids: list[int]

    # additional_molding_option_ids: list[int] -- questionable. What is it exactly? Standalone equipment?

    def to_dto(self) -> MoldingAreaCreateDTO:
        return MoldingAreaCreateDTO(**self.model_dump(exclude={"casting_technology_ids"}))


class MoldingAreaUpdate(MoldingAreaInputBase):
    name: str = Field(None)
    description: str | None = None
    pressure_units: str | None = None

    casting_technology_ids: list[int] = Field(None)

    # additional_molding_option_ids: list[int] -- questionable.

    def to_dto(self) -> MoldingAreaUpdateDTO:
        return MoldingAreaUpdateDTO(
            **self.model_dump(exclude={"casting_technology_ids"}, exclude_unset=True)
        )


class MoldingAreaResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int


class MoldingAreaLookupResponse(MoldingAreaResponseBase):
    name: str
    pressure_units: str | None = None


class MoldingAreaShortResponse(MoldingAreaResponseBase):
    name: str
    pressure_units: str | None = None


class MoldingAreaDetailResponse(MoldingAreaResponseBase, ReferenceEntityMetadataSchemaMixin):
    name: str
    description: str | None = None
    pressure_units: str | None = None

    casting_technologies: list["CastingTechnologyShortResponse"]


class MoldingAreaListItemResponse(MoldingAreaResponseBase, SoftArchiveMetadataSchemaMixin):
    name: str
    description: str | None = None
    pressure_units: str | None = None

    casting_technologies: list["CastingTechnologyLookupResponse"]


class MoldingAreaLookupsListResponse(ListResponse[MoldingAreaLookupResponse]):
    pass


class MoldingAreaListResponse(ListResponse[MoldingAreaListItemResponse]):
    pass
