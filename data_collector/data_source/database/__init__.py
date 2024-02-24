from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:///./sql_app.db",
    connect_args={
        "check_same_thread": False,
    },
)

LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db_session():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
