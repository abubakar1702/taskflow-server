"""API v1 router configuration"""
from fastapi import APIRouter
from app.api.v1.endpoints import tasks, projects, auth, user

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["tasks"]
)

api_router.include_router(
    projects.router,
    prefix="/projects",
    tags=["projects"]
)

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"]
)

api_router.include_router(
    user.router,
    prefix="/users",
    tags=["users"]
)