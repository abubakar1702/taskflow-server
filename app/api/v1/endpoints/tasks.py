from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session
from app.api.deps import get_db
from app.schemas.task import TaskCreate, TaskRead
from app.models.task import Task
from app.crud.task import TaskCRUD

router = APIRouter()

@router.get("/", response_model=list[TaskRead])
def read_tasks(
    skip: int = 0,
    limit: int = Query(default=10, lte=100),
    db: Session = Depends(get_db)
):
    tasks = TaskCRUD.get_multi(db, skip=skip, limit=limit)
    return tasks