# app/schemas/order_schema.py
from pydantic import BaseModel
from datetime import datetime
from typing import List

# 👇 Adiciona isso:
class ProductResponse(BaseModel):
    id: int
    nome: str
    preco: float

    class Config:
        from_attributes = True

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    subtotal: float

class OrderCreate(BaseModel):
    user_id: int
    items: List[OrderItemCreate]
    total: float

# 👇 Atualiza aqui
class OrderItemResponse(BaseModel):
    id: int
    quantity: int
    subtotal: float
    product: ProductResponse  

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total: float
    created_at: datetime
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True

class OrderDetailResponse(BaseModel):
    id: int
    total: float
    created_at: datetime
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True
