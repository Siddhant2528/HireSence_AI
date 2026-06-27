from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.Core.db import get_db
from app.Models.Users import User
from app.Schema.login import LoginSchema


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

