from pydantic import BaseModel, PositiveInt, PositiveFloat
from typing import Optional

class Book(BaseModel):
    title: str
    author: str
    numb_pages: int
    category: Optional[str] = None