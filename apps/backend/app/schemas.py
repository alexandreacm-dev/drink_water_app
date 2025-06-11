from pydantic import BaseModel
from datetime import date
from typing import Optional

class UserBase(BaseModel):
    name: str
    weight: float

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True

class WaterConsumptionBase(BaseModel):
    user_id: int
    date: date
    consumed_ml: float

class WaterConsumptionCreate(WaterConsumptionBase):
    pass

class WaterConsumption(WaterConsumptionBase):
    id: int
    goal_ml: float
    reached_goal: bool
    
    class Config:
        orm_mode = True