from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    email: str
    token: Optional[str] = Field(default=None)