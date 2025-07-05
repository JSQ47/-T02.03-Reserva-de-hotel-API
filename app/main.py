from fastapi import FastAPI
from app.core.database import Base, engine
from app.controllers import auth_controller

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Reservas Hotel", description="Backend con FastAPI + Swagger", version="1.0")

app.include_router(auth_controller.router, prefix="/api/auth", tags=["Auth"])
