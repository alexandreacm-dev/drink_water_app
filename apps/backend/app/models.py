from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    weight_kg = Column(Float, nullable=False)
    water_logs = relationship("WaterLog", back_populates="user")


class WaterLog(Base):
    __tablename__ = 'water_logs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date, default=datetime.date.today)
    amount_ml = Column(Integer, default=0)

    user = relationship("User", back_populates="water_logs")
