from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str

class UsuarioOut(BaseModel):
    id: int
    nombre: str
    email: EmailStr

    class Config:
        orm_mode = True
