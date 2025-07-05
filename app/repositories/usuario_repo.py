from sqlalchemy.orm import Session
from app.models.usuario import Usuario

def create_user(db: Session, nombre: str, email: str, hashed_password: str):
    db_user = Usuario(nombre=nombre, email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()
