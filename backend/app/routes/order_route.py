# app/routes/order_route.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.order_schema import OrderDetailResponse
from app.services.order_service import finalize_order, create_order, pay_order, get_order_detail

from app.schemas.order_schema import OrderResponse

router = APIRouter(prefix="/orders", tags=["Pedidos"])

@router.post("/{user_id}", response_model=OrderResponse)
def finalizar_pedido(user_id: int, db: Session = Depends(get_db)):
    return create_order(db, user_id)


@router.post("/{order_id}/pay")
def pagar_pedido(order_id: int, db: Session = Depends(get_db)):
    return pay_order(db, order_id)

@router.get("/{order_id}", response_model=OrderDetailResponse)
def ver_detalhes_pedido(order_id: int, db: Session = Depends(get_db)):
    return get_order_detail(db, order_id)