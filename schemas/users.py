from typing import Optional

from pydantic.main import BaseModel


class UserBase(BaseModel):
    class Config:
        orm_mode = True
        title = 'users'

    id: int
    name: str


class UserCreate(UserBase):
    id: Optional[int]
    name: str
