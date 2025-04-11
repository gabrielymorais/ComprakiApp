from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Market(Base):
    __tablename__ = "markets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    logo_url = Column(String, nullable=False)
    city = Column(String, nullable=False)
    cnpj = Column(String, nullable=False, unique=True)
    address = Column(String, nullable=False)
    password = Column(String, nullable=False)
