from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models.user import User
from schemas.user import UserCreate

router = APIRouter()

@router.get("/users")
def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users

@router.get("/users/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users")
def post_users(user: UserCreate, session: Session = Depends(get_session)):
    user_db = User(**user.model_dump())

    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return {
        "message": "User created",
        "user": user_db
    }

@router.put("/users/{user_id}")
def post_user(user: UserCreate, user_id: int, session: Session = Depends(get_session)):
    user_db = session.get(User, user_id)

    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    user_db.name = user.name
    user_db.email = user.email
    user_db.token = user.token

    session.commit()
    session.refresh(user_db)

    return user_db

@router.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user_db = session.get(User, user_id)

    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    session.delete(user_db)
    session.commit()

    return {"message": "User deleted"}