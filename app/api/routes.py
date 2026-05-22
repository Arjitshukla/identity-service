from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.crud.user import create_user, get_users
from app.db.database import get_db

router = APIRouter()


@router.post("/users")
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.email, user.username)


@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    return get_users(db)