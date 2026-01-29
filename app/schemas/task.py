from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, date
from enum import Enum
from .user import UserRead
from .project import ProjectRead
from uuid import UUID


class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class SubtaskBase(BaseModel):
    title: str
    is_completed: bool = False


class SubtaskCreate(SubtaskBase):
    assigned_to_id: Optional[UUID] = None


class SubtaskRead(SubtaskBase):
    id: Optional[UUID] = None
    assignee : Optional[UserRead] = None

    model_config = {
        "from_attributes": True
    }


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo
    due_date: Optional[datetime] = None
    priority: int = 2


class TaskCreate(TaskBase):
    project_id: Optional[UUID] = None
    creator_id: Optional[UUID] = None
    assignee_ids: List[UUID] = Field(default_factory=list)


class TaskRead(TaskBase):
    id: UUID
    creator_id: UUID
    created_at: datetime
    updated_at: datetime
    creator: Optional[UserRead] = None
    assignees: List[UserRead] = Field(default_factory=list)
    subtasks: List[SubtaskRead] = Field(default_factory=list)
    project: Optional[ProjectRead] = None

    model_config = {
        "from_attributes": True
    }