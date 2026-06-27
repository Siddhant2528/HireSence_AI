from sqlalchemy import Integer,String,Column
from app.Core.db import Base

class User(Base):

    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)