from pydantic import BaseModel
from typing import Optional
from enum import Enum

class StatusEnum(str, Enum):
    todo = "todo"
    in_progress = "in-progress"
    done = "done"

# ----- User -----
class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True  # Pydantic V2 replacement for orm_mode

# ----- Task -----
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[StatusEnum] = StatusEnum.todo
    owner_id: Optional[int] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: StatusEnum
    owner_id: Optional[int]

    class Config:
        from_attributes = True