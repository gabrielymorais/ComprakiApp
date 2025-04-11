from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.services.product_service import create_product, get_products_by_market

router = APIRouter(prefix="/products", tags=["Produtos"])

@router.post("/", response_model=ProductResponse)
def criar_produto(produto: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, produto)

@router.get("/market/{mercado_id}", response_model=list[ProductResponse])
def listar_produtos_do_mercado(mercado_id: int, db: Session = Depends(get_db)):
    produtos = get_products_by_market(db, mercado_id)
    return produtos

