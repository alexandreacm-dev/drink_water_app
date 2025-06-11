from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    weight_kg: float

class UserResponse(UserCreate):
    id: int
    class Config:
        orm_mode = True

class WaterLogCreate(BaseModel):
    amount_ml: int

class WaterLogResponse(BaseModel):
    date: date
    amount_ml: int
    meta_ml: int
    reached_goal: bool
    class Config:
        orm_mode = True
