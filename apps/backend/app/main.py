from fastapi import FastAPI
from apps.backend.app.routers  import user
from apps.backend.app.routers import water
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Drink Water API",
    description="API para o aplicativo de lembrar de beber água",
    version="1.0.0"
)

app.include_router(user.router)
app.include_router(water.router)
