# from typing import List
# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from .. import schemas, crud
from ..database import SessionLocal
# from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date

from .. import schemas, crud
# from ..database import get_db

router = APIRouter(
    prefix="/water",
    tags=["water"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.WaterConsumption)
def create_water_consumption(
    water_consumption: schemas.WaterConsumptionCreate, 
    db: Session = Depends(get_db)
):
    user = crud.get_user(db, user_id=water_consumption.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.create_water_consumption(db=db, water_consumption=water_consumption)

@router.get("/{user_id}/today", response_model=schemas.WaterConsumption)
def read_today_consumption(
    user_id: int, 
    db: Session = Depends(get_db),
    today: date = date.today()
):
    consumption = crud.get_water_consumption(db, user_id=user_id, date=today)
    if not consumption:
        user = crud.get_user(db, user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Retorna dados iniciais se não houver registro hoje
        return {
            "user_id": user_id,
            "date": today,
            "consumed_ml": 0,
            "goal_ml": user.weight * 35,
            "reached_goal": False
        }
    
    return consumption

@router.get("/{user_id}/history", response_model=List[schemas.WaterConsumption])
def read_consumption_history(
    user_id: int, 
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db)
):
    user = crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.get_water_consumption_history(db, user_id=user_id, skip=skip, limit=limit)
