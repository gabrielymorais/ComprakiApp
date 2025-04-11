from sqlalchemy.orm import Session
from app.models.cart_model import CartItem
from app.schemas.cart_schema import CartItemCreate
from fastapi import HTTPException

def add_to_cart(db: Session, user_id: int, item_data: CartItemCreate):
    existing_item = db.query(CartItem).filter_by(user_id=user_id, product_id=item_data.product_id).first()
    
    if existing_item:
        existing_item.quantity += item_data.quantity
    else:
        new_item = CartItem(user_id=user_id, **item_data.dict())
        db.add(new_item)

    db.commit()

def get_cart_by_user(db: Session, user_id: int):
    return db.query(CartItem).filter_by(user_id=user_id).all()

def remove_from_cart(db: Session, user_id: int, product_id: int):
    item = db.query(CartItem).filter_by(user_id=user_id, product_id=product_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado no carrinho")
    db.delete(item)
    db.commit()
