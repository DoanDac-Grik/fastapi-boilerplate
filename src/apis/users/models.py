from sqlmodel import Field, SQLModel
from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

class UserBase(SQLModel):
    name: str = Field(max_length=50)
    gender: Gender 

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Join",
                "gender": "male"
            }
        }


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

# DTO
class BodyCreateDto(UserBase):
    pass

class BodyUpdateDto(SQLModel):
    name: str | None = Field(max_length=50, default=None)
    gender: Gender | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Join",
                "gender": "male"
            }
        }