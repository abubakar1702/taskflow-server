from sqlmodel import Session, select
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash
from uuid import UUID
from typing import Optional

class UserCRUD:
    @staticmethod
    def get(db: Session, user_id: UUID) -> Optional[User]:
        return db.get(User, user_id)

    @staticmethod
    def get_by_username(db: Session, username: str) -> Optional[User]:
        statement = select(User).where(User.username == username)
        return db.exec(statement).first()

    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[User]:
        statement = select(User).where(User.email == email)
        return db.exec(statement).first()

    @staticmethod
    def create(db: Session, user_in: UserCreate) -> User:
        hashed_password = get_password_hash(user_in.password)
        # Create user data excluding the original password
        user_data = user_in.model_dump(exclude={"password"})
        db_user = User(**user_data, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user