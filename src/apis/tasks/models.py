from sqlmodel import Field, SQLModel
from enum import Enum

class Status(Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"

class TaskBase(SQLModel):
    task: str = Field(max_length=5)
    status: Status

    class Config:
        json_schema_extra = {
            "example": {
                "task": "Reading book",
                "status": "doing"
            }
        }


class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

# DTO
class BodyCreateDto(TaskBase):
    pass

class BodyUpdateDto(SQLModel):
    task: str | None = Field(max_length=100, default=None)
    status: Status | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "task": "Reading book",
                "status": "doing"
            }
        }