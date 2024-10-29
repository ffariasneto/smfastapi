from pydantic import BaseModel, field_validator
from typing import Optional

class CallCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str

    @field_validator('status')
    def check_status(cls, value):
        print(type(value))
        if value != "Aberto" and value != "Em Andamento" and value != "Resolvido":
            raise ValueError("Name status invalid")
        return value