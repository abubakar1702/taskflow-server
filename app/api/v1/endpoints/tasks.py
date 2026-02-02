from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session
from app.api.deps import get_db
from app.schemas.task import TaskCreate, TaskRead
from app.models.task import Task
from app.crud.task import TaskCRUD
from app.models.user import User
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=list[TaskRead])
def read_tasks(
    skip: int = 0,
    limit: int = Query(default=10, lte=100),
    db: Session = Depends(get_db)
):
    tasks = TaskCRUD.get_multi(db, skip=skip, limit=limit)
    return tasks

@router.get("/my-tasks", response_model=list[TaskRead])
def read_my_tasks(
    skip: int = 0,
    limit: int = Query(default=10, lte=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    tasks = TaskCRUD.get_multi(db, skip=skip, limit=limit, creator_id=current_user.id)
    return tasks