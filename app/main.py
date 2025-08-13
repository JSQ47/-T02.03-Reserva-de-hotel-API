# app/main.py
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.core.database import Base, engine
from app.controllers import auth_controller

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Reservas Hotel",
    description="Backend con FastAPI + Swagger",
    version="1.0",
)

# Rutas de API
app.include_router(auth_controller.router, prefix="/api/auth", tags=["Auth"])

# ---- Servir frontend (index.html) ----
# Coloca tu archivo en: app/static/index.html
STATIC_DIR = Path(__file__).parent / "static"
STATIC_DIR.mkdir(exist_ok=True)  # por si no existe

# Montamos el frontend en /app para no chocar con /api ni /docs
app.mount("/app", StaticFiles(directory=str(STATIC_DIR), html=True), name="app")

# Redirige la raíz "/" a "/app/" (carga index.html)
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/app/")
