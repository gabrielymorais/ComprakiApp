from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.services.user_service import register_user, authenticate_user
from app.config.database import get_db

router = APIRouter(prefix="/users", tags=["Usuários"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    auth_result = authenticate_user(db, login_data)
    if not auth_result:
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")
    return JSONResponse(content=auth_result)
