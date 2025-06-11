from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    weight = Column(Float)

class WaterConsumption(Base):
    __tablename__ = "water_consumption"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    date = Column(Date)
    consumed_ml = Column(Float)
    goal_ml = Column(Float)
    reached_goal = Column(Boolean, default=False)