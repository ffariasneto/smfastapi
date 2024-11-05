from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    email: str
    token: Optional[str] = Field(default=None)

