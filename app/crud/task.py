from typing import Optional, List
from sqlmodel import Session, select
from uuid import UUID

from app.models.task import Task
from app.schemas.task import TaskBase, TaskCreate

class TaskCRUD:
    @staticmethod
    def get(db: Session, task_id: UUID) -> Optional[Task]:
        return db.get(Task, task_id)

    @staticmethod
    def get_multi(db: Session, skip: int = 0, limit: int = 100) -> List[Task]:
        return db.exec(select(Task).offset(skip).limit(limit)).all()

    @staticmethod
    def create(db: Session, task_in: TaskCreate) -> Task:
        db_task = Task(**task_in.model_dump())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    @staticmethod
    def update(db: Session, db_task: Task, task_in: TaskBase) -> Task:
        for field, value in task_in.model_dump(exclude_unset=True).items():
            setattr(db_task, field, value)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task