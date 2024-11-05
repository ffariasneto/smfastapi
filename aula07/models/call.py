from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Call(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    description: Optional[str] = Field(default=None)
    status: str
    create_date: datetime = Field(default=datetime.now())