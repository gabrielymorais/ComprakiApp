from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Dados da conexão (Docker)
DB_USER = os.getenv("POSTGRES_USER", "compraki")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "compraki123")
DB_NAME = os.getenv("POSTGRES_DB", "compraki_db")
DB_HOST = os.getenv("DB_HOST", "db")  # nome do container do banco
DB_PORT = os.getenv("DB_PORT", "5432")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency para injeção de sessão no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
