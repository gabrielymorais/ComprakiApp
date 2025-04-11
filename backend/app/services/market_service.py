from sqlalchemy.orm import Session
from app.models.market import Market
from app.schemas.market_schema import MarketCreate
from app.utils.security import hash_senha, verificar_senha  

def create_market(db: Session, market: MarketCreate):
    hashed_password = hash_senha(market.password)
    db_market = Market(
        name=market.name,
        description=market.description,
        logo_url=market.logo_url,
        city=market.city,
        cnpj=market.cnpj,
        address=market.address,
        password=hashed_password
    )
    db.add(db_market)
    db.commit()
    db.refresh(db_market)
    return db_market

def get_all_markets(db: Session) -> list[Market]:
    return db.query(Market).all()

def get_market_by_id(db: Session, market_id: int) -> Market | None:
    return db.query(Market).filter(Market.id == market_id).first()

def get_market_by_name(db: Session, name: str):
    return db.query(Market).filter(Market.name.ilike(f"%{name}%")).all()

def authenticate_market(db: Session, cnpj: str, password: str): 
    market = db.query(Market).filter(Market.cnpj == cnpj).first()
    if not market or not verificar_senha(password, market.password):  
        return None
    return market
