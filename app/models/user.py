from sqlmodel import SQLModel, Field, Relationship
from typing import List
from uuid import UUID, uuid4
from datetime import datetime


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    first_name: str
    last_name: str
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"onupdate": datetime.utcnow}
    )

    tasks: List["Task"] = Relationship(back_populates="creator")
    projects_created: List["Project"] = Relationship(back_populates="creator")
    subtasks: List["Subtask"] = Relationship(back_populates="assigned_to")

