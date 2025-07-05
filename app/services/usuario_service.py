from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app.repositories.usuario_repo import create_user, get_user_by_email

def register_user(db: Session, nombre: str, email: str, password: str):
    hashed_password = bcrypt.hash(password)
    return create_user(db, nombre, email, hashed_password)

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user and bcrypt.verify(password, user.hashed_password):
        return user
    return None
