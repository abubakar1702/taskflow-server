from sqlmodel import SQLModel, Field, Relationship
from typing import List
from datetime import datetime
from uuid import UUID, uuid4
from .user import User

class Project(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    description: str | None = None
    creator_id: UUID = Field(foreign_key="user.id")
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    creator: "User" = Relationship(back_populates="projects_created")
    tasks: List["Task"] = Relationship(back_populates="project")