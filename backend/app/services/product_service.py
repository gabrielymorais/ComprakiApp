from sqlalchemy.orm import Session
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate
from fastapi import HTTPException

def create_product(db: Session, product_data: ProductCreate):
    novo_produto = Product(**product_data.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

def get_products_by_market(db: Session, mercado_id: int):
    return db.query(Product).filter(Product.mercado_id == mercado_id).all()


def update_product_by_name(
    db: Session,
    nome: str,
    produto_update: ProductUpdate
) -> Product:
    produto = db.query(Product).filter_by(nome=nome).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    for field, value in produto_update.dict(exclude_unset=True).items():
        setattr(produto, field, value)

    db.commit()
    db.refresh(produto)
    return produto
