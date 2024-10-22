from pydantic import BaseModel, PositiveInt, PositiveFloat
from typing import Optional

class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    stock: PositiveInt