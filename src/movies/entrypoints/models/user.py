from .model_deps import Base
from sqlalchemy import (
    Column,
    Integer,
    String
)

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    preferences = Column(String)
    preference_key = Column(Integer)
    email = Column(String)
    password = Column(String)