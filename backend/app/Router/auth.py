from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.Core.db import get_db
from app.Models.Users import User
from app.Schema.login import LoginSchema
from app.Schema.Register import RegisterSchema


router=APIRouter()

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if user is None:
        return {"message": "User not found"}

    if user.password != data.password:
        return {"message": "Incorrect password"}

    return {
        "message": "Login Successful",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }


@router.post("/register")
def register(data: RegisterSchema, db: Session = Depends(get_db)):

    # Check if email already exists
    email_exists = db.query(User).filter(User.email == data.email).first()

    if email_exists:
        return {"message": "Email already exists"}

    # Check if username already exists
    username_exists = db.query(User).filter(User.username == data.username).first()

    if username_exists:
        return {"message": "Username already exists"}

    # Create new user
    new_user = User(
        name=data.name,
        username=data.username,
        email=data.email,
        password=data.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered Successfully",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "username": new_user.username,
            "email": new_user.email
        }
    }