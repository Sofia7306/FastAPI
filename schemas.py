from pydantic import BaseModel
from typing import List, Optional

class TrackBase(BaseModel):
    title: str
    artist: str
    genre: str

class TrackCreate(TrackBase):
    pass

class TrackOut(TrackBase):
    id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

