from pydantic import BaseModel, Field

class MarketBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: str | None = None
    logo_url: str | None = None
    city: str
    cnpj: str
    address: str 

class MarketCreate(MarketBase):
    password: str  
class MarketRead(MarketBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class MarketLogin(BaseModel):
    cnpj: str
    password: str
