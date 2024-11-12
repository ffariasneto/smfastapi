from sqlmodel import SQLModel, Field
from typing import Optional

class Project(SQLModel, table=True):
    id: int = Field(primary_key=True)
    # project_id
    title: str
    description: Optional[str] = Field(default=None)
    # Status