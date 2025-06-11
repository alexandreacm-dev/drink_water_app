from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal
from datetime import date

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/{user_id}/drink", response_model=schemas.WaterLogResponse)
def drink_water(user_id: int, log: schemas.WaterLogCreate, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        return {"error": "User not found"}
    log_today = crud.add_water_log(db, user_id, log.amount_ml)
    meta = int(user.weight_kg * 35)
    return {
        "date": log_today.date,
        "amount_ml": log_today.amount_ml,
        "meta_ml": meta,
        "reached_goal": log_today.amount_ml >= meta
    }

@router.get("/users/{user_id}/logs", response_model=List[schemas.WaterLogResponse])
def get_logs(user_id: int, db: Session = Depends(get_db)):
    logs = crud.get_user_logs(db, user_id)
    user = crud.get_user(db, user_id)
    meta = int(user.weight_kg * 35)
    return [
        {
            "date": log.date,
            "amount_ml": log.amount_ml,
            "meta_ml": meta,
            "reached_goal": log.amount_ml >= meta
        } for log in logs
    ]
