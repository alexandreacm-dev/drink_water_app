from fastapi import FastAPI
from apps.backend.app.routers  import user
from apps.backend.app.routers import water
# from .routers import users, water
from .database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Water Reminder API",
    description="API para aplicativo de registro de consumo de água",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(water.router)

@app.get("/")
def read_root():
    return {"message": "Water Reminder API"}