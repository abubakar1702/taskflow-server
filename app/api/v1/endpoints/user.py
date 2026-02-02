from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.schemas.user import UserCreate, UserRead
from app.crud.user import UserCRUD
from app.db.session import get_session

router = APIRouter()

@router.post("/signup", response_model=UserRead)
def signup(user_in: UserCreate, db: Session = Depends(get_session)):
    # check if username already exists
    if UserCRUD.get_by_username(db, user_in.username):
        raise HTTPException(status_code=400, detail="Username is not available")
    
    # check if email already exists
    if UserCRUD.get_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email is already registered")
    
    user = UserCRUD.create(db, user_in)
    return user
