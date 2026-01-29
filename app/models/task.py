from datetime import datetime
from typing import List
from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4
from .user import User
from .project import Project
from enum import Enum

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskPriority(int, Enum):
    low = 1
    medium = 2
    high = 3
    urgent = 4

class Task(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.todo
    due_date: datetime | None = None
    priority: TaskPriority = TaskPriority.medium
    creator_id: UUID = Field(foreign_key="user.id")
    project_id: UUID | None = Field(default=None, foreign_key="project.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"onupdate": datetime.utcnow}
    )

    creator: User = Relationship(back_populates="tasks")
    project: Project | None = Relationship(back_populates="tasks")
    subtasks: List["Subtask"] | None = Relationship(back_populates="task")


class Subtask(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str
    is_completed: bool = False
    task_id: UUID = Field(foreign_key="task.id")
    assigned_to_id: UUID | None = Field(default=None, foreign_key="user.id")

    task: "Task" = Relationship(back_populates="subtasks")
    assigned_to: User | None = Relationship(back_populates="subtasks")