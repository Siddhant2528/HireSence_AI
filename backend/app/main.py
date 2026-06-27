from fastapi import FastAPI,Depends
from app.Core.db import engine, Base,get_db
from app.Models.Users import User
from sqlalchemy.orm import Session
from app.Router.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()



app.include_router(auth_router)


@app.get("/")
def home():
    return {"messsage":"server is running "}



@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"Database": "Connected Successfully"}