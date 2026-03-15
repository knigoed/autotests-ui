from pydantic import BaseModel, Field

class Market(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    tags: list[str] = []
    market: Market


