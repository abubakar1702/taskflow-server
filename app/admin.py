from sqladmin import Admin, ModelView
from app.models.user import User
from app.models.project import Project
from app.models.task import Task, Subtask

class UserAdmin(ModelView, model=User):
    column_list = ["id", "username", "email", "is_active"]
    column_searchable_list = ["username", "email"]
    column_filters = ["is_active"]
    icon = "fa-solid fa-user"

class ProjectAdmin(ModelView, model=Project):
    column_list = ["id", "name", "is_active", "created_at"]
    column_searchable_list = ["name"]
    icon = "fa-solid fa-project-diagram"

class TaskAdmin(ModelView, model=Task):
    column_list = ["id", "title", "status", "priority", "due_date"]
    column_filters = ["status", "priority"]
    column_searchable_list = ["title", "description"]
    icon = "fa-solid fa-tasks"

class SubtaskAdmin(ModelView, model=Subtask):
    column_list = ["id", "title", "is_completed"]
    column_searchable_list = ["title"]
    icon = "fa-solid fa-list-check"

def setup_admin(app, engine):
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)
    admin.add_view(ProjectAdmin)
    admin.add_view(TaskAdmin)
    admin.add_view(SubtaskAdmin)
    return admin
