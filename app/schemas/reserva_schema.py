from pydantic import BaseModel
from datetime import date

class ReservaCreate(BaseModel):
    habitacion: str
    fecha_inicio: date
    fecha_fin: date

class ReservaOut(ReservaCreate):
    id: int
    usuario_id: int

    class Config:
        orm_mode = True
