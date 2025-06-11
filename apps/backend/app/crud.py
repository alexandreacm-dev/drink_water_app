from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, weight=user.weight)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_water_consumption(db: Session, user_id: int, date: date):
    return db.query(models.WaterConsumption).filter(
        models.WaterConsumption.user_id == user_id,
        models.WaterConsumption.date == date
    ).first()

def get_water_consumption_history(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.WaterConsumption).filter(
        models.WaterConsumption.user_id == user_id
    ).order_by(models.WaterConsumption.date.desc()).offset(skip).limit(limit).all()

def create_water_consumption(db: Session, water_consumption: schemas.WaterConsumptionCreate):
    # Calcular meta diária (35ml por kg)
    user = get_user(db, water_consumption.user_id)
    goal_ml = user.weight * 35
    
    db_water = models.WaterConsumption(
        user_id=water_consumption.user_id,
        date=water_consumption.date,
        consumed_ml=water_consumption.consumed_ml,
        goal_ml=goal_ml,
        reached_goal=water_consumption.consumed_ml >= goal_ml
    )
    
    db.add(db_water)
    db.commit()
    db.refresh(db_water)
    return db_water