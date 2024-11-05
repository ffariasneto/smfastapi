from pydantic import BaseModel, EmailStr
from typing import Optional

class TaskCreate(BaseModel):
    name: str
    email: EmailStr
    token: Optional[str] = None