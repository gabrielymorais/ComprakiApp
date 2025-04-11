from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import product_route
from app.routes import user_route
from app.routes import market_route
from app.routes import cart_route
from app.routes import order_route

from app.config.database import Base, engine


# ⚠️ IMPORTA os modelos para garantir que as tabelas sejam criadas
from app.models import user  # Certifique-se que esses arquivos existem

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicializa o app FastAPI
app = FastAPI(title="Compraki API")

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode mudar depois para ['http://localhost:4200'] por exemplo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas
app.include_router(user_route.router)
app.include_router(market_route.router)
app.include_router(product_route.router)
app.include_router(cart_route.router)
app.include_router(order_route.router)

@app.get("/")
def read_root():
    return {"message": "API do Compraki no ar, camarada!"}
