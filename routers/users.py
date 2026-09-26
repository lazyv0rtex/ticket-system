from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.user import UserCreate, UserUpdate
from database import get_db
from services.user import (
    create_user,
    get_user,
    get_all_users,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

@router.post("/")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.model_dump())

@router.put("/{user_id}")
def update_user_endpoint(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user.model_dump())

@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
