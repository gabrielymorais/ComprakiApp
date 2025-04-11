from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.cart_schema import CartItemCreate, CartItemResponse
from app.services.cart_service import add_to_cart, get_cart_by_user, remove_from_cart

router = APIRouter(prefix="/cart", tags=["Carrinho"])

@router.post("/{user_id}", response_model=None)
def adicionar_ao_carrinho(user_id: int, item: CartItemCreate, db: Session = Depends(get_db)):
    add_to_cart(db, user_id, item)
    return {"message": "Item adicionado ao carrinho"}

@router.get("/{user_id}", response_model=list[CartItemResponse])
def listar_carrinho(user_id: int, db: Session = Depends(get_db)):
    return get_cart_by_user(db, user_id)

@router.delete("/{user_id}/{product_id}", response_model=None)
def remover_do_carrinho(user_id: int, product_id: int, db: Session = Depends(get_db)):
    remove_from_cart(db, user_id, product_id)
    return {"message": "Item removido do carrinho"}
