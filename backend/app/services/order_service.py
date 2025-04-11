# app/services/order_service.py
from sqlalchemy.orm import Session
from app.models.order_model import Order, OrderItem
from app.models.cart_model import CartItem
from fastapi import HTTPException
from sqlalchemy.orm import joinedload
# app/services/order_service.py


from sqlalchemy.orm import Session, joinedload
from app.models.order_model import Order, OrderItem
from app.models.cart_model import CartItem
from fastapi import HTTPException


def create_order(db: Session, user_id: int):
    cart_items = db.query(CartItem).filter(CartItem.user_id == user_id).all()

    if not cart_items:
        raise HTTPException(status_code=400, detail="Carrinho vazio!")

    total_price = sum(item.product.preco * item.quantity for item in cart_items)

    new_order = Order(user_id=user_id, total=total_price)
    db.add(new_order)
    db.flush()  # Garante que o order.id esteja disponível

    for item in cart_items:
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            subtotal=item.quantity * item.product.preco
        )
        db.add(order_item)

    for item in cart_items:
        db.delete(item)

    db.commit()

    return db.query(Order)\
        .options(joinedload(Order.items).joinedload(OrderItem.product))\
        .filter(Order.id == new_order.id)\
        .first()

    


def finalize_order(db: Session, user_id: int):
    cart_items = db.query(CartItem).filter_by(user_id=user_id).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Carrinho vazio")

    # Calcula o total do pedido
    total = sum(item.quantity * item.product.preco for item in cart_items)

    # Cria o pedido
    order = Order(user_id=user_id, total=total)
    db.add(order)
    db.flush()  # Garante que order.id esteja disponível

    # Cria itens do pedido
    for item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            subtotal=item.quantity * item.product.preco
        )
        order.items.append(order_item)


    # Limpa o carrinho
    for item in cart_items:
        db.delete(item)

    db.commit()
    db.refresh(order)
    return order

def pay_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    order.status = "pago"
    db.commit()
    db.refresh(order)
    return {"mensagem": "Pedido pago com sucesso!", "pedido_id": order.id, "status": order.status}


def get_order_detail(db: Session, order_id: int):
    return db.query(Order)\
        .options(joinedload(Order.items).joinedload(OrderItem.product))\
        .filter(Order.id == order_id)\
        .first()
