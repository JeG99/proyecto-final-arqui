import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData

def get_postgres_uri():
    host = os.environ.get("DB_HOST", "postgres")
    port = 5432
    password = os.environ.get("DB_PASS", "abc123")
    user, db_name = "movies", "movies"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

Base = declarative_base(
    metadata=MetaData(),
)

engine = create_engine(
    get_postgres_uri(),
    isolation_level="REPEATABLE READ",
)

def start_mappers():
    Base.metadata.create_all(engine)