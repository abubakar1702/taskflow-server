from typing import Optional, List
from sqlmodel import Session, select
from uuid import UUID

from app.models.project import Project
from app.schemas.project import ProjectBase, ProjectCreate, ProjectRead

class ProjectCRUD:
    @staticmethod
    def get_multi(
        db: Session,
        skip: int = 0,
        limit: int = 100,
    ) -> list[ProjectRead]:
        result = db.exec(
            select(Project).offset(skip).limit(limit)
        ).all()
        return result