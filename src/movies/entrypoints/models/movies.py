from .model_deps import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    TIMESTAMP
)

class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    preference_key = Column(Integer)
    movie_title = Column(String)
    rating = Column(Float)
    year = Column(Integer)
    create_time = Column(TIMESTAMP(timezone=True), index=True)