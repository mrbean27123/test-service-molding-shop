from pydantic import BaseModel, ConfigDict


class InputBase(BaseModel):
    model_config = ConfigDict(
        extra="forbid",  # 🚫 Input validation: forbid unexpected fields
        str_strip_whitespace=True,  # 🧼 String normalization (strip() all strings automatically)
    )
