from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.Core.config import Db_URl


engine =create_engine(Db_URl)

SessionLocal= sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base=declarative_base()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
