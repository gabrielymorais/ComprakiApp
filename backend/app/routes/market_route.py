from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.market_schema import MarketCreate, MarketRead, MarketLogin
from app.services.market_service import create_market, get_all_markets, get_market_by_id, get_market_by_name
from app.config.database import get_db
from fastapi import Query
from typing import List
from app.services.market_service import authenticate_market


router = APIRouter(prefix="/markets", tags=["Markets"])

@router.post("/", response_model=MarketRead, status_code=status.HTTP_201_CREATED)
def create_market_route(market: MarketCreate, db: Session = Depends(get_db)):
    return create_market(db, market)

@router.get("/", response_model=list[MarketRead])
def list_markets_route(db: Session = Depends(get_db)):
    return get_all_markets(db)

@router.get("/search", response_model=list[MarketRead])
def search_market_by_name(name: str = Query(...), db: Session = Depends(get_db)):
    markets = get_market_by_name(db, name)
    if not markets:
        raise HTTPException(status_code=404, detail="Nenhum mercado encontrado com esse nome")
    return markets


@router.post("/login")
def login_market_route(credentials: MarketLogin, db: Session = Depends(get_db)):
    market = authenticate_market(db, credentials.cnpj, credentials.password)
    if not market:
        raise HTTPException(status_code=401, detail="CNPJ ou senha inválidos")
    return {
        "message": "Login realizado com sucesso",
        "market_id": market.id,
        "market_name": market.name
    }

@router.get("/{market_id:int}", response_model=MarketRead)
def get_market_route(market_id: int, db: Session = Depends(get_db)):
    db_market = get_market_by_id(db, market_id)
    if db_market is None:
        raise HTTPException(status_code=404, detail="Mercado não encontrado")
    return db_market