from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin
from app.repositories import user_repository
from app.utils.jwt_utils import create_access_token
from passlib.context import CryptContext
from app.schemas.user_schema import UserLogin  # ajuste conforme onde ele está

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(db: Session, user: UserCreate):
    existing_user = user_repository.get_user_by_email(db, user.email)
    if existing_user:
        raise ValueError("Email já está em uso.")
    hashed_pw = pwd_context.hash(user.password)
    return user_repository.create_user(db, user, hashed_pw)

def authenticate_user(db: Session, login_data: UserLogin):
    user = user_repository.get_user_by_email(db, login_data.email)
    if not user or not pwd_context.verify(login_data.password, user.password):
        return None
    token = create_access_token({"sub": user.email})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
        }
    }
