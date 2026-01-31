from fastapi import APIRouter, Depends
from app.schemas.project import ProjectRead
from sqlmodel import Session
from app.api.deps import get_db
from app.crud.project import ProjectCRUD

router = APIRouter()


@router.get("/", response_model=list[ProjectRead])
def read_projects(
    skip : int = 0,
    limit : int = 100,
    db : Session = Depends(get_db)
):
    projects = ProjectCRUD.get_multi(db, skip, limit)
    return projects