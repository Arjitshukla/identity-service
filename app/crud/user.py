from sqlalchemy.orm import Session
from app.db.models import User


def create_user(db: Session, email: str, username: str):
    user = User(email=email, username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(User).all()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()