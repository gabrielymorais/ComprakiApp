from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    nome: str
    descricao: str  
    preco: float
    imagem_url: str
    mercado_id: int

class ProductResponse(BaseModel):
    id: int
    nome: str
    descricao: str  
    preco: float
    imagem_url: str
    mercado_id: int

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    nome: Optional[str]
    descricao: Optional[str]
    preco: Optional[float]
    imagem_url: Optional[str]

    class Config:
        from_attributes = True  