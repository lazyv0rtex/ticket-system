from sqlalchemy.orm import Session
from models.database_models import User
from auth import hash_password

def create_user(db: Session, user: dict):
    db_user = User(
        name=user["name"],
        email=user["email"],
        username=user["username"],
        hashed_password=hash_password(user["password"])
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user_id: int, user_data: dict):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.name = user_data["name"]
        db_user.email = user_data["email"]
        db_user.username = user_data["username"]
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False
