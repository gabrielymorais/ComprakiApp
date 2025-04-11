from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.config.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    preco = Column(Float, nullable=False)
    imagem_url = Column(String, nullable=True)
    mercado_id = Column(Integer, ForeignKey("markets.id"), nullable=False)
