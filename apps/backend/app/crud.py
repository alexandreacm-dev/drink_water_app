from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def add_water_log(db: Session, user_id: int, amount_ml: int):
    today = date.today()
    log = db.query(models.WaterLog).filter_by(user_id=user_id, date=today).first()
    if not log:
        log = models.WaterLog(user_id=user_id, date=today, amount_ml=amount_ml)
        db.add(log)
    else:
        log.amount_ml += amount_ml
    db.commit()
    db.refresh(log)
    return log

def get_today_log(db: Session, user_id: int):
    today = date.today()
    return db.query(models.WaterLog).filter_by(user_id=user_id, date=today).first()

def get_user_logs(db: Session, user_id: int):
    return db.query(models.WaterLog).filter_by(user_id=user_id).all()

def get_all_users(db: Session):
    return db.query(models.User).all()