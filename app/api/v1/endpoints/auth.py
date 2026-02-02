from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.user import User
from app.crud.user import UserCRUD
from app.core.security import verify_password, create_access_token

from app.schemas.user import UserLogin

router = APIRouter()

@router.post("/login")
def login(
    login_data: UserLogin,
    db: Session = Depends(get_session)
):
    user = UserCRUD.get_by_username(db, login_data.username)
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    token = create_access_token(data={"sub": str(user.id)})
    return { "full_name": f"{user.first_name} {user.last_name}", "username": user.username, "email": user.email, "access_token": token, "token_type": "bearer"}
